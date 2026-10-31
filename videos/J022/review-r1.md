SCRIPT: J022 · Claude can now build and backtest your trading strategy in Qube (recreating @samin_yasar12 "Claude copies insider trades")
VERDICT: Send back to Scriptwriter

Vs the original: hook 6 · engine 9 · energy 7 · reward 8 · CTA 7 · Qube 9 · language 7 · copy 8

Reviewed: beatmap.md, J022-1-SCRIPT.md, J022-2-EDIT.md, J022-3-ASSETS.md against `knowledge/reference/DdzGPvzIN4C/transcript.srt` and the lesson card. Old files (outline.md, script.md, script-v1.md) were not reviewed. Script Room J022 was last updated by agents, so there are no Mark edits in it.

## Step 0 · Side by side with the original

| Original (exact) | Ours | Score note |
|---|---|---|
| "Claude can now automatically copy the trades of Wall Street insiders," | A: "Claude can now automatically build you a trading strategy and test it on ten years of past prices." | Frame kept, but the stop-power came from the forbidden power (it trades for you) plus the villain (insiders). Ours is a true chore (build and test) with no stake. A stranger doesn't stop for "test it on past prices". **Hook 6.** |
| "and you can set this entire thing up inside Claude." | 1. "And you can set this entire thing up inside Claude." | Kept. Small truth problem (row 2 below). |
| "First, connect LiquidTrade, which lets Claude interact with stocks, crypto, forex, and even prediction markets." | 2–3. "First, connect Qube, which turns what you tell Claude into exact rules. When to buy, when to sell, how much, and even when to get out." | Good swap. Same "#1 / which… / four things / and even" engine. "Sell" and "get out" sound like the same thing (row 3). |
| "Then connect it to QuiverQuant. This gives Claude access to data showing what insiders… are actually buying and selling." | 4. "Then Qube tests those rules on ten years of past prices, and shows you every trade they would've made." | Rewrite is justified (there's no second tool). "#2" beat kept. |
| "Now here's where it gets crazy." | 5. Same | Kept, same close-up. OK under the Oct 23 method, which overrides the brief's don't-copy list. |
| "You can create a routine that has Claude automatically check those trades throughout the day…" | 6. "You can have Claude automatically find what's broken in your strategy and fix it. Round after round, until you're happy with the result." | Good. It's a real escalation, and it's Mark's approved wording, except "round after round" (row 5). |
| "When it finds one, Claude can send you the trade, explain what happened, and ask for your approval." | 7. "When you like the results, paper trade your strategy first, with fake money." | The safety step is needed, but the wording is stiff (row 6). The original's "ask for your approval" got cut, so line 8's "approve it" has nothing to answer. |
| "Approve it, and Claude can execute the trade through LiquidTrade for you." | 8. "Then approve it, and Qube can run it live through a real broker for you." | Approve what? Nobody asked. Also an approval screen isn't a known Qube feature (row 7). |
| "So you're basically turned Claude into a trading agent that can research, monitor, and execute from one place." | 9. "So you've basically turned Claude into a trading agent that can build, test and run your strategy from one place." | Good small swap. |
| "Comment signal, and I'll send you my full video showing you exactly how to build it." | 10. "Comment QUBE and I'll send you the free link and a step-by-step on building your first strategy." | The original promises how to build *the thing you just watched*. Ours promises a general first strategy, and the DM doesn't cover connecting Claude. **CTA 7** (only Mark can close the gap, see below). |

- **Engine 9:** same beats, same order, same big moments (#1 and #2 cards, the four-item list, the close-up re-hook, the human step, the recap, the keyword over a preview). You can tell which Reel it is.
- **Energy 7:** 167 words, about 52s at Joshua's 3.2 words a second, against 44s in the original. Lines 7–8 slow things down right where the original peaks ("Approve it, and Claude can execute the trade"). The edit has one 3.2s shot (5.6–8.8) in a video that should cut every 1.5s.
- **Reward 8:** a four-step recipe, a free tool and a real labelled backtest on screen. That's as good as the original's demo basket, and more honest. The example strategy, though, is only seen in fast-typed terminal text (fix in the edit, row 11).
- **Qube 9:** brought in at the "#1, connect ___" slot where LiquidTrade was (about 9s), on screen throughout, last line "Comment QUBE…". Not in the hook, as Mark asked.
- **Language 7:** "approve it" (line 8), "paper trade your strategy first, with fake money" (line 7) and "when to sell… when to get out" (line 3) fail the guy-from-LA test. The rest passes.
- **Copy 8:** 8 of 11 lines are kept or small swaps (beat-map tally checked against the transcript). The three rewrites are justified.

## Checker

```
python3 tools/check-script.py videos/J022/J022-1-SCRIPT.md
Spoken words: 167 (top hook 18 + script 149) · presenter: joshua · about 52s at 3.2 words/s
No flags.
```
Decision: nothing to clear. The line 9 recap would normally break `anti-ai-patterns` #9 and `retention-writing` #9 (no recap), but it's the original's beat, so it's kept under `remix-for-product`.

## Passes

| Pass | Result |
|---|---|
| 1 Worth making | Pass. Persona Priya (brief and beat map). The viewer gets a recipe, a free tool and a labelled result. The J016 overlap is Mark's call (brief, Needs Mark #1). |
| 2 Logic | Pass, apart from lines 1 and 8. Order is rules → backtest → improve → paper → live. The re-hook sits at 43% instead of 60–75%, which matches the original (41%) and is noted in the beat map. 52s is within 35–60s. |
| 3 Facts | Pass (list below). |
| 4 Product truth | **Fail:** line 8 "approve it" (no known Qube approve step; the beat map says so itself), line 1 "set this entire thing up inside Claude" (you need a Qube login, and the results are viewed in Qube). |
| 5 Compliance | Pass. Paper trading comes before live and is said out loud. Labels are planned on every result screen. No promised return. |
| 6 Spoken lines | **Fail:** lines 3, 7 and 8. |
| 7 Hooks | Hook A fails on stop-power. B is the same weak promise. C is fine. 3 hooks against the brief's 5 (`tqx-voice` allows 3–5, so it's not a fix). |
| 8 On-screen | Mostly good. Overloaded at 16.6–22.5, a dead shot at 5.6–8.8, "YOU APPROVE" has to follow line 8. |
| 9 CTA | Exact approved wording, last line. The step-by-step it promises isn't live yet (Mark). |
| 10 Fix log | No "trading idea" or "test your own idea". No Qube in the hook. Keyword is QUBE. Three documents. No placeholders. Lines end. **One repeat:** a vague "it" with nothing to point to ("approve it": Oct 15, "What rules?" class, `spoken-sentence-rules` #2). |

## Fixes

| Line | Problem | Rule (skill) | Fix |
|---|---|---|---|
| Hook A | No stop-power. The original's hook works because Claude does something you'd think it can't (trades for you). Ours stops at "test it on past prices", a chore. | Hook stop-power (script-critic step 0); `hook-writing` #7 (keep its hook, swap only what's untrue) | "Claude can now automatically build a trading strategy, test it on ten years of prices, and trade it for you." (20 words. "Trades for you" is on the TQX homepage, `product-truth-qube`, and it's paid off by line 8.) |
| Hook B | Same weak promise as A. | `hook-writing` | "If you use Claude, it can now build a trading strategy, test it, and trade it for you." |
| 1 | "Set this entire thing up inside Claude" isn't quite true: you need a Qube login, and the backtest is viewed in Qube. The original's card flagged the same overclaim. | `product-truth-qube` (Claude connection) | "And you can do this entire thing from inside Claude." |
| 3 | "When to sell… and even when to get out": to the ear, sell and get out are the same thing. | `spoken-sentence-rules` #2, #5; `product-truth-qube` approved line | "When to buy, when to sell, how much, and even when to get out if it goes wrong." |
| 4 | 19 words, and "ten years of past prices" said again right after the hook. Costs time. | `retention-writing` #8 | "Then Qube tests those rules on ten years of prices and shows you every trade." |
| 6 | "Round after round" is product-page wording. Mark's approved words are "over and over". | `fix-log` Oct 15; `spoken-sentence-rules` #3 | "You can have Claude automatically find what's broken in your strategy and fix it. Over and over, until you're happy with the result." |
| 7 | "Paper trade your strategy first, with fake money" is stiff, and "with fake money" is tacked on. Nobody talks like that. | Language (step 0); `spoken-sentence-rules` #3 | "When you like the results, try it on fake money first." (Edit chip: "FAKE MONEY · PAPER TRADING".) |
| 8 | "Then approve it": approve what, and where? The original's "ask for your approval" was cut, so nothing sets it up. No Qube approve screen is known (the beat map says so). Fails the LA test. | `spoken-sentence-rules` #2, #4; `product-truth-qube`; `finance-compliance` ("go live only once you've seen how it behaves") | "Then, if it holds up, Qube can run it live through a real broker for you." |
| Length | 52s at 3.2 words a second against 44s. The fixes above come out about even on words. | Energy (step 0); `script-logic` #10 | Record the body at a faster "telling a friend something crazy" pace, jump-cut every breath, and aim for 48s or less. |
| EDIT 0.0–5.6 | Text has to match the new hook. | `on-screen-text` | 2.1–5.6: "build · test · trades for you" (gold on "trades for you"). |
| EDIT 5.6–8.8 | One slow push-in for 3.2s, where the original cuts every 1.5s. The brief also asked for a cut to the face. | `retention-writing` #7 | Cut at about 7.2s to Joshua full-frame on "inside Claude", then back to A3. |
| EDIT 8.8–12.5 | The example strategy (the "type this tonight" reward) is only in fast-typed terminal text that nobody can read. | Reward (step 0); `on-screen-text` | When the rule is typed, pop on-screen text for 1.5s: "Buy when the S&P 500 drops 2% in a day", with the S&P 500 line under it. |
| EDIT 16.6–22.5 | Five things of on-screen text (label, result, worst drop, holding line, source) in about 5s, over a scrolling list. The honest "lost to just holding" line is small and grey, so it gets missed. | `on-screen-text` (8 words or fewer, one at a time) | Stage them: "$10,000 test → $14,428" at 17.2 (1.5s) → "Worst drop: −$2,606" (1.5s) → "Just holding SPY: $28,634" for at least 2s, same size, white. Keep the label and source line on the whole time. |
| EDIT 31.6–40.3 | "YOU APPROVE" matches a line that's being cut. | `on-screen-text` | 35.6: "IF IT HOLDS UP" pops on "holds up", then "LIVE" lights gold on "live". |
| ASSETS A7 | The typed prompt says "Test every change on the same ten years of prices, and keep going round after round." Frank will read that as overfitting, on screen. | `trading-fundamentals` (overfitting) | Type: `Find what's broken in this strategy and fix it. Show me each version and how it did.` |
| ASSETS A10 (fallback) | Joshua's finger tapping the trackpad over the A9 graphic looks like pressing a Qube button that doesn't exist. | `remix-for-product` (no faked features); A10's own "never mock up a Qube button" | Fallback: A9 all lit, full top third, with Joshua's face below. No tap. |

## Facts checked

- "ten years" → SPY dip-rule row, Jan 2015 – Dec 2024 (`claims-and-proof`, TQX's own backtests)
- "$10,000", "$14,428", "62 trades", "−$2,606", "Just holding SPY: $28,634 · price only, no dividends" → same row
- "TQX backtest · SPY daily closes · no fees" → same row (split-adjusted Robinhood daily closes)
- "S&P 500 = about 500 of the biggest US companies" → `terminology`
- Qube writes the rules, backtests and shows every trade, improves over rounds, runs live through a real broker → `product-truth-qube` (Build / Test / Improve / Go live, Mark Oct 22)
- "trade it for you" (proposed hook) → `product-truth-qube`, homepage line "AI that creates, tests & trades for you all in one platform."
- "free · no card required", tqx.ai/igqube2 → `product-truth-qube`

## Mark's own lines flagged, not changed

- **CTA (line 10):** the wording is Mark's (Oct 22, `cta-and-offer`). The original promises how to build *the thing in the video*; ours promises a general first strategy. An option closer to the original, which the Breakdown DM covers because it uses this exact S&P 500 rule: "Comment QUBE and I'll send you the free link and a step-by-step showing you exactly how to build it." Mark's call. Either way, the DM has no Claude-connection steps, so viewers who want "this entire thing inside Claude" won't get them.
- **Line 6:** "find what's broken… fix it… until you're happy with the result" is Mark's approved wording. Frank may read "until you're happy" as tuning to the past. Line 7 (fake money first) answers that. Not changed.

## Only Mark can decide (from the brief, still open)

1. J016 overlap (same rule, numbers and twist).
2. Does Qube have its own paper trading? (Line 7 says fake money without saying where.)
3. Does Qube have a real go-live screen? (Decides A10.)
4. The Breakdown DM has to be live in ManyChat before posting. Should it include the Claude connection steps?
5. Joshua's A1 run has to show 62 trades / $14,428 / −$2,606.
