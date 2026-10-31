SCRIPT: J024 · $30,000 Wall Street software just got replaced by a free AI tool
VERDICT: Ready for Director (round 2; every round-1 fix landed, nothing new broke)

Vs the original: hook 9 · engine 9 · energy 9 · reward 9 · CTA 9 · Qube 9 · language 9 · copy 9 · word count 8 · flow 9 · **overall 8.9** (round 1: 8.6)

Header: "**Original video:** https://www.instagram.com/p/Db3P17nN1Og/" is still there (fix-log Oct 24). Pass.

## Round 1 fixes

| # | Round-1 fix | Landed? | Where I checked |
|---|---|---|---|
| 1 | Line 13: "...and now you can use one for free." → "...and we just opened one up to everyone." | Yes, word for word | SCRIPT line 13 (diff against `J024-1-SCRIPT-v1-prev.md`: only this line changed), EDIT 42.8–48.4s, beat map row 51.7–54.4 (reason rewritten to match) |
| 2 | Line 3 visual: cut A4 (sample +55.43% / Sharpe 1.22) and use Qube's empty plain-English box, 2 cuts with a push-in | Yes | EDIT 12.5–15.9s now shows the empty box (A6, first 2s), "No result or number on screen". A4 row, its "Still open" note, its label line and its entry in the phone-filmed list are all gone from ASSETS. A6 has a new step 2 for the empty-box shot with a CHECK (no result, return or number). `grep` finds no "A4", "55.43", "814" or "Sharpe" left in EDIT or ASSETS. "Never on screen" now says no return figure or trade count anywhere in the video |
| 3 | Optional: drop "BILLIONS" and "LOCKED BEHIND HEDGE FUND DOORS" on lines 13–14 | Yes | EDIT 42.8–53.1s: on-screen text is "none (the one-word captions carry it, like the original)" on both rows. The desk-cut burst is unchanged |

Line 18.1–20.0s (line 5) was updated to "A6, after the empty-box shot", so the A6 clip order still matches the video. Good catch by the writer.

## Step 0: side by side with @daniel.cross.ai (transcript.srt, lesson card, beat map)

| Dimension | R1 | R2 | Why |
|---|---|---|---|
| Hook stop-power | 9 | 9 | Unchanged. The original's hook word for word, one swap ("GitHub repo" → "AI tool"), "$30,000 worth of software" from frame 1, split screen, 16 fast cuts. |
| Engine kept | 9 | 9 | Unchanged. Every beat in order, ChatGPT at 50% (original 51%), "Completely free" at 71% (original 75%), landing at 86% (original 90%). |
| Energy and pace | 8 | 9 | Line 13 now turns instead of repeating line 12, so the second burst of desk cuts builds into "hedge fund doors" without a flat spot. With the headline text gone, lines 13–14 look like the original's 45–55s: cuts and one-word captions only. |
| Reward | 9 | 9 | Unchanged. The tool's name, how it works, every trade shown, free with no card. |
| CTA | 9 | 9 | Unchanged. Standard CTA, last spoken line, end screen "Comment QUBE". |
| Qube | 9 | 9 | Unchanged. Comes in where the original names Kronos, not in the hook. "We" in line 13 points back to "My team at TQX" in line 1. |
| Language | 9 | 9 | "and we just opened one up to everyone" reads out loud cleanly in Joshua's voice. No "trading idea", no "rules". |
| Copy | 8 | 9 | Line 13 now keeps the original's standout turn ("and a group of researchers just gave it away" → "and we just opened one up to everyone"): same "and [who] just [did it]" shape, same David-vs-Goliath stakes. Tally still 3 kept, 9 small swaps, 3 rewritten (each with a reason). Line 11 is still a weaker list line than "Crypto, Forex, equities, and more.", but it stays true; leaving it, same as round 1. |
| Word count | 8 | 8 | Still 182 against 166 (+9.6%). The fix was 8 words for 8, so it's still inside 149–183, one word under the cap. Any later line change must not add a word. |
| Flow | 8 | 9 | 12 → 13 no longer says "free" twice in a row ("free" now: hook, 12, CTA, spread out). 13 → 14 flows: "opened one up to everyone" → "used to be locked behind hedge fund doors" (the original's order). Every question answered, every "it" points at Qube. |

No score under 8. No automatic send-back.

## Checker

```
Spoken words: 182 (top hook 19 + script 163) · presenter: joshua · about 57s at 3.2 words/s
No flags.
```
Decision: nothing to decide. Original 166 words (`wc -w` on transcript.srt, as in round 1). New line 13 is 18 words, under 20.

## Fixes

| Line | Problem | Rule (skill) | Fix |
|---|---|---|---|
| none | | | |

Checked and fine (no change):
- ASSETS IDs now jump from A3 to A5 because A4 was cut. Nothing points at A4 any more, so it can't be filmed by mistake. Optional, not blocking: the writer can add "(A4 cut in round 1)" under the table so Joshua doesn't think a row went missing. Don't renumber; every EDIT cue would have to change.
- Line 3's new visual (empty box) is quieter than the original's dashboard insert at that beat, but the original's dashboard is a P&L screen we can't copy (lesson card "What we can't copy"). The hard cut, the music lift and the push-in keep the re-hook's energy, and the empty box sets up line 4's "no code" answer. Fine.
- Line 13 "we just opened one up to everyone": "one" points at "tools like this" in the same sentence. Clear out loud.
- Round-1 "checked and fine" items (line 4, line 6, line 9, re-hook at 22%) unchanged and still fine.

## Passes

| Pass | Result |
|---|---|
| 0 Checker | No flags |
| 1 Worth making | Priya. A tool she can try today, free, no card. Not a repeat of J008 / J022 / J014. Real screens, no metaphor. Pass |
| 2 Logic | Promise: a $30K Wall Street tool just got replaced by a free AI tool. Payoff: lines 1, 12, 13. One idea. 182 / 149–183. Second hook line 12 at 71%. Build → test, no live step said. Line 13 now earns its place (`script-logic` #3). Pass |
| 3 Facts | See below. Nothing new apart from line 13's second half, which is the original's claim swapped to TQX |
| 4 Product truth | Every Qube line is in `product-truth-qube`. "Opened one up to everyone" sits on "Free · no card required" / "Start free". No TQX OS. Pass |
| 5 Compliance | No return spoken or shown anywhere now (A4 gone). No ticker call. "Backtest, not live results" on A9. "Example" on the typed S&P 500 sentence. No comparison with other bots' results. Pass |
| 6 Spoken lines | Every sentence ends. Every "it" = Qube or the strategy; "we" = TQX; "one" = a tool like this. Contractions. Longest line 19 words (line 6). "T-Q-X" as letters. Pass |
| 7 Hook | Makes sense cold, "$30,000" in the first words, not repeated by line 1. Pass |
| 8 On-screen | Every line has a visual. No on-screen text copies the voice (lines 13–14 cleaned up). Labels in place. Pass |
| 9 CTA | One ask, standard wording, last spoken line. QUBE flow sends the link. Pass |
| 10 Fix log | Every row checked again: one hook, the original's · Qube not in the hook · ±10% · "strategy", no "rules", no "trading idea" · J022 lines word for word incl. "if it all goes wrong" · "up to five years of real price data" · standard CTA, no "follow" · basics not explained · Original video link line. No Script Room edits from Mark on J024 yet (`data/mark-edits/`). No past correction came back |

Facts checked:
- "$30,000 software", "depended on for decades", "spent billions" → the original's claims, taken as given (Mark, Oct 23 and Oct 25). Not checked
- "My team at TQX built an AI called Qube" → `product-truth-qube`
- "allows you to build a trading strategy from natural language" → `product-truth-qube` (Mark's J022 line)
- "When to buy, when to sell, how much, and even when to get out if it all goes wrong" → `product-truth-qube` / fix-log (Mark's J022 line)
- "Qube writes the code for you" → `product-truth-qube`
- "up to five years of real price data" → `product-truth-qube` (Mark's J020 line)
- "every single trade, wins and losses" → `product-truth-qube`, `finance-compliance` (losses shown)
- "Completely free, no card needed" → `product-truth-qube` ("Free · no card required")
- "we just opened one up to everyone" → the original's "a group of researchers just gave it away", swapped to TQX; backed by "Start free" / "Free · no card required" (`product-truth-qube`)
- A6 typed sentence (2% / 2% / 10% / 3%) → a made-up example, labeled "Example" on screen
- A4 sample result → removed from the video (round-1 fix)

Mark's own lines flagged, not changed: line 2 and line 6 (his J022 lines), line 10 (his J020 wording), line 15 (his standard CTA). None needs a change.
