SCRIPT: J022 · Claude can now build, test and trade your strategy (recreating @samin_yasar12 "Claude copies insider trades") · Round 2
VERDICT: Ready for Director

Vs the original: hook 8 · engine 9 · energy 8 · reward 9 · CTA 8 · Qube 9 · language 8 · copy 8

Reviewed: beatmap.md, J022-1-SCRIPT.md, J022-2-EDIT.md, J022-3-ASSETS.md (round 2) against `knowledge/reference/DdzGPvzIN4C/transcript.srt`, the lesson card and my round-1 review (`review-r1.md`). Script Room J022 has no Mark edits (every line's text matches its orig). Mark's CTA (line 10) and "until you're happy with the result" (line 6) are his calls and aren't scored down.

Two small fixes are left (table below). Neither is a rewrite, and neither needs another round: whoever touches the files next (INK or the Director) can apply them. Everything else open is Mark's to decide.

## Step 0 · Side by side with the original

| Original (exact) | Ours (round 2) | Note |
|---|---|---|
| "Claude can now automatically copy the trades of Wall Street insiders," | A: "Claude can now automatically build a trading strategy, test it on ten years of prices, and trade it for you." | The forbidden power is back: Claude trades for you. It has no villain like "insiders", but it's a known name, a span ("ten years") and a payoff that line 8 delivers. 20 words, about 5.7s. **Hook 8.** Depends on Mark question 1. |
| "and you can set this entire thing up inside Claude." | 1. "And you can do this entire thing from inside Claude." | Small swap. Note: my round-1 fix makes the claim *bigger* than the original's ("do the whole thing", including going live, versus "set it up"). See Mark question 1. |
| "First, connect LiquidTrade, which lets Claude interact with stocks, crypto, forex, and even prediction markets." | 2–3. "First, connect Qube, which turns what you tell Claude into exact rules. When to buy, when to sell, how much, and even when to get out if it goes wrong." | Same engine. "If it goes wrong" fixes the sell / get-out blur. |
| "Then connect it to QuiverQuant. This gives Claude access to data…" | 4. "Then Qube tests those rules on ten years of prices and shows you every trade." | 15 words, clean. |
| "Now here's where it gets crazy." | 5. Same | Kept. |
| "You can create a routine that has Claude automatically check those trades…" | 6. "You can have Claude automatically find what's broken in your strategy and fix it. Over and over, until you're happy with the result." | Mark's wording, now in full. |
| "When it finds one, Claude can send you the trade, explain what happened, and ask for your approval." | 7. "When you like the results, try it on fake money first." | Sounds like a person now. One echo left (fix 1). |
| "Approve it, and Claude can execute the trade through LiquidTrade for you." | 8. "Then, if it holds up, Qube can run it live through a real broker for you." | Same "…can ___ through ___ for you" shape. No vague "approve it", and no approve screen we'd have to fake. Pays off the hook. |
| "So you're basically turned Claude into a trading agent that can research, monitor, and execute from one place." | 9. "So you've basically turned Claude into a trading agent that can build, test and trade from one place." | INK's unrequested change: accepted (see below). |
| "Comment signal, and I'll send you my full video showing you exactly how to build it." | 10. Mark's CTA | Mark's call. Last line, over the DM preview (A12). |

- **Engine 9:** unchanged. Same beats, same order, the #1/#2 cards, the four-item list, the close-up re-hook, the human step, the recap, the keyword over a preview.
- **Energy 8:** 166 words. That's about 47s at the 3.5 words a second the docs now ask Joshua for (original: 44s at 3.6). The dead 3.2s shot is gone (cuts at 7.2 and 8.2), the four-item list cuts every 1.2s, and lines 7–8 are now short where the original peaks. The checker still says 52s at his measured 3.2, so the score only holds if he reads fast. That's written into SCRIPT, EDIT and A0.
- **Reward 9:** the rule is now on screen for 1.5s ("Buy when the S&P 500 drops 2% in a day"), and the result is staged one number at a time, with "Just holding" in white for 2s. You get a recipe you can type tonight, a free tool and an honest, labelled result. That's more than the original gives (it holds the how-to back for the DM).
- **CTA 8:** not scored on Mark's wording. It's the last line, over real footage of what they get, and it names the thing.
- **Qube 9:** in the "#1, connect ___" slot at about 9s, on screen from then on, not in the hook.
- **Language 8:** every line passes the guy-from-LA test on its own. The one thing that doesn't read like a person talking is the echo between lines 6 and 7 (fix 1).
- **Copy 8:** 1 kept, 7 small swaps, 3 rewrites (4, 6, 7), all justified. Checked against the transcript.

## INK's unrequested change to line 9

"build, test and run your strategy" → "build, test and trade". **Accepted.** Why:
- It's closer to the original: three bare verbs with no object, the same as "research, monitor, and execute".
- It repeats the hook's build / test / trade, so the recap closes the loop the hook opened.
- It matches the tqx.ai homepage line, "creates, tests & trades for you all in one platform" (`product-truth-qube`).
- It's 2 words shorter, which helps the 48s target.
- The truth is the same as before: "run" already meant going live. So it rides on Mark question 1, like hook A and line 1. The beat map logs the change, with its reason.

## Round-1 fixes: did they land?

| Round-1 fix | Landed? |
|---|---|
| Hook A: add "and trade it for you" | Yes, word for word |
| Hook B: same promise | Yes |
| Line 1: "do this entire thing from inside Claude" | Yes, but see Mark question 1. My fix widened the claim |
| Line 3: "if it goes wrong" | Yes |
| Line 4: shorten to 15 words, cut the repeated "past" | Yes |
| Line 6: "over and over" (Mark's words) | Yes |
| Line 7: "try it on fake money first" | Yes (my wording leaves an echo, fix 1) |
| Line 8: "if it holds up", no "approve it" | Yes |
| Length: faster read, 48s target | Yes: SCRIPT header, EDIT pace note, A0 step 3 |
| EDIT hook text "build · test · trades for you" | Yes |
| EDIT cut to Joshua at about 7.2s, no slow push-in | Yes (7.2 and 8.2) |
| EDIT rule on screen for 1.5s | Yes (9.6–11.1) |
| EDIT numbers staged, "Just holding" white for 2s or more | Yes (20.3–22.3) |
| EDIT "IF IT HOLDS UP" replaces "YOU APPROVE" | Yes |
| ASSETS A7 prompt (no "round after round on the same ten years") | Yes |
| ASSETS A10 fallback: no finger tap | Yes |

16 of 16 landed.

## Checker

```
python3 tools/check-script.py videos/J022/J022-1-SCRIPT.md
Spoken words: 166 (top hook 20 + script 146) · presenter: joshua · about 52s at 3.2 words/s
No flags.
```
Decision: nothing to clear. The line 9 recap is the original's beat, so it's kept (`remix-for-product`).

## Passes

| Pass | Result |
|---|---|
| 1 Worth making | Pass. Persona: Priya. A recipe, a free tool and a labelled result. The J016 overlap is Mark's call. |
| 2 Logic | Pass. Hook promise (build, test, trade it for you) → paid off by lines 2–4 and 8. Order: rules → backtest → improve → fake money → live. Re-hook at 46%, matching the original's 41% (noted in the beat map). Line 2 says "what you tell Claude", so hook A's "automatically build" doesn't read as "AI picks stocks for you". |
| 3 Facts | Pass (list below). |
| 4 Product truth | Pass, with one question only Mark can answer: whether Claude can start the live run (hook A, line 1, line 9). Everything else is in `product-truth-qube`. |
| 5 Compliance | Pass. Fake money said out loud before live. "If it holds up" is a human check. "Backtest, not live results" stays on every result screen. No promised return. |
| 6 Spoken lines | Pass, apart from the echo in line 7 (fix 1). Every sentence ends. No vague "it": every "it" is the strategy. Contractions throughout. |
| 7 Hooks | A and B now have the stop-power. C is a calmer warning-style option. All make sense cold, none is repeated by line 1, and line 1 works after each one. |
| 8 On-screen | Pass, apart from one term (fix 2). Every line has a picture. Text adds proof. Labels and the source line are in place. One idea on screen at a time in 17.6–22.3. |
| 9 CTA | Mark's wording, last line. The step-by-step it promises isn't live in ManyChat yet (Mark). |
| 10 Fix log | Clean. No "trading idea" or "test your own idea". No Qube in the hook. "Over and over until you're happy with the result" is intact. QUBE keyword. Three documents. No placeholders. |

## Fixes (small; apply before Mark sees it, no new round needed)

| Line | Problem | Rule (skill) | Fix |
|---|---|---|---|
| 7 | "…until you're happy with the result. When you like the results, try it…" The same idea twice in a row (happy → like, result → results). Said out loud, it sounds like the line is repeating itself. This was my round-1 wording, so it's my miss. | `spoken-sentence-rules` read-aloud test; `anti-ai-patterns` #11 | "Once it looks good, try it on fake money first." (EDIT 30.6–33.7 keeps its text and pictures; "FAKE MONEY · PAPER TRADING" still pops on "fake money".) |
| EDIT 20.3–22.3 | "Just holding SPY: $28,634". Everything else on screen calls it "the S&P 500" (the rule text, the term line), so "SPY" is a second name for the same thing, and Priya won't know it. | `terminology` rule 1 (one term per thing); `claims-and-proof` wording ("just bought the S&P 500 and held it") | "Just holding the S&P 500: $28,634", with "price only, no dividends" under it. "SPY" stays in the source line ("TQX backtest · SPY daily closes · no fees"), which is exact. |

## Facts checked

- "ten years" → SPY dip-rule row, Jan 2015 – Dec 2024 (`claims-and-proof`, TQX's own backtests)
- "$10,000 test → $14,428", "Worst drop: −$2,606", "62 trades", "Just holding: $28,634 · price only, no dividends" → same row
- "TQX backtest · SPY daily closes · no fees" → same row (split-adjusted Robinhood daily closes)
- "Buy when the S&P 500 drops 2% in a day" → same row's rule (buy at the close of any day down 2%+); A5's typed prompt matches it exactly (+2% / −3% from the buy price, one position, no fees)
- "S&P 500 = about 500 of the biggest US companies" → `terminology`
- Builds the rules, backtests and shows every trade, improves over rounds, runs live through a real broker → `product-truth-qube` (Build / Test / Improve / Go live, Mark Oct 22)
- "trade it for you", "build, test and trade from one place" → tqx.ai homepage line, "AI that creates, tests & trades for you all in one platform" (`product-truth-qube`)
- "free · no card required", tqx.ai/igqube2 → `product-truth-qube`

## Mark's own lines flagged, not changed

- **CTA (line 10):** kept as he wrote it. The closer-to-the-original option is in ASSETS "Still open". Not scored down.
- **Line 6:** "until you're happy with the result" kept. Line 7 (fake money first) covers Frank's overfitting worry.

## Only Mark can decide

1. **Can Claude start the live run through the Qube connection, or only Qube's own screen?** Hook A ("Claude can now… trade it for you"), line 1 ("do this entire thing from inside Claude") and line 9 ("turned Claude into a trading agent that can… trade") all say Claude can. `product-truth-qube` only covers Claude building and testing. If yes: no change. If no: line 1 goes back to the original's "And you can set this entire thing up inside Claude." (true either way, and a "kept" line), and hook A and line 9 need one short rewrite pass.
2. Does Qube have its own paper trading? (Line 7 says fake money without saying where.)
3. Does Qube have a real go-live screen? (Decides whether A10 is filmed or the A9 graphic is used.)
4. The Breakdown DM has to be live in ManyChat before posting. Should it add the Claude-connection steps?
5. Joshua's A1 run has to show 62 trades / $14,428 / −$2,606 / $28,634.
6. J016 overlap: same rule and numbers. Which one to film, or does J022 replace J016?
