# Approval · M23

Verdict: SEND BACK (light, EDIT and ASSETS only. The script is approved word for word. Don't change a spoken line. No new REDPEN round needed; MAX re-checks these 4 fixes, then it goes to Mark.)

## REDPEN's 10 light-round fixes: all landed

| # | Fix | Landed? |
|---|---|---|
| 1 | Line 4 "pulls" → "grabs" | Yes |
| 2 | Line 7 opens "Then the trader agent…" | Yes |
| 3 | Line 8 "risking more than 2%" | Yes |
| 4 | Line 14 "+ You can too." | Yes |
| 5 | EDIT line 2: "Qube · builds and tests strategies · no code" | Yes |
| 6 | EDIT layout: A1 shows for 1s, then the agent's recording full width | Yes |
| 7 | EDIT line 13: "simulation account = no real money" | Yes |
| 8 | ASSETS: six-agent check before A2 | Yes |
| 9 | ASSETS: A2 step 4 moved to "Still open (Mark)" | Yes |
| 10 | ASSETS: A8 CHECK on the backtest reason | Yes |

Checker: 211 words (hook 15 + 196), range 173–211, no flags. About 70s; the header says why (words matched, not seconds).

## If send back (fixes)

The script is clean. These are editor-precision gaps (fix-log Oct 12, "Can you be so precise that nobody could mess this up?"). Two of them come from fix 6 meeting asset sizes that didn't change.

1. **ASSETS · A7 is too tall to sit under A1.** A1 is 360px tall and A7 is 480px, so the pair is 840px in a 640px top third. The editor has to guess. (`storyboarding`, fix-log Oct 12)
   - "Canva, 1080×480, dark #0B0F14, 16px rounded corners, red #EF4444 4px border. Inter Bold 48px white, key word in gold #E8B04B."
   - → "Canva, 1080×280, dark #0B0F14, 16px rounded corners, red #EF4444 4px border. Inter Bold 40px white (line 2 can wrap to two lines), key word in gold #E8B04B."

2. **EDIT · Layout paragraph: A1 can't "fill" the top third.** It's 1080×360 (only A1 (12) is 640 tall). Also say where A7 goes.
   - "On the word each agent is named, A1 fills the top third for 1s with that box lighting up."
   - → "On the word each agent is named, A1 (1080×360) shows for 1s, centred in the top third on dark #0B0F14, with that box lighting up."
   - "Exception: rule cards A7 (1)–(3) sit under the red A1 (8) as written."
   - → "Exception: on lines 8–10, the red A1 (8) sits at the top of the top third, and the rule cards A7 (1)–(3) (1080×280) sit directly under it, filling the rest."

3. **EDIT · "Labels that must stay on": two labels in the same corner on A8.** A8 is both a Claude recording ("Claude · Codex → Qube", top-left) and a retest frame ("Backtest, not live results", top-left). (`on-screen-text`, `finance-compliance`: the backtest label must stay readable)
   - "\"Claude · Codex → Qube\" top-left on every Claude recording (A2, A3, A4, A8)."
   - → "\"Claude · Codex → Qube\" top-left on every Claude recording (A2, A3, A4, A8). On A8 it sits directly under \"Backtest, not live results\", same size, 12px gap."

4. **beatmap.md · out of date after the light round** (housekeeping, Mark doesn't see it, but the next agent reads it):
   - "4. \"The data agent pulls up to five years of its price data.\"" → "4. \"The data agent grabs up to five years of its price data.\""
   - "7. \"The trader agent is ready to trade it, but a separate risk manager has the power to say no.\"" → "7. \"Then the trader agent is ready to trade it, but a separate risk manager has the power to say no.\""
   - "8. \"It says no to any trade that risks more than 2% of the account.\"" → "8. \"It says no to any trade risking more than 2% of the account.\""
   - "14. \"I built this whole firm without writing any code.\"" → "14. \"I built this whole firm without writing any code. You can too.\""
   - Length: "208 words (hook 15 + lines 193)… About 69s" → "211 words (hook 15 + lines 196)… About 70s"

## The Director's checks

| Check | Result |
|---|---|
| Side by side with raycfu: would a viewer of it recognise ours? | Yes. Big claim → one ticker in, "the entire firm goes to work" → "Here's how I built it out." → role by role, one line and one card each → "but a separate risk manager has the power to say no" at 45% → "The best part is…" at 67% → landing → keyword. Same order and moments, with punch-ins where his are. |
| The original's script with Qube slipped in, or a rewrite? | Slipped in. 10 of 16 units are kept or small swaps. The 6 rewrites each have a reason (Mark's hook; no debate agent; no memory or win-rate claim; no guide). Qube enters with Mark's line, where raycfu's tool starts. |
| Promise paid off, payoff usable? | Yes. All 6 agents are named with one job each by about 35s. Priya leaves with a six-job org chart, the three exact "no" rules, the fix-and-retest loop, the backtest → simulation account → live order, and a free tool. More usable than raycfu's, whose build sits behind the guide. |
| One persona, one shape, one idea, one enemy → difference? | Priya · new power steps (raycfu's shape) · one idea: a firm of 6 agents, one that can say no · Wall Street gatekeeping (implied by "quant trading firm") → pro quant tools, no code (line 14). |
| Every sentence sells the next (first-time read) | Yes, hook through line 15. Each "it" points back one line. Line 10's "it's a no" sets up line 11, line 12's "it's a yes" answers it, "That's when" carries it into line 13, and "You can too." hands line 14 to the CTA. |
| Would Mark say every word? | Yes. Short, plain, LA. "Here's how I built it out" is raycfu's phrase and sounds spoken. No "rules" for strategy parts, no "trading idea", no "hooked up", no fixed ten years. |
| Compliance (final sign-off) | Clean. No return, win rate or trade count spoken or shown as a claim. NVDA carries "Example" and no "buy". "Backtest, not live results" on A6 and A8. Badge top-right on A9. LIVE stays greyed with a lock, and nothing goes live for this video. "First…then live" keeps the order (`finance-compliance`). No keys, emails or paths. |
| Would Frank find anything wrong? | Only the gap below: line 8 gives an exact 2%, line 9's "max loss" has no number. Not wrong, just less exact. Mark's call. |
| Blanks, placeholders, unsourced numbers | None. "2%" is Mark's own setting (brief); "up to five years" is in `product-truth-qube`. |

## Mark's lines, flagged, not changed

- Hook: "I built a quant trading firm on Claude. 6 agents, each one has a job." Unchanged.
- Line 2: "I start by connecting Qube to Claude." Unchanged.
- Line 15, the standard CTA. Unchanged.

## Needs Mark (only he can decide)

- **P1:** the spoken "simulation account" (your J022 word) vs the badge "Paper trading · simulated results". Both kept as written.
- **Line 9, the daily max loss:** line 8 says 2%. If you want the max loss said or shown as a number too, give the figure. Otherwise it stays as is.
- **Line 10, "if the backtest doesn't hold up":** give a real pass mark if your risk manager has one. Otherwise it stays.
- **A8:** your recorded run has to really say no, then yes, for the backtest reason. Never staged.
- **A2 step 4:** the Qube team names the screen that shows Qube connected.
- **NVDA** as the example ticker, unless you want another one.

Score vs the gold: matches raycfu beat for beat and gives a more usable payoff; the one thing weaker is the "best part" beat (fix and retest until it's a yes is honest, but it isn't as big a wow as his memory and win-rate chart, which we can't claim).
