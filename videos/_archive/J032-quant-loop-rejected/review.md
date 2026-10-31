SCRIPT: J032 · Quants never trust a strategy the first time it works (recreating @raycfu "How Quants use Loop Engineering to create a trading bot") · cut-down v2, round 1
VERDICT: Send back to Scriptwriter

Vs the original: hook 10 · engine 8 · energy 8 · reward 8 · CTA 8 · Qube 8 · language 8 · copy 7 · flow 7 (overall 8.0)

Word count: 165 (hook 17 + 148), about 52s at 3.2 words a second. The ±10% rule doesn't apply to this video (Mark, Oct 27, fix-log), so length isn't scored. With the fixes below it comes to about 175 words, about 55s. Every word added back is the original's.
Header: the `**Original video:** https://www.instagram.com/p/DahCoW1Pfyo/` line is there. Pass.
Reviewed: SCRIPT, EDIT, ASSETS and beatmap.md (cut-down), the long version in `long-v1/`, `knowledge/reference/DahCoW1Pfyo/transcript.srt`, the lesson card, the fix log (Oct 27 row) and `data/script-room/J032.json`. There are no Mark edits on J032. Claims from Mark and from the original are taken as given and not scored.

## Checker

```
Spoken words: 165 (top hook 17 + script 148) · presenter: joshua · about 52s at 3.2 words/s
No flags.
```
Nothing to decide.

## Step 0 · Side by side with the original's strongest beats

| Original's big beat (time) | Ours | Verdict |
|---|---|---|
| Hook: "Most people don't realize that quant traders never trust a strategy the first time that it works." (0s) | Word for word | Kept. 10 |
| Promise: "They run it through a loop… until they find one that sticks." (3.6s) | Word for word, line 1 | Kept |
| The "that's me" line: "come up with an idea, backtests once, and then **once it looks great**, they go live and two weeks later they are bleeding money" (8.4s) | 2. "Most people backtest once, go live, and two weeks later, they're bleeding money." | **Weaker.** "Once it looks great" is the reason they go live. It also ties back to the hook ("the first time that it works") and forward to the payoff ("no matter how good it looked before"). Without it, going live has no reason and the A3 green curve has no spoken beat. Fix 1 |
| The loop said as a rhythm, tool on screen (17s) | 4–5. "In Qube, you build a strategy, backtest it, and score it. You read why it failed, feed that back in, and the AI builds a better version to test again." | Kept, and Qube sits in the original's tool slot (20s vs 17s). Good |
| Open loop: "And this is the most important part." (61s) | Moved up to line 3 as "the last step decides what you keep" (18s) | Good idea, but the wording breaks the logic. Fix 2 |
| The quotable flip: "…does not find better strategies faster. It just finds prettier noise faster." (62–66s) | 6. "But a loop that keeps testing on the same data just finds prettier noise faster." | **Weaker.** The flip needs both halves. "Faster" only lands against "better strategies faster". With one half it's just a statement, and "faster" leaves the viewer asking "faster than what?". The beatmap says the flip is "kept word for word", but the setup it flips is gone. Fix 3 |
| The fix: "The fix that quants use is called an out-of-sample gate." (70.5s) | 7. "So the last step is an out-of-sample gate." | Pays off line 3, but see Fix 2 |
| Survivor vs collapse pair: "If it does not, it gets thrown out no matter how good it looked before." (79.5s) | 9–10. "If it holds up, you keep it." / "If it doesn't, it gets thrown out, no matter how good it looked before." | Kept. The pair is the last picture before the CTA, as in the original |
| CTA (82.5s) | Standard CTA, straight after the payoff | Fine (`retention-writing` #9). Mark's standard CTA. CTA 8 |

**Does it still feel like the original?** Yes. The hook, the mistake, the loop, the trap, the gate and the keep / thrown-out pair are all there, in the original's order. Cutting the two checks follows Mark's note and leaves one idea, the loop and its final test (`script-logic` #2). Engine 8.

**Does the open loop pay off?** Yes, at lines 7–10. But the label is wrong. "The last step" (line 3) points at the loop the viewer is about to hear, and line 5 ends that loop on "test again". On screen, A4's ring ends on IMPROVE. Then line 7 says the last step is the gate, and line 8 says the gate comes *after* the loop ("survives the loop"). A viewer who follows along hears two different "last steps". Line 3 also starts with "a quant" and ends with "you", in the same sentence ("what you keep": keep what?).

**Does every sentence sell the next?** Yes, except at three joins. 2 → 3: they go live for no stated reason. 3 → 7: the "last step" mismatch. 6: "faster" has no setup. Flow 7. All three are fixed below by putting the original's own words back, so copy goes up with flow.

## Fixes

| Line | Problem | Rule (skill) | Fix |
|---|---|---|---|
| 2 | "Most people backtest once, go live…" drops the original's "once it looks great", which is the reason for going live. It also breaks the thread from the hook ("first time it works") to line 10 ("how good it looked before"). | Every sentence sells the next (`script-logic` #3b) · copy the original (`remix-for-product`) | "Most people backtest once, and once it looks great, they go live. Two weeks later, they're bleeding money." (18 words, the original's own words) |
| 3 | "the last step decides what you keep": "last step" reads as the last step of the loop, which line 5 and A4 say is "test again" / IMPROVE. The gate comes after the loop (line 8). "What you keep" is vague, and the person switches from "a quant" to "you" inside one sentence. | One thing, one name (`terminology` rule 1) · vague nouns (`spoken-sentence-rules` #2) · the loop has to pay off cleanly (`retention-writing` #1) | "A quant runs a loop instead, and one last test decides which strategy they keep." |
| 6 | "…just finds prettier noise faster." keeps only half of the original's quotable flip, so "faster" is left hanging. | Copy the big moments (`remix-for-product`, brief "Big moments") · every sentence ends (`spoken-sentence-rules` #1) | Two numbered lines: "But a loop that keeps testing on the same data doesn't find better strategies faster." / "It just finds prettier noise faster." (the second is word for word). "Prettier noise" now lands at about 66%, inside the 60–75% re-hook window (`script-logic` #11) |
| 7 | "So the last step is an out-of-sample gate." It must match the new line 3. | Same as line 3 | "So that last test is an out-of-sample gate." |
| 8 | "…gets one final test on data it's never seen." After the line 7 fix, "last test" and "final test" would sit side by side. | Over-tidy repetition (`anti-ai-patterns` #11) | "Every strategy that survives the loop gets tested on data it's never seen." |
| Follow-ons in the three docs | Lines 2, 3, 6, 7 and 8 change, and the script gets one more numbered line | Three docs stay in step (`make-script`) | SCRIPT: renumber, header to about 175 words / about 55s. EDIT: re-time every row from line 2 on. Line 2: the A3 green line holds bright on "once it looks great", toggle on "go live". Line 3: the gold caption word becomes "one last test". Line 6: the A7 score climbs on "doesn't find better strategies faster", and the big "prettier noise" sits on the new line 6b only. Line 7: A8 card reads `THE LAST TEST`, punch-in on "So that last test". Line 8: the gate drops in on "gets tested". ASSETS: the A0 close-up lines for lines 3 and 7 take the new wording; the take rule becomes about 55s, redo over 60s; the A8 card text changes. Beatmap: update rows 8.4, 16.0, 62.0, 70.5 and 72.8 with the reasons, plus the count and rhythm. |

Optional, not blocking:
- Line 4 "In Qube," is Qube's only spoken mention, and it's said cold. The screen (the Qube page plus the "Qube" text on the word) carries it, so I've left it as is. If Mark wants more reason to comment, `cta-and-offer` has his approved J021 close, reworded for this video: "And if you want to run this loop yourself for completely free, comment QUBE and I'll send it over to you." That's Mark's choice, not the writer's.

## Three docs consistency (as they stand)

Consistent. SCRIPT, EDIT, ASSETS and the beatmap all have the same 11 lines plus the hook, word for word, and 165 words. The EDIT times add up at 3.2 words a second (0–51.6s, every row checked). EDIT and ASSETS use the same asset IDs (A0–A11). The A0 close-up list matches the EDIT punch-ins. The A2 → A6 recording order holds. No stale long-version references are left: no ICIR, no shelf life, no A12/A13, no 428 words.
- "Backtest, not live results" is on every Qube run frame (A2, A5 from the backtest on, A6). "Example strategy" is on the SPY typing. "Example" is on A3, A7, A9 and A10. Pass.
- The gate is never said or shown as a Qube feature ("Never on screen" list). Pass.
- Small point: the EDIT header lists the re-hook punch-ins as "lines 1, 3, 7, 11", but line 6 also has a 115% punch-in in its row. After the fix, add line 6 to the header.

## Passes 1–10 (cut-down)

| Pass | Result |
|---|---|
| 1 Worth making | Pass. Daniel. Usable: run the loop, then test the survivor on data it's never seen. It's a cut of an approved video, not a repeat |
| 2 Logic | Promise: why quants don't trust a first win. One idea: the loop and its final test. Payoff: line 10. Re-hook: line 6 now (57%), about 66% after Fix 3. Problems: Fixes 1–3 |
| 3 Facts | Every quant claim is the original's (taken as given). No new numbers |
| 4 Product truth | "build", "backtest", "the AI builds a better version" = Build / Test / Improve (`product-truth-qube`). The gate isn't claimed for Qube. Pass |
| 5 Compliance | Pass. No return promised. "Bleeding money" describes the mistake. Labels are as listed above |
| 6 Spoken lines | Line 3: "what you keep" (Fix 2). Everything else ends cleanly, uses contractions and sounds like Joshua |
| 7 Hook | The original's, word for word. Line 1 doesn't repeat it |
| 8 On screen | Every line has a visual. The insert changes every 2–3s |
| 9 CTA | Standard, last spoken line, straight after the payoff |
| 10 Fix log | Pass: one hook, no guide, no "follow", strategy wording, link line, Oct 27 length note followed |

Facts checked: "two weeks later… bleeding money", "prettier noise" and the out-of-sample gate → the original (`transcript.srt` 3–4, 18–22), taken as given. Build / backtest / AI improves → `product-truth-qube` "How it works". "Free sign-up" → `cta-and-offer` standard CTA.
Mark's own lines flagged, not changed: none. (His only J032 input is the Oct 27 length note, which is followed.)

## For the Director (not writer fixes)
- `brief.md` and `approval.md` still describe the 428-word version: the ±10% target, and "never cut lines 9, 14, 19". Add a line noting Mark's Oct 27 override before approving the cut.
- The Script Room (`data/script-room/J032.json`) still holds the long version, marked Approved. Push the cut once it passes.
