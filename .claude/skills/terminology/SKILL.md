---
name: terminology
description: TQX's approved glossary. For each term, the exact word to use, what it means, the words never to use instead, how to capitalize it, whether to explain it on camera, and an example sentence. Use when writing or checking any TQX, Qube or GATC script, caption, asset list or DM, so terms don't drift and internal jargon never reaches the audience.
---

# TQX terminology

Every word fix Mark has made lives here. If a term isn't in this table and a script needs it, use the plainest everyday word, explain it the first time, and add it here once Mark approves it.

## Hard rules

1. **One term per thing, per script.** Pick "trading bot" or "AI agent" and keep it. Never drift between bot, algo, model and agent in the same video.
2. **Explain a term the moment it first appears, unless the persona already knows it** (see `audience-profile`). Marcus and Frank don't need "backtest" explained; Daniel and Priya do.
3. **Vague nouns aren't allowed.** "Rules", "it", "they" and "the thing" must point to something the viewer has just heard or is seeing.
   - Bad: "...and find the rules for you." (Which rules?)
   - Fixed: "And it'll come back with something like, 'Buy when it drops 2% in a day.'"
4. **Internal words never go on camera or into the creator's instructions** (see the internal-only column).
5. **Fake money: GATC says "simulation account", everything else says "paper trading".** "Simulation account" is TQX's name for the account a GATC agent trades in. For Qube, series and general explainers, say "paper trading" or "fake money". Don't switch between the two in one video.
   - Mark's edit (J022, a Qube video, Oct 23): Bad: "Once it looks good, try it on fake money first." Fixed: "Once it looks good, try it on a simulation account first." When the line names the place you try a strategy before going live, use his wording, not "fake money". Whether Qube videos now always say "simulation account" is waiting on Mark (`data/mark-edits/proposals.md` P1).
6. **What Qube builds is a "strategy", and its parts are "sections". Don't call them "rules"** (Mark, Oct 23, in J020 and J022; same confusion as Oct 15's "turns it into rules"). One named rule inside a strategy is fine: Mark kept "Then an entry rule buys..." and "Then Qube tests those rules...".

   | Bad | Fixed (Mark's) |
   |---|---|
   | "Qube breaks your strategy into four rules, and each one handles a different job." | "Qube breaks your strategy into four sections, and each one has a different job." |
   | "Qube takes your rules and runs them through five years of real prices." | "Qube takes your strategy and tests it on up to five years of real price data." |
   | "One rule scans the 10 biggest US stocks looking for a drop." | "First it scans the 10 biggest US stocks looking for a drop in price." |

## The glossary

| Approved term | What it means | Never say | Capitalization | Explain on camera? | Example sentence |
|---|---|---|---|---|---|
| paper trading / paper money | Trading the real market with fake money, so nothing real is on the line | "practice account" (nobody says it), "play money" | lowercase | Yes, every time for beginners | "This is paper trading. That means fake money, so nothing real is on the line." |
| simulation account | TQX's name for the fake-money account a GATC agent trades in | "demo account", "test account" | lowercase | Yes: "a fake-money account" | "First you make a simulation account. That's a fake-money account, so your agent can trade without touching real cash." |
| backtest | Testing your rules on past prices to see what would have happened | "back-test", "simulation" (as a synonym) | lowercase | Yes for Daniel, Priya, Kai; no for Marcus or Frank | "I'm testing those rules on ten years of past prices. That's called a backtest." |
| "Backtest, not live results" | The label on every backtest shown on screen | "results", "returns" with no label | as written | It's on screen, not spoken | On-screen: "+$4,428 · 2015–2024 · 62 trades · Backtest, not live results" |
| drawdown | The biggest drop from a high point before the account recovers | "loss" (when you mean drawdown), "dip" | lowercase | Yes | "At its worst point, it was down about $2,600. That's called a drawdown." |
| stop-loss | A rule that sells for you before a small loss turns into a big one | "stop", "SL" | lowercase, hyphenated | Yes | "That 5% rule is called a stop-loss. It sells for you before a small loss turns into a big one." |
| max loss for the day | A loss limit; once you hit it, you stop trading for the day | "keeps to your max loss" (nobody talks like that) | lowercase | Say what it does | "It stops trading for the day the second you hit your max loss." |
| quant trading | Trading with rules and data instead of your gut | "systematic investing" | lowercase | Yes | "Quant trading just means trading with rules and data instead of your gut." |
| AI trading | Quant trading plus AI | "robo-trading" | "AI" caps | Yes for beginners | "AI trading is really two things stuck together. Quant trading, plus AI." |
| algorithmic trading | A computer follows fixed rules and places the trades by itself | "algo" on first mention | lowercase | Yes | "Algorithmic trading means a computer follows fixed rules and places the trades by itself." |
| trading bot | Rules that place trades automatically (consumer word) | mixing with "agent" in the same script | lowercase | Usually no | "Watch me build a trading bot in 60 seconds." |
| AI agent / agent | An AI that trades on its own; what people enter into GATC | mixing with "bot" in the same script | lowercase | Yes the first time | "In GATC, only AI agents trade. No humans placing orders." |
| team of agents | Several AI agents working together in one GATC entry, each with one job (one reads the news, one makes the trades, one can say no) | "AI team", "GATC team", "agent team", "agent group" (internal platform word) | lowercase | Yes the first time: "a team of agents, each with one job" | "Open Claude or Codex and type, 'Build me a team of agents for GATC.'" |
| factor | A clue that a stock might go up | "alpha factor" (too deep for beginners) | lowercase | Yes | "A factor is just a clue that a stock might go up." |
| signal decay | When an edge fades because too many people find it | "alpha decay" | lowercase | Yes | "When an edge fades like this, it's called signal decay." |
| bull / bear | Bull thinks the price is going up; bear thinks it's going down | | lowercase | Yes | "A bull thinks the price is going up. A bear thinks it's going down." |
| the spread | The gap between the price you buy at and the price you can sell at | "bid-ask" without explaining | lowercase | Yes | "Every trade costs you the spread. That's the gap between the price you buy at and the price you can sell at." |
| day trading | Buying and selling on the same day, trying to catch small price moves | | lowercase | Yes | "Day trading means buying and selling on the same day." |
| futures and options | Contracts that let you bet big on where a price is going | "derivatives" | lowercase | Yes | "Futures and options are contracts that let you bet big on where a price is going." |
| 0DTE | Options that expire the same day you buy them | | caps | Yes | "0DTE means the option expires the same day." |
| leverage | Borrowing to make your bet bigger | "margin" as a synonym | lowercase | Yes | "100x leverage means a 1% move against you wipes out your whole bet." |
| S&P 500 | About 500 of the biggest US companies | "the S&P", "SPX" on camera | "S&P 500" | Yes the first time | "When the S&P 500, that's about 500 of the biggest US companies, drops 2% in one day, buy." |
| Qube | TQX's no-code strategy builder | "QUBE" in speech or captions, "the Qube app" | "Qube" (the CTA keyword is "QUBE") | Only what it does | "I start by connecting Qube to Claude." |
| GATC | The Global AI Trading Championship | "the tournament", "the GATC" | all caps | Full name on first mention | "It's called GATC, and there's HK$14 million on the line." |
| Claude / Codex | Claude (Anthropic) and Codex (OpenAI); both connect to Qube and GATC from the command line | "Claude Code" on camera (fine in the creator's B-roll steps), "ChatGPT Codex" | as written | No | "Open Claude or Codex and type what you want." |
| Jev | TQX's decision model: picks one option from a list you give it | | "Jev" | Yes | "You give Jev the options. It picks one and tells you how sure it is." |
| TQX | The company and the platform at tqx.ai. Said as letters: "T-Q-X". The site is said "T-Q-X dot A-I" | "tee-quix", "the TQX app" | all caps | No | "We built this at TQX." |
| strategy | A full set of trading rules: when to buy, when to sell, how much, and when to get out | "system", "setup" as synonyms, "trading idea" (nobody in LA says it; Mark, Oct 23) | lowercase | Usually no | "A strategy is just your rules written down. When to buy, when to sell, how much, and when to get out." |
| ready-made strategy | One of Qube's templates you can start from | "preset", "blueprint"; "template" is fine on screen, say "ready-made strategy" out loud | lowercase | Say what it is | "Pick one of the ready-made strategies and run it." |
| win rate | The share of trades that made money | "hit rate", "accuracy" | lowercase | Yes | "A 40% win rate can still make money if the wins are bigger than the losses." |
| slippage | The difference between the price you expected and the price you actually got | "execution drag" | lowercase | Yes | "You hit buy at $100 and got $100.30. That 30 cents is called slippage." |
| liquidation | The exchange closing your position for you because your money ran out | "wiped" or "rekt" on their own (Kai-level slang is fine only after the real word) | lowercase | Yes | "A 1% move against you and the exchange closes your trade for you. That's called liquidation." |
| overfitting | Tuning rules so closely to past prices that they fit luck, not a real pattern | "curve-fitting" on first mention | lowercase | Yes, except Marcus and Frank | "Tweak the rules enough and they'll fit the past perfectly. That's called overfitting, and it falls apart live." |
| look-ahead bias | A test that secretly uses information it couldn't have had at the time | "data leakage" | lowercase, hyphenated | Yes, except Marcus and Frank | "One wrong cell and your test is secretly using tomorrow's price to make today's trade. That's called look-ahead bias." |
| Sharpe ratio | How much a strategy made for the risk it took. Higher is better | "Sharpe" on its own with beginners | capital S | Marcus: no. Everyone else: yes, or leave it out | "The Sharpe ratio measures how much it made for the risk it took. Higher is better." |
| API keys | Two passwords that let your agent talk to TQX | "tokens", "credentials", "secrets" | "API keys" | Yes: "they work like passwords" | "TQX gives you two API keys. Treat them like passwords." |
| prize pool | The total GATC prize money: HK$14 million | "jackpot", "winnings" | lowercase | No | "The prize pool is 14 million Hong Kong dollars. That's about 1.8 million US." |

## Internal-only (never on camera, and never in viewer-facing text)

| Term | Why it's internal |
|---|---|
| TQX OS | Never mention it, anywhere |
| persona names (Daniel, Priya, Marcus, Ethan, Frank, Kai) | Planning labels |
| tracker code / editor code (J001, M05, M16) | Production IDs |
| "slop", "thesis", "persona" | Planning words |

## Words for the creator's asset instructions

The creator follows the asset sheet literally. Use these exact words there:

| Approved | Never |
|---|---|
| "on-screen text" (the words that pop up over the video) | "text card", "lower third", "super" |
| "top third" (defined once as the 1080×640 box above the presenter) | "header area", "upper zone" |
| "screen recording of [exactly what is typed, where, in which app]" | "screen recording" on its own |
| exact numbers ("4 numbers: +$4,428, 62 trades...") | "stat cards", "Day N", "a few numbers" |
