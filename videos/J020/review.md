SCRIPT: J020 · Claude tests your strategy on five years of prices (recreating @buildwithai.club "Claude tests your trade 10,000 times")
VERDICT: Send back to Scriptwriter

Vs the original: hook 7 · engine 7 · energy 6 · reward 8 · CTA 6 · Qube 7 · language 6 · copy 7

Reviewed: beatmap.md, J020-1-SCRIPT.md, J020-2-EDIT.md, J020-3-ASSETS.md, against `knowledge/reference/DezOgThKETj/transcript.srt` and the lesson card. Old outline.md and script.md ignored (rejected drafts).

## Side by side (Pass 0)

| Score | n | Why |
|---|---|---|
| Hook stop-power | 7 | Same frame ("Claude can now… before you risk a single dollar"), but their stopper is "10,000 times". Ours is "on five years of prices", which is softer, and "test your stock trades" is slightly off: Qube tests a strategy, not trades the viewer has made. The "607 trades" counter at 2s carries the number on screen, so it holds up, just not as hard as theirs. |
| Engine kept | 7 | Same beats in the same order: hook, reveal, four parts with a tab bar, "But the craziest…", full-screen count-up, recap, honesty line, keyword. But the reveal (line 1) drops the three things that made theirs land: news ("just"), a count ("11") and "free". No count means no open loop through the middle. The edit also puts the re-hook in a full-face close-up, which the original saves for the honesty line only. |
| Energy and pace | 6 | 186 words / about 58s against their 164 words / 44s. Joshua reads at 3.2 words a second, slower than their 3.7, so at the same word count we're already about 7s longer. Our extra 22 words go on restating lines (line 10, "five years" said twice, "it's got hindsight in it, since…"). Line 6, "is called a backtest", lands flat where theirs lands on a name ("the time machine"). |
| Reward | 8 | Better than theirs on substance: a complete rule the viewer could type tonight, a real labelled result, and the loss shown. Theirs was an example run from a README nobody saw. |
| CTA | 6 | Theirs pays off a loop the whole video built ("all 11 skills": only 5 explained, the rest behind the keyword). Ours is the fixed generic line, so nothing in the video makes the DM feel like the missing piece. And the Breakdown DM it promises still isn't live. The fix is partly Mark's call (see flags). |
| Qube slipped in | 7 | Slipped in in the right place (line 1, about 5s, where they reveal their tool), on screen the whole way, and the last line is "Comment QUBE…". But Qube is only spoken once before the CTA. Line 7, where their tool does its big trick ("It takes your trade and…"), says "It" instead of "Qube". |
| Language (guy from LA) | 6 | Two hard fails (line 1: "turns what you type into rules. Each one handles a different job"; line 11: "it's got hindsight in it, since we know these stocks won") and four soft ones (hook "test your stock trades on five years of prices", line 2 "trading opportunities", line 6 "is called a backtest", line 10 "all that"). |
| Copy check | 7 | The beat map is honest: 8 small swaps, 3 rewrites, 0 lines kept word for word. But line 1 throws away more of the original than it has to (the count and "free" can stay true), and line 6 swaps a named feature for a flat term. With the fixes below, 9 of 11 lines keep the original's frame. |

Five scores are under 8, so it goes back. The lines to change are below.

## Length: exactly what to cut

The original is 164 words. At Joshua's pace, our ceiling for 44–48s is about 150–155 words. The fixes below bring it to **152 words, about 47.5s** at 3.2 words a second (about 46s with hook C).

| Line | Now (words) | Cut to (words) | Saves |
|---|---|---|---|
| 10 | "So you get to see all that before putting your money on the line." (14) | **Delete the whole line.** The hook already says "before you risk a single dollar", and lines 8–9 are the moment you see it. | −14 |
| 3 | "Another puts no more than $2,000 into any of those stocks." (11) | "Another caps each stock at $2,000." (6) | −5 |
| 4 | "Then there's an entry rule that buys the day one of them drops 3%." (14) | "Then an entry rule buys the day one of them drops 3%." (11) | −3 |
| 5 | "And there's an exit rule that takes profit at 3% or cuts your losses at 5%." (16) | "And an exit rule takes profit at 3%, or cuts your losses at 5%." (13) | −3 |
| 6 | "But the craziest part is called a backtest." (8) | "But the craziest part is the backtest." (7) | −1 |
| 7 | "It takes your rules, runs them through five years of past prices, and shows every trade." (16) | "Qube takes your rules and runs them through five years of real prices." (13). The trade list scrolling on screen shows "every trade". | −3 |
| 11 | "Of course, it's a backtest, not live results. And it's got hindsight in it, since we know these stocks won." (20) | "Of course, it's a backtest, not live results, and we already know these stocks took off." (16) | −4 |
| 2 | "One rule scans the 10 biggest US stocks looking for trading opportunities." (12) | "One rule scans the 10 biggest US stocks looking for a drop." (11) | −1 |
| 1 | (18) | Rewritten at the same length (see table) | 0 |

Total: 186 → 152. Hook A, lines 8, 9 and 12 stay exactly as they are.

## Checker

```
python3 tools/check-script.py videos/J020/J020-1-SCRIPT.md
Spoken words: 186 (top hook 18 + script 168) · presenter: joshua · about 58s at 3.2 words/s
No flags.
```
Decision: no flags to rule on. The word count is the problem; see "Length" above.

## Line by line

| Line | Problem | Rule (skill) | Fix |
|---|---|---|---|
| Hook A | "test your stock trades": Qube tests a strategy, and the viewer hasn't made any trades yet. "Trades" also clashes with "607 trades" later, where it means something else. | Words people say (`spoken-sentence-rules` #3), approved fix "Claude can now build you a trading strategy" (`fix-log` Oct 23) | "Claude can now test your trading strategy on five years of prices before you risk a single dollar." (18, same length) |
| 1 | "which turns what you type into rules. Each one handles a different job": which rules? "Each one" points at a vague plural. And the line drops the original's count and "free", so nothing pulls the viewer through lines 2–5. | Vague nouns (`spoken-sentence-rules` #2, `fix-log` "What fucking rules?"), open loop (`retention-writing` #1), keep the engine (`remix-for-product`) | "Claude's hooked up to Qube, which breaks your strategy into four rules. Each one handles a different job." (18). "Four rules" is true (stocks, size, entry, exit, which is the approved "when to buy, when to sell, how much, when to get out" line). It gives "each one" something to point at, and it's their "11 skills… each one handles a different job" with our true count. "Free" stays on screen ("Qube · free to start, no card") as already planned. |
| 2 | "looking for trading opportunities" is ad copy, not talk. It's also wrong about what the rule does: this rule only picks the stocks, and the 3% drop is the entry rule in line 4. | Words people say (`spoken-sentence-rules` #3), cause and effect (`script-logic` #5) | "One rule scans the 10 biggest US stocks looking for a drop." (11). It keeps their "One… scans… looking for" and sets up line 4. |
| 3 | Too long for what it says ("puts no more than $2,000 into any of those stocks"). | Pace (`retention-writing` #8) | "Another caps each stock at $2,000." (6). "Caps it at" is how people say it. |
| 4–5 | "Then there's an… / And there's an…" repeats "there's" across two lines, which costs 6 words and some punch. | Pace (`retention-writing` #8) | 4: "Then an entry rule buys the day one of them drops 3%." · 5: "And an exit rule takes profit at 3%, or cuts your losses at 5%." Both are complete sentences, one breath each. |
| 6 | "is called a backtest" sounds like a textbook. Theirs works because "the time machine" is a name that makes you wait. Ours names a term Daniel doesn't know yet. | Words people say (`spoken-sentence-rules` #3), re-hook carries content (`retention-writing` #3) | "But the craziest part is the backtest." Line 7 explains it right away, with Qube named in it (next row). |
| 7 | "It takes your rules…": this is where their tool does its trick, and we say "It", not "Qube". Qube is spoken only once before the CTA. "five years of past prices, and shows every trade" repeats the hook and what the screen already shows. | Qube slipped in where the original shows its tool (`remix-for-product`, `cta-and-offer`), every line earns its place (`script-logic` #3) | "Qube takes your rules and runs them through five years of real prices." (13). This is also the one-clause explanation of "backtest" for Daniel (`terminology` rule 2). |
| 9 | "down about $3,200": from where? A drawdown is measured from the high, not from the $10,000 start, and Frank will read it as "fell to $6,800". Mark approved the same wording in J018, so it's a check, not a rewrite. | Drawdown (`trading-fundamentals`), reference points (`spoken-sentence-rules` #5) | Keep the line. In the A3 run, confirm −$3,207 is the drop from a high. If it is, add "from its high" on screen: "Worst drop from a high: −$3,207". |
| 10 | Restates the hook ("before you risk a single dollar" / "before putting your money on the line"), and "all that" is vague. It costs 14 words, about 4s. | Every line earns its place (`script-logic` #3), length (`script-logic` #10) | Delete. Edit change below. |
| 11 | "it's got hindsight in it, since we know these stocks won": nobody says a stock "won", and "it's got hindsight in it" is how a paper talks, not how a person does. 20 words, the longest line in the script. | Words people say (`spoken-sentence-rules` #3), required caveat (`claims-and-proof` "10 biggest US stocks", `trading-fundamentals` hindsight) | "Of course, it's a backtest, not live results, and we already know these stocks took off." (16). It keeps their "Of course, it's a…", the hindsight point says why in plain words, and "Today's 10 biggest companies = hindsight" stays on screen with the term. |
| 12 | Fixed CTA, correct keyword. It's the weakest beat against the original only because nothing in the video makes it the missing piece. | `cta-and-offer` | No wording change by the writer. See Mark flags (offer and Breakdown DM). |
| EDIT 27.5–30.0 | A full-face close-up on line 6. The original keeps its re-hook in the split (the "Time Machine" tab gets outlined) and saves the sudden face shot for the honesty line. Using it twice kills the pattern break at 45.7s. | Copy the original's moves (`remix-for-product`, brief "Copy its moves") | Keep line 6 in the split: BACKTEST tab outlined in gold, 110% punch-in on Joshua, music drop as planned. The full-face close-up is used only on line 11. |
| EDIT 41.6–45.7 | This row goes with line 10. | — | Delete the row. Move the "back to split" cut to line 9 (the original cuts back to split at 33.92s after the count-up). Show the equity curve with the dip circled, the step bar extending `BACKTEST ✓ → PAPER → LIVE`, and "Go live" still locked. Drop the $1 coin (it would land on the loss line). |
| EDIT 38.8–41.6 | "Worst drop: −$3,207" | `trading-fundamentals` drawdown | "Worst drop from a high: −$3,207", if A3 confirms it (line 9 row). |
| EDIT, all times | Timed to 186 words. | — | Re-time to 152 words (about 47.5s) once the take is in. Remove the "If the take runs over 58s, cut line 10" note. |
| ASSETS A0 steps 5–6 | Step 5 records line 6 close-up (no longer needed). Step 6 has the old line 11. | Assets match the script (`fix-log` Oct 11) | Step 5: cut it (the punch-in comes from the main take). Step 6: the new line 11 text. Step 4: "lines 1–9, 11, 12". |
| ASSETS A5 (3), (4) | The NVDA chip flashing "BUY" is a drawn example, not a trade from the run, and on its own it reads like a ticker call. | Ticker calls (`finance-compliance`); the original tags every drawn chart "EXAMPLE" | Add "Example" bottom-left on A5 (3) and (4), like A6. |
| ASSETS "Still open", length bullet | Says 58s, "first cut: line 10". | — | Update to 152 words / about 47.5s, with line 10 cut. |

## Passes

| Pass | Result |
|---|---|
| 1 Worth making | Clean. Persona Daniel. He gets a full rule, a real labelled result and a tool to run it in. |
| 2 Logic | Promise (test it before you risk a dollar) paid at lines 7–9. One idea. Re-hook at about 55% after cuts (the original is at 50%; copying it is fine). Payoff at about 80%. Fix line 2 (rule overlap). Order is backtest, then paper (on screen only), then live: fine. |
| 3 Facts | Clean, apart from the line 9 drawdown check. |
| 4 Product truth | Clean. "Hooked up to Qube", "breaks your strategy into four rules", "runs them through five years of real prices", free to start, no card: all in `product-truth-qube`. |
| 5 Compliance | Clean. "Say I'd put in $10,000" first, loss spoken, label on every result, nothing says go live. A5 needs the "Example" tag. |
| 6 Spoken lines | Lines 1, 2, 6, 10, 11 and hook A (see table). |
| 7 Hooks | A and B make sense cold. C ("607 trades…") is weaker cold but saved by the counter on screen. All have a number or stake. None is repeated word for word by line 1. |
| 8 On-screen | Strong. Every line has a cue, numbers exact on screen, labels kept on. Fixes: the close-up on line 6, the line 10 row, "from a high". |
| 9 CTA | Exact wording, last line, Qube slipped in at about 5s. The Breakdown DM still isn't live (Mark). |
| 10 Fix log | "Trading idea" not used. No Qube in the hook. Three documents. No blanks. Keyword exact. Two vague-noun repeats (lines 1 and 10), both fixed above. |

Facts checked:
- 10 stocks (AAPL, MSFT, NVDA, AMZN, GOOGL, META, TSLA, AVGO, JPM, BRK.B), buy at the close on a 3%+ drop, $2,000 each, +3% / −5%, no fees, Jan 2021 – Dec 2025, $10,000: `claims-and-proof` → TQX's own backtests → "10 biggest US stocks"
- $18,147 / +$8,147 ("about $8,100"), 607 trades, worst drop −$3,207 ("about $3,200"): same row. Whether −$3,207 is measured from a high has to be confirmed in A3.
- Hindsight caveat: same row ("Say it has some hindsight in it") and `trading-fundamentals`
- "Free to start, no card", tqx.ai/igqube2, Claude hooked up to Qube, every trade shown: `product-truth-qube`
- All numbers come from our own test, not a Qube run yet. A3's CHECK step is the gate (`claims-and-proof` "Proof on screen").

Mark's own lines flagged, not changed: none. Every line in `data/script-room/J020.json` still matches the writer's original; the live Script Room `edits/J020` doc wasn't read here, so check it before the rewrite.

Only Mark can decide (not counted against the writer):
1. Hook A opens "Claude can now…", like J022's hook A. If they post close together, use hook B or C here.
2. CTA offer. To get the original's "all 11 skills" pull, the DM would need to send something from this video (for example, the exact prompt Joshua types in A1). Then the CTA could be "Comment QUBE and I'll send you the free link, this exact strategy, and a step-by-step on building your first one." The flow doesn't send that today, so the line stays as it is unless Mark adds it.
3. The Breakdown DM still isn't live in ManyChat. The CTA promises it.
4. Paper trading isn't spoken. It's shown on screen (`BACKTEST ✓ → PAPER → LIVE`, "Go live" locked). OK as is, or add "then on paper" (+3 words)?
5. Same rule and numbers as J018. Which one goes first?
6. A real Qube run (A2, A3) before filming. If any number differs, stop.
