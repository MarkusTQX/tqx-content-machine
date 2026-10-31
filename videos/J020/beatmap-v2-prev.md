# J020 · Beat map (Pass 0)

**Original:** @buildwithai.club · "Claude tests your trade 10,000 times" · https://www.instagram.com/p/DezOgThKETj/ · 44.1s · 164 words (about 3.7 words a second) · 4,384 likes, 6,947 comments, 33K followers
**Transcript:** `knowledge/reference/DezOgThKETj/transcript.srt` · **Card:** `knowledge/cards/reference/2026-10-22_buildwithai.club_claude-tests-your-trade-10000-times.md`
**Presenter:** Joshua (3.2 words a second) · **Persona:** Daniel, the burned retail trader ("I know what I should do. I just don't do it once the trade is open.")
**Method:** `remix-for-product` "The method" (Mark, Oct 23). Their script is the draft. Qube goes in where they show their tool. Only what's untrue for us is swapped: Qube isn't open source, has no "11 skills" and no "10,000 replays of the day" feature, so those become what Qube really does (Claude hooked up to Qube, Qube writes the rules, backtests them on five years of past prices, shows every trade). The only numbers used are the "10 biggest US stocks" row in `claims-and-proof`.
**Hard cuts in the original:** 4.76s (full screen, the reveal), 10.16s (back to split, tab bar), 24.44s (full screen, counter from 0), 33.92s (back to split), 37.44s (face close-up), 39.72s (split, CTA), 42s (follow card).

## The engine we keep

1. Tool named in the first word, money at stake: "Claude can now test… before you risk a single dollar." Promise shown on screen by 2s, buy button locked.
2. Reveal at about 5s: what makes it possible ("each one handles a different job").
3. The smaller parts, one every 3 to 5s, with a progress bar across the top and the best part greyed out at the far right.
4. "But the craziest one…" re-hook at about 50%, then a full-screen cut where a number counts up from 0.
5. "So you get to see… before putting your money on the line."
6. The honesty line in a sudden face close-up.
7. The comment keyword, last.

## Line by line

| Time (orig.) | Original line (exact) | Our line | kept / small swap / rewritten (why) |
|---|---|---|---|
| 0.0–4.1 | "Claude can now test your stock trade 10,000 times before you risk a single dollar." | Hook A: "Claude can now test your stock trades on five years of prices before you risk a single dollar." | **Small swap.** "10,000 times" → "on five years of prices": Qube has no 10,000-replay feature; it backtests on past prices (Jan 2021 – Dec 2025, `claims-and-proof`). "trade" → "trades": Qube tests a strategy that makes many trades, not one trade. Claude stays first (`hook-writing` #7); no Qube in the hook (`fix-log` Oct 23). |
| 4.8–9.5 | "Someone just open sourced 11 free day trading skills for Claude and each one handles a different job." | 1. "Claude's hooked up to Qube, which turns what you type into rules. Each one handles a different job." | **Rewritten** (first half only). Qube isn't open source and has no 11 skills (`product-truth-qube`). What's true: Claude connects to Qube, and Qube turns what you type into rules. Their ending, "each one handles a different job", is kept word for word. "Free" moves on screen ("free to start, no card"). |
| 10.0–13.0 | "One skill scans thousands of stock charts looking for trading opportunities." | 2. "One rule scans the 10 biggest US stocks looking for trading opportunities." | **Small swap.** "skill" → "rule"; "thousands of stock charts" → "the 10 biggest US stocks" (the stocks in our test). Rest kept. |
| 13.5–15.8 | "Another tracks breaking news that could move those stocks." | 3. "Another puts no more than $2,000 into any of those stocks." | **Small swap.** Qube has no news feature. Swapped for Qube's real "how much" rule ($2,000 per stock, `claims-and-proof`). "Another… those stocks" kept. |
| 16.2–21.7 | "Then there's an entry skill that watches for the right signal and an exit skill that plans when to take profit or cut your losses." | 4. "Then there's an entry rule that buys the day one of them drops 3%." · 5. "And there's an exit rule that takes profit at 3% or cuts your losses at 5%." | **Small swap.** "skill" → "rule"; "watches for the right signal" → the real signal (a 3% drop); "plans when to take profit or cut your losses" → the real levels (+3%, −5%). Split into two full sentences so each is one breath and ends (`spoken-sentence-rules` #1, #9). "take profit" and "cut your losses" kept. "Profit" and "losses" carry the reference point (from where it bought). |
| 22.1–24.2 | "But the craziest one is called the time machine." | 6. "But the craziest part is called a backtest." | **Small swap.** "the time machine" → "a backtest" (what Qube really does). "one" → "part": a backtest isn't one of the rules, so "one" would point at the wrong thing (`script-logic` #6). "But the craziest… is called" kept. |
| 24.2–29.3 | "It takes your trade and simulates the rest of the trading day 10,000 times using historical price data." | 7. "It takes your rules, runs them through five years of past prices, and shows every trade." | **Small swap.** Their feature swapped for Qube's: backtest on past prices, every trade shown (`product-truth-qube`). "It takes your…" kept. This line is also the one-clause explanation of "backtest" for Daniel. |
| 29.6–33.7 | "Then it shows how often you would have made money, hit your stop loss or ended somewhere in between." | 8. "Say I'd put in $10,000. 607 trades later, it was up about $8,100." · 9. "At its worst point, it was down about $3,200." | **Rewritten.** Their 29.4% / 25.5% split isn't ours, and our target-vs-stop split isn't sourced yet (brief, "Needs sourcing"). Same job (what the test shows), with our real result: $18,147, 607 trades, worst drop −$3,207 (`claims-and-proof`). "Say I'd put in $10,000" first (`finance-compliance`); the loss shown as openly as the gain. "At one point / at its worst" wording as in the approved J018. |
| 34.0–37.0 | "So you get to see the historical odds before putting your money on the line." | 10. "So you get to see all that before putting your money on the line." | **Small swap.** "the historical odds" → "all that": "odds" reads as a promise about the future (card, "What we can't copy"). Rest kept word for word. |
| 37.4–39.3 | "Of course, it's a simulation, not a guarantee." | 11. "Of course, it's a backtest, not live results. And it's got hindsight in it, since we know these stocks won." | **Small swap** + one required sentence. "a simulation, not a guarantee" → "a backtest, not live results" ("guarantee" is banned even negated, `finance-compliance`). The hindsight sentence is required with this test (`claims-and-proof`, `trading-fundamentals`). "Of course, it's a…" kept. |
| 39.7–43.8 | "To get all 11 skills and the full setup guide, follow Build with AI and comment trade." | 12. "Comment QUBE and I'll send you the free link and a step-by-step on building your first strategy." | **Rewritten.** Our fixed keyword CTA, exact wording (`cta-and-offer`). |

**Tally (11 original lines):** kept word for word 0 · small swap 8 · rewritten 3 (line 2 of theirs, the result line, the CTA). No original line is kept fully word for word because every one of them names their tool's features, their numbers, or a banned word. Inside the swaps, their phrasing is kept: "Claude can now test your stock trade(s)… before you risk a single dollar", "each one handles a different job", "One… scans… looking for trading opportunities", "Another… those stocks", "Then there's an entry… and an exit… take profit or cut your losses", "But the craziest… is called", "It takes your…", "So you get to see… before putting your money on the line", "Of course, it's a…".

## What changed, and why

| Original beat | Ours | Why |
|---|---|---|
| "10,000 times" in the hook | "on five years of prices" | The true number for our test. "607 trades" is the payoff, saved for the count-up, same as their "10,000" counter |
| "Someone just open sourced 11 free… skills" | "Claude's hooked up to Qube" | Qube isn't open source; the Claude connection is the real "can now" |
| Scanner, News, Entry, Exit, Time Machine | Stocks, Size, Buy, Sell, Backtest | Their tab bar becomes the four rule pieces every strategy needs (`product-truth-qube` approved rules line) plus the test. The best one is still last and greyed out until the re-hook |
| 10,000 replays of the rest of the day, 29.4% / 25.5% | Five years of past prices, 607 trades, about +$8,100, worst point about −$3,200 | Our own real backtest (`claims-and-proof`). Losses shown |
| "a simulation, not a guarantee" | "a backtest, not live results" + hindsight | Banned word; required caveat |
| "comment trade" for 11 skills + setup guide | "Comment QUBE…" | Our live flow (`cta-and-offer`) |

**Not said out loud, on purpose:** paper trading. The original has no "next step" line, so we don't add one; the edit shows the "Go live" button locked the whole way, and the step bar ends "Backtest → Paper → Live". Nothing in the script tells anyone to go live (`finance-compliance`). If REDPEN or Mark wants it spoken, the cheapest place is line 10: "So you get to see all that, then try it on paper, before putting your money on the line." (+5 words).

**Length:** 186 spoken words with hook A, about 58s at Joshua's 3.2 words a second. The original is 164 words in 44s, said fast (3.7 a second). Our extra 22 words are the required lines: the result with its $10,000 setup and worst point, the hindsight sentence, and the fixed CTA (19 words against their 17). Inside `script-logic` #10's 60s, over the brief's 44–48s. If the take runs long, cut line 10 first (−13 words, about 4s). Beat timing tracks the original: re-hook at 47% (theirs 50%), result 52–73% (theirs 55–77%), honesty line at 80% (theirs 85%).
