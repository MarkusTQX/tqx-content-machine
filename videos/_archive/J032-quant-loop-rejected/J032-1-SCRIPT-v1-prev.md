# J032 · SCRIPT (Joshua reads this)

**Recreating:** @raycfu · "How Quants use Loop Engineering to create a trading bot" · 7,166 likes and 4,933 comments on a 268K-follower account
**Original video:** https://www.instagram.com/p/DahCoW1Pfyo/
**Words:** original 443 words (91s) · ours 427 words
**Length:** about 87s at the original's quick pace, no pauses between lines (the original is 91s at 4.9 words a second; at Joshua's usual pace it would run about 2:12) · Presenter: Joshua

---

## Hook (the original's, word for word)

**Hook.** Most people don't realize that quant traders never trust a strategy the first time that it works.

---

## Script

1. They run it through a loop that tests each strategy over and over again until they find one that sticks.

2. Here's how to build this out.

3. Most people come up with an idea, backtest it once, and then once it looks great, they go live. Two weeks later, they're bleeding money.

4. That strategy died because it was one guess with nothing iterating on it.

5. A quant runs a testing loop instead.

6. Let me show you what that loop looks like in Qube.

7. You build a strategy, backtest it, and score it against a specific metric.

8. You read why it failed, feed that information back in, and then the AI builds a better version.

9. Then you test that version, score it, read the failures, and run it again.

10. Each round keeps the versions that scored well and improves the ones that didn't.

11. The whole edge in quant trading is the iteration, and most people don't iterate at all.

12. The loop also needs a way to score each strategy, or else it just wanders.

13. The metric that quants use is called ICIR, and all it measures is how consistently your strategy performs over time.

14. A strategy that makes a little bit of money every single week completely beats out a strategy that makes a lot of money in one week and loses it all in the next.

15. That consistency score is what your loop should optimize toward.

16. And here's the second check that most people skip.

17. Even a real strategy has a shelf life.

18. If the signal decays in two days, you're basically just paying fees to chase noise.

19. If it decays in 50 days, you have a real tradeable edge.

20. Your loop should reject these short-lived signals.

21. And this is the most important part.

22. A loop that optimizes on the same data it was built on doesn't find better strategies faster.

23. It just finds prettier noise faster.

24. Every extra iteration is just another chance to accidentally fit the past data.

25. The fix that quants use is called an out-of-sample gate.

26. Every strategy that survives the loop gets tested one final time on fresh data it's never seen.

27. If the consistency holds on fresh data, then the score is real.

28. If it doesn't, it gets thrown out, no matter how good it looked before.

29. We built Qube so you can run this loop on your own strategy. No code needed.

30. Comment QUBE and I'll send you the link for the free sign-up.
