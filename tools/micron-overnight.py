"""Micron (MU) overnight vs daytime since the earliest Yahoo data: checks the viral J021 claim.
Usage: tools/.venv/bin/python tools/micron-overnight.py
"""
import yfinance as yf
df = yf.download("MU", period="max", auto_adjust=False, progress=False)
df.columns = [c[0] if isinstance(c, tuple) else c for c in df.columns]
df = df[(df["Open"] > 0) & (df["Close"] > 0)]
o, c = df["Open"], df["Close"]
on = (o / c.shift(1)).dropna(); day = c / o
print(f"MU {df.index[0].date()} to {df.index[-1].date()}, {len(df)} days")
for lab, r in (("Overnight (buy close, sell next open)", on), ("Daytime (buy open, sell close)", day)):
    m = r.prod(); print(f"{lab}: $1 -> ${m:,.4f} ({(m-1)*100:+,.0f}%)")
print(f"Hold: $1 -> ${c.iloc[-1]/c.iloc[0]:,.2f}")
