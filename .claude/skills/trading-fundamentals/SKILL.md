---
name: trading-fundamentals
description: Correct, plain-English meanings of the trading concepts TQX videos use (backtest, paper trading, drawdown, stop-loss, overfitting, look-ahead bias, leverage, fees and spread, signal decay and more), the common misconceptions about each, and how we explain them on camera. Use when writing or checking any trading explanation, so nothing is slightly wrong in a way experienced traders spot instantly.
---

# Trading fundamentals

Frank (the skeptic) catches a slightly wrong explanation in one second, and his comment sets the tone for everyone reading. Get every concept exactly right at the depth the persona needs. Approved spoken wording is in `terminology`; this file is about getting the meaning right.

## Core concepts

### Backtest
- **Correct:** Running a fixed set of rules over past prices to see what would have happened. It shows what the rules would have done, never what they will do.
- **Misconception:** "It made 40% in the backtest, so it'll make 40% live." Backtests are often far better than live results. Across 888 Quantopian algorithms, backtest Sharpe ratio explained under 2.5% of how they did afterwards (Wiecki et al. 2016).
- **How we say it:** "Testing your rules on past prices. That's called a backtest." Always label it on screen: "Backtest, not live results".

### Paper trading (forward test)
- **Correct:** Trading the live market with fake money. It comes after the backtest and before real money, so you see how the rules behave on prices they've never seen.
- **Misconception:** That a backtest and paper trading are the same thing. A backtest uses old prices; paper trading uses today's.
- **Order:** idea → rules → backtest → paper trading → live. Never put paper trading before the backtest.

### Live trading
- Real money in a real brokerage account. Nothing in a TQX video should suggest a viewer go live without testing first.

### Drawdown
- **Correct:** The biggest drop from a high point before the account recovers. It's measured from the peak, not from where you started.
- **Bad:** "It lost $2,600." (Sounds like a final loss.)
- **Fixed:** "At its worst point, it was down about $2,600 from its high. That's called a drawdown."

### Stop-loss
- **Correct:** An order that sells once the price falls to a level you set, so a small loss doesn't turn into a big one.
- **Misconception:** That it guarantees you get out at exactly that price. If the price jumps past it (overnight, on news), you can sell lower than your stop.

### Overfitting
- **Correct:** Tuning rules so closely to past prices that they fit the noise, not a real pattern. Looks amazing in the backtest; falls apart live.
- **Fact:** With 5 years of data, trying just 45 variations can produce a winner that's pure luck (Bailey, Borwein, López de Prado & Zhu 2014).
- A picture that has worked: someone painting a bullseye around bullet holes after shooting.

### Look-ahead bias
- **Correct:** The test accidentally uses information that wasn't available at the time, like tomorrow's price to make today's trade. Results look amazing and are fake.
- **How we've said it:** "One wrong cell and your test is secretly using tomorrow's price to make today's trade."

### Hindsight in stock picks (survivorship bias)
- **Correct:** Testing on today's biggest or surviving companies flatters the result, because you already know they won.
- Say so when it applies. Example: a backtest on today's 10 biggest US companies "has some hindsight in it".

### Fees and the spread
- **Correct:** Every trade costs fees plus the spread (the gap between the price you buy at and the price you can sell at). More trades means more cost.
- **Fact:** Trading cut yearly returns by 2.65 points for men and 1.72 for women (35,000+ US households, 1991–97, Barber & Odean 2001).

### Slippage
- **Correct:** The difference between the price you expected and the price you actually got.

### Leverage and liquidation
- **Correct:** Leverage means borrowing to make your bet bigger. At 100x, $100 controls $10,000, so a 1% move against you is $100: your whole stake. Liquidation is the exchange closing your position for you when your money runs out.

### Win rate vs payoff
- **Correct:** Win rate alone says nothing. A strategy can win 40% of the time and still make money if the wins are bigger than the losses, or win 70% and lose money if the losses are bigger.

### Sharpe ratio (for Marcus-level content)
- **Correct:** Return earned per unit of risk (volatility). Higher is better. Don't use it with beginners without explaining it.

### Signal decay
- **Correct:** An edge fades as more people find and trade it.
- **Fact, stated carefully:** McLean & Pontiff (2016) looked at 97 predictors from published research. Returns were 26% lower out of sample and 58% lower after publication. The authors attribute the extra drop after publication to people trading on it. Don't say all of the drop came from copying.

### Regime change
- **Correct:** Market behavior shifts (calm to panic, trending to choppy), and rules that worked in one regime stop working in the next.

### Quant trading, algorithmic trading, AI trading
- Quant trading: rules from data, not gut feeling.
- Algorithmic trading: a computer follows fixed rules and places trades by itself.
- AI trading: quant trading plus AI, where AI helps find, build or test the rules.
- Don't claim AI predicts the future. The CFTC's own warning: "AI technology can't predict the future or sudden market changes."

## Explaining at the right depth

| Persona | Depth |
|---|---|
| Daniel, Priya, Kai | Explain every term in one plain sentence the first time it appears |
| Ethan | Explain, but the career or credential angle can go deeper |
| Marcus | Don't explain basics; give exact mechanics |
| Frank | Don't explain basics. Get every detail exactly right, and show the source and the label on screen |

## Checks before a concept goes in a script

1. Is the definition right, including the edge cases above?
2. Does any number say exactly what the source measured: who, where, which years? (See `claims-and-proof`.)
3. Does the order of steps match the real process? (Backtest before paper trading.)
4. If you used a picture to explain it, does every part of the picture map to the real thing without contradicting it?
