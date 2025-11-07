# FRED API Data Sources

## Overview

The Federal Reserve Economic Data (FRED) API provides reliable economic time series data. This skill uses four key series to track government shutdown liquidity impacts.

## Series Configuration

| Indicator | Series ID | Frequency | Description |
|-----------|-----------|-----------|-------------|
| **TGA** | WTREGEN | Weekly (Wed) | Treasury General Account balance at Federal Reserve |
| **Bank Reserves** | WRESBAL | Weekly (Wed) | Total bank reserves held at Federal Reserve |
| **EFFR** | EFFR | Daily | Effective Federal Funds Rate (Fed's policy rate proxy) |
| **SOFR** | SOFR | Daily | Secured Overnight Financing Rate (actual market funding cost) |

## API Access

**Endpoint**: `https://api.stlouisfed.org/fred/series/observations`

**Required Parameters**:
- `series_id`: One of the series codes above
- `api_key`: Authentication key
- `file_type`: `json` (recommended) or `csv`
- `observation_start`: Start date (YYYY-MM-DD)
- `observation_end`: End date (YYYY-MM-DD)

**Example Request**:
```
https://api.stlouisfed.org/fred/series/observations?series_id=WTREGEN&api_key=YOUR_KEY&file_type=json&observation_start=2025-10-01&observation_end=2025-11-07
```

## Data Update Schedule

- **Weekly data (TGA, Reserves)**: Published every Wednesday after market close
  - Reflects data as of previous Wednesday
  - Best time to run analysis: **Wednesday evenings or Thursday mornings**
  
- **Daily data (EFFR, SOFR)**: Published next business day
  - SOFR: Published ~8:00 AM ET by NY Fed
  - EFFR: Published ~9:00 AM ET by NY Fed

## Key Interpretation Notes

### TGA (Treasury General Account)

The government's "checking account" at the Fed. 

- **Rising TGA during shutdown** → Revenue inflow continues while spending stops
- **Falling TGA after shutdown** → Fiscal spending resumes, funds return to economy
- **Mechanical relationship**: TGA ↑ implies Bank Reserves ↓ (and vice versa)

### Bank Reserves

Total reserves commercial banks hold at the Federal Reserve.

- **Ample reserves** (QE era): >$2.5T → TGA shocks absorbed, no market impact
- **Scarce reserves** (QT era): <$2T → TGA shocks transmit to funding rates
- **Current critical zone**: ~$2.8T → High sensitivity to TGA fluctuations

### EFFR (Effective Federal Funds Rate)

Volume-weighted median rate on overnight fed funds transactions.

- Fed's primary policy rate target (currently set via IORB - Interest on Reserve Balances)
- In well-functioning markets: EFFR ≈ IORB (Fed's control rate)
- **EFFR stability** indicates Fed retains policy control

### SOFR (Secured Overnight Financing Rate)

Rate on overnight Treasury repo transactions (collateralized lending).

- Broader market indicator (~$1T daily volume)
- More sensitive to liquidity conditions than EFFR
- **SOFR > EFFR** (positive premium) indicates funding market stress

### SOFR Premium

**Definition**: `SOFR - EFFR` (measured in basis points)

**Interpretation**:
- **0-5 bps**: Normal market conditions
- **5-15 bps**: Moderate liquidity stress
- **15-30 bps**: Significant stress (stealth tightening effect)
- **>30 bps**: Acute crisis (requires Fed intervention)

**Historical context**:
- 2013 shutdown: ~0 bps (no effect)
- 2018-19 shutdown: Up to 75 bps (significant tightening)
- 2025 shutdown: Up to 36 bps post-rate-cut (acute stress requiring SRF)

## Data Quirks and Limitations

1. **Weekly data gaps**: TGA and Reserves only update weekly, making daily tracking impossible
2. **Holiday effects**: EFFR/SOFR not published on Fed holidays or weekends
3. **Month/quarter-end spikes**: SOFR often spikes at period-ends due to balance sheet constraints (separate from shutdown effects)
4. **Revision policy**: Data rarely revised, but check FRED for any updates
5. **SRF not in FRED**: Standing Repo Facility usage must be checked separately on NY Fed website

## Additional Context Data (Not Currently Used)

Potentially useful for deeper analysis:

- **IORB** (IORB): Interest rate on reserve balances (Fed's control rate)
- **ON RRP** (RRPONTSYD): Overnight Reverse Repo volume
- **10Y Treasury** (DGS10): For term spread analysis
- **Debt subject to limit** (GFDEBTN): For debt ceiling context

## Rate Limits

- FRED API: Generally very permissive
- No formal rate limit documented
- Recommended: <100 requests per minute to be safe
- Current skill usage: 4 series × 1 request = 4 requests per run (well within limits)

## Error Handling

Common API errors:
- `400 Bad Request`: Check date format (must be YYYY-MM-DD)
- `404 Not Found`: Invalid series_id
- `500 Internal Server Error`: FRED service issue, retry after delay

## References

- FRED API Documentation: https://fred.stlouisfed.org/docs/api/fred/
- Series catalog: https://fred.stlouisfed.org/
- NY Fed SOFR page: https://www.newyorkfed.org/markets/reference-rates/sofr
