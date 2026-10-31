SCRIPT: J029 · How long it takes to build a trading strategy with each tool (recreating @thecodingjesusquant "How long does it take to crack each quant role?") · Round 4 (Oct 27 fresh-body pass)
VERDICT: Send back to Scriptwriter

Vs the original: hook 8 · engine 9 · energy 8 · reward 8 · CTA 8 · Qube 9 · language 7 · copy 7 (overall 8.0, from 8.4 on v3; three small line fixes, then ready)

Mark's test this round, "rewording it in a way that actually makes sense, like somebody from LA would actually speak": 12 of 15 body lines pass out loud in Joshua's voice. Lines 4, 12 and 14 don't (below).

Word count: original 159 · ours 170 (+6.9%, range 143–175). Pass. With the three fixes below: 173, still inside.
Flow (`script-logic` #3b): one break. Line 12's "This" doesn't point at anything the viewer just heard (see table). Everything else sells the next line: niche tool → nobody learns it → but it's easy → number → disclosure → loop → Excel picture → easy one → its catch → last one → what it does → payoff on the number → CTA.
Header: `**Original video:** https://www.instagram.com/p/DayGvQMMzyd/` present. Pass.

Reviewed: J029-1-SCRIPT.md, -2-EDIT.md, -3-ASSETS.md and beatmap.md against their `-v3-prev` copies (diffed); `knowledge/reference/DayGvQMMzyd/transcript.srt`; J028-1-SCRIPT.md; approval.md; fix-log (J029 row: Mark's line 1, Oct 27). Claims and numbers from Mark and the original are taken as given and not scored.

## Step 0 · Copy check, line over line

| Original (exact) | Ours | Own sentence? |
|---|---|---|
| "So how long does it take to crack every quant trading industry role?" | Hook: "So how long does it take to build a trading strategy with every quant trading tool?" | Hook, word for word with the one swap (role → Mark's topic). Pass |
| "For research, we have around 12,000 hours, 9,000 of those being hardcore math." | 1. "For Python, we have around 300 hours, 200 of those are just learning to code." | **Mark's line. Not sent back, not scored** |
| "Hardware engineer, think FPGA, low latency." | 2. "Pine Script. That's TradingView's own coding language." | Yes. "think A, B" frame gone |
| "Not a lot of people go for this." | 3. "Hardly anybody learns it." | Yes. Every word different |
| "...not on anybody's radar... probably not as competitive as you think." | 4. "Shame, because it's honestly not that hard to pick up." | Yes, own frame. Fails on language (below) |
| "Dev, around 1,200 hours." | 5. "QuantConnect? You're looking at about 150 hours." | Yes |
| "We can cut this down by 300 to 400 hours with getcracked.io." | 6. "Full disclosure, we built the bottom one." | Yes. No "biased", clear of J028 line 2 |
| "More with our upcoming placement accelerator." | 7. "Stick around for that one." | Yes, and a real open loop |
| "Then we have DevOps." | 8. "Excel's up next." | Yes |
| "Think infrastructure as code, chef, deployments, CICD, etc." | 9. "You're dragging formulas down a sheet of old prices." | Yes. A picture, not a list. Best line in the body |
| "800 hours, trade-offs, the easiest one..." | 10. "Call it 60 hours. ChatGPT's as easy as it gets. You ask, boom, there's a strategy." | Yes |
| "...really things nobody wants to do, 500 hours, lowest bar to entry." | 11. "5 minutes, anyone can do it. But you've got no idea if it works." | Yes |
| "And lastly, we have something that you'll compete against other people fiercely in." | 12. "Last one. This used to take a whole team at a hedge fund." | Yes. Fails on "This" (below) |
| "This is statistics, probability, EV, trading games," | 13. "Zero code. Pick a ready-made strategy, backtest it, let the AI make it better." | Yes. "This is A, B, C, D" frame gone |
| "almost everything that you can think of that you need to execute and trade well." | 14. "That's pretty much everything you need, in one spot." | **No.** Same frame: "almost everything... you need" → "pretty much everything you need", one word swapped and the tail trimmed. Read it over theirs and it's their sentence. Automatic send-back (`remix-for-product` #3) |
| "This is going to take 1,500 hours." | 15. "In Qube, it's built and tested in 15 minutes." | Yes. Still ends on the number |

## Checker

```
Spoken words: 170 (top hook 16 + script 154) · presenter: joshua · about 53s at 3.2 words/s
No flags.
```
No flags to decide.

## Fixes

| Line | Problem | Rule (skill) | Fix |
|---|---|---|---|
| 14 | Lightly reworded copy of the original's "almost everything that you can think of that you need..." (same frame, "almost" → "pretty much") | `remix-for-product` #3, critic copy check (Mark, Oct 27) | "No team, no coder. Just you and one app." (9 words, same count). Pays line 12's hedge-fund team, and "one app" sets up "In Qube" |
| 4 | "Shame, because..." is British. A guy from LA says "Which is crazy, because..." or "It's a shame, 'cause..." | `spoken-sentence-rules` #11 (American English), read-aloud test #3 | "Which is crazy, because it's honestly not that hard to pick up." (+2 words) |
| 12 | "This used to take a whole team at a hedge fund." "This" points at nothing heard. It's the rule's own bad example ("That used to take a whole team of people") | `spoken-sentence-rules` #2 and #4, `script-logic` #3b | "Last one. Building a strategy used to take a whole hedge fund team." (+1 word; "Building a strategy" echoes the hook, "whole" stays the one emphasis word) |
| Knock-ons | | | EDIT spoken cells for lines 4, 12, 14 word for word; re-time from 13.1s (+0.6s after line 4, +0.3s after line 12, end ≈ 54s); beat map rows, Pass 3 table, count (173) and "every sentence sells the next" line; script header (ours 173, about 54s); EDIT "Times" note (about 54s). ASSETS unchanged (no spoken text) |

Language read-aloud, the lines that pass: 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 15. "You ask, boom, there's a strategy" and "dragging formulas down a sheet of old prices" sound like Joshua talking to a friend. Line 15's "it's" works once line 12 names "a strategy".

## J028 overlap (videos/J028)

None spoken. No "biased", "nobody has actually tested", "plain English", "every single trade", "No code required" or "years of prices" in J029. Shared on purpose and cleared by the Director: a disclosure line ("Full disclosure, we built..." vs J028's "And yes, I am biased because we built one"), a no-code difference ("Zero code" vs "No code required"), ChatGPT as the untested one (different words), and Qube last. The suggested line 14 fix adds nothing from J028.

## Docs consistency

- EDIT: all 16 spoken cells match the script word for word; times re-cut to the 170-word take (about 53s); v3's stale "For Python from scratch" cell is now fixed. Pass.
- Beat map: per-line counts (15 · 7 · 4 · 10 · 7 · 7 · 5 · 3 · 9 · 16 · 14 · 13 · 14 · 9 · 9 · 12 = 154 + hook 16 = 170) check out against the script. Its Pass 3 row for line 14 calls it an "own sentence"; it isn't (above).
- ASSETS: identical to v3, six numbers match the script and EDIT (300, 100, 150, 60 hrs, 5 min, 15 min). Pass.
- approval.md still describes v3 ("This is no code, ready-made strategies...", 174 words). Director to rewrite after this round.

## Passes

- Pass 1, worth making: persona Daniel, six tools and a free one to try. Pass.
- Pass 2, logic: promise = a time for every tool, paid at each reveal and line 15. Second hook at line 12 (66%). One break, line 12 (fix above).
- Pass 3, facts: unchanged from v3. Same six numbers; line 15's "tested" was already the green on-screen label; "Zero code", "ready-made strategy", "backtest", "AI make it better" = Build/Test/Improve in `product-truth-qube`; hedge-fund team = `positioning`. Pass.
- Pass 4, product truth: no TQX OS, free sign-up, Qube said once in speech before the CTA. Pass.
- Pass 5, compliance: "Our estimates" on screen to the end screen; disclosure line marks the bias; no returns or backtest results shown. Pass.
- Pass 6, spoken lines: contractions throughout, every sentence ends, no "trading idea". Lines 4 and 12 fail (above).
- Pass 7, hook: the original's, one swap, no Qube. Pass.
- Pass 8, on screen: reveals on the right words, never two at once, "untested"/"tested" labels on "5 minutes"/"15 minutes". Pass.
- Pass 9, CTA: standard, last spoken line, end screen "Comment QUBE". Pass.
- Pass 10, fix log: Mark's line 1 (Oct 27) kept exactly. Nothing from earlier rows comes back.

Facts checked: Python 300/200, Pine Script 100 (screen only), QuantConnect 150, Excel 60, ChatGPT 5 min, Qube 15 min → Mark's estimates (brief, Oct 27), not fact-checked · "used to take a whole team at a hedge fund" → `positioning` · ready-made strategy, backtest, AI improve, no code → `product-truth-qube` Build/Test/Improve · "free sign-up" → `cta-and-offer`
Mark's own lines flagged, not changed: line 1 ("For Python, we have around 300 hours, 200 of those are just learning to code.") keeps the original's "we have around X hours, Y of those" frame. It's Mark's, so it stays and isn't scored.
