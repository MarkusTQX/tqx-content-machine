# J022 · Beat map (Pass 0)

**Original:** @samin_yasar12 · "Claude copies Wall Street insiders' trades" · https://www.instagram.com/p/DdzGPvzIN4C/ · 43.9s · about 150 words (3.6 words a second) · 6,418 likes, 4,222 comments, 9,968 followers
**Transcript:** `knowledge/reference/DdzGPvzIN4C/transcript.srt` · **Card:** `knowledge/cards/reference/2026-09-27_samin_yasar12_claude-copies-insider-trades.md`
**Presenter:** Joshua (3.2 words a second) · **Persona:** Priya, who already types into Claude at work and is scared of wasting money on a toy
**Method:** `remix-for-product` "The method" (Mark, Oct 23). The original transcript is the draft. Qube goes where it connects its tools. Only what's untrue for us is swapped.
**Hard cuts in the original:** 0.8, 2.1, 3.3, 4.8, 5.7, 6.9, 8.5, 9.0, 9.4, 9.8, 10.9, 12.2, 13.0, 18.1, 19.4, 20.6, 23.5, 25.1, 27.4, 28.5, 30.0, 31.0, 32.5, 35.4, 37.8, 38.6, 40.4, 41.1, 43.1 (29 cuts, about one every 1.5s).

## Line by line

| Time (orig.) | Original line (exact) | Our line | kept / small swap / rewritten (why) | Our time |
|---|---|---|---|---|
| 0.0–2.5 | "Claude can now automatically copy the trades of Wall Street insiders," | Hook A: "Claude can now automatically build you a trading strategy and test it on ten years of past prices." | **small swap.** "Claude can now automatically…" kept. The power swapped: Claude + Qube doesn't copy insiders. It builds the strategy (Qube writes the rules) and backtests it. "Ten years" = the SPY test, 2015–2024 (`claims-and-proof`). "Build you a trading strategy" is Mark's own fix (`spoken-sentence-rules` #3). | 0.0–5.6 |
| 2.5–5.7 | "and you can set this entire thing up inside Claude." | 1. "And you can set this entire thing up inside Claude." | **kept.** Moved to its own line so hooks B and C can sit in front of it. | 5.6–8.8 |
| 5.7–6.9 | "First, connect LiquidTrade," | 2. "First, connect Qube, which turns what you tell Claude into exact rules." | **small swap.** "First, connect ___, which…" kept. LiquidTrade → Qube. Their tool's job (trading markets) → Qube's real job: you describe it in plain English, Qube writes the rules (`product-truth-qube` Build step and its approved "exact rules" line). | 8.8–12.5 |
| 6.9–12.2 | "which lets Claude interact with stocks, crypto, forex, and even prediction markets." | 3. "When to buy, when to sell, how much, and even when to get out." | **small swap.** Same four-item list with "and even" on the last one. Their four markets → the four parts of the rules (`product-truth-qube` approved line). Answers "what rules?" (`fix-log` Oct 15). The exact rule being typed is on screen (S&P 500 dip rule), so it isn't spoken. | 12.5–16.6 |
| 12.2–13.0 | "Then connect it to QuiverQuant." | 4. "Then Qube tests those rules on ten years of past prices, and shows you every trade they would've made." | **rewritten (why):** there is no second tool for us to connect, and saying one would be untrue. The #2 step stays, and keeps "Then…": the data their #2 brings is the ten years of prices Qube already has. | 16.6–22.5 |
| 13.0–18.1 | "This gives Claude access to data showing what insiders and politicians and even major investors are actually buying and selling." | (merged into 4: "…and shows you every trade they would've made.") | **small swap**, merged into line 4 to save 4 seconds. "Data showing what they're actually buying and selling" → every trade the rules would've made (`product-truth-qube` Test step: "every single trade"). Insiders and politicians are cut: untrue for us and on the brief's don't-copy list. | (in 4) |
| 18.1–19.4 | "Now here's where it gets crazy." | 5. "Now here's where it gets crazy." | **kept.** Same tight close-up. Mark's order (Oct 23) is to keep it. The brief's don't-copy list named this line; Mark's later instruction wins. | 22.5–24.4 |
| 19.4–27.4 | "You can create a routine that has Claude automatically check those trades throughout the day, compare them against your portfolio, and find any new positions worth looking at." | 6. "You can have Claude automatically find what's broken in your strategy and fix it. Round after round, until you're happy with the result." | **rewritten (why):** checking insider trades isn't something we do. Kept "You can… have Claude automatically…". The power swapped to Qube's Improve step: the AI suggests changes and tests them over rounds. Wording is the approved line in `product-truth-qube` and Mark's ending fix (`fix-log` Oct 15). | 24.4–31.6 |
| 27.4–31.0 | "When it finds one, Claude can send you the trade, explain what happened, and ask for your approval." | 7. "When you like the results, paper trade your strategy first, with fake money." | **rewritten (why):** `finance-compliance` doesn't let us go from the backtest straight to "approve it, it goes live". Paper trading has to come first, said out loud. Claude sending an approval card isn't a documented Qube feature, so we don't claim it. Kept the "When ___," opener and the human step. | 31.6–35.6 |
| 31.0–35.4 | "Approve it, and Claude can execute the trade through LiquidTrade for you." | 8. "Then approve it, and Qube can run it live through a real broker for you." | **small swap.** "Approve it, and ___ can ___ through ___ for you." kept. LiquidTrade → a real broker (`product-truth-qube` Go live, Mark Oct 22). Which brokers is unknown, so we don't name one or say "your broker". | 35.6–40.3 |
| 35.4–40.4 | "So you're basically turned Claude into a trading agent that can research, monitor, and execute from one place." | 9. "So you've basically turned Claude into a trading agent that can build, test and run your strategy from one place." | **small swap.** Grammar slip fixed ("you've"). Research, monitor, execute → build, test, run: Qube's real steps. "Trading agent" kept: it's the only name for the thing in this script (`terminology` rule 1). | 40.3–46.6 |
| 40.4–43.9 | "Comment signal, and I'll send you my full video showing you exactly how to build it." | 10. "Comment QUBE and I'll send you the free link and a step-by-step on building your first strategy." | **small swap.** "Comment ___ and I'll send you ___ on how to build it" kept. SIGNAL → QUBE, and the exact words from `cta-and-offer`. Still over a preview of what they get. | 46.6–52.0 |

## Tally

11 spoken units (hook A + 10 lines): **2 kept** (1, 5) · **6 small swaps** (hook A, 2, 3, 8, 9, 10) · **3 rewritten** (4, 6, 7). Original line 5 is merged into line 4.

## Numbers used (SPY dip-rule row, `claims-and-proof`, on screen only)

Nothing extra is spoken except "ten years", which is the test's span. On screen at line 4: "$10,000 → $14,428 · 62 trades · 2015–2024", worst drop "−$2,606" in red, "Just holding SPY: $28,634 · price only, no dividends", and "Backtest, not live results". The improve step gets no number (none exists).

## Length

167 spoken words with hook A (hook 18 + body 149, checker count), about 52s at 3.2 words a second. The original is 44s at 3.6. Same beats, slower presenter, plus the paper-trading step that has to be said out loud. About 2s over the brief's 45–50s; inside `script-logic`'s 35–60s.

**Re-hook timing:** "Now here's where it gets crazy" lands at about 43%, where the original has it (41%), not at `script-logic`'s 60–75%. Kept to match the original's beats.
