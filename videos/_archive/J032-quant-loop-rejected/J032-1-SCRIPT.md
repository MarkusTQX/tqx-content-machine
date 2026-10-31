# J032 · SCRIPT (Joshua reads this)

**Recreating:** @raycfu · "How Quants use Loop Engineering to create a trading bot" · 7,166 likes and 4,933 comments on a 268K-follower account
**Original video:** https://www.instagram.com/p/DahCoW1Pfyo/
**Words:** original 443 words (91s) · ours 175 words (cut to ~50s on Mark's note, Oct 27)
**Length:** about 55s at Joshua's usual pace (3.2 words a second) · Presenter: Joshua

---

## Hook (the original's, word for word)

**Hook.** Most people don't realize that quant traders never trust a strategy the first time that it works.

---

## Script

1. They run it through a loop that tests each strategy over and over again until they find one that sticks.

2. Most people backtest once, and once it looks great, they go live. Two weeks later, they're bleeding money.

3. A quant runs a loop instead, and one last test decides which strategy they keep.

4. In Qube, you build a strategy, backtest it, and score it.

5. You read why it failed, feed that back in, and the AI builds a better version to test again.

6. But a loop that keeps testing on the same data doesn't find better strategies faster.

7. It just finds prettier noise faster.

8. So that last test is an out-of-sample gate.

9. Every strategy that survives the loop gets tested on data it's never seen.

10. If it holds up, you keep it.

11. If it doesn't, it gets thrown out, no matter how good it looked before.

12. Comment QUBE and I'll send you the link for the free sign-up.
