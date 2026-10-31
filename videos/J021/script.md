# J021 · I tested the overnight trick in Qube
Presenter: Joshua · Persona: Daniel, the burned retail trader · Shape: 5, shock number → the opposite → why (the "why" is the cost twist) · Product: Qube · Length: ~56s (180 words: 162 body + 18 in hook 1)
Remix of: knowledge/cards/reference/2026-09-23_joe.investss_overnight-returns-stock-market-is-broken.md (gold aimed at: 2026-09-20_svermm_night-trading-beats-day-trading.md; paper beat from 2026-09-29_markvictorn_micron-overnight-trade.md)

## Hooks
1. "If you trade the open, watch this before you try the overnight trick. I tested it in Qube." · On screen: "Watch this before you try it" · First frame: Qube backtest chart pinned in the top third, green overnight line and grey daytime line, "Backtest, not live results" top-left, Joshua's face below · Mechanism: firm rule 2, warn before an action (Joshua's "If you..." opener)
2. "Buy at the close, sell at the open. In a ten-year test in Qube, that almost doubled $10,000." · On screen: "$10,000 → $19,225 overnight" · First frame: same Qube chart, the overnight line's end tagged "$19,225", "Backtest, not live results · SPY · 2015–2024" · Mechanism: viral opening, shock number from a simple rule (svermm, markvictorn)
3. "Here's what the buy at the close, sell at the open videos don't tell you. I tested it in Qube." · On screen: "What the overnight videos leave out" · First frame: same Qube chart, the overnight line greyed out with a "?" where the cost line will go · Mechanism: firm rule 1, promise a hidden truth
4. "Ten years of the buy at the close, sell at the open trick, tested in Qube, in under a minute." · On screen: "10 years, tested in under a minute" · First frame: same Qube chart, a small timer counting up in the top-right of the clip · Mechanism: firm rule 3, short timeframe
5. "Everyone's posting the overnight trick. Nobody adds what it costs to trade. So I did, in Qube." · On screen: "Nobody adds the cost. So I did." · First frame: same Qube chart, cursor resting on Qube's cost setting · Mechanism: tip, "everyone says X, nobody shows Y"
Top 3: [2, 1, 5]: 2 puts the number in the first 3 seconds like the svermm and markvictorn openers; 1 is Joshua's own "If you..." move and lands right before Daniel's mistake; 5 names the no-costs pattern and opens the loop the body pays off.

## Script
1. I typed it into Qube. Buy SPY right before the close, sell it the second the market opens.
   (Visual: screen recording in the top third: Joshua types into Qube, exactly "Buy SPY at the close every day. Sell it at the next day's open." Qube's rules appear, then the backtest starts running) (On screen: "Buy at the close · sell at the next open")
2. SPY holds about 500 of the biggest US companies.
   (On screen: "SPY: about 500 of the biggest US companies") (Visual: Qube run still loading behind the text)
3. Qube ran it on ten years of past prices. Say I'd put in $10,000. It almost doubled.
   (Visual: Qube results screen, green overnight line climbs; pops in on "doubled") (On screen: "Overnight: $10,000 → $19,225 · SPY · 2015–2024 · 2,515 round trips · Backtest, not live results")
4. Now the exact opposite. Buy at the open, sell at the close. About $14,800.
   (Visual: Joshua edits the Qube sentence to "Buy SPY at the open every day. Sell it at the close.", reruns; a grey daytime line draws in under the green one) (On screen: "Daytime: $10,000 → $14,771 · SPY · 2015–2024 · Backtest, not live results")
5. And researchers wrote a whole paper on overnight versus daytime returns.
   (Visual: our own title card over the Qube screen for 3 seconds: "A tug of war: overnight versus intraday expected returns" · Dong Lou, Christopher Polk & Spyros Skouras · Journal of Financial Economics, 2019. Title and authors only, none of the paper's numbers) (On screen: "Lou, Polk & Skouras · 2019")
6. So should you switch? Not till you add the costs.
   (Visual: back to the Qube chart; punch-in on Joshua on "switch?"; cursor moves to Qube's cost setting) (On screen: "The part the viral videos skip")
7. I added a cost of one cent per $100 on every buy and every sell.
   (Visual: screen recording: cost set to 0.01% per buy and per sell, Run clicked) (On screen: "Cost: 0.01% per buy and per sell · one cent per $100")
8. Overnight fell to about $11,600. Daytime actually lost money.
   (Visual: rerun; the green line sinks, the grey line turns red and ends under $10,000) (On screen: "Overnight $11,625 · Daytime $8,930 · with costs · SPY · 2015–2024 · Backtest, not live results")
9. Both trade every day, so tiny costs pile up.
   (On screen: "2,515 buys + 2,515 sells · overnight, 10 years") (Visual: Qube's trade list scrolling fast)
10. And just holding SPY the whole time? About $28,500. That beat both.
   (Visual: a gold "Just holding" line draws in above both lines; pops in on "$28,500") (On screen: "Just holding: $10,000 → $28,529 · SPY · 2015–2024 · price only, no dividends · Backtest, not live results")
11. Run two checks before you trust any rule from a video. One, add the costs. Two, compare it to just holding.
   (On screen, builds as he counts: "1. Add the costs" then "2. Compare it to just holding") (Visual: the Qube chart with all four lines stays up behind the list)
12. Comment QUBE and I'll send you the free link and a step-by-step on building your first strategy.
   (Visual: last 2 seconds, end screen) (On screen: "Comment QUBE")

## Notes
Second hook: line 10 (about 72%) · Open loop: line 6 (about 45%), closed at line 8 · Payoff: line 11 (about 80%)
Facts used (all from `claims-and-proof` → "TQX's own backtests" → SPY overnight vs daytime row, `tools/overnight-test.py`; $10,000 each, compounded, Jan 2 2015 – Dec 31 2024, Yahoo Finance daily prices, split-adjusted, no dividends):
- "almost doubled" / $19,225 / 2,515 round trips → overnight, no costs (+92.3%)
- "about $14,800" / $14,771 → daytime, no costs (+47.7%)
- "one cent per $100 on every buy and every sell" / 0.01% → the cost in the same row (0.01% per side, checked in `tools/overnight-test.py`: `(1 - 0.0001) ** 2` per day)
- "about $11,600" / $11,625 → overnight with the cost (+16.3%)
- "Daytime actually lost money" / $8,930 → daytime with the cost (−10.7%)
- "2,515 buys + 2,515 sells" → 2,515 round trips, a buy and a sell each
- "about $28,500" / $28,529 → just holding SPY, price only (+185.3%)
- Paper title, authors, journal, year → same row (Lou, Polk & Skouras, Journal of Financial Economics, 2019). Our numbers only, none of the paper's.
- "about 500 of the biggest US companies" → `terminology` (S&P 500 row; SPY holds the S&P 500)
Labels: "Backtest, not live results" and "SPY · 2015–2024" on every result; "price only, no dividends" on the holding line.
Not used: the "two crowds" explanation (not in `claims-and-proof`), the optional Claude/Codex line (kept Joshua typing into Qube himself, and inside 55s).
Before filming (from the brief, still open): every Qube screen above must be a real Qube run of this test. The numbers came from our Python script, not Qube. If Qube can't buy at the close and sell at the next open, add a cost per buy and sell, or draw a holding line, that beat comes off the Qube screen and is labelled as TQX's own test. If Qube shows different numbers, stop and tell Mark. The CTA's "step-by-step" needs the Breakdown DM live in ManyChat.
