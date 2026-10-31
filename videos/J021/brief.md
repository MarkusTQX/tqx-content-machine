# J021 · I tested the overnight trick in Qube
Presenter: Joshua · Persona: Daniel, the burned retail trader · Why they care: he trades the open on his phone, and the viral claim says the gains happen while he's asleep. He wants to know if he should switch, without risking money to find out.
Source: knowledge/cards/reference/2026-09-23_joe.investss_overnight-returns-stock-market-is-broken.md (same topic: 2026-09-20_svermm_night-trading-beats-day-trading.md, 2026-09-29_markvictorn_micron-overnight-trade.md). Mark's direction: recreate it for Joshua with Qube placed visibly in the video.
Outside gold to aim at: #5 @svermm "Night trading beats day trading" (1.32x likes to followers, the strongest of the three). Keep its moves: chart pinned in the top third above the face from the first cut, number in the first beat, "now the exact opposite" flip, a spoken open loop just before the answer. Borrow one beat from #6 @markvictorn: the paper's title and authors on screen right after the flip. Beat all three where they fail: none of them gives the viewer anything to do, and svermm's ending contradicts his own hook. Ours ends on a tested answer and two checks the viewer can run.
Shape: 5, shock number → the opposite → why (kept from the original, per `remix-for-product`) · Target length: 45–55s, about 145–175 words at Joshua's 3.2 words a second (originals ran 42–56s)
Enemy → difference: Get-rich numbers with no costs and no test behind them (the "up millions of percent" pattern; call out the pattern, never the creators) → Test it before you risk it.
Product: Qube · Placement: first 8s. Qube is how the rule gets tested on screen, so it's the answer: say "Qube" in the hook and keep a Qube screen pinned in the top third the whole way through. Keyword CTA is the last spoken line.
The promise (what the hook promises): I'll test the viral "buy at the close, sell at the open" rule on ten years of the S&P 500 in Qube and show you what really happens.
The payoff (what they walk away with, usable today): Overnight did beat daytime, but a cost of one cent per $100 traded wiped out most of it, and both lost to just holding. Plus two checks to run on any viral rule before trying it: add the cost of every buy and sell, and compare it to just holding.
CTA: "Comment QUBE and I'll send you the free link and a step-by-step on building your first strategy."
Facts we can use: all from `claims-and-proof` → "TQX's own backtests" → SPY overnight vs daytime row (`tools/overnight-test.py`). $10,000 each, compounded, Jan 2 2015 – Dec 31 2024, 2,516 trading days, Yahoo Finance daily prices (split-adjusted, no dividends).
- Overnight (buy at the close, sell at the next open): $19,225 (+92.3%), 2,515 round trips, worst drop −29.4%.
- Daytime (buy at the open, sell at the close): $14,771 (+47.7%), worst drop −24.6%.
- Just holding SPY (price only): $28,529 (+185.3%).
- With a 0.01% cost on every buy and every sell: overnight $11,625 (+16.3%), daytime $8,930 (−10.7%).
- Allowed wording: "Overnight beat daytime. But both lost to just holding, and a tiny trading cost wiped most of it out." Label on every result: "Backtest, not live results", plus "SPY · 2015–2024 · price only, no dividends".
- The paper: Lou, Polk & Skouras, "A tug of war: overnight versus intraday expected returns", Journal of Financial Economics, 2019. Show title and authors on screen as proof the pattern is studied. Quote our numbers only, never the paper's.
- The "two crowds" explanation (retail at the open, institutions into the close): **needs sourcing.** It isn't in `claims-and-proof`. Default: skip the "why" beat (it's a second idea anyway) and use the cost twist as the open loop instead. Only add a one-line "why" if the paper's own explanation is added to `claims-and-proof` first.
Not a repeat of: J016 (SPY dip rule built in Qube, twist "made money, still lost to just holding"; written, not filmed) is the closest. Keep J021's lead twist on the trading cost, with holding as the second, shorter beat, so the two don't land the same punchline. M02 (holding the S&P 500 beats the average investor) shares the "just hold" fact but not the rule or the test. No other match.
Don't copy: the "138 million percent" / "+138,330,342%" Micron number and the "-99.92%" flip (unsourced, no costs; Mark: never use them); the "The stock market is broken" headline; the unnamed "research paper" and the millions-percent ticker list; "you need to start night trading" as an instruction; "you're statistically more likely to make profit"; "see my portfolio" / "see my trades in real time" offers; the portfolio screenshot; their footage and charts. (Their wording is now copied on purpose: Mark, Oct 23.)

## Engine and beats (for the outline)

| Time | Beat | Spoken (direction, not lines) | Qube on screen (top third, face below) |
|---|---|---|---|
| 0–5s | Hook | Joshua's "If you..." opener: the rule in plain words + "watch me test it in Qube" | Frame 1: Qube backtest chart, overnight vs daytime lines, "Backtest, not live results" |
| 5–12s | The rule, tested | Type it in: "Buy SPY at the close every day, sell at the next open." Say what SPY is (a fund of about 500 of the biggest US companies). $10,000, ten years → almost doubled, about $19,200 | Screen recording: the sentence typed into Qube, rules appear, backtest runs, "+$9,225 · 2015–2024 · 2,515 round trips" |
| 12–18s | Flip | "Now the exact opposite": buy at the open, sell at the close → about $14,800, up about half | Same rule edited in Qube, rerun, second line appears in red/grey |
| 18–23s | Proof it's studied | Not a fluke: there's a published paper on this exact pattern | Paper title card: Lou, Polk & Skouras, Journal of Financial Economics, 2019 |
| 23–27s | Second hook / open loop (~50–60%) | "So should you start doing this?" then the part those videos skip: costs | Cursor on Qube's cost setting |
| 27–38s | Twist: costs | Every buy and every sell costs something. Add one cent per $100 traded, rerun: overnight falls to about $11,600; daytime loses money ($8,900). It traded about 2,500 times, so the tiny cost adds up | Qube rerun with the cost on, overnight line collapses: "Overnight $11,625 · Daytime $8,930 · 0.01% per buy and sell" |
| 38–46s | Payoff (~80%) | Just holding the S&P 500 the whole time: about $28,500. Overnight beat daytime, but both lost to doing nothing. The two checks: add the cost of every trade, compare it to just holding | Holding line added on top, "Just holding: +$18,529" |
| 46–52s | CTA | Keyword CTA, last spoken line | End screen "Comment QUBE" |

Notes for the Scriptwriter:
- It's holding overnight, not trading at night. Say it the way Daniel would get it: you buy right before the market closes and sell the second it opens. Frank will catch "night trading" used loosely.
- Counts: 2,515 round trips is a buy and a sell each day. The cost is 0.01% on each side, so say "every buy and every sell", not "per trade" without saying which.
- Numbers said the way people talk ("almost doubled", "up about half", "nearly tripled"), exact figures on screen.
- Optional Claude line (fix-log, Oct 15): "You can type the same sentence into Claude or Codex and it sends it straight to Qube." One line only. Joshua's strongest mode is typing into Qube himself.
- Never tell the viewer to start this rule. End on the test, not on "do this".

## Needs Mark before filming

1. **A real Qube run of this test, screen-recorded.** The numbers above came from our Python script, not from Qube. `claims-and-proof` says product results must be real Qube screens, and if Qube shows different numbers we stop and tell you. Someone needs to check with the Qube team that Qube can (a) buy at the close and sell at the next open on daily prices, (b) add a cost per buy and sell, and (c) show a buy-and-hold line. If it can't do one of these, that beat moves off the Qube screen and is labelled as TQX's own test.
2. **The Breakdown DM still isn't live in ManyChat.** The QUBE CTA promises "a step-by-step"; until you add that DM, the CTA promises more than the flow sends.
