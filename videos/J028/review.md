SCRIPT: J028 · I ranked 6 AI chatbots for trading, S to F (recreating our own M05 "Quant trading tools ranked S to F") · Round 5 (the 40s cut, Mark Oct 27)
VERDICT: Ready for Director

Vs the original: hook 8 · engine 9 · energy 9 · reward 8 · CTA 8 · Qube 9 · language 9 · copy 8 · flow 9 (overall 8.6)

Length: 130 spoken words, about 40.6s at Joshua's 3.2 words a second. Inside 35–60s, on Mark's 40s target. M05 runs 83.7s (past 60s), so the ±10% word rule doesn't apply: it's cut to its strongest beats (`script-logic` #10). Pass.

Reviewed: J028-1-SCRIPT.md, -2-EDIT.md, -3-ASSETS.md and beatmap.md against their `-v4-prev.md`; `knowledge/own-videos/M05/transcript.srt`; J029 and J032 current scripts. Claims from Mark and from M05 taken as given.

## Checker

```
Spoken words: 130 (top hook 16 + script 114) · presenter: joshua · about 41s at 3.2 words/s · limit 35-60s = 112-192 words, aim 40-50s
No flags.
```

## Copy check (Oct 27: hook copied, body fresh)

| # | M05 | Ours | Result |
|---|---|---|---|
| H | "I ranked 6 tools for building a trading strategy from S to F, so you don't have to." | "I ranked 6 AI chatbots for trading from S to F, so you don't have to." | Word for word, only Mark's tool swap. Pass |
| 1 | "And yes, I am biased because we built one." | "Full disclosure, we built something on this list." | Fresh. Pass |
| 2 | "Asking chat GPT what to buy. F tier. You're just getting an opinion that nobody has actually tested." | "ChatGPT for stock picks. F tier. Super confident, zero proof." | Fresh. Pass |
| 3 | "Excel. D tier. … Your results look amazing, but they're fake." | "Gemini. D tier. It can make up a profit number without running one trade." | Fresh. Pass |
| 4 | "Meta trader. C tier. It's popular for Forex…" | "Grok. C tier. All the hype on X, none of the testing." | Fresh. Pass |
| 5 | "Trading view. B tier. Really good charts and it can test strategies…" | "Perplexity. B tier. Legit sources, but it won't test your strategy." | Fresh. Pass |
| 6 | "Quant connect. A tier. Very powerful for testing strategies, but you have to write real code…" | "Claude. A tier. It'll even code your strategy, but the testing's on you." | Fresh. Pass |
| 7 | "Notice the pattern?" | "See the problem?" | Same job (re-hook question), different words. Pass |
| 8 | "Cube. S tier. You describe the idea in plain English. It turns it into exact rules, tests them on past prices and runs it." | "Claude plus Qube. S tier. Type your strategy like you're texting a friend. Claude builds it in Qube, tests it, and shows you every trade." | Three-step shape is close, but the words are `product-truth-qube`'s and Mark's J022 line, not M05's. Pass |
| 9 | M05's ending | Agreed J028 CTA | Mark's call |

## Bias line vs the batch

"Full disclosure, we built something on this list." Doesn't echo J029 line 6 ("Heads up, that bottom one's ours.") or J032 line 7 ("My team makes it, so I'm not exactly neutral."). No other current script uses "Full disclosure". Still owns the bias up front at about 6s (`finance-compliance` #6). Pass.

## Every tier line: LA speech and true

| Line | Natural? | True and fair? |
|---|---|---|
| 2 ChatGPT "Super confident, zero proof." | Yes | Yes: an untested opinion (M05's own reason, Mark's ranking) |
| 3 Gemini "It can make up a profit number without running one trade." | Yes | Fair and safe: "can" says it's possible, not that it always does, and any chatbot can invent a number it never calculated (`positioning`: say what a tool does, never "useless"). EDIT keeps the answer blurred, so no real figure is shown |
| 4 Grok "All the hype on X, none of the testing." | Yes | Yes: it pulls from X; it doesn't test a strategy |
| 5 Perplexity "Legit sources, but it won't test your strategy." | Yes | Yes |
| 6 Claude "It'll even code your strategy, but the testing's on you." | Yes | Yes: it writes the code, and running a backtest on price data is left to you |
| 8 S tier | Yes ("like you're texting a friend" is Mark's) | Yes (`product-truth-qube`: Claude connection, Test, every trade). "Backtest, not live results" on screen |

## Flow

Hook (6 ranked) → we built one → the one everyone uses, at the bottom → Gemini fakes a number → Grok, Perplexity, Claude: three "no testing" in a row → "See the problem?" (26.2s, 65%) → Claude plus Qube does the testing and shows every trade (27.2s) → argue or comment QUBE. With the pattern sentence cut, the problem is named three times in the C, B and A lines and by the "YOU TEST IT" chips, and the S tier answers it with "tests it". Every line sells the next. Pass.

## EDIT and ASSETS vs the cut

Every spoken sentence in SCRIPT appears in the EDIT spoken column (checked by script). Times run 0–40.6s plus the 2s end screen. No stale lines in EDIT or ASSETS ("biased" only as M05's source big text for A3; "insane", "0 lines of code", "QUANT TRADING" pill, Google news insert all listed under "Dropped"). New on-screen words are covered: "ZERO PROOF", "0 trades run" + "MADE UP" (A4/A5), "Tested? ✗", "You test it" chip, "YOU TEST IT" board chips (A2), A0 close-up is "See the problem?". ASSETS "Still open" refers to line 9 (correct number). Pass.

## Fixes

| Line | Problem | Rule (skill) | Fix |
|---|---|---|---|
| 3 (optional, not blocking) | With "ask it to test a strategy" cut, the profit number comes in by sound with no lead-in. The "Backtest my strategy" bubble (A4a) covers it on screen | Every sentence sells the next (`script-logic` #3b) | Writer's call: "Gemini. D tier. Ask it to backtest, and it can make up a profit number without running one trade." (+5 words, 135 total, about 42s) |

Facts checked: no spoken numbers. "tests it, and shows you every trade" → `product-truth-qube` (Test, Claude connection). "like you're texting a friend" → Mark's Oct 15 line. Tier order and each chatbot's description → Mark's direction, taken as given; line 3 checked for fairness only (above).

Mark's own lines flagged, not changed:
- Hook "6 AI chatbots": the sixth entry is Claude plus Qube. Works as the reveal.
- Line 9 CTA "…I'll send you the full breakdown": Breakdown DM not live in ManyChat yet (P6). Fallback is in ASSETS "Still open".

For the Director: `approval.md` still describes the v3/v4 long version and needs redoing for the 40s cut.
