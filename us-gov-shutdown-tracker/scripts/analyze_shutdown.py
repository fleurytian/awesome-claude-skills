#!/usr/bin/env python3
"""
US Government Shutdown Liquidity Analysis Script

Fetches TGA, Bank Reserves, EFFR, and SOFR data from FRED API
and analyzes the liquidity impact of government shutdowns.
"""

import requests
import pandas as pd
import json
import sys
from datetime import datetime, timedelta

# FRED API Configuration
API_KEY = "b36495528d4933449ac821a9fa35852d"
BASE_URL = "https://api.stlouisfed.org/fred/series/observations"

SERIES_CONFIG = {
    'TGA': 'WTREGEN',
    'Bank_Reserves': 'WRESBAL',
    'EFFR': 'EFFR', 
    'SOFR': 'SOFR'
}

def fetch_fred_data(series_id, start_date, end_date):
    """Fetch data from FRED API"""
    url = f"{BASE_URL}?series_id={series_id}&api_key={API_KEY}&file_type=json&observation_start={start_date}&observation_end={end_date}"
    
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        if 'observations' in data:
            df = pd.DataFrame(data['observations'])
            df['date'] = pd.to_datetime(df['date'])
            df['value'] = pd.to_numeric(df['value'], errors='coerce')
            return df[['date', 'value']].dropna()
        return None
    except Exception as e:
        print(f"Error fetching {series_id}: {str(e)}", file=sys.stderr)
        return None

def analyze_shutdown(start_date=None, baseline_date=None, end_date=None):
    """
    Main analysis function
    
    Args:
        start_date: Shutdown start date (YYYY-MM-DD), defaults to 2025-10-01
        baseline_date: Baseline comparison date (YYYY-MM-DD), defaults to one week before start
        end_date: Analysis end date (YYYY-MM-DD), defaults to today
    """
    # Set defaults
    if start_date is None:
        start_date = "2025-10-01"
    if end_date is None:
        end_date = datetime.now().strftime("%Y-%m-%d")
    if baseline_date is None:
        baseline_dt = datetime.strptime(start_date, "%Y-%m-%d") - timedelta(days=7)
        baseline_date = baseline_dt.strftime("%Y-%m-%d")
    
    # Fetch data starting from baseline
    print(f"Fetching data from {baseline_date} to {end_date}...\n")
    
    all_data = {}
    for name, series_id in SERIES_CONFIG.items():
        df = fetch_fred_data(series_id, baseline_date, end_date)
        if df is not None:
            all_data[name] = df
            print(f"✓ {name}: {len(df)} observations")
        else:
            print(f"✗ {name}: Failed to fetch")
    
    if not all_data:
        print("\nError: No data retrieved")
        return None
    
    # Merge data
    merged = None
    for name, df in all_data.items():
        df_renamed = df.rename(columns={'value': name})
        if merged is None:
            merged = df_renamed
        else:
            merged = pd.merge(merged, df_renamed, on='date', how='outer')
    
    merged = merged.sort_values('date').reset_index(drop=True)
    
    # Calculate SOFR Premium
    merged['SOFR_Premium_bps'] = (merged['SOFR'] - merged['EFFR']) * 100
    
    # Filter weekly data (TGA/Reserves published on Wednesdays)
    weekly_data = merged[merged['TGA'].notna() & merged['Bank_Reserves'].notna()].copy()
    
    # Find key points
    baseline_dt = pd.to_datetime(baseline_date)
    shutdown_dt = pd.to_datetime(start_date)
    
    baseline_row = weekly_data[weekly_data['date'] <= baseline_dt].iloc[-1] if len(weekly_data[weekly_data['date'] <= baseline_dt]) > 0 else None
    first_shutdown = weekly_data[weekly_data['date'] >= shutdown_dt].iloc[0] if len(weekly_data[weekly_data['date'] >= shutdown_dt]) > 0 else None
    peak_tga = weekly_data.loc[weekly_data['TGA'].idxmax()]
    latest = weekly_data.iloc[-1]
    
    # Build result
    result = {
        'raw_data': merged.to_dict('records'),
        'weekly_data': weekly_data.to_dict('records'),
        'key_points': {
            'baseline': baseline_row.to_dict() if baseline_row is not None else None,
            'shutdown_start': first_shutdown.to_dict() if first_shutdown is not None else None,
            'tga_peak': peak_tga.to_dict(),
            'latest': latest.to_dict()
        },
        'analysis': analyze_liquidity_status(baseline_row, peak_tga, latest)
    }
    
    return result

def analyze_liquidity_status(baseline, peak, latest):
    """Determine liquidity stress status"""
    if baseline is None or peak is None or latest is None:
        return {"status": "INSUFFICIENT_DATA", "conclusion": "Not enough data for analysis"}
    
    # Changes vs baseline
    tga_change_pct = ((latest['TGA'] - baseline['TGA']) / baseline['TGA']) * 100
    reserves_change_pct = ((latest['Bank_Reserves'] - baseline['Bank_Reserves']) / baseline['Bank_Reserves']) * 100
    premium_change = latest['SOFR_Premium_bps'] - baseline['SOFR_Premium_bps']
    
    # Changes vs peak
    tga_from_peak = latest['TGA'] - peak['TGA']
    reserves_from_peak = latest['Bank_Reserves'] - peak['Bank_Reserves']
    
    # Determine status
    if tga_from_peak < -10 and reserves_from_peak > 10:
        status = "EASING"
        conclusion = "Liquidity stress significantly easing. TGA releasing funds, reserves recovering. Shutdown likely ended or fiscal spending resumed."
    elif abs(tga_from_peak) < 20 and abs(reserves_from_peak) < 20:
        status = "STABLE"
        conclusion = "Liquidity conditions relatively stable. TGA and reserves showing minimal change."
    elif tga_change_pct > 5 and reserves_change_pct < -2:
        status = "TIGHTENING"
        conclusion = "Liquidity stress intensifying. TGA accumulating, reserves declining. Shutdown's 'stealth tightening' effect persists."
    else:
        status = "MIXED"
        conclusion = "Mixed liquidity signals. Requires continued monitoring."
    
    return {
        "status": status,
        "conclusion": conclusion,
        "metrics": {
            "tga_vs_baseline_pct": round(tga_change_pct, 2),
            "reserves_vs_baseline_pct": round(reserves_change_pct, 2),
            "premium_vs_baseline_bps": round(premium_change, 1),
            "tga_from_peak_bn": round(tga_from_peak, 2),
            "reserves_from_peak_bn": round(reserves_from_peak, 2)
        }
    }

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Analyze US Government Shutdown Liquidity Impact')
    parser.add_argument('--start-date', help='Shutdown start date (YYYY-MM-DD)', default=None)
    parser.add_argument('--baseline-date', help='Baseline comparison date (YYYY-MM-DD)', default=None)
    parser.add_argument('--end-date', help='Analysis end date (YYYY-MM-DD)', default=None)
    parser.add_argument('--output', help='Output JSON file path', default=None)
    
    args = parser.parse_args()
    
    result = analyze_shutdown(args.start_date, args.baseline_date, args.end_date)
    
    if result:
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(result, f, indent=2, default=str)
            print(f"\n✓ Results saved to {args.output}")
        else:
            print("\n" + "="*80)
            print("ANALYSIS SUMMARY")
            print("="*80)
            print(json.dumps(result['analysis'], indent=2, default=str))
