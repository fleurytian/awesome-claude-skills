#!/usr/bin/env python3
"""
Generate visualization charts for government shutdown liquidity analysis
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json
import sys
from datetime import datetime

def create_charts(data_json, output_path, shutdown_date="2025-10-01"):
    """
    Create visualization charts from analysis data
    
    Args:
        data_json: Analysis result JSON (from analyze_shutdown.py)
        output_path: Path to save the chart image
        shutdown_date: Official shutdown start date for annotations
    """
    
    # Load data
    if isinstance(data_json, str):
        with open(data_json, 'r') as f:
            data = json.load(f)
    else:
        data = data_json
    
    # Convert to DataFrame
    df = pd.DataFrame(data['raw_data'])
    df['date'] = pd.to_datetime(df['date'])
    
    weekly_df = pd.DataFrame(data['weekly_data'])
    weekly_df['date'] = pd.to_datetime(weekly_df['date'])
    
    # Get key dates
    tga_peak_date = pd.to_datetime(data['key_points']['tga_peak']['date'])
    shutdown_dt = pd.to_datetime(shutdown_date)
    
    # Create figure
    fig, axes = plt.subplots(3, 1, figsize=(14, 10))
    fig.suptitle('US Government Shutdown - Liquidity Impact Analysis', 
                 fontsize=16, fontweight='bold')
    
    # Chart 1: TGA vs Bank Reserves
    ax1 = axes[0]
    ax1.plot(weekly_df['date'], weekly_df['TGA'], 'o-', 
             color='#d62728', linewidth=2, markersize=8, label='TGA Balance')
    ax1_twin = ax1.twinx()
    ax1_twin.plot(weekly_df['date'], weekly_df['Bank_Reserves'], 's-', 
                  color='#1f77b4', linewidth=2, markersize=8, label='Bank Reserves')
    
    # Add event markers
    ax1.axvline(shutdown_dt, color='orange', linestyle='--', 
                linewidth=2, alpha=0.7, label='Shutdown Begins')
    ax1.axvline(tga_peak_date, color='red', linestyle='--', 
                linewidth=2, alpha=0.7, label='TGA Peak')
    
    ax1.set_ylabel('TGA ($Billions)', fontsize=11, color='#d62728', fontweight='bold')
    ax1_twin.set_ylabel('Bank Reserves ($Billions)', fontsize=11, color='#1f77b4', fontweight='bold')
    ax1.tick_params(axis='y', labelcolor='#d62728')
    ax1_twin.tick_params(axis='y', labelcolor='#1f77b4')
    ax1.grid(True, alpha=0.3)
    ax1.set_title('Treasury General Account vs Bank Reserves', 
                  fontsize=12, fontweight='bold', pad=10)
    
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax1_twin.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=9)
    
    # Chart 2: EFFR and SOFR
    ax2 = axes[1]
    ax2.plot(df['date'], df['EFFR'], '-', color='#2ca02c', 
             linewidth=2, label='EFFR (Fed Funds Effective Rate)', alpha=0.8)
    ax2.plot(df['date'], df['SOFR'], '-', color='#ff7f0e', 
             linewidth=2, label='SOFR (Secured Overnight Financing Rate)', alpha=0.8)
    
    ax2.axvline(shutdown_dt, color='orange', linestyle='--', linewidth=2, alpha=0.7)
    ax2.axvline(tga_peak_date, color='red', linestyle='--', linewidth=2, alpha=0.7)
    
    # Check for rate cuts
    baseline_effr = df[df['date'] < shutdown_dt]['EFFR'].iloc[-1] if len(df[df['date'] < shutdown_dt]) > 0 else None
    latest_effr = df['EFFR'].iloc[-1]
    if baseline_effr and latest_effr < baseline_effr - 0.2:
        rate_cut_date = df[df['EFFR'] < baseline_effr - 0.1]['date'].iloc[0]
        ax2.axvline(rate_cut_date, color='green', linestyle='--', 
                    linewidth=2, alpha=0.7, label='Fed Rate Cut')
    
    ax2.set_ylabel('Rate (%)', fontsize=11, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='upper right', fontsize=9)
    ax2.set_title('Short-Term Funding Rates', fontsize=12, fontweight='bold', pad=10)
    
    # Chart 3: SOFR Premium
    ax3 = axes[2]
    ax3.plot(df['date'], df['SOFR_Premium_bps'], '-', color='#9467bd', 
             linewidth=2.5, marker='o', markersize=5)
    ax3.fill_between(df['date'], 0, df['SOFR_Premium_bps'], alpha=0.3, color='#9467bd')
    
    ax3.axvline(shutdown_dt, color='orange', linestyle='--', linewidth=2, alpha=0.7)
    ax3.axvline(tga_peak_date, color='red', linestyle='--', linewidth=2, alpha=0.7)
    ax3.axhline(0, color='black', linestyle='-', linewidth=1, alpha=0.5)
    
    ax3.set_ylabel('Premium (basis points)', fontsize=11, fontweight='bold')
    ax3.set_xlabel('Date', fontsize=11, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    ax3.set_title('SOFR Premium over EFFR (Liquidity Stress Indicator)', 
                  fontsize=12, fontweight='bold', pad=10)
    
    # Format x-axis
    for ax in axes:
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=7))
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Chart saved to {output_path}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate shutdown liquidity charts')
    parser.add_argument('data_json', help='Input JSON file from analyze_shutdown.py')
    parser.add_argument('--output', help='Output image path', default='shutdown_analysis.png')
    parser.add_argument('--shutdown-date', help='Shutdown start date (YYYY-MM-DD)', 
                        default='2025-10-01')
    
    args = parser.parse_args()
    
    create_charts(args.data_json, args.output, args.shutdown_date)
