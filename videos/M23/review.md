SCRIPT: M23 · I built a quant trading firm on Claude
VERDICT: Send back to Scriptwriter (light round: 4 small line fixes, 3 EDIT/ASSETS fixes, no rework)

Vs the original (@raycfu "AI agent trading firm", 192 words): hook 9 · engine 9 · energy 8 · reward 8 · CTA 8 · Qube 9 · language 8 · copy 8 · word count 9 · flow 8

| Score | Why |
|---|---|
| Hook 9 | Mark's own line, not scored down. A big claim made small ("a quant trading firm" / "on Claude") plus a count that opens the loop. Paid off: all 6 agents named by line 7 (about 28–35s). |
| Engine 9 | Same beats, same order: claim → one input, "the entire firm goes to work" → "Here's how I built it out" → role by role → "but a separate risk manager has the power to say no" → "The best part is…" at 67% → landing → keyword. Recognisable as raycfu's. |
| Energy 8 | Short lines, a stamp on every "no", a re-hook at 67%. Drag: lines 3–7 all open "The ___ agent…", five times in a row (`anti-ai-patterns` #11). raycfu breaks it with "Then a trader agent…". Fix on line 7. |
| Reward 8 | More usable than the original: six jobs in order, the risk manager's exact no-rules, the fix-and-retest loop, backtest → simulation account → live, and a free tool. Line 5 is thin out loud, but the four section chips on screen make up for it. |
| CTA 8 | The standard CTA is Mark's, so it isn't scored down. The one point lost is the lead-in: line 14 is about Mark ("I built…") and never turns to the viewer, so nothing hands over to the comment. raycfu's offer line says "for yourself". Fix on line 14. |
| Qube 9 | Comes in where raycfu's org chart and tool start, with Mark's line word for word. It's on screen for strategy, backtest and trader, and the CTA is "Comment QUBE…". |
| Language 8 | Mostly LA-plain. "pulls up to five years" can be heard as "pulls up" (line 4). |
| Copy 8 | 6 of raycfu's 10 sentences (not counting the hook) are kept or small swaps. Every rewrite has a reason in the brief: no debate agent, no memory claim, no guide. Lines 8–10 are new, built from raycfu's "Vetoed: 3.4% position" card, which is fair. |
| Word count 9 | 208 against 192 (+8.3%; range 173–211). With the fixes below it's 211, still in range but at the ceiling. |
| Flow 8 | Every "it", "that" and "those" checks out (table below), and lines 1–13 each lead into the next. Two small gaps: Qube is named in line 2 but nobody hears what it is until line 5 (fixed on screen, below), and line 14 doesn't sell line 15. |

Checker: `python3 tools/check-script.py videos/M23/M23-1-SCRIPT.md` → "Spoken words: 208 (top hook 15 + script 193) · about 69s at 3.0 words/s · LENGTH: over 60s… · No flags."
- LENGTH over 60s: accepted. This is a recreation matched on words, not seconds (`script-logic` #10), and the script header and brief both say why. With the fixes the checker reads 211 words, about 70s, no flags (tested on a scratch copy).
- Nothing else flagged. No sentence goes over 20 words (the longest, line 7, is 19, or 20 with the fix).

## Line by line (first-time viewer read)

| Line | Clear? What "it/this/that" points to | Leads into the next? |
|---|---|---|
| Hook | Yes (Mark's) | Yes: "6 agents" → what do they do? |
| 1 | "the entire firm" = the hook's firm | Yes: "how?" |
| 2 | "built it out" = the firm. **Qube isn't explained** | Partly: "What's Qube?" hangs until line 5 |
| 3 | "that stock" = line 1's ticker (one line back, across line 2: OK) | Yes |
| 4 | "its" = that stock. **"pulls up to" mishears** | Yes |
| 5 | Clear | Yes |
| 6 | "it" = the strategy, "those prices" = line 4's data | Yes |
| 7 | "trade it" = the strategy | Yes, the twist |
| 8 | "It" = the risk manager | Yes |
| 9 | "we" = Mark's firm. Fine | Yes |
| 10 | Clear | Yes, sets up line 12 |
| 11 | Clear, doesn't give away the next beat (`retention-writing` #3) | Yes |
| 12 | "tests it" = the strategy, "it's a yes" answers line 10's "it's a no" | Yes: "That's when" |
| 13 | "That's when" = the yes, "runs it" = the strategy | Yes |
| 14 | "this whole firm" echoes the hook | **Weak**: doesn't turn to "you" before the CTA |
| 15 | Standard CTA (Mark) | End |

## Fixes

| Line | Problem | Rule (skill) | Fix |
|---|---|---|---|
| 4 · "The data agent pulls up to five years of its price data." | Out loud, "pulls up to five years" can be heard as "pulls up" (opens), then "to five years" | Words people say, read-aloud test (`spoken-sentence-rules` #3) | "The data agent grabs up to five years of its price data." (same word count) |
| 7 · "The trader agent is ready to trade it, but a separate risk manager has the power to say no." | Fifth line in a row that opens "The ___ agent…", which sounds like a list being read off. raycfu's own line opens "Then a trader agent…" | Over-tidy symmetry (`anti-ai-patterns` #11), keep the original's copy (`remix-for-product`) | "Then the trader agent is ready to trade it, but a separate risk manager has the power to say no." (+1 word) |
| 8 · "It says no to any trade that risks more than 2% of the account." | Not wrong. A one-word trim to pay for line 14, and it then matches the A7 card word for word ("any trade risking more than 2% of the account") | Word range (`script-logic` #10), on-screen matches the voice (`on-screen-text`) | "It says no to any trade risking more than 2% of the account." (−1 word) |
| 14 · "I built this whole firm without writing any code." | Stays on Mark ("I built…"), so it doesn't sell the CTA. raycfu's offer line hands it to the viewer ("how to build this out for yourself"). Without a "you", the jump to "Comment QUBE" has no reason behind it | Every sentence sells the next one (`script-logic` #3b), the landing line is TQX's point (`positioning`) | "I built this whole firm without writing any code. You can too." (+3 words) |

New total: 211 words (hook 15 + 196). In range (173–211), but at the ceiling: if Mark adds a word on the day, cut "And" from line 10.

## EDIT and ASSETS fixes

| Where | Problem | Rule (skill) | Fix |
|---|---|---|---|
| EDIT · 9.3–13.7 (line 2), on-screen text | A first-time viewer hears "Qube" with no idea what it is, and won't find out for three lines. "Claude → Qube" adds nothing to the voice | Make sense to a first-time viewer (fix-log Oct 23 "How does that make sense to a first time viewer?"), on-screen adds information (`on-screen-text`) | On-screen text, pops on "Qube", holds to the end of the line: "Qube · builds and tests strategies · no code" ("no code" gold). Keep the "Claude · Codex → Qube" label top-left on the recording |
| EDIT · Layout, "The org chart (A1) is the thread… pinned at the top of the top third whenever a screen recording is under it" | A1 is 1080×360, which leaves a 1080×280 band of the 640 top third for the 16:9 recordings. A terminal recording that small can't be read, and the editor has to guess how to fit it | Precise enough that nobody could get it wrong (fix-log Oct 12) | Replace with: "On the word each agent is named, A1 fills the top third for 1s with that box lighting up. Then cut to that agent's recording, full width in the top third (1080×640, scaled to fit width, centred), with A1 hidden. A1 comes back on the next agent's name. Exception: rule cards A7 (1)–(3) sit under the red A1 (8) as written." |
| EDIT · 56.3–62.3 (line 13), on-screen text | "Simulation account" is said but never explained. Priya doesn't know the jargon (`audience-profile`), and `terminology` says explain it: "a fake-money account" | Explain a term the moment it appears (`terminology` #2) | Small second line under the A10 path, pops on "simulation account": "simulation account = no real money" (Inter Bold 36px, light grey #9AA3AE). Nothing spoken changes |
| ASSETS · "Before recording anything… Mark's six-agent firm is set up in that Claude session" | Doesn't say who sets up the six agents or how, and the risk manager's settings have to match lines 8–10 or the A8 "no" won't match the voice | No blanks, full instructions (fix-log Oct 11, Oct 12) | New step before A2: "Mark (or the Qube team) checks that the six agents exist in that Claude session with these jobs: research (news and earnings on the ticker), data (up to five years of price data), strategy (builds it in Qube), backtest (tests it in Qube), risk manager (says no to any trade risking more than 2% of the account, stops trading for the day at the max loss, says no if the backtest doesn't hold up), trader (simulation account only for this video). If any are missing, tell Mark before recording." |
| ASSETS · A2 step 4, "Hold 3s on the screen that shows Qube is connected" | Which screen? The creator has nothing to type or look for (`product-truth-qube`: the setup steps aren't written down yet) | "Screen recording of what?" (fix-log Oct 12) | Add to "Still open (Mark)": "A2 step 4: the Qube team names the exact command or screen that shows Qube connected in Claude (no keys or file paths in shot). Until then, step 4 can't be filmed." |
| ASSETS · A8 CHECK | Lines 10–12 describe a "no" because the backtest doesn't hold up, followed by a fix-and-retest loop. If the real run says no for the 2% or the max-loss reason, the screen won't match the voice | Screen matches the script, never staged (`claims-and-proof` "Proof on screen") | Add to the A8 CHECK: "The 'no' must be the risk manager's backtest reason (the backtest doesn't hold up). If it says no for a different reason, send Mark the screenshot before the edit." |

## Passes

- Pass 1 (worth making): clean. Persona is Priya. She gets a six-job org chart, exact no-rules, the order to run it in, and a free tool. Not a repeat: J017 is the GATC version, as the brief notes.
- Pass 2 (logic): promise = six agents, one job each → paid off in lines 3–7. One idea. Re-hook at 67% (line 11). Full payoff at 73–90% (lines 12–13). Ends 3s after the payoff. Order: build → backtest → risk check → simulation account → live, correct. Word range: in.
- Pass 3 (facts): not fact-checked (Mark, Oct 23). Sources listed below.
- Pass 4 (product truth): clean. "Up to five years", live through a real broker, and Claude trading through Qube are all in `product-truth-qube`. No TQX OS.
- Pass 5 (compliance): clean. NVDA has "Example" under it and no "buy" next to it. "Backtest, not live results" is on A6 and A8. Simulation-account frames carry the badge top-right. No returns, win rates or trade counts.
- Pass 6 (spoken lines): fixes on lines 4 and 14 above. One term per thing: "simulation account", "strategy", "risk manager" are each used the same way all the way through.
- Pass 7 (hook): makes sense cold, has a number ("6") and a name ("Claude"), and line 1 doesn't repeat it.
- Pass 8 (on-screen): every line has a visual. Fixes on line 2, line 13 and the layout above.
- Pass 9 (CTA): standard, last spoken line, the DM sends the link. Qube named out loud at about 12.7s, after "connecting" (Mark's placement; the brief's "within the first 8s" doesn't fit at Mark's 3 words a second). On screen from 5.0s through the "Claude · Codex → Qube" label on A2. No change.
- Pass 10 (fix log): every row checked. No "practice account", "trading idea", "rules" for strategy parts, "hooked up", ten-year history, placeholders, trailing sentences, non-standard CTA or TQX OS. Re-hook doesn't give away the next beat. "I start by connecting Qube to Claude." is word for word.

Facts checked (not questioned, sources only):
- "2%" per trade and the daily max loss → Mark's own risk settings (brief, taken as given)
- "up to five years of price data" → `product-truth-qube` (Mark's J020 edit)
- "live through a real broker", Claude trading through the Qube connection → `product-truth-qube` (Mark, Oct 22 and 23)
- "Free · no card required", tqx.ai/igqube2 (A11) → `product-truth-qube`

Needs Mark (only he can decide):
- **P1, "simulation account" vs the badge.** Line 13 says "simulation account" (your J022 wording), but the `finance-compliance` badge reads "Paper trading · simulated results". Both kept as written until you answer P1 (`data/mark-edits/proposals.md`).
- **Line 10, "if the backtest doesn't hold up".** Lines 8 and 9 give exact triggers. This one doesn't. If your risk manager has a real pass mark (for example "loses money in the backtest"), say it and the line can use it. Otherwise it stays.
- **Length.** About 70s at your pace (the original runs 40s at 4.8 words a second). Words matched, as the brief says.

Mark's own lines flagged, not changed:
- Hook: "I built a quant trading firm on Claude. 6 agents, each one has a job." Unchanged.
- Line 2: "I start by connecting Qube to Claude." Unchanged. The "what's Qube?" gap is fixed on screen instead.
- Line 15, the standard CTA: unchanged. The lead-in is fixed on line 14 instead.
