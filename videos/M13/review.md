SCRIPT: M13 · I ranked 6 AI trading apps from S to F (Mark)
VERDICT: Send back to Scriptwriter (round 1)

Score: 7.5 / 10

Vs the format (our M05; no outside original): hook 9 · engine 9 · energy 8 · reward 7 · CTA 9 · Qube 8 · language 7 · copy / past-video repeat 7

- Hook 9: Mark's own line on M05's formula, makes sense cold, count and promise clear.
- Engine 9: M05's beat order kept: hook → bias → F to A, one beat each → re-hook → product in S → debate + keyword. One app every 4–5s, which is tighter than M05.
- Energy 8: Mark's pace, tier word on its own, no setup lines.
- Reward 7: the S tier doesn't clearly beat the A tier. Composer's credit ("AI builds and tests your strategy") is almost Qube's pitch. Composer's own site says "AI-powered strategy creation" in natural language plus backtesting. Its catch (live trading US only) is never answered by Qube's lines, so a viewer in HK or SG is left asking "so is Qube any different?"
- Language 7: line 7 ("See the split? Bottom three, someone else's call. Top three, you test your own.") is clipped note-speak. "You test your own" never says own what. A guy from LA doesn't say "see the split".
- Copy 7: line 7 repeats J028's re-hook frame ("See the problem? Grok, Perplexity and Claude all dump the testing on you."): same "See the ___?" plus a named group. Line 1 reuses M05's "...because we built one." Both break the brief's "fresh words" rule.

Checker: `python3 tools/check-script.py videos/M13/M13-1-SCRIPT.md` gives 160 spoken words (hook 15, script 145), about 53s at 3.0 w/s, no flags. Inside 35–60s and inside the brief's 150–165 words. After the fixes below, expect about 168–172 words, about 56–57s. That's still under 60. Cap is 172 words: if the checker shows more, cut "too" in line 3 and "any" in line 9 first. Never cut from the split line or the Qube lines.

## List pattern (Oct 28 rule, J029)
Lines 2–6 all follow `Name. X tier. [what it is], but [the catch].` exactly: tier always second, catch always after "but", no entry drops it. Clean. Qube (lines 8–9) keeps name → tier → what it does, as the brief allows for the payoff. No change.

## Fixes

| Line | Problem | Rule (skill) | Fix |
|---|---|---|---|
| 1 | "Fair warning, we built one." owns the bias but never marks the ranking as opinion. It also reuses M05's words ("because we built one"). And "built one" of what? | `finance-compliance` Always #6 (mark rankings as opinion), brief "Don't copy" (M05's bias line, words fresh), hook-only-copy / past-video check | **"Just my take, and fair warning, one of these is ours."** (11 words) |
| 7 | (a) Same frame as J028's re-hook "See the problem? …" (past-video repeat). (b) Note-speak fragments and a dangling "your own". (c) Logic: 3Commas's catch was "you pick a preset and tweak it", so "someone else's call" doesn't fit it. Kai, who runs 3Commas, would say "I set my own settings." | Past-video repeat (`fix-log` Oct 27 J032, `script-critic` copy check), `spoken-sentence-rules` (no fragment that leaves the listener waiting), `tqx-voice` Mark (flip with a short line), `script-logic` #3b | **"Here's the line. Below it, you're running their bots or their picks. Above it, you test your own strategy."** (19 words). It matches the line the board draws between C and B, covers all three bottom catches (marketplace strategy and preset bot = their bots, Holly = their picks) and is new against M05 and J028. Re-record the close-up take with these words. |
| 6 → 8–9 | The A-tier catch ("live trading is US only") isn't answered by the S tier. Composer also says AI builds and backtests, so Qube's lines don't show why it sits above A. | `script-logic` #3b (a question left open is an automatic send-back), #1 (payoff), #12 (region fit) | **Preferred:** Mark answers one product fact that `product-truth-qube` lists as unknown: can Qube go live through a broker outside the US? If yes, line 9 becomes **"Qube tests it on years of prices and shows you every trade, losers too, and it's not US only."** Then keep "before real money goes in" by ending line 8 there or folding it in, max 20 words a sentence. **If no or unknown (fallback, all sourced):** line 9 becomes **"Qube tests it on years of US and Hong Kong prices. You see every trade, losers too, before real money goes in."** (HK and US templates are on the Qube page, `product-truth-qube`.) Don't say or imply Qube trades live outside the US unless Mark confirms it. |
| 8 | "You type your strategy in plain English…" is close to M05's "You describe the idea in plain English" and J033's "you just type your strategy in plain English". | Past-video overlap | **Keep.** This is Qube's approved one-line wording family (`product-truth-qube`, J022/J024). Repeating it is by design, not a copy. Flag only. |
| 2–6 | Fairness. Every catch is fair and none implies a scam, results or prices. Cryptohopper also has a strategy designer, so the line is fair only because it names "its marketplace". | `positioning` (describe from their site, ranking as opinion), `finance-compliance` (scams) | **Keep as written.** Never change line 2 to "only sells" or "all you get". |

## Docs to update (same round)
| Doc | Problem | Fix |
|---|---|---|
| EDIT + ASSETS A1 | Brief: first frame shows **five** logos waiting. EDIT and A1 stack **six**, including Qube, which gives away the S-tier payoff at 0s. | A1: five logos plus a grey "?" tile in the sixth slot. Qube's logo appears for the first time on the S hit. |
| EDIT 5.0–6.7 + ASSETS A3 | Big text "We built one" | Change to **"One of these is ours"**, plus a small "my take" tag. Re-time the row for the 11-word line (about 3.7s). |
| EDIT 30.0–34.7 + ASSETS A2 split overlay | Labels "their call" / "you test it" | Change to **"their bots · their picks"** (grey, F/D/C) and **"your strategy, tested"** (gold, B/A/S). The white line between C and B lands on "Here's the line." |
| EDIT 39.7–46.3 | If the fallback line 9 is used | Add "US + HK stocks" next to "Backtest, not live results". Keep the backtest label from the first result frame to the end of the line. |
| ASSETS A0 step 5 | Old split words | Use the new line 7 words for the close-up take. |
| beatmap.md | Says "none of M05's sentences is reused" while line 1 reuses M05's "we built one". Count and timings change after the fixes. | Update the line 1 and line 7 rows, the count, the "every sentence sells the next" chain (add the A → S answer), and re-run the checker. Carry the new times into EDIT. |
| SCRIPT header | Word count | Update "ours 160 words" and the length after the fixes. |

## Compliance: clean
- "Backtest, not live results" stays on screen whenever a Qube result or trade list shows. Losses are shown (A5 CHECK requires a red row before "losers too").
- No prices, results or win rates for any app; blur rule in ASSETS.
- No scam implication; Composer's US-only is sourced on screen.
- Standard CTA with the approved debate lead-in (`cta-and-offer`). "Original video" link written out.
- No banned phrases. "Before real money goes in" keeps test-before-risk.
- After fix 1, the ranking is marked as opinion.

## Flow to the S payoff (after the fixes)
6 apps ranked → my take, one is ours → worst: its marketplace sells you someone else's strategy → presets you tweak → the AI's calls → good testing, heavy to learn → strong, but live is US only → here's the line: their bots or picks below, your own strategy tested above → Qube: your strategy in plain English or Claude/Codex → tested on years of prices, every trade, losers too, and it answers A's catch → argue or comment QUBE.

## Facts checked
- Composer live trading US only → help.composer.trade/article/62-international-users, checked today Oct 28: "Composer live trading is not currently available to international users outside of the US." OK.
- Composer credit "AI builds and tests your strategy" → composer.trade: "Build trading algorithms with AI, backtest them, then execute", "AI-powered strategy creation". OK. This is also why the S line has to answer A.
- Cryptohopper marketplace → cryptohopper.com: "buy strategies and bot templates from our marketplace"; also AI and a strategy designer. OK as written.
- 3Commas, Trade Ideas, TrendSpider → the writer's site checks (beatmap table). Each is a fair, opinion-framed catch with no figures.
- Qube: plain English, Claude/Codex, years of prices, every trade, free sign-up, HK + US templates → `product-truth-qube`. Live trading region → **unknown, Mark only**.

## Past videos checked
- M05: format by Mark's choice. Line 1 reused M05's wording (fix 1).
- J028: line 7 had the same re-hook frame (fix 2). The Qube wording overlap is approved product wording.
- J029, J033: no other overlap. Third S-to-F board is Mark's call (brief flag).

Mark's own lines flagged, not changed: the hook (Mark's, Oct 28, kept) and the tier order (Director's pick, Mark can move any app).
Only Mark can decide: whether Qube can go live outside the US (picks the line 9 version).
