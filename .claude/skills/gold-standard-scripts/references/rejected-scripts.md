# Rejected scripts: what bad looks like

Real TQX scripts and lines that Mark threw out or had rewritten (Oct 2026), each with the reason in his words and the version that replaced it. Paste this into the gold-standard-scripts input. Use it to learn the failure, never as a template.

How to read it:
- **Part 1** is scripts rejected as a whole: the content was the problem.
- **Part 2** is scripts rejected for blanks and wrong wording.
- **Part 3** is single lines that were rewritten.

---

## Part 1. Rejected for content: "slop"

**Verdict (Mark, Oct 21):** "The scripts were written well, but the content was not necessarily great. It falls into a slop category: something we can do a lot of really quickly." No Joshua video has passed 200 views. Only two Mark videos passed 500: the tool tier list (M05) and the S&P 500 video.

**Why it fails:**
- Anyone could post it. It explains what AI trading is, which every finance account already does.
- The metaphor (a spam filter) carries the whole video instead of a real result, tool or moment.
- No proof: no real Qube run, no real trade, no real number.
- The viewer gets nothing they can use or try today.

**What good looked like instead:** M05 "Quant trading tools, ranked S to F". It ranks real tools people use, picks a fight ("You won't like where ChatGPT landed"), and hands the viewer a tool to try.

### J010 · Day 1: What AI trading actually is (final version, still slop)

**Title:** Day 1: What AI trading actually is

**Hooks:**
- AI trading isn't what you think.
- Your spam filter already thinks like a quant.
- AI trading, explained with your spam folder.
- Day 1: what AI trading actually is.
- If you're new to AI trading, start here.

**Script:**
1. Everyone's talking about AI trading. So what is it, actually? Let's break it down.
   (On screen: "Day 1 of 30 · What AI trading actually is") (Visual: series title card, pipeline bar empty at the top)
2. AI trading is really two things stuck together. Quant trading, plus AI.
   (On screen: "Quant trading + AI = AI trading")
3. Quant trading means you don't trade on a gut feeling. You trade on rules, and those rules come from data.
   (On screen: "Quant = rules from data, not gut feeling")
4. Think about the spam filter in your email. It asks one question about every new email. Is this spam, yes or no?
   (Visual: inbox screen recording, a new email arrives, a yes/no stamp lands on it)
5. Back in the day, people wrote those rules by hand. Like, "free money" in the subject line? Spam.
   (Visual: a typed rule card: IF subject has "free money" → SPAM)
6. That's quant trading. The emails are prices. The question is, "Is this stock about to go up?" And the rules are your strategy.
   (On screen, one at a time: "Emails = prices" · "Spam? = Going up?" · "The rules = your strategy")
7. Now here's the AI part. Your spam filter doesn't need people writing rules anymore. It learns them on its own, from tons of old emails.
   (Visual: thousands of emails stream into the filter, rules appear by themselves)
8. Trading works the same way now. You can open Claude or Codex and type, "Look at the last 10 years of S&P 500 prices. When should I have bought?" And it'll come back with something like, "Buy when it drops 2% in a day."
   (Visual: terminal screen recording: Joshua types the question into Claude, the answer prints out) (On screen: "Claude · Codex")
9. But here's the catch. Your spam filter still lets junk through sometimes. And a trading strategy is wrong a lot.
   (Visual: one spam email slips into the inbox, red flash)
10. That's why quants never trust a rule until they've tested it on past prices first. That's called a backtest.
   (On screen: "Backtest = testing your rules on past prices")
11. That's Day 1. Tomorrow, I'll show you the six steps every quant strategy goes through, from data all the way to real money.
   (Visual: pipeline bar at the top flashes all six steps: Data · Factors · Backtest · Portfolio · Paper · Live)
12. Follow so you don't miss Day 2.

J011–J013 (Day 2: the 6 steps / restaurant picture; Day 3: the quant loop / free throws; Day 4: strategies expire / shortcut home) fail the same way.

---

## Part 2. Rejected for blanks and wrong wording

**Verdict (Mark, Oct 11):** "You have to not give me blanks. Joshua is not gonna sit there and fill in the blanks. He wants a full script, every time. So figure it out. We can make assets that match scripts." And on "practice account": "Can you go through the entire internet and show me where people say I'm trading on a practice account?"

### J016 · Build a trading bot in 60 seconds (first draft: REJECTED, blanks)

**Title:** Build a trading bot in 60 seconds, no code

**Hooks:**
- Give me 60 seconds. You'll have a trading bot.
- You don't need to code to build a trading bot.
- 60 seconds. One trading idea. Let's test it.
- Stop guessing. Test your trading idea in 60 seconds.
- Build a trading bot before this video ends.

**Script:**
1. Okay, the timer's on. I'm building a trading bot with zero code. Let's go.
   (On screen: 60-second countdown starts, top right, stays for the whole video)
2. First, I need an idea. Here's a simple one. When the S&P 500 drops 2% in one day, buy. Sell once it's back up 2%, or if it falls another 3%.
   (On screen: the idea in one line) (Visual: Qube, empty prompt box)
3. The S&P 500 is just the 500 biggest US companies in one fund.
4. I type that in plain English, like I'm texting a friend.
   (Visual: screen recording, typing)
5. And Qube turns it into exact rules. When to buy, when to sell, how much, and when to get out if it goes wrong.
   (Visual: the rules appear)
6. Now the important part. I'm testing those rules on [REAL FIGURE: years of past prices used, e.g. "the last ten years"] of past prices. That's called a backtest.
7. Basically, if I'd run this exact bot back then, what would've happened?
   (Visual: backtest running, progress bar)
8. Here it is. On $10,000, it [REAL FIGURE: made or lost about $X] over that time.
   (On screen: exact result · "Backtest, not live results")
9. But look at this. At its worst point, it was down [REAL FIGURE: biggest drop in $ on $10,000]. That's called a drawdown. It's the biggest drop from a high point before it recovers.
   (Visual: the drawdown section highlighted in red)
10. Be honest. Could you have sat through that without panic-selling?
11. And that's a full trading bot, tested, in under a minute.
   (Visual: timer hits zero)
12. Now, a backtest isn't a promise. Past prices aren't future prices. But it beats putting real money on a hunch.
13. Comment QUBE and I'll send you the full breakdown.

**What was wrong:** three [REAL FIGURE] blanks, so Joshua couldn't film it. Also: "back up 2%" (from what?), and the S&P 500 was used before it was explained.

### J016 · the version that replaced it

**Title:** Build a trading bot in 60 seconds, no code

**Hooks:**
- Watch me build a trading bot in 60 seconds.
- You don't need to code to build a trading bot.
- 60 seconds. One trading idea. Let's test it.
- My trading bot made $4,400. Here's the problem.
- Build a trading bot before this video ends.
- Watch Claude build me a trading bot in 60 seconds.

**Script:**
1. Okay, the timer's on. I'm building a trading bot with zero code. Let's go.
   (On screen: 60-second countdown starts, top right)
2. First, I need an idea. Here's a simple one. When the S&P 500, that's about 500 of the biggest US companies, drops 2% in one day, buy.
   (On screen: the idea in one line) (Visual: terminal with Claude open, cursor blinking)
3. Then sell once it's up 2% from where I bought, or if it falls another 3%.
4. So I open Claude, and I just type that out, like I'm texting a friend. Claude's hooked up to Qube, so it sends my idea straight over. You can do the exact same thing with Codex.
   (Visual: screen recording: typing the idea into Claude, then Qube opens with the new strategy) (On screen: "Claude · Codex → Qube")
5. And Qube turns it into exact rules. When to buy, when to sell, how much, and when to get out if it goes wrong.
   (Visual: the rules appear)
6. Now the important part. I'm testing those rules on ten years of past prices, 2015 to 2024. That's called a backtest.
   (Visual: backtest running, progress bar)
7. Here it is. Say I'd put in $10,000. It made about $4,400 over those ten years.
   (On screen: "+$4,428 · 2015–2024 · 62 trades · Backtest, not live results")
8. But at its worst point, it was down about $2,600. That's called a drawdown. It's the biggest drop from a high point before it recovers.
   (On screen: "Worst drop: −$2,606") (Visual: the drawdown section highlighted in red)
9. And that's a full trading bot, tested, in under a minute.
   (Visual: timer hits zero)
10. But here's the twist. If I'd just bought the S&P 500 and held it the whole time, I'd have made about $18,600.
   (On screen: "Just holding: +$18,634 · Bot: +$4,428") (Visual: two lines on one chart)
11. So my bot made money, and still lost to doing nothing. That's exactly why you test an idea before you put real money on it.
12. Comment QUBE and I'll send you the full breakdown.

**What changed:** a real backtest was run on SPY daily closes (2015–2024) so every number is filled in and true, and the twist (it lost to just holding the S&P 500) came out of the real data.

### J018 · Day 1 of the AI paper-trading challenge (second draft: REJECTED, "practice account" + blanks)

**Title:** Day 1: AI is trading a $10,000 practice account, and I can't touch it

**Hooks:**
- Day 1: AI is trading a $10,000 practice account.
- I'm letting AI trade for 30 days. No help from me.
- What happens if you let AI trade for a month?
- 30 days. $10,000 in fake money. Zero help from me.
- I gave AI $10,000 of fake money. Real market.

**Script:**
1. Quick thing first. This is paper money. That means fake money, but real market prices. Every trade happens at the real price, at the real time.
   (On screen, whole series, top corner: "Paper account · fake money · real prices")
2. Why fake money? Because you never hand real money to a strategy you haven't watched trade the live market.
3. Here's the deal. For 30 days, the AI makes every trade. I'm not allowed to buy, sell or change a thing.
   (On screen: "Day 1 / 30") (Visual: Joshua signs a sticky note "I won't touch it" and sticks it on the screen)
4. Every trading day, I'll show you exactly how much it made or lost, and why. Good days and bad days.
   (On screen: P&L counter at $0)
5. Here's what it's running. [STRATEGY IN ONE PLAIN LINE, e.g. "It buys US stocks that have been going up, and sells anything that drops 5%."]
   (Visual: the strategy's rules on screen)
6. I described that idea to AI in plain English, and it turned it into exact rules. Now those rules run on their own.
   (Visual: Qube screen: typed idea → rules)
7. It can't put more than [REAL FIGURE: max $ per stock] into any one stock. That way one bad stock can't wipe out the account.
8. And if it's down [REAL FIGURE: daily max loss in $] in a day, it stops trading until tomorrow. That's called a daily loss limit.
   (On screen: "Max per stock: $[X] · Daily loss limit: $[Y]")
9. Before I hit start, I tested these exact rules on past prices. That's called a backtest. In that test, it [REAL FIGURE: made or lost about $X on $10,000 over which years].
   (On screen: exact figure · "Backtest, not live results")
10. But that was the past. This is the real market, right now. My guess? It's [JOSHUA'S CALL: up or down] by Friday. Comment yours.
   (Visual: this week's market headline behind Joshua)
11. Okay. It's running.
   (Visual: click Start; the first trade notification pops)
12. Follow to see what it does tomorrow.

**What was wrong:** "practice account" (nobody says it; the term is paper trading). "My $10,000" in the first draft read as real money. Blanks for the risk limits, the backtest and "this week's market".

### J018 · the version that replaced it

**Title:** Day 1: AI is paper trading $10,000, and I can't touch it

**Hooks:**
- Day 1: AI is paper trading $10,000.
- I'm letting AI trade for 30 days. No help from me.
- What happens if you let AI trade for a month?
- 30 days. $10,000 of paper money. Zero help from me.
- I'm not allowed to touch my AI's trades for 30 days.

**Script:**
1. Quick thing first. This is paper trading. That means fake money, so nothing real is on the line.
   (On screen, whole series, top corner: "Paper trading · simulated results")
2. Why fake money? Because you never hand real money to a strategy you haven't watched trade first.
3. Here's the deal. For 30 days, the AI makes every trade. I'm not allowed to buy, sell or change a thing.
   (On screen: "Day 1 / 30") (Visual: Joshua signs a sticky note "I won't touch it" and sticks it on the screen)
4. Every trading day, I'll show you exactly how much it made or lost, and why. Good days and bad days.
   (On screen: P&L counter at $0)
5. Here's what it's running. Every day, it watches the 10 biggest US companies. If one drops more than 3% in a day, it buys.
   (Visual: ten company logos in a grid; one flashes red)
6. It sells once that stock bounces back 3%, or if it falls 5% from where it bought. That 5% rule is called a stop-loss. It sells for you before a small loss turns into a big one.
   (On screen: "Buy: down 3% in a day · Sell: back up 3% · Stop-loss: down 5%")
7. I described that idea to AI in plain English, and it turned it into exact rules. Now those rules run on their own.
   (Visual: Qube screen: typed idea → rules)
8. And it can't put more than $2,000 into any one stock. That way one bad stock can't wipe out the account.
9. Before I hit start, I tested these exact rules on the last five years of prices. That's called a backtest. On $10,000, it made about $8,100. But at one point, it was down about $3,200.
   (On screen: "+$8,147 · 2021–2025 · 607 trades · worst drop −$3,207 · Backtest, not live results")
10. But that was the past. My guess? It's down by Friday. Comment yours.
11. Okay. It's running.
   (Visual: click Start)
12. And there's the first trade. Tesla dropped more than 3% today, so it just bought $2,000 of Tesla.
   (On screen: "Bought $2,000 of TSLA") (Visual: trade notification pops)
13. Follow to see what it does tomorrow.

### J019 · Week 1 recap (first draft: REJECTED, blanks everywhere)

**Title:** Week 1: What AI did with my $10,000

**Hooks:**
- Week 1 of letting AI trade my $10,000.
- Here's every dollar my AI made or lost this week.
- I wanted to stop the AI this week. I couldn't.
- Week 1: AI vs just buying the S&P 500.
- One week of AI trading. No edits.

**Script:**
1. One week ago, I gave an AI a $10,000 paper account. That's fake money, real market prices. And I promised not to touch it.
   (On screen: "Week 1 · Paper account · fake money · real prices")
2. After five trading days, it's [REAL FIGURE: up or down about $X].
   (On screen: exact P&L) (Visual: P&L counter rolls to the number)
3. If I'd just bought the S&P 500 instead, that's the 500 biggest US companies in one fund, I'd be [REAL FIGURE: up or down about $Y].
   (Visual: two lines, AI vs S&P 500, same chart)
4. So [VERDICT: "the AI beat doing nothing" or "doing nothing beat the AI"], for now.
5. Best day was [DAY]. It made [REAL FIGURE] because [REASON IN PLAIN WORDS].
   (Visual: green day highlighted, the trade on screen)
6. Worst day was [DAY]. It lost [REAL FIGURE] because [REASON IN PLAIN WORDS].
   (Visual: red day highlighted, the trade on screen)
7. And here's the hard part. On [DAY], I really wanted to step in and [WHAT JOSHUA WANTED TO DO].
8. If I had, I'd be [REAL FIGURE: what would've happened, worked out from that day's prices].
   (Visual: a "what if" line splitting off the chart)
9. That's the whole point of rules. The AI doesn't care that it's down. It just does what it said it would do.
10. Its biggest drop so far was [REAL FIGURE]. That's called a drawdown. It's the most it fell from its high point.
   (Visual: the drawdown section in red)
11. Three weeks left. Same rule: I don't touch it.
12. Follow to see if it [keeps it / gets it back]. Comment your call.

**What was wrong:** almost every line was a blank ([DAY], [REAL FIGURE], [REASON IN PLAIN WORDS]). It was replaced by a fully scripted, simulated week (J019–J023) where every number adds up across episodes (Tesla +$64, Nvidia −$100, Meta +$62, week +$26) and the "Paper trading · simulated results" badge stays on screen.

---

## Part 3. Single lines rewritten

**Verdict (Mark, Oct 15):** "Are you 100% sure you're talking like somebody from LA? I can pick up on a lot of weird things that just standalone don't make sense."

### J010
- **Rejected:** "AI does the same thing for trading. You can ask Claude or Codex, in plain English, to dig through years of past prices and find rules for you. Way faster than writing them by hand."
- **Why:** What rules? What rules?
- **Replaced with:** "Trading works the same way now. You can open Claude or Codex and type, "Look at the last 10 years of S&P 500 prices. When should I have bought?" And it'll come back with something like, "Buy when it drops 2% in a day.""

### J012
- **Rejected (1st):** "That loop used to take a whole team. Now you can hand it to Claude or Codex, and they'll run it for you. Version after version."
- **Why:** "Now you hand it to Claude or Codex and they run it version after version. No idea what you're talking about."
- **Rejected (2nd):** "That whole loop used to take a team of people. Now you can type your idea into Claude or Codex, and it'll build it, test it, find what's broken, fix it, and test it again. Over and over."
- **Why:** "Over and over, like this sentence doesn't end. You're stating something without an ending."
- **Replaced with:** "That whole loop used to take a team of people. Now you can type your idea into Claude or Codex, and it'll build it, test it, find what's broken, fix it, and test it again. Over and over until you're happy with the result."

### J014
- **Rejected (1st):** "You type your idea into Claude or Codex in plain English. They plug straight into Qube, which turns it into exact rules, tests them on past prices, and sticks to your max loss. Even on the days you wouldn't."
- **Why:** "Keeps to your max loss. Read that back to yourself... the more I say it, the more confused I am."
- **Rejected (2nd):** "You type your idea into Claude or Codex, like you're texting a friend. It's hooked up to Qube, so your idea gets turned into written rules and tested on years of past prices. And it stops trading for the day the second you hit your max loss. Even on the days you'd want to keep going."
- **Why:** same problem as J012: the last sentence is a fragment with no ending of its own.
- **Replaced with:** "You type your idea into Claude or Codex, like you're texting a friend. It's hooked up to Qube, so your idea gets turned into written rules and tested on years of past prices. And it stops trading for the day the second you hit your max loss, even on the days you'd want to keep going."

### J016
- **Rejected:** "I type it into Claude in plain English, like I'm texting a friend. Claude's plugged into Qube, so it does the building. Codex works too."
- **Why:** "The bot gets built by typing into Claude. What?"
- **Replaced with:** "So I open Claude, and I just type that out, like I'm texting a friend. Claude's hooked up to Qube, so it sends my idea straight over. You can do the exact same thing with Codex."

### J017
- **Rejected:** "And you don't have to code it from scratch. You can build your team with Claude or Codex, right from your terminal, and plug it straight into GATC."
- **Why:** fixed in the same pass for the same reason: "plug it straight into GATC" (plug what?) doesn't say what happens.
- **Replaced with:** "And you don't need to know how to code to build one. Just open Claude or Codex and type, "Build me a GATC team. One AI reads the news, one makes the trades, and one can say no." It sets the whole team up for you."

---

## The patterns, in one list

1. Content anyone could post, carried by a metaphor, with nothing for the viewer to use.
2. Blanks or placeholders of any kind.
3. Words nobody says ("practice account", "keeps to your max loss").
4. Vague nouns ("the rules", "it", "they") that don't point to anything.
5. Sentences that trail off without an ending.
6. Lines that only make sense if you heard three lines earlier.
