# Approval · J031 (v5)
Verdict: APPROVED for Mark
If send back: none. Both v4 send-back fixes are in (the v4 approval is kept as approval-v4-prev.md).

## The v4 send-back fixes landed (diffed against the *-v5-prev.md docs)
| Fix | Check | Result |
|---|---|---|
| 1. Line 8 | "Most people read papers like this and stop. Getting a tested strategy out of one in minutes?" It's in the SCRIPT, the EDIT spoken cell at 32.5–37.8 and `beatmap.md`. There's no "working" left in the four docs | Yes. "Tested" is true (the strategy was backtested) and isn't a performance claim (`finance-compliance`) |
| Word count | `check-script.py`: 137 (hook 14 + script 123), no flags. +9.6%, inside ±10% | Yes |
| 2. Weaknesses frame | A10 is held 30.3–31.9s (1.6s), with "held at least 1.5s" written in. The trade list is 1.0s, and it scrolls | Yes |
| A10b | Still cuts on "then optimized" (31.9s) and runs on to 33.0s, label still on. Line 8's row starts with the run-on, then Joshua from 33.0s | Yes |
| Other lines | No other spoken line changed. The ASSETS doc is unchanged | Clean |

Score vs the gold: line for line it's as strong as the @julias.algos original (critic 8.8/10). The engine and beats are the same, the hook is word for word (Codex → Claude), the prompt is a screenshot moment she only half gives, and line 8 is now cleaner than hers.

## Earlier record (v4 approval: what was sent back and why)
1. Line 8 "a working strategy" read as a performance claim (`finance-compliance`). Fixed to "tested".
2. The A10 weaknesses frame was only 1.0s. It's now 1.6s.

## The critic's round-4 doc fixes all landed
| Fix | Check | Result |
|---|---|---|
| ASSETS A0 step 6 | Retakes of "That's when everything changes." | Yes |
| ASSETS A5 prompt | Step 8 "Then optimize it in Qube based on those weaknesses and backtest it again", CHECK says "all 8 steps" | Yes |
| EDIT 13.8–18.4 | Prompt text includes step 8 | Yes |
| ASSETS A10b (new) | Qube's optimization round, version/run history side by side, real numbers, stop-and-tell-Mark if no round | Yes (`product-truth-qube`: optimization, run history, version tracking) |
| EDIT 28.1–32.5 | Cut on "then optimized" to A10b with its own label, dates and trade count; label list includes A10b | Yes |
| Recording order / A11 | A10 → A10b → A11. Run time covers the optimization round | Yes |
| ASSETS A8 title | "putting together" | Yes |
| Word count | `check-script.py`: 137 (hook 14 + script 123), no flags. My own recount: 137. +9.6%, inside ±10% (112.5–137.5) | Yes, no room left |
| Leftovers | No "interesting", "executable", "working" or "136" in the SCRIPT, EDIT or ASSETS. The "stitching together" in the EDIT header describes the original (allowed by the critic) | Clean |

## Director's checks
| Question | Answer |
|---|---|
| Recognisable side by side? | Yes. The hook is word for word except Codex → Claude. Same pain → "Or does it?" flip → screen demo → logo pile → re-hook ("But Qube builds…") → weaknesses → teaser question → answer → close |
| Hook copied, body ours? | The hook is the original's. Line 8 is fresh, passes the copy check, and sounds like natural LA speech. Lines 1–7 and 9 are Mark's: not scored, not sent back |
| Past videos checked? | The line was missing, so I added it to the brief after checking video-map, own-videos transcripts, every video folder incl. `_archive`, and slop. No other video uses a paper or PDF as its input. Closest are J022 (same Claude + Qube path, but a typed idea) and J021 (research, but no paper) |
| Promise paid off, payoff usable? | Yes. A named paper (Faber 2007), the 8-step prompt held readable, a labelled backtest with every trade, the weaknesses, an optimization round, and the free sign-up |
| One persona, shape, idea, enemy → difference? | Marcus · shape 3 problem → solution · paper to tested strategy · gatekeeping → pro quant tools, no code |
| Compliance | Clean. No number said. "Backtest, not live results" + period + trade count on every Qube result frame (A9, A10b). Keys and emails blurred. Nothing goes live |
| Would Frank find anything wrong? | No. "In minutes" is backed by the real run time (A11, with a stop past 15 minutes) |
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
0. Script Room: check that line 8 there reads "a tested strategy", to match the SCRIPT doc.
1. Paper pick: Faber (2007). Swap it if you'd rather show another; the script doesn't name it.
2. Recording: Qube connected to Claude on Joshua's laptop. Is SPY in Qube? If not, use the 10 biggest US stocks. Qube must run at least one optimization round (A10b), or line 7 needs your call.
3. SSRN: if it asks Joshua to sign in at A1, he stops and asks you.
