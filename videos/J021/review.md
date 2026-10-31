SCRIPT: J021 · I tested the overnight trick in Qube (Joshua)
VERDICT: Send back to Scriptwriter

Reviewed: beatmap.md, J021-1-SCRIPT.md, J021-2-EDIT.md, J021-3-ASSETS.md, against @joe.investss Ddo1OMSIZeo (transcript.srt + lesson card). Gold named in the brief: #5 @svermm. Older files (outline.md, script.md, the old review) ignored.

Vs the original: hook 8 · engine 7 · energy 6 · reward 7 · CTA 6 · Qube 8 · language 7 · copy 6

## Side by side (scored first)

| Score | Why | What gets it to 8+ |
|---|---|---|
| Hook 8 | Copied word for word, with a bigger number that's real (311M % vs their unsourced 138M %), Micron kept as the known name, and the chart on screen from frame 1. At 28 words it's long, but it's their line and it reads like speech. | Hold. Fix hooks B and C (table). |
| Engine 7 | 0–15s is clearly their Reel: number, "exact opposite", "isn't the only one", "what's actually going on?", "missing the entire point", keyword CTA. But the widening beat at 13–20s goes flat. They go from one stock to "hundreds of stocks". We go from 300 million percent to "almost doubled" on one fund, said in a test-report voice ("We ran the S&P 500 too"). | Lines 5–8 rewrite: "The S&P 500 does it too." keeps the widening energy (true: overnight beat daytime on SPY too). |
| Energy 6 | About 57s against their 42s, so it's 36% longer for the same beats. Lines 6–8 and 10 are the slow ones: three number lines in a row, then a 19-word cost line full of prepositions ("one cent per $100 on every buy and every sell"). | Cut it to about 160 words (about 50s) with the line fixes below. Most of the saving comes from lines 6, 7 and 10. |
| Reward 7 | Better than the original's: they give a "huh" fact, we give a cost test plus "just holding beat both". But the hook's number is Micron and the payoff is only about the S&P 500, so the Micron number is never closed. The brief's "two checks" are never said. | Line 11 says "On the S&P 500" so nobody thinks Micron collapsed. The CTA qualifier (below) states the test-it point. |
| CTA 6 | Their CTA offers a thing people want ("my entire portfolio, completely free") in an "if you want X" shape. Ours is the generic QUBE line, not linked to anything in the video. | Copy their shape: "And if you want to run this test yourself, comment QUBE and I'll send you the free link and a step-by-step on building your first strategy." |
| Qube 8 | Slipped in at the exact spot (right after the claim), pinned in the top third, CTA is "Comment QUBE…". It's only true once the runs are real Qube runs (Mark's list). | Hold. |
| Language 7 | Most lines pass the read-aloud test. Two fail: line 6 "We ran the S&P 500 too" (nobody "runs the S&P 500"; it sounds like you manage the index), and line 10 "one cent per $100 on every buy and every sell" (nobody says it that way). Line 7 "turned $10,000 into" is the get-rich phrase our enemy uses. | Fixes in the table. |
| Copy 6 | Of their 13 lines, 4 are kept and 3 are small swaps: 7 of 13, about half. Of our 15 lines (hook + 14), 7 are theirs. Lines 1, 6, 7, 8, 10, 11 and 12 are new. The cuts are justified (the two-crowds beat is unsourced, the paper's numbers aren't ours), but the CTA was rewritten when it could have been a small swap. | CTA as a small swap of theirs (+1 line). Line 5 → "The S&P 500 does it too." brings back their widening move. Optional: source the two-crowds line (below). |

Rules second: this follows almost every rule, but it's flatter in the middle and weaker at the CTA than the original. That's what needs fixing.

## Checker

```
Spoken words: 184 (top hook 28 + script 156) · presenter: joshua · about 58s at 3.2 words/s
1 flag(s):
  Hook A           Long sentence (28 words): If you bought Micron every day when the market closed and so...
```
Decision: **accepted.** It's the original's hook, copied. It reads in one breath the way they said it (6.9s at their pace, about 8.8s at Joshua's). If the proposed CTA goes in (26 words), accept that too for the same reason (it copies their CTA shape; Mark's own M03 CTA was 21).

## Line by line

| Line | Problem | Rule (skill) | Fix |
|---|---|---|---|
| 5–8 | The widening beat dies. "We ran the S&P 500 too" + three lines of numbers reads like a test report, while theirs gets bigger ("hundreds of stocks"). | Engine kept (`remix-for-product`), energy (`retention-writing` #8) | 5: "And Micron isn't the only one that does this." (keep) · 6: "The S&P 500 does it too. That's about 500 of the biggest US companies." · 7: "Say you put in $10,000 ten years ago. Buying at the close and selling at the open, you'd have about $19,200." · 8: "The exact opposite only got you about $14,800." |
| 6 | "We ran the S&P 500 too": nobody says "ran the S&P 500". It sounds like you manage the index. | Words people say (`spoken-sentence-rules` #3) | "The S&P 500 does it too. That's about 500 of the biggest US companies." |
| 7 | "turned $10,000 into about $19,200": "turn $X into $Y" is the get-rich phrasing (`finance-compliance` Never row; it's the "$89 → $68,024" enemy in `positioning`). The $10,000 is also hypothetical, so it needs "say". "The overnight trade" is a new name nobody has heard yet. | `finance-compliance` (hypotheticals use "say"), `spoken-sentence-rules` #6 | "Say you put in $10,000 ten years ago. Buying at the close and selling at the open, you'd have about $19,200." |
| 10 | 19 words, hard to say: "one cent per $100 on every buy and every sell" stacks prepositions. Nobody in LA talks like that. "Trading costs" here, then "cost" on screen: keep one word. | Words people say (`spoken-sentence-rules` #3, #9), one term per thing (`terminology` rule 1) | "Those tests had zero trading fees. So we added a tiny one, a penny for every hundred bucks, every time you buy or sell." (On screen stays exact: "0.01% on every buy and every sell".) |
| 11 | "The overnight trade fell to about $11,600." The hook's number is Micron, so viewers can think Micron collapsed. It didn't: I reran `micron-overnight.py` with 0.01% each side, and Micron still ends at $1 → about $368,000 (+36.8 million %). Frank will check. | Hook paid off honestly (`script-logic` #1, #7) | "On the S&P 500, the overnight trade fell to about $11,600. The opposite one lost money." Never say or imply that costs wiped out the Micron number. |
| 13 | "the entire point" is vague (kept from the original), and the landing never says TQX's point (test it before you risk it). | Landing line (`positioning`) | Keep line 13 as is (it's theirs). Land the point in the CTA qualifier (next row). |
| 14 | Generic CTA, not linked to anything in the video. The original's "if you want X, comment Y, I'll send it" shape was dropped. "A step-by-step" isn't sent yet (Breakdown DM not live). | CTA as strong as the original (`script-critic` step 0), `cta-and-offer` (approved wording + qualifier) | "And if you want to run this test yourself, comment QUBE and I'll send you the free link and a step-by-step on building your first strategy." Beat map: mark it "small swap". |
| Hook B | "would've turned $1 into about $3.1 million": a "$1 into millions" line is exactly the get-rich pattern we push back on. It's also the same mechanism as A, so it adds no variety. | `finance-compliance`, `hook-writing` (different mechanisms) | "One Micron trade is up over 300 million percent since 1984, and all you do is hold it overnight." (Mechanism: number + "that's all it takes". Line 1 still works after it.) |
| Hook C | "the viral Micron trick of buying at every close and selling at every open": "of buying at every close" isn't how people talk. | Words people say (`spoken-sentence-rules` #3) | "Watch this before you try that viral Micron trick, where you buy at the close and sell at the open." |
| 9 | "So what's actually going on?" is then answered with a catch (costs), not with why overnight wins. The loop "why does overnight beat daytime?" stays open. | Close every loop (`retention-writing` #1) | **Mark's direction, not changed.** Optional: check Lou, Polk & Skouras (2019) for its own clientele explanation (traders at the open vs at the close). If it's there, add it to `claims-and-proof` and restore their line "There's two different crowds trading at two different times." as a kept line (+1 copy). |
| Length | About 57s, and the brief allows 45–55. The fixes above take it to about 160 words (about 50s). | `script-logic` #10 | Apply the fixes to lines 6, 7, 8 and 10. Re-time the EDIT. |

## EDIT and ASSETS

| Where | Problem | Rule (skill) | Fix |
|---|---|---|---|
| EDIT 8.8–10.3 "TESTED ON QUBE", 10.3–12.5 "THE EXACT OPPOSITE", 22.5–26.6 "About 500 of the biggest US companies" | The on-screen text repeats the voice instead of adding proof. | `on-screen-text` (adds proof, not a copy of the voice) | 8.8: "Qube · MU · Jun 1984 – Oct 2026" · 10.3: "Buy at the open · sell at the close" (the original's card spelled out both trades) · 22.5: "SPY · 2015–2024 · price only, no dividends" as the main line |
| EDIT 34.1–43.8 | Has to follow the line 10/11 rewrites. On-screen "Overnight: $11,625" needs "S&P 500" next to it so it can't be read as Micron. | `on-screen-text`, `script-logic` #7 | "S&P 500 overnight: $11,625" · "S&P 500 daytime: $8,930" |
| EDIT/ASSETS after rewrite | Lines 6–8 change. The A4/A5 timing and the counter cues move with them. | `make-script` (3 docs match) | Re-time. No asset change needed. |
| ASSETS A1 | Everything in the hook depends on Qube having Micron daily prices back to June 1984. | `claims-and-proof` (product results = real screens) | Already flagged. Add a backup: if Qube's MU history starts later, record Qube's earliest date and send it back so the hook number can be rewritten from that run. |
| ASSETS A1–A7 | Fine otherwise: exact typed sentences, CHECK numbers match the claims rows, labels covered. | | none |

## Skill and claims notes (for `skill-updating`, not changed here)

- `claims-and-proof` Micron row says "Costs would wipe most of it out (see the SPY overnight row)". That's inferred, not tested. At 0.01% each side Micron still ends at about $368,000 per $1 (+36.8 million %). At 0.002% it's about $2.0 million. Reword the row, or add the tested numbers.
- `remix-for-product` still ends with "Would the original creator recognize their... wording? If yes, rewrite." and `gold-standard-scripts` says "Never copy... a line". Both contradict the new method (copy the script, slip Qube in). The brief's "Don't copy" list still has "So what's actually going on?".

## Passes

- Pass 1 worth making: clean. Persona Daniel. Usable: a cost test and holding as the yardstick. Not a repeat: J016 lands on holding, J021 leads on cost.
- Pass 2 logic: see line 11 (Micron gap) and line 9 (open loop, Mark's call). One idea, re-hook at about 57–60%, payoff at about 80%.
- Pass 3 facts: clean (below). The paper link is still missing.
- Pass 4 product truth: "We tested this on Qube" is true only once the runs exist (Mark's list).
- Pass 5 compliance: line 7 and hook B (get-rich phrasing). Labels are on every result in the EDIT.
- Pass 6 spoken lines: lines 6, 10, hook C.
- Pass 7 hooks: B (same mechanism as A, get-rich phrasing). All three make sense cold. None is repeated by line 1.
- Pass 8 on-screen: three duplicate cards (above).
- Pass 9 CTA: line 14. The Breakdown DM isn't live.
- Pass 10 fix log: clean. No "trading idea" or "test your own idea", no Qube in the hook, no vague "it/rules", every sentence ends, three docs, no placeholders, QUBE keyword.

## Facts checked

- "since 1984", "over 300 million percent", hook B "$1 → about $3.1 million" → `claims-and-proof` Micron row (Jun 1 1984 – Oct 22 2026, +311M %, $3.1M). Rerun today: $1 → $3,114,376 over 10,680 overnight periods. Matches.
- "down over 99 percent" → Micron row ($1 → $0.0002, −99.98%)
- "about 500 of the biggest US companies" → `terminology` (S&P 500)
- "ten years", $10,000 → "about $19,200" / "about $14,800" → SPY row ($19,225 / $14,771, Jan 2 2015 – Dec 31 2024)
- "one cent per $100" = 0.01% each side → SPY row
- "about $11,600", "lost money" → SPY row ($11,625 / $8,930)
- "about $28,500" → SPY row ($28,529, price only)
- Paper card (Lou, Polk & Skouras, JFE 2019) → SPY row. The link is still "to be added".
- Micron with costs (my check, for the logic note only, not for the script): +36.8 million % at 0.01% each side. Not in `claims-and-proof`.

Mark's own lines flagged, not changed: "We tested this on Qube." (his slip-in, from the `remix-for-product` example) · "So what's actually going on?" kept on his direction (see line 9) · the S&P 500 swap for the paper line (his ask).

Still for Mark (unchanged from ASSETS): real Qube runs for A1, A2 and A4–A7 · Micron history back to 1984 in Qube · the Breakdown DM in ManyChat · the paper link.
