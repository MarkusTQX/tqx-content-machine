# M23 · Beat map (Pass 0)

**Original (the engine):** @raycfu · "AI agent trading firm" · https://www.instagram.com/p/DcuOeJ4vmde/ · 40.4s · 192 words (4.8 words a second) · 2,346 likes, 3,867 comments, 268K followers
**Transcript:** `knowledge/reference/DcuOeJ4vmde/transcript.srt` · **Card:** `knowledge/cards/reference/2026-08-31_raycfu_ai-agent-trading-firm.md`
**Presenter:** Mark (fast, no pauses, about 3 words a second) · **Persona:** Priya, who already uses Claude at work and is scared of wasting money on a toy
**Method:** `remix-for-product` "The method" (Mark, Oct 23). The raycfu transcript is the draft. The hook is Mark's own, word for word. Qube goes in where raycfu's org chart starts, with Mark's line. Only what isn't true for Mark's firm is swapped.
**Whisper slips in the transcript** (from the card's name check): "stock ticket" = ticker, "prize action" = price action, "my ways" = more ways. Quoted below as he says them.

## Line by line

| Time (orig.) | Original line (exact) | Our line | kept / small swap / rewritten (why) | Our time |
|---|---|---|---|---|
| 0.0–2.9 | "Most people don't realize that someone just built an entire Wall Street trading firm with AI agents." | Hook: "I built a quant trading firm on Claude. 6 agents, each one has a job." | **rewritten (why):** Mark's own hook, word for word (brief). Same job: a big claim made small ("a trading firm" / "on Claude"), plus a count that opens the loop. First person, so it's true: Mark built it. No "Wall Street". | 0.0–5.0 |
| 2.9–6.9 | "You give the system a single stock ticker and the entire AI trading floor goes to work." | 1. "I give Claude one stock ticker, and the entire firm goes to work." | **small swap.** "give ___ a single stock ticker, and the entire ___ goes to work" kept. "You" → "I" (Mark's own firm), "the system" → "Claude" (the hook's name), "AI trading floor" → "firm" (the hook's word, and the brief's don't-copy list). It's what he actually types, not "an idea". | 5.0–9.3 |
| 6.9–7.8 | "Here's how you build it out." | 2. "Here's how I built it out. I start by connecting Qube to Claude." | **small swap + Qube in.** "you build" → "I built". Then Mark's line word for word (fix-log Oct 23), right where raycfu's org chart starts, inside the first 14s. | 9.3–13.7 |
| 7.8–12.5 | "Four specialized analyst agents dig into the data, analyze company fundamentals, breaking market news, track social sentiment, and prize action." | 3. "The research agent reads the news and earnings on that stock." · 4. "The data agent grabs up to five years of its price data." | **small swap.** Same layer, the agents that dig into the data. Four analysts → Mark's two: research (news + earnings, his "fundamentals" and "breaking market news") and data (his "price action", in Mark's own words, "up to five years of real price data", `product-truth-qube`). "That stock" and "its" point back to the ticker in line 1. Social sentiment cut: not in Mark's firm. Split in two so each agent gets its own line and UI card. | 13.7–21.3 |
| 12.5–17.9 | "A bull and bear agent debate both sides of the trade against each other in order to challenge the hidden risk." | 5. "The strategy agent builds a trading strategy in Qube." · 6. "The backtest agent tests it on those prices and shows every trade." | **rewritten (why):** there's no debate agent in Mark's firm (brief). Build and test take this slot, both in Qube ("build", "test", "every single trade", `product-truth-qube`). "A trading strategy", never "trading idea" (fix-log Oct 23). The strategy's sections (when to buy, when to sell, how much, when to get out) are shown on screen one by one instead of spoken, to stay in the word range. "Those prices" = the data agent's five years. | 21.3–28.3 |
| 17.9–25.7 | "Then a trader agent plans the execution, but a separate risk management agent has the power to veto the move before the portfolio management agent signs it off." | 7. "Then the trader agent is ready to trade it, but a separate risk manager has the power to say no." · 8. "It says no to any trade risking more than 2% of the account." · 9. "The second we hit our max loss, trading stops for the day." · 10. "And if the backtest doesn't hold up, it's a no." | **small swap.** "___ trader agent ___, but a separate risk ___ has the power to ___" kept, "but" and all: it's the twist. "Plans the execution" → "is ready to trade it" (it = the strategy). "Veto the move" → "say no" (brief). Portfolio manager cut (not in Mark's firm). Then the risk manager's exact no-rules (brief, Mark's settings, taken as given): 2% per trade, the daily max loss (approved wording, `terminology`, said without an unclear "it"), and the backtest check. That last one sets up line 12. | 28.3–46.7 |
| 25.7–26.8 | "The best part is the system has persistent memory." | 11. "The best part is what happens when the risk manager says no." | **small swap.** "The best part is ___" kept, at 68% (re-hook, `script-logic` #11). Raises the stakes without naming what's next (Mark's J020 lesson, `retention-writing` #3). | 46.7–50.7 |
| 26.8–32.0 | "Every trader recommendation gets graded and logged against actual market results so the agents study their own mistakes and improve over time." | 12. "The strategy agent fixes what's broken, and the backtest agent tests it again, until it's a yes." · 13. "That's when the trader agent runs it on a simulation account first, then live through a real broker." | **rewritten (why):** "graded and logged… improve over time" isn't ours (no "gets better over time", brief's don't-copy list). The true version is Qube's Improve step (fix what's broken, test it again) as a loop that ends on the risk manager's yes, Mark's own "find what's broken, fix it, and test it again" (fix-log Oct 15). "It's a yes" answers line 10's "it's a no". Then the payoff: the trader agent from line 7 finally trades, in the real order, backtest → simulation account → live (`script-logic` #5). "Simulation account" (Mark's J022 edit), "live through a real broker" (`product-truth-qube`). | 50.7–62.3 |
| 32.0–36.2 | "I put together a complete setup guide on how to build this out for yourself with the GitHub repo link." | 14. "I built this whole firm without writing any code. You can too." | **rewritten (why):** we don't send guides (Mark, Oct 23). Same "I…build this out" beat, turned into TQX's difference, no code (`positioning`), which is what makes the free sign-up worth a comment. "This whole firm" echoes the hook. | 62.3–65.3 |
| 36.2–39.3 | "If you want it, just like the video and comment firm and I'll send it to you." | 15. "Comment QUBE and I'll send you the link for the free sign-up." | **small swap.** "Comment ___ and I'll send ___ to you" kept. FIRM → QUBE, standard CTA word for word (Mark, Oct 23). No "like the video". | 65.3–69.3 |
| 39.3–40.4 | "Follow for my ways to make money and run your business with tech and AI." | (cut) | **cut.** No follow line, no money framing (`cta-and-offer`, `finance-compliance`). | |

## Tally

16 spoken units (hook + 15 lines): **10 small swaps** (1, 2, 3, 4, 7, 8, 9, 10, 11, 15) · **6 rewritten** (hook: Mark's own; 5, 6: no debate agent; 12, 13: no memory claim; 14: no guide). The original's last line is cut.

## The six agents, in the order they're named

| # | Agent | Line | On screen (box lights up) |
|---|---|---|---|
| 1 | Research agent | 3 | "RESEARCH" |
| 2 | Data agent | 4 | "DATA" |
| 3 | Strategy agent | 5 | "STRATEGY" |
| 4 | Backtest agent | 6 | "BACKTEST" |
| 5 | Trader agent | 7 | "TRADER" |
| 6 | Risk manager | 7 | "RISK MANAGER" (red, the one that can say no) |

All six are named by 35s, so the hook's count is paid off before the twist.

## Promise and payoff

- **Promise (hook):** Mark built a quant trading firm on Claude, and you'll see all 6 agents and the one job each one has.
- **Payoff:** lines 3–7 (the six jobs), lines 8–10 (the risk manager's exact no-rules), lines 12–13 (the loop that ends in a yes, then simulation account → live), line 14 (no code).
- **Re-hooks:** line 2 punch-in (13%), the "but" in line 7 (45%), "The best part is…" in line 11 (68%).

## Length

211 words (hook 15 + lines 196). The original: 192 words. Range 173–211 (±10%, `script-logic` #10). About 70s at Mark's 3 words a second. The original runs 40s because raycfu reads at 4.8 words a second; we match the words, not the seconds (brief).

## Numbers used

Spoken: "2%" (Mark's own per-trade limit, his setting, taken as given) and "up to five years" (`product-truth-qube`). No returns, win rates or trade counts anywhere. On screen: "Backtest, not live results" on every backtest frame; "Paper trading · simulated results" badge top-right on every simulation-account frame.
