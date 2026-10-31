SCRIPT: J026 · 10 ways to trade with Claude
VERDICT: Ready for Director (round 3, final). Both round-2 fixes landed, nothing broke. Only Mark's-call items remain, none blocking.

Vs the original: hook 7* · engine 9 · energy 8 · reward 8 · CTA 7* · Qube 9 · language 8 · copy 8 · word count PASS · flow 8 · **overall 8.1 / 10** (round 2: 8.0, round 1: 7.6)

\* Hook and CTA sit below the original only because of fixed limits: "make money" is banned (`finance-compliance` Never #1) and the CTA can only promise the link (`cta-and-offer`, Mark Oct 23). Mark's call (brief "Needs Mark" #5, ASSETS "Needs Mark"). Open, not blocking.

## Round 2 fixes

| # | Round 2 fix | Landed? | Where checked |
|---|---|---|---|
| 1 | Item 5 → "Replays any strategy over years of prices, every trade shown" | Yes | SCRIPT item 5, EDIT row 6.2–7.1, beat map row 5 (with the r2 reason). 10 words, same as before |
| 2 | Item 7 → "Checks clues a stock might go up, like 20-day momentum" | Yes | SCRIPT item 7, EDIT row 8.4–9.3, beat map row 7 (with the r2 reason). 10 words, same as before |
| 3 | EDIT text style: titles on one line, 960px max, item 7 title alone drops to 68px if it doesn't fit | Yes | EDIT "Text style (A11)" line. Words unchanged |

"Test" now appears in 6 ("Test-Drive"), 8 ("tested"), 9 and 10 ("tests"), each doing real work, and no two items start with the same verb. The blur from round 2 is gone. No "Tests any" / "Tests clues" left in any of the four docs. ASSETS untouched (it points to "the exact words from the SCRIPT doc", so no stale copy).

## Step 0 · side by side with @raycfu (Dd2dbtOPpv-), brief re-score

**Word count (on-screen, nothing spoken):** unchanged. Subtitles 95 vs 87 (+9%), titles 25 vs 25, all text 136 vs 131 (+4%). Pass. Header word line still correct.

| # | Ours (subtitle, changed rows only) | Round 2 | Round 3 | Why |
|---|---|---|---|---|
| 5 | Replays any strategy over years of prices, every trade shown | 7 | 7 | "Replays" is what a backtest does, says it in plain words, and breaks the "Tests…" run |
| 7 | Checks clues a stock might go up, like 20-day momentum | 7 | 7 | Same line with a different verb; no longer echoes item 5 |
| All other rows | unchanged | | | Scores as round 2 |

Energy holds at 8, language 8 → 8 (cleaner across 5–10); overall up a hair from the repeat being gone.

## Checker

```
python3 tools/check-script.py videos/J026/J026-1-SCRIPT.md
Spoken words: 126 (top hook 6 + script 120) · presenter: joshua · about 39s at 3.2 words/s
No flags.
```
Decision: no flags. The checker counts on-screen text as spoken, so "about 39s" doesn't apply; real length is 14s from the EDIT timing.

## Fixes

| Line | Problem | Rule (skill) | Fix |
|---|---|---|---|
| ASSETS A11 "title "N. Title" at 76px gold" | Optional, not blocking. The new one-line / 960px / 68px-for-item-7 rule is in the EDIT text style but not repeated in A11, which the editor builds the text pack from | `on-screen-text` | If the Director touches ASSETS anyway, add the same sentence to A11 item 2. Otherwise the EDIT line covers it |

## Passes (round 3 re-check)

- **Pass 1 worth making:** pass, unchanged.
- **Pass 2 logic:** pass. Order and promise/payoff unchanged; best item still last.
- **Pass 3 facts:** pass, no new numbers.
- **Pass 4 product truth:** pass. "Replays… every trade shown" = Qube backtest with full trade list (`product-truth-qube`).
- **Pass 5 compliance:** pass. No return words; labels on 5, 6, 7, 9, 10 unchanged.
- **Pass 6 reading the text:** pass. The "test" repeat is fixed. "Simulation account" (Mark's P1) still flagged, not changed.
- **Pass 7 hook:** pass (Mark's call).
- **Pass 8 on-screen:** pass. Item 7 title width now handled in EDIT.
- **Pass 9 CTA:** pass (Mark's call).
- **Pass 10 fix log:** pass. No "trading idea", no fixed price-history length, Qube not in the hook, one hook, standard CTA, original link present.

Facts checked:
- "6 specialized agents" → Mark's M23 firm (taken as given)
- US and HK templates, backtest with every trade, AI optimization over rounds, factor research with 20-day momentum, live through a real broker → `product-truth-qube`
- A5 CHECK 62 trades, +$4,428, $14,428 → `claims-and-proof` TQX backtests row 1
- A10 CHECK 607 trades, +$8,147, $18,147 → `claims-and-proof` TQX backtests row 2
- A9 no fixed number; any number on screen kept as Qube shows it and labelled.

Mark's own lines flagged, not changed (open, not blocking):
- Item 2 "Build a strategy from natural language" (J022 line 1) and item 3 "Finds what's broken in your strategy and fixes it" (J022 line 5): kept as written.
- P1: item 6 "simulation account" next to the "Paper trading · simulated results" badge.
- Hook "make money" → "trade", and the link-only CTA.
- Item 10's longer hindsight label vs the short one.
- Items 6 and 8: which Qube screens to record (shoot blockers, not script blockers).

## Round 1 fixes (kept from round 2)

| # | Round 1 fix | Landed? | Where checked |
|---|---|---|---|
| 1 | Item 9 → "AI Strategy Optimizer: Suggests changes and tests each one, round after round"; A9 = optimization rounds on the A2 strategy, label if a number shows | Yes | SCRIPT item 9, EDIT row 10.5–11.4 (label "Backtest, not live results" top-left), ASSETS A9 (3+ rounds, CHECK, screenshot to Mark if only one round), beat map |
| 2 | Item 10 → "Builds and tests a 10-stock strategy from a single text brief" | Yes | SCRIPT item 10, EDIT row, ASSETS A10, beat map. No longer repeats item 2 |
| 3 | Item 6 title → "Test-Drive Trading", subtitle kept | Yes | SCRIPT, EDIT, beat map. Subtitle unchanged (Mark's "simulation account") |
| 4 | Item 4 → "…breakouts for US and HK stocks"; A4 shows the market | Yes | SCRIPT, EDIT, ASSETS A4 (with a CHECK that "US" and "Hong Kong/HK" are readable) |
| 5 | Item 7 → "Quant-Desk Factor Research" / "Tests clues a stock might go up, like 20-day momentum" | Yes | SCRIPT, EDIT, beat map |
| 6 | "your strategy" in 4 subtitles in a row | Yes | Item 5 now says "any strategy". "your strategy" is left in 3, 6, 8, not back to back after item 3 |
| 7 | A1 = M23's real six-agent run first, org chart only as fallback | Yes | EDIT row 1.7–2.7, labels note, ASSETS A1 (6 agent moments, crop, blur, label), ASSETS notes |
| 8 | Item 10 hindsight label (low priority) | Yes | EDIT row and labels note ("Backtest, not live results · today's biggest stocks", extra frames come from the CTA's start), A11 label list, ASSETS "Needs Mark" (short label is Mark's call) |

Nothing from v1 left behind: no "Strategy Library", "Simulation Trader", "ready to test" or "fully tested" in any of the four docs. Header word line updated (136).

