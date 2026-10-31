# Approval · J026

Verdict: APPROVED for Mark (re-check, Oct 25). All 5 fixes from the light send-back landed in EDIT and ASSETS. SCRIPT unchanged word for word (diff against -v3-prev is empty). Nothing else changed, nothing broke. The earlier send-back is kept below as the record (copy in approval-v1-prev.md).

## Re-check of the 5 fixes

| # | Fix | Landed? | Where checked |
|---|---|---|---|
| 1 | A1: backtest moment before any result, trader moment with no balance/P&L, "pick another frame" if a number shows | Yes | ASSETS A1 steps 2–3, EDIT row 1.7–2.7 |
| 2 | A4: tell the editor if a template card shows a result; label it if so | Yes | ASSETS A4 CHECK, EDIT row 5.0–6.2, EDIT labels line |
| 3 | No 0.1s gaps: each item holds until the next cuts in | Yes | EDIT Timing line, and every table row now runs end to start (2.7–4.0 … 11.5–12.7); item 6's scale note now says "its 1.2s" |
| 4 | A11: title one line, 960px max, item 7 alone to 68px | Yes | ASSETS A11 item 2, matches EDIT text style |
| 5 | A6 uses A3's fixed version; A8 in the same Claude session, after A6 | Yes | ASSETS A6 step 1, A8 step 2 |

Compliance: signed off. Every number on an insert is now either labelled or kept off screen.

## Earlier send-back (fixes, all landed)

The on-screen text is clean. Two of these are compliance gaps in the inserts (labels a viewer could miss), and three are editor-precision gaps (fix-log Oct 12: "so precise that nobody could mess this up").

1. **ASSETS A1 (and EDIT row 1.7–2.7) · unlabelled backtest and simulation moments.** A1 step 2 cuts in "the backtest agent running the test" and "the trader agent on the simulation account". At about 0.17s each, a result number or a simulated balance can flash with no "Backtest, not live results" and no "Paper trading · simulated results" on it. Only "Claude · Codex → Qube" is on A1. (`finance-compliance` Always #1–2, `on-screen-text` required labels)
   - "the backtest agent running the test, the trader agent on the simulation account"
   - → "the backtest agent starting the test (before any result shows), the trader agent placing the order on the simulation account (no balance, P&L or result showing)"
   - Add to A1 step 3: "No backtest result, balance or P&L may show in any of the 6 moments. A label can't be read at 0.17s, so if a moment shows a number, pick another frame."

2. **ASSETS A4 (and EDIT row 5.0–6.1) · template cards may carry sample results.** A4 and its EDIT row say "No label". If Qube's template list shows a return, Sharpe or trade count on any card, it goes out unlabelled. (`finance-compliance` Always #1, `product-truth-qube`: the page's sample result carries its label)
   - Add to A4's CHECK: "If any template card shows a return, Sharpe or trade number, tell the editor."
   - EDIT row 5.0–6.1: "No label" → "No label, unless a template card shows a result number. Then "Backtest, not live results" top-left."

3. **EDIT · 0.1s gaps between items.** The table runs 2.7–3.9, then 4.0–4.9, then 5.0–6.1, and so on, so nine 0.1s gaps have no instruction. The editor has to guess: a blank desk frame, or hold? (`storyboarding`, fix-log Oct 12)
   - Add to the "Timing" line: "Each item holds until the next one cuts in. No gaps: 1.7–2.7, 2.7–4.0, 4.0–5.0, 5.0–6.2, 6.2–7.2, 7.2–8.4, 8.4–9.4, 9.4–10.5, 10.5–11.5, 11.5–12.7, CTA 12.7–14.0."

4. **ASSETS A11 item 2 · title rule missing from the text pack.** The critic's optional note, now required, since the editor builds the text from A11. (`on-screen-text`)
   - "title "N. Title" at 76px gold" → "title "N. Title" at 76px gold, one line, 960px wide at most. If item 7's title doesn't fit, drop that title alone to 68px."

5. **ASSETS A6 and A8 · which strategy.** A6 says "open the A2 strategy" without saying which version, and A8 doesn't say which Claude session. Item 8 says "your tested strategy", so A6 and A8 must use the same strategy that was tested and fixed, in the order test → simulation → live. (`script-logic` #5)
   - A6 step 1: "open the A2 strategy" → "open the A2 strategy (A3's fixed version, the one A9 uses)"
   - A8 step 2: "In Claude, type exactly" → "In the same Claude session as A2 and A3, after A6 is recorded, type exactly"

## The Director's checks

| Check | Result |
|---|---|
| Side by side with @raycfu: would a viewer of it recognise ours? | Yes, beat for beat. 3-line serif title with 3 highlighted words (0–1.7s), 10 items about 1.1s each with a gold title, white subtitle and a middle insert, keyword CTA over the same locked desk shot, loop back to frame 1, 14s, no voice, music only. |
| Is ours at least as strong line by line? | Mostly yes. Inserts are stronger: each shows exactly what its line says, where theirs showed an empty 0/12 dashboard, a Pocket Option chart under "wallets" and a 2023 terminal. Item 1 (agents really working) and item 10 (one prompt, 10 stocks, built and tested) beat theirs. Weaker, by fixed limits only: the hook ("trade" vs "make money", `finance-compliance` Never #1), the CTA (a link vs templates, `cta-and-offer`), and the two big middle visuals (a simulation screen and a live start, vs a shocked face and Man City). |
| The original's script with Qube slipped in, or a rewrite? | Slipped in. 7 of 13 units kept or small swaps ("10 ways … with [AI]", "Multi-Agent Trading", "Auto Bug ___ / Finds ___ and ___", "AI ___ Engine", "Builds ___ from a single text brief", "Comment "X" to get ___"). The 6 rewrites are items that aren't trading, or are copy trading, "24/7" or price tags, and each keeps its slot's job (money word up front, big visuals at 6 and 8, re-hook at 67%). Qube comes in on item 1, where the original first shows a tool. |
| Promise paid off, payoff usable? | Yes. "10 ways to trade with Claude" → 10 real things by 12.6s, each with its real screen, plus the free sign-up link. More usable than the original, whose "how" sat behind the DM. |
| One persona, one shape, one idea, one enemy → difference? | Priya · numbered list (shape 2) · one idea: 10 things Claude and Qube do for a trader, no code · Wall Street gatekeeping (implied) → pro quant tools, no code (multi-agent, backtests, factor research, optimization). |
| Word count | On-screen only (nothing spoken in either). Subtitles 95 vs 87 (+9%, range 78–96), titles 25 vs 25, all text 136 vs 131. Each subtitle 8–11 words (original 4–12). Pass. |
| Compliance (final sign-off) | Text clean: no "make money", no return, win rate or dollar figure, no ticker call, no named broker. Live comes after simulation, and "tested" sits in item 8. Labels on items 5, 6, 7, 9, 10 and the hindsight label on 10. A5 (62 trades, +$4,428) and A10 (607 trades, +$8,147) match `claims-and-proof` rows exactly, with stop-and-tell CHECKs. The two insert gaps (fixes 1 and 2) are closed. Signed off. |
| Would Frank find anything wrong? | Nothing now that fixes 1–2 are in. One thing for Mark to look at, not a fix: "Hands-Free Live Trading" is close to how bot scams pitch themselves. "your tested strategy" in the subtitle answers it, so it stays. If Mark wants it safer, "Live Trading" alone is his call. |
| Mark's own lines | Kept as written: item 2 "Build a strategy from natural language" (J022 line 1), item 3 "Finds what's broken in your strategy and fixes it" (J022 line 5), item 6 "simulation account" (P1 still open). |
| Blanks, placeholders, unsourced numbers | None in the SCRIPT. "6 specialized agents" is Mark's M23 firm; "20-day momentum", "US and HK", "years of prices" and "a real broker" are in `product-truth-qube`; "10-stock" is A10's own test. |

## Still open for Mark (shoot blockers, not script blockers)
- Item 6 (A6): which Qube screen shows the simulation account running.
- Item 8 (A8): which screen and account show Claude starting a live run, and whether a live broker connection is set up for Joshua.
- Item 1 (A1): M23's real run or the org-chart fallback.
- P1: "simulation account" next to the "Paper trading · simulated results" badge.
- Hook "make money" → "trade", the link-only CTA, and item 10's longer hindsight label.

Score vs the gold: the format is raycfu's beat for beat, and the inserts are more honest and stronger than his. It sits just under the original (critic 8.1) only where compliance caps it: the hook's money word, the CTA's offer and the two big middle visuals.
