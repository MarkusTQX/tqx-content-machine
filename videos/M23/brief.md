# M23 · I built a quant trading firm on Claude
Presenter: Mark (use the Mark section of `tqx-voice`: fast, no pauses, short flips, ~3 words a second) · Persona: Priya, the AI-curious tinkerer · Why they care: she already uses Claude at work and wants to "see what happens if I let an AI run it". This shows her the six jobs a trading firm needs, set up inside the Claude she already has, with one agent whose whole job is to say no before any money moves, which answers her fear of wasting money on a toy.
Source: Mark's idea, from scratch: "I built a quant trading firm on Claude. 6 agents, each one has a job." There's no single original, so the format to follow line by line is the closest outside gold below.
Original Reel link: https://www.instagram.com/p/DcuOeJ4vmde/ (@raycfu, the engine; not a copy of a topic)

The original's engine to keep (@raycfu "AI agent trading firm", `knowledge/cards/reference/2026-08-31_raycfu_ai-agent-trading-firm.md`, transcript `knowledge/reference/DcuOeJ4vmde/transcript.srt`): big claim ("someone just built an entire Wall Street trading firm with AI agents") → one small input, and "the entire AI trading floor goes to work" → "Here's how you build it out." → the org chart, role by role, one line and one UI card per agent → the twist inside the chain: "but a separate risk management agent has the power to veto the move" → "The best part is…" bonus at about 65% → the offer → keyword CTA. 11 sentences, 192 words, 40s at 4.8 words a second. Big moments: the input line at 3s (small effort, big machine), the veto at 20s (makes the system feel careful, not reckless), "the best part" at 26s, CTA over a close-up. Punch-ins wide/close at every new beat; the UI insert changes about every 2s. Comments (3,867) beat likes (2,346): the keyword did the work.

Outside gold to aim at: @raycfu "AI agent trading firm" is the line-by-line format (not in the `gold-standard-scripts` table; the table has his loop Reel, #7). Moves to borrow, not formats to follow:
- @max_kelleyy "DO NOT build an AI trading bot" (gold #3): one sentence per part, and the shot switches to that part's real screen on the same word; the cautious "start on paper" line right before the CTA (ours: the trader runs it on a simulation account first). Real screen, low-polish look.
- @ai.honeycove "Vibe Trading": the quick one-breath roster ("One researches, one builds, one runs the backtest, another reviews the risk") if the Scriptwriter needs to compress two agents into one line; key phrase highlighted yellow on every screenshot; end line that echoes the hook.

Shape: 1. Steps / how-to, "new power" variant (numbered parts, one job each, real screen each, "the best part", keyword), which is the raycfu shape kept as is (`remix-for-product`) · Target length: **192 words, range 173–211** (the engine's word count ±10%, `script-logic` #10). At Mark's ~3 words a second that's about 60–70s. Runs longer than the original's 40s only because Mark reads slower; match the words, not the seconds, and cut filler, never the payoff.

Enemy → difference: Wall Street gatekeeping (firms have analysts, quants, risk desks and traders; retail has an app and a chart) → Pro quant tools, no code ("This used to take a team of people at a hedge fund. Now you can do it without writing code." `positioning`).

Product: Qube, with Claude. Claude connected to Qube does the building, the testing and the live trading (`product-truth-qube`: "Claude can build it, test it and trade it for you" is true). · Placement: right after "Here's how I built it out.", where raycfu's org chart starts: Mark's line, word for word, **"I start by connecting Qube to Claude."** (within the first 8s). Then Qube is on screen for every agent that works in it (strategy, backtest, trader). Qube is not in the hook (`hook-writing` #8: nobody knows Qube yet; Claude is the known name). The keyword CTA is the last spoken line.

The promise (what the hook promises): Mark built a quant trading firm on Claude, and you'll see all six agents and the one job each one has.
The payoff (what they walk away with, usable today): the full org chart, six jobs in order (research → data → strategy → backtest → risk → trader), the risk manager's exact "no" rules, the order every strategy goes through (backtest → simulation account → live), and the free tool to build the same firm without code.

CTA: "Comment QUBE and I'll send you the link for the free sign-up." (standard CTA, `cta-and-offer`, Mark Oct 23). No guide, no repo, no "like the video", no "follow".

## The hook (one hook, Mark's own words)

**"I built a quant trading firm on Claude. 6 agents, each one has a job."**

Keep it word for word (Mark's words; `hook-writing` #7 spirit: one hook, no A/B/C). It already does what raycfu's line does: a big claim ("a quant trading firm") made small ("on Claude"), a count that opens the loop ("6 agents"), and a promise of the org chart ("each one has a job"). 14 words, under 5s. First person replaces raycfu's "someone just built", which is also what makes it honest (Mark built it). On screen frame 1: title "I built a quant trading firm on Claude", "trading firm" in yellow, plus an empty org chart of 6 grey boxes in the top third (they light up one by one as each agent is named).

## The 6 agents (one job each)

| # | Agent | Its one job | Where it works | On screen |
|---|---|---|---|---|
| 1 | Research agent | Reads the market news and earnings every morning and flags which stocks are moving, and why | Claude | Claude output: a short "moving today" list with one-line reasons (our own run; tickers only as a labelled example, no "buy" language) |
| 2 | Data agent | Pulls up to five years of real price data on those stocks | Claude → Qube | Price history loading for the flagged stocks |
| 3 | Strategy agent | Builds the strategy in Qube from plain English: when to buy, when to sell, how much, and even when to get out if it all goes wrong | Qube | The Qube strategy, its sections highlighted one by one |
| 4 | Backtest agent | Tests the strategy in Qube on up to five years of real price data and shows every single trade, the wins and the losses | Qube | Qube backtest with the trade list; "Backtest, not live results" label |
| 5 | Risk manager (the twist: it can say no) | Has the power to say no before anything trades. No trade risks more than 2% of the account. It stops trading for the day the second it hits the max loss. If the backtest doesn't hold up, the answer is no. | Claude + Qube | Red "Risk manager · NO" card with the exact reason, then a green "Approved" card (the honest version of raycfu's "Vetoed → Approved") |
| 6 | Trader agent | Only after a yes: runs it on a simulation account first, then, once it holds up, live through a real broker, right from Claude through the Qube connection | Qube | Simulation account screen with the "Paper trading · simulated results" badge top-right; a "Live" step greyed until it holds up |

Order follows reality (`script-logic` #5, `trading-fundamentals`): build → backtest → risk check → simulation account → live. The 2% and the daily max loss are Mark's own settings for his firm, said as his rules, not as results (take as given; he can change the number).

## Beat map, line by line against the original (Scriptwriter owns the final words)

Each of our lines does the same job as the raycfu line next to it. Mark each one "kept / small swap / rewritten (why)" in the beat map. Every sentence sells the next one (`script-logic` #3b).

| # | raycfu line (job) | Ours (direction) | Mark |
|---|---|---|---|
| 1 | "Most people don't realize that someone just built an entire Wall Street trading firm with AI agents." (hook: big claim) | **Hook, Mark's words:** "I built a quant trading firm on Claude. 6 agents, each one has a job." | rewritten: Mark's own hook |
| 2 | "You give the system a single stock ticker and the entire AI trading floor goes to work." (one small input, big machine) | Mark says one plain sentence to Claude and the whole firm goes to work. Say what he types, as a quote, not "an idea" (Mark hates "trading idea"). Example direction: "I tell Claude what I want to trade, and the entire firm goes to work." | small swap |
| 3 | "Here's how you build it out." (re-hook, punch-in) | "Here's how I built it out. I start by connecting Qube to Claude." (Qube placement; Mark's line word for word) | small swap + Qube in |
| 4 | "Four specialized analyst agents dig into the data… fundamentals, breaking market news, track social sentiment, and price action." (role 1, the research layer) | Agents 1 and 2: the research agent reads the news and earnings and flags what's moving; the data agent pulls up to five years of real price data on them | small swap |
| 5 | "A bull and bear agent debate both sides of the trade… to challenge the hidden risk." (role 2) | Agents 3 and 4: the strategy agent builds it in Qube (when to buy, when to sell, how much, and even when to get out if it all goes wrong); the backtest agent tests it on up to five years of real price data and shows every single trade | rewritten: no debate agent in Mark's firm; build and test take this slot |
| 6 | "Then a trader agent plans the execution, but a separate risk management agent has the power to veto the move before the portfolio management agent signs it off." (the twist: the one that can say no) | Keep the "but": the trader agent is ready to run it, **but a separate risk manager has the power to say no.** Then its exact no-rules (2% per trade, stops for the day at the max loss, no if the backtest doesn't hold up). Only after a yes does the trader run it on a simulation account first, then live through a real broker, right from Claude | small swap (portfolio manager → trader; "veto" → "say no") |
| 7 | "The best part is the system has persistent memory." (re-hook / bonus, about 65%) | "The best part is what happens when it says no." Don't name what comes next (Mark's J020 lesson, `retention-writing` #3) | small swap |
| 8 | "Every trader recommendation gets graded and logged… so the agents study their own mistakes and improve over time." (bonus payoff) | The true version (Qube's Improve step): the strategy agent finds what's broken and fixes it, the backtest agent tests it again, over and over until the risk manager says yes. No claim that results get better | rewritten: their memory/improvement claim isn't ours |
| 9 | "I put together a complete setup guide… with the GitHub repo link." (the offer) | The landing line, TQX's difference: this used to take a whole team of people at a hedge fund, and Mark built it without writing a single line of code | rewritten: we don't send guides (Mark, Oct 23) |
| 10 | "If you want it, just like the video and comment firm and I'll send it to you." (CTA) | "Comment QUBE and I'll send you the link for the free sign-up." (Mark's qualifier is fine in front if words allow: "If you want to build your own…") | standard CTA |
| 11 | "Follow for more ways to make money and run your business with tech and AI." | Cut. No follow line, no money framing | cut |

Rhythm: one agent every 5–7s (raycfu's is 2–5s; Mark is slower). Re-hooks: line 3 punch-in, the "but" in line 6 at about 55–60%, "the best part" at about 70–75%. Full payoff (the loop that ends in a yes, then the no-code landing) at about 80–90%. End within seconds of it.

Where the words go if the draft runs long (target 173–211): compress agents 1+2 into one honeycove-style breath ("One reads the news, one pulls the prices…"), keep the risk manager's line whole (it's the twist), never cut the CTA or Mark's two lines.

## Facts we can use (each from a skill; no outside numbers in this video)

- Qube: build a strategy from plain English, backtest on historical data, every single trade shown; AI suggests changes and tests them over rounds; runs live through a real broker. Free to start, no card. (`product-truth-qube`)
- "I start by connecting Qube to Claude." is how the connection is said (Mark, Oct 23). Never "hooked up" or "plugged in". (`product-truth-qube`, fix-log)
- What Qube builds is a "strategy"; its parts are "sections", never "rules" (one named rule inside it is fine). (`terminology` #6, fix-log)
- "Allows you to build a trading strategy from natural language" / "When to buy, when to sell, how much, and even when to get out if it all goes wrong." (Mark's J022 lines; `product-truth-qube`)
- Price history: "up to five years of real price data" or "years of prices", never a fixed ten. (`product-truth-qube`, Mark's J020/J022 edits)
- Claude can start live trading through the Qube connection, so "Claude can build it, test it and trade it" is true. (`product-truth-qube`, Mark Oct 23)
- Try it first on "a simulation account" (Mark's J022 edit, used here as he wrote it; P1 in `data/mark-edits/proposals.md` is still open, so use one term the whole video, never switch to "fake money" or "paper trading" in the spoken lines).
- "It stops trading for the day the second it hits the max loss." (approved wording, `terminology`)
- "This used to take a team of people at a hedge fund. Now you can do it without writing code." (`positioning`)
- The 2% per-trade limit and the daily max loss: Mark's own risk settings, given as his rules. Not a result, so no source row needed. No returns, win rates or trade counts are claimed anywhere in this video, so `claims-and-proof` has nothing to add.
- On screen: "Backtest, not live results" on every backtest frame; "Paper trading · simulated results" badge top-right on every simulation-account frame; no API keys, emails or account numbers visible (`finance-compliance`).
- Term clash to flag, not fix: the spoken line says "simulation account" (Mark's J022 wording) but the `finance-compliance` badge reads "Paper trading · simulated results". Keep the badge as written until Mark answers P1; the Script critic lists it under "Needs Mark".

## Mark's lessons from fix-log that apply here (checker list)

- "sections", not "rules", for the parts of a strategy (J020).
- "simulation account" for where it runs first (J022).
- "I start by connecting Qube to Claude." word for word (J020).
- Every sentence sells the next one; answer every question you raise (J021).
- No vague setups like "say you put in…": say exactly what was done (J021). No vague nouns: every "it" points at a named agent or the strategy (Oct 15).
- Standard CTA only (Oct 23). Words within 173–211 (J021).
- Raise the stakes without naming what's next ("The best part is what happens when it says no.", J020 "That's not even the craziest part.").
- Exact triggers: "drops by 3% or more", "up 2% from where it bought" style; the risk manager's rules are exact numbers, not "too risky" (J020).
- Hook: Qube not in it; Claude is (J022 note). Mark's hook words are final; flag, never change them.
- "strategy", never "trading idea" (Oct 23). No "fake money" for the account.
- Don't explain basics Mark's viewers know (S&P 500, backtest at length). One half-line for "backtest" is the most.
- Every sentence ends (Oct 15). Lines stand alone.

## Not a repeat of
- **J017** "How to build a trading firm out of AI agents" (TradingAgents → GATC, Joshua, written, not filmed): closest topic. M23 differs: Qube, not GATC; Mark in first person ("I built"); six agents with Mark's jobs, not the TradingAgents roles; ends on the standard QUBE CTA, not GATC. If both ever get filmed, J017 should stay the GATC version.
- **J022** "Claude can now…" (Joshua): same Qube path (build → test → fix → simulation account → live). M23 differs in shape (org chart of six agents, not steps of one tool), presenter, hook and twist (the agent that says no).
- **J020** (Qube tests a rule 607 times): no shared numbers; M23 uses no backtest result.
- Mark's M01–M22: no agent or build video. None close.

## Don't copy (from the raycfu card's "what we can't copy")
- "Someone just built an entire Wall Street trading firm": we say what Mark built, in his words. No "Wall Street", no "entire AI trading floor" as a claim about firms.
- The win-rate chart (66% → 71% → 74%), "224 trades logged", and "the agents study their own mistakes and improve over time": no win rates, no "gets better over time". Our loop is fix and retest until it passes, nothing more.
- Their demo tickers and made-up fundamentals ("Orbit Dynamics (ORBT)", "Q3 revenue up 21% YoY", "Bullish mentions up 310%"): our own Claude and Qube screens only; any ticker shown is inside a labelled example, never a call.
- "Comment firm… setup guide… GitHub repo", "like the video", "Follow for more ways to make money": standard QUBE CTA only.
- The bull/bear debate and the portfolio manager: not in Mark's firm.
- Their footage, serif title style and UI cards: our own screens and layout. Keep the moves (org chart lighting up, red "no" card, punch-ins), not the look.
- From max_kelleyy: no phone-filmed monitor with tabs and taskbar visible (privacy). From honeycove: no "AI hedge fund" claim, no unrelated P&L screens.

Reject check: passes. Priya walks away with a six-job org chart she can copy, the exact "no" rules a risk manager should have, the order to run it in, and a free tool to build it without code.
