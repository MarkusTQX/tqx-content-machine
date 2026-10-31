"""Overnight vs intraday returns for SPY: a real TQX test for J021.
Buy at the close, sell at the next open (overnight) vs buy at the open, sell at the close (intraday).
$10,000 each, compounded, no fees, no dividends. Price data: Yahoo Finance daily OHLC (split-adjusted, not dividend-adjusted).
Usage: tools/.venv/bin/python tools/overnight-test.py
"""
import yfinance as yf

START, END = "2015-01-01", "2025-01-01"
df = yf.download("SPY", start=START, end=END, auto_adjust=False, progress=False)
df.columns = [c[0] if isinstance(c, tuple) else c for c in df.columns]
o, c = df["Open"], df["Close"]
overnight = (o / c.shift(1)).dropna()          # close(t-1) -> open(t)
intraday = (c / o)                              # open(t) -> close(t)
hold = c.iloc[-1] / c.iloc[0]

def run(r, label):
    eq = 10000 * r.cumprod()
    peak = eq.cummax(); dd = (eq / peak - 1).min()
    wins = (r > 1).mean()
    print(f"{label}: $10,000 -> ${eq.iloc[-1]:,.0f} ({(eq.iloc[-1]/10000-1)*100:+.1f}%), trades {len(r)}, up days {wins*100:.1f}%, worst drop {dd*100:.1f}%")
    return eq

print(f"Data: SPY {df.index[0].date()} to {df.index[-1].date()}, {len(df)} trading days")
run(overnight, "Overnight (buy close, sell next open)")
run(intraday, "Intraday (buy open, sell close)")
print(f"Buy and hold (close to close, price only): $10,000 -> ${10000*hold:,.0f} ({(hold-1)*100:+.1f}%)")
# with a realistic cost: 0.01% per side (about one cent per $100 traded), 2 trades a day
cost = (1 - 0.0001) ** 2
run(overnight * cost, "Overnight with 0.01% cost per trade")
run(intraday * cost, "Intraday with 0.01% cost per trade")
