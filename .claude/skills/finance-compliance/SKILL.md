---
name: finance-compliance
description: TQX's guardrails for finance content - no promised returns, required on-screen labels, paper vs live wording, simulated results, banned phrases, and how to talk about losses, scams and product results. Use when writing, reviewing or approving any TQX script, caption, DM or on-screen text that mentions money, returns, trading results or a product's performance.
---

# Finance compliance

These are the rules TQX content has followed so far. They have **not** been reviewed by a lawyer. Treat them as the minimum, and add anything legal review requires.

## Never

| Never | Why | Instead |
|---|---|---|
| Promise or imply returns ("you'll make", "turn $500 into...") | Legally risky; looks like a scam | Show what happened in a labeled test, and say it can lose |
| "guaranteed", "risk-free", "passive income", "can't lose", "easy money", "get rich" | Banned phrases | Describe what the tool does, not what money you'll make |
| Ticker calls ("buy NVDA now") | Personalized advice | Use tickers only inside a labeled backtest or simulated example |
| Present a backtest as a real result | Misleading | Label every backtest "Backtest, not live results" |
| Present simulated or paper results as real money | Misleading | Say "paper trading" and keep the badge on screen |
| Call fake money "my $10,000" | Reads as real money; Frank will call it out | "AI is paper trading $10,000" |
| Tell viewers to go live (Qube or GATC) before testing | Skips the backtest and paper trading | "Test it on past prices, then on paper. Go live only once you've seen how it behaves." |
| Show API keys, passwords or emails on screen | Security | Blur or never show them |
| Imply a viewer will win GATC prize money | Overpromise | State the prize pool as a fact about the competition, nothing more |

## Always

1. **Backtests:** on-screen label "Backtest, not live results", plus the period and the number of trades where space allows.
2. **Paper trading / simulated series:** "Paper trading · simulated results" badge in the top-right corner for the entire video, and the script says "paper trading" or "fake money" out loud near the start.
3. **Losses shown as openly as wins.** If a series has winning days, it shows losing days in the same detail.
4. **Every number sourced** (see `claims-and-proof`), with the source on screen.
5. **Hypothetical examples are called examples.** Use "say", "picture" or "for example" before made-up numbers. "Say you had $10,000."
6. **Rankings and opinions are marked as opinion.** "And yes, I'm biased. We built one."

## Examples

| Bad | Fixed |
|---|---|
| "This bot made $4,428." | "Say I'd put in $10,000. It made about $4,400 over those ten years." + on screen "Backtest, not live results" |
| "Day 1: AI is trading my $10,000." | "Day 1: AI is paper trading $10,000, and I can't touch it." |
| "Use Qube and stop losing money." | "Test your idea on past prices before you put real money on it." |
| "This strategy works." | "It made money in the test, and still lost to just holding the S&P 500. That's why you test before you trade." |

## Scams and other companies

- Calling out scam patterns is fine and builds trust. Describe the pattern ("promised 10% a month"), cite the regulator (CFTC, FBI IC3), and don't name a person or company as a scam unless a regulator or court has.
- Other tools can be ranked and compared, but describe each one accurately from its own website, and say the ranking is an opinion.

## Region notes

- Some features are US-only (for example Robinhood's AI agent trading, May 2026). If the video targets Hong Kong or Singapore viewers, say "in the US".
- GATC Season 1 regions: Hong Kong, Singapore and the US.

## Before publishing, check

- [ ] No banned phrase
- [ ] Every backtest labeled
- [ ] Every simulated or paper result badged and said out loud
- [ ] No promised return, no ticker call
- [ ] Every number sourced on screen
- [ ] No keys, passwords or emails visible
