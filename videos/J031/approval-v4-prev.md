# Approval · J031 (v4)
Verdict: SEND BACK (to Scriptwriter, one word plus one edit timing; no other line changes)

If send back:
1. **Line 8: "Getting a working strategy out of one in minutes?"** "A working strategy" reads as "a strategy that works", which is a performance claim. `finance-compliance` lists "This strategy works." as the bad example. Line 7 has just shown its weaknesses, so Frank will say "working? says who?" The original avoided this with "executable". Fix: swap "working" for a word that means built and tested, not profitable. Suggestion: **"Getting a tested strategy out of one in minutes?"** It's the same word count, so the total stays at 137, and it's true (the strategy was backtested). The Scriptwriter can pick a different word, but the total must stay at 137 or fewer. Then update the SCRIPT, the EDIT spoken cell at 32.5–37.8, `beatmap.md` and the Script Room. (`finance-compliance`, `script-logic` #10)
2. **EDIT 28.1–32.5: the weaknesses frame is now 1.0s (30.6–31.6), down from 1.9s, so viewers can't read it.** The brief's payoff is Claude's weaknesses held readable, and `finance-compliance` Always #3 says the weak spots get shown openly. Fix: hold A10 weaknesses.png readable for at least 1.5s. For example, let the A10b optimized frame run on over the first words of line 8 (from 32.5s) instead of starting it at 31.6s, or take time from the trade list. Keep the "then optimized" cut on the word. (`on-screen-text`, `finance-compliance`)

Score vs the gold: line for line it's as strong as the @julias.algos original (critic 8.8/10). The engine and beats are the same, the hook is word for word (Codex → Claude), and the prompt is a screenshot moment she only half gives. Once fix 1 is in, line 8 is cleaner than her line.

## The critic's round-4 doc fixes all landed
| Fix | Check | Result |
|---|---|---|
| ASSETS A0 step 6 | Retakes of "That's when everything changes." | Yes |
| ASSETS A5 prompt | Step 8 "Then optimize it in Qube based on those weaknesses and backtest it again", CHECK says "all 8 steps" | Yes |
| EDIT 13.8–18.4 | Prompt text includes step 8 | Yes |
| ASSETS A10b (new) | Qube's optimization round, version/run history side by side, real numbers, stop-and-tell-Mark if no round | Yes (`product-truth-qube`: optimization, run history, version tracking) |
| EDIT 28.1–32.5 | Cut on "then optimized" to A10b with its own label, dates and trade count; label list includes A10b | Yes (but see fix 2) |
| Recording order / A11 | A10 → A10b → A11. Run time covers the optimization round | Yes |
| ASSETS A8 title | "putting together" | Yes |
| Word count | `check-script.py`: 137 (hook 14 + script 123), no flags. My own recount: 137. +9.6%, inside ±10% (112.5–137.5) | Yes, no room left |
| Leftovers | No "interesting", "executable" or "136" in the SCRIPT, EDIT or ASSETS. The "stitching together" in the EDIT header describes the original (allowed by the critic) | Clean |

## Director's checks
| Question | Answer |
|---|---|
| Recognisable side by side? | Yes. The hook is word for word except Codex → Claude. Same pain → "Or does it?" flip → screen demo → logo pile → re-hook ("But Qube builds…") → weaknesses → teaser question → answer → close |
| Hook copied, body ours? | The hook is the original's. Line 8 is fresh, passes the copy check, and sounds like natural LA speech. Lines 1–7 and 9 are Mark's: not scored, not sent back |
| Past videos checked? | The line was missing, so I added it to the brief after checking video-map, own-videos transcripts, every video folder incl. `_archive`, and slop. No other video uses a paper or PDF as its input. Closest are J022 (same Claude + Qube path, but a typed idea) and J021 (research, but no paper) |
| Promise paid off, payoff usable? | Yes. A named paper (Faber 2007), the 8-step prompt held readable, a labelled backtest with every trade, the weaknesses, an optimization round, and the free sign-up |
| One persona, shape, idea, enemy → difference? | Marcus · shape 3 problem → solution · paper to tested strategy · gatekeeping → pro quant tools, no code |
| Compliance | Clean apart from fix 1. No number said. "Backtest, not live results" + period + trade count on every Qube result frame (A9, A10b). Keys and emails blurred. Nothing goes live |
| Would Frank find anything wrong? | "A working strategy" (fix 1). "In minutes" is backed by the real run time (A11, with a stop past 15 minutes) |
| Blanks, placeholders, unsourced numbers? | None |

## Mark's lines: flagged, not changed
- **Line 2 "Connect TQX to Claude":** `product-truth-qube` says Qube is what connects to Claude. Already flagged in fix-log on Oct 27. The line stands as Mark wrote it.
- **Line 7 "flagged its weaknesses":** this gives the check to Qube, but the frame on those words is Claude's step-7 answer (labelled "Claude · Codex → Qube"). If Qube shows its own weak points in the run, use that frame. Otherwise A10 stays.
- Lines 1, 3–7 and 9 match fix-log Oct 27 exactly. For information only: lines 1 and 3–7 stay close to the original's sentences. They're Mark's, so they're not sent back.

## Director's own fixes (brief only, old copy kept as brief-v4-prev.md)
- Updated the brief to the Oct 27 method (only the hook copied, body fresh). It still said "copy it line by line" and quoted the original's line 8/9 as our landing.
- Line 8 note: the brief now says line 7's "it" is Qube, as Mark wrote it.
- Added the "Past videos checked" line.

## Still open for Mark (not blocking)
1. Paper pick: Faber (2007). Swap it if you'd rather show another; the script doesn't name it.
2. Recording: Qube connected to Claude on Joshua's laptop. Is SPY in Qube? If not, use the 10 biggest US stocks. Qube must run at least one optimization round (A10b), or line 7 needs your call.
3. SSRN: if it asks Joshua to sign in at A1, he stops and asks you.
