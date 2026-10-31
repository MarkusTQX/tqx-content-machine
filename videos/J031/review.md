SCRIPT: J031 · Let's turn this research paper into a trading strategy (Claude + Qube)
VERDICT: Send back to Scriptwriter (round 4, docs only). The spoken script is clean: new line 8 passes the copy check, sounds like LA and flows from 7 into 9. No spoken line changes. Three doc fixes below, then it's Ready for Director. No re-review is needed on the script itself.

Vs the original: hook 9 · engine 9 · energy 8 · reward 9 · CTA 8 · Qube 9 · language 9 · copy 9 (line 8 only; Mark's lines not scored) · word count PASS (137, +9.6%) · flow 9 · **overall 8.8 / 10**

## Line 8 (the only change since v3)

| | Text |
|---|---|
| Original (39.4–44.9s) | "Reading quant papers is extremely useful, but having AI turn them into executable strategies in minutes?" |
| v3 (copied) | same as the original, word for word |
| v4 (now) | "Most people read papers like this and stop. Getting a working strategy out of one in minutes?" |

- **Copy check: pass.** The first sentence is new: a "most people stop here" contrast instead of the original's "useful, but". The second keeps only the beat's engine, a short question that ends on "in minutes?" so line 9 can answer it. Its words and frame are different ("getting a working strategy out of one" vs "having AI turn them into executable strategies"). It doesn't read as her sentence.
- **LA test: pass.** "Most people read papers like this and stop." is how people talk. "Getting a working strategy out of one in minutes?" is a natural spoken fragment, and "one" clearly means one of those papers. "Executable" is gone. No word a guy from LA wouldn't say.
- **Flow: pass.** 7 → 8: "...and then optimized." → "Most people read papers like this and stop." This is the right turn: we went all the way and most people stop at reading. 8 → 9: "...in minutes? That's when everything changes." The question is asked and then answered. "Papers like this" works because the Faber page is on screen earlier.
- Optional, not needed: "...and stop there." reads a touch softer out loud, but it adds a word and puts the count at 138, which fails. If anyone wants it, cut "working" at the same time. My call is to leave line 8 as it is.

## Word count (exact)

- Original: 125 (transcript.srt).
- Ours: 137 (checker: hook 14 + script 123). That's +9.6%, inside ±10% (112.5–137.5).
- **There is no room left.** Any later fix that adds even one spoken word fails. Every doc fix below leaves the spoken words alone.

## Checker

```
python3 tools/check-script.py videos/J031/J031-1-SCRIPT.md
Spoken words: 137 (top hook 14 + script 123) · presenter: joshua · about 43s at 3.2 words/s
No flags.
```
Decision: no flags. The ±10% check is done by hand above.

## Fixes (docs only, no spoken change)

| Line / doc | Problem | Rule (skill) | Fix |
|---|---|---|---|
| ASSETS A0 step 6 | Joshua is told to record extra takes of the old line 9: "That's where things get interesting." Mark changed it to "That's when everything changes." (fix-log Oct 27) | `remix-for-product` step 5 (docs match the script) | Step 6 becomes: **Record "That's when everything changes." three more times, a little slower, looking straight into the lens.** |
| Line 7 "...and then optimized" → ASSETS A5, new asset, EDIT 28.1–32.5 | Mark's line 7 now says it optimized, but nothing in the shoot makes that happen or shows it. The A5 prompt stops at step 7 ("Explain where the strategy might fail"), no asset captures an improve round, and the EDIT has no frame on "then optimized". If it isn't recorded, line 7 says something the video never shows. | `claims-and-proof`, `product-truth-qube` (Improve: "AI optimization… suggests changes and tests them over rounds"), `on-screen-text` | (1) A5: add **"8. Then optimize it in Qube based on those weaknesses and backtest it again"**, update its CHECK to "all 8 steps", and update EDIT 13.8–18.4's prompt text to match. (2) New asset **A10b "Qube's optimization round"** (Joshua): keep recording until Qube finishes at least one optimization round. Show the improved version next to the first one (version or run history). Hold 3s. Screenshot (optimized.png). **CHECK: it must be Qube's real result from this run. Don't change any number, and none of them is said.** (3) EDIT 28.1–32.5: on "then optimized" (about 31.6–32.5s), cut to A10b with the "Backtest, not live results" + dates + trade count label. (4) Recording order: A10 → A10b → A11. A11's "in minutes" CHECK must cover the optimize round too |
| ASSETS A8 title | 'Logo stacks for "stitching together"'. Line 5 now says "putting together" (Mark, Oct 27) | `remix-for-product` step 5 | Title becomes **Logo stacks for "putting together"**. The EDIT header can keep "stitching together", because it describes the original |
| approval.md | It approves the old version: it quotes "stitching together" and says "lines 1, 3, 8, 9 the original's" | `director` approval | The Director re-approves v4 after the fixes above. No Scriptwriter action needed |

Optional, for the Scriptwriter to decide: line 7 says "it" (Qube) "flagged its weaknesses", but the frame on those words is Claude's step-7 answer, labelled "Claude · Codex → Qube". If Qube shows its own weak points in the run, use that frame instead. If not, keep A10 as it is. It still shows the run's real weaknesses.

## Side by side (all lines)

| # | Original | Ours | Whose | Score |
|---|---|---|---|---|
| Hook | "...using Codex." | "...using Claude." | original's, word for word (method) | 9 |
| 1 | "Usually, turning a research paper into something tradable means hours of reading, decoding equations, and manually implementing the strategy." | "Turning a research paper ... the strategy. Or does it?" | Mark | not scored |
| 2 | "Instead, I drop the raw PDF directly into Codex." | "Connect TQX to Claude and drop in the PDF." | Mark | not scored |
| 3 | "I'm asking Codex to act like a quant researcher..." | "I'm telling Claude to act like a quant researcher..." | Mark | not scored |
| 4 | "Codex actually reads the methodology section, then translates it into implementable code." | "Claude reads the methodology section, then Qube translates it into usable code." | Mark | not scored |
| 5 | "...stitching together signal processing libraries, reinforcement learning frameworks, and backtesting the code." | "...putting together data, charting tools, and backtesting frameworks." | Mark | not scored |
| 6 | "But Codex built the entire workflow automatically." | "But Qube builds the entire workflow automatically." | Mark | not scored |
| 7 | "Then it ran the backtest, generated the charts, and even flagged weaknesses." | "...showed every trade, flagged its weaknesses and then optimized." | Mark | not scored |
| 8 | "Reading quant papers is extremely useful, but having AI turn them into executable strategies in minutes?" | "Most people read papers like this and stop. Getting a working strategy out of one in minutes?" | ours, fresh (v4) | 9 |
| 9 | "That's where things get interesting." | "That's when everything changes." | Mark | not scored |
| 10 | (caption-only sponsor link) | standard CTA | standard | 8 |

The engine is the same beat for beat. The re-hook is at line 6 (~60%), the weaknesses are on screen at ~72%, and the teaser question in line 8 is answered by line 9.

## Passes

- **Pass 1 worth making:** pass (unchanged).
- **Pass 2 logic and flow:** pass. Every sentence leads into the next one, and line 8's question is answered by line 9.
- **Pass 3 facts:** pass. No numbers are spoken. The original's and Mark's claims are taken as given.
- **Pass 4 product truth:** pass on the spoken script. "Then optimized" matches `product-truth-qube` (Improve), but the shoot has to capture it (fix above).
- **Pass 5 compliance:** pass. The "Backtest, not live results" + dates + trade count label goes on every Qube result frame, A10b included.
- **Pass 6 spoken lines:** pass. Line 8 reads cleanly out loud in two breaths.
- **Pass 7 hook:** pass (unchanged).
- **Pass 8 on-screen:** fail on the missing "then optimized" frame (fix above).
- **Pass 9 CTA:** pass.
- **Pass 10 fix log:** pass on the script: Mark's Oct 27 lines are kept exactly, only the hook is copied, and line 8 is fresh. The docs fail on the stale A0 retake line and the A8 title (fixes above).

Facts checked: no spoken numbers. "In minutes" → A11's real run time (CHECK at 15 minutes), which must now include the optimize round. "Optimized" → `product-truth-qube` row 3 (Improve). "Up to five years of real price data" → `product-truth-qube` (prompt only).

Mark's own lines flagged, not changed: line 2 says "TQX" where `product-truth-qube` says Qube connects to Claude. This was already flagged in fix-log Oct 27 and the line stands. For Mark's information only: lines 1 and 3–7 still sit close to the original's sentences. They're his lines, so they're not scored or sent back.
