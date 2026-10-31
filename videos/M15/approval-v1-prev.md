# Approval · M15
Verdict: SEND BACK (one short round: 1 spoken line + 1 label. Everything else is approved as it stands.)

## The critic's fixes: did they land?
| Review item | Now | Landed? |
|---|---|---|
| Line 5 "I'm scared to look" (J033, @copyandrea) | "I hit run. No clue how this ends." | Yes |
| Line 10 "in minutes, before risking a single dollar" (J020, J027) | "But now anyone can build a strategy and test it before their money's on the line." | Old repeat gone, but the new wording is a new problem (fix 1) |
| 8B "its" with no owner + repeat of line 7 | "Here's every trade it lost. And here's its worst drop." | Yes |
| 9A "Not even close" (optional) | Kept | Fine. The drop in 8A carries it, and it's the same line in A and B |
| A9 pick rule hole | Above = A, below = B, equal or anything else = stop and send Mark both | Yes. Beatmap and script header match |
| A10 fewer than three losers | Count goes to INK; none = Mark sees it before filming | Yes |
| A7 "or let Claude run it" | "Mark clicks Run in Qube himself" | Yes |
| Docs: 15 words, no wink, 1.6s/card 0–5s, label window | All four fixed. EDIT times re-timed to the new lines (A 49.0s, B 48.0s) | Yes |

Checker (`tools/check-script.py`): A 147 words, about 49s, no flags. B 144 words, about 48s, no flags. Both are inside 35–60s and the brief's 130–150.

## Send back: fixes
1. **Line 10, "before their money's on the line".** This is a light rewording of J020's original Reel line, "before putting your money on the line". J020's brief lists that line, and the creator's catchphrase "on the line", under Don't copy. It was also J020's own line 10 until round 2 cut it. So the round-1 fix swapped one J020 echo for another (no repeats with past videos, Mark Oct 27–28; copy check). Write it fresh. Keep the same idea (build it, test it on past prices, before real money), keep it about 15–17 words, and say it out loud. Don't use "on the line", "risk a single dollar" or "in minutes". Keep the EDIT card "BUILD · TEST · BEFORE REAL MONEY" if it still matches the new line. (`spoken-sentence-rules`, `claims-and-proof`)
2. **Holding-SPY label (EDIT row 24.0s, ASSETS A9).** Every past just-holding-SPY comparison carries "price only, no dividends" (`claims-and-proof`, the SPY dip-rule and overnight rows; J021). M15's split screen (A8 vs A9) doesn't. Line 6A says "It even beat just holding the S&P 500", and Frank will ask about dividends straight away. Add to A9's CHECK: "Note whether Qube's hold result includes dividends." In EDIT, add a label under the A9 number: "price only, no dividends", or Qube's own wording if it includes them. If A8 beats A9 only by a hair (about the size of five years of dividends, roughly 7%), send Mark both screenshots before picking A. (`finance-compliance` Always #1 and #4)

Not blockers (no change needed):
- Line 7, "And this is the part nobody on your feed shows you.", has the same "the part nobody…" re-hook shape as J027 line 6 ("And the part nobody's talking about?"). The idea is different, and it calls back to Mark's "Nobody shows proof", so it stays. The Scriptwriter can vary it if line 10's rewrite makes it easy.
- Script Room `data/script-room/M15.json` is still the v1 text ("scared to look"). Sync it after this round.
- I updated the brief myself (my own doc): beat 8 dropped the stale "in minutes / risking a dollar" wording, and the fourth-claim timing now matches ASSETS (5 words, about 2s, 152 words).

## Checked and clean
- **Mark's lines untouched:** the hook (Grok first, his concept; "the financial advisor" is the Director's fill, his to swap) and line 1, "Everybody says this. Nobody shows proof. I'm gonna change that." The Grok/M14 overlap stays flagged for Mark, not changed, with different first frames planned.
- **Honest both ways:** A says "beat holding" only after A8 vs A9 on the same dates and the same $10,000. B says it lost to holding plainly. Losses and the worst drop show in both. No returns are promised, the claim cards carry no numbers, and "Backtest, not live results", Qube's period and trade count stay on from 24.0s through line 8 and in the recap. Result numbers come only from Mark's run, with no reruns.
- **Product truth:** "I start by connecting Qube to Claude" and "up to five years of real price data" are the mandated wording. No install commands, keys or emails on screen. The CTA is the standard one.
- **Repeats (M13, M14, M16, J020–J033, every version):** besides fix 1, none. "No clue" appears only in a J032 draft (a different sentence). "Not even close" appears only in J022 drafts, not its final. The idea (the AI-claim genre vs a full test) is distinct from M14 (six Grok bots), M16 (Claude vs Codex), J016, J009 and J031.
- **Voice:** Mark picks a fight and wins it with proof. Short flips and plain words, no AI patterns.
- **Shape and structure:** one persona (Frank), one shape (5 + 7), one idea, one enemy → difference. The promise (proof) is paid off with the full test, losses included, and the honest answer.

Score vs the gold: about 8/10. The open and the proof are gold-level (#5/#6's flip into the real source, #10's result on the real screen). Line 10 is the one weak line, because it borrows a creator's phrase.
