# J032 · Pass 0 beat map (the original, line by line)

**Original:** @raycfu · https://www.instagram.com/p/DahCoW1Pfyo/ · 91.35s · 443 words (transcript `knowledge/reference/DahCoW1Pfyo/transcript.srt`)
**Ours:** 428 words (range 399–487, −3%) · about 87s at the original's pace (4.85 words a second), about 2:12 at Joshua's usual 3.2 · Presenter: Joshua · Persona: Daniel

| Time | Original line (exact) | Our line | kept / small swap / rewritten (why) |
|---|---|---|---|
| 0.0–3.4 | "Most people don't realize that quant traders never trust a strategy the first time that it works." | Same | kept (hook, word for word) |
| 3.6–6.8 | "They run it through a loop that tests each strategy over and over again until they find one that sticks." | Same | kept |
| 6.8–8.4 | "Here's how to build this out." | Same | kept |
| 8.4–13.9 | "Most people come up with an idea, backtests once, and then once it looks great, they go live and two weeks later they are bleeding money." | "Most people come up with an idea, backtest it once, and then once it looks great, they go live. Two weeks later, they're bleeding money." | small swap: grammar ("backtest it"), contraction, split in two so neither sentence runs over 20 words (`spoken-sentence-rules` #9). Every word kept |
| 13.9–16.0 | "That strategy died because it was one guess with nothing iterating on it." | Same | kept |
| 16.0–17.3 | "A quant runs a loop testing strategy instead." | "A quant runs a testing loop instead." | small swap: "a loop testing strategy" stacks three nouns and makes "strategy" mean two things in one breath. Same meaning, said the way people talk |
| 17.3 | (the tool's screen comes up: ITERON, unnamed) | "Let me show you what that loop looks like in Qube." | small swap / added: Qube slipped in where the original shows its tool (`remix-for-product` step 2). This line hands "loop" from line 5 to the steps on screen, so every sentence sells the next (`script-logic` #3b); it's Joshua's own "Let me show you" move (`tqx-voice`). Not in the hook or the promise (brief, Mark Oct 27) |
| 17.3–25.7 | "You generate a strategy, backtest it, score it against a specific metric, read why it failed, feed that information back in, and then you generate a better version." | "You build a strategy, backtest it, and score it against a specific metric. You read why it failed, feed that information back in, and then the AI builds a better version." | small swap: "generate" → "build" (Qube's Build step, `product-truth-qube`); "you generate a better version" → "the AI builds a better version" (Qube's Improve step: "the AI suggests changes and tests them over rounds"). Split at the comma so each half is one breath (31 → 13 + 18). Rest word for word |
| 25.7–28.9 | "Then you test that version, score it, read the failures, and run it again." | Same | kept |
| 28.9–32.3 | "Each round keeps the variance that scored well and refines the ones that did not." | "Each round keeps the versions that scored well and improves the ones that didn't." | small swap: "variance" is a Whisper slip for "variants" (the screen says "Variant population"); "versions" is the plainer word, Qube's own ("version tracking") and it ties to "that version" in the line before. "refines" → "improves" (Qube's step name), "did not" → "didn't" |
| 32.3–35.8 | "The whole edge in quant trading is the iteration and most people don't iterate at all." | Same | kept (re-hook, 38%) |
| 35.8–39.9 | "The loop also needs a way to score each strategy or else it just wonders." | "…or else it just wanders." | small swap: Whisper fix |
| 37.0–42.0 | "The metric that quants use is called ICIR and all it measures is how consistently your strategy performs over time." | Same | kept (check 1; the term is explained in the same breath) |
| 42.0–47.2 | "A strategy that makes a little bit of money every single week completely beats out a strategy that makes a lot of money in one week and loses it all in the next." | Same | kept: 33 words, over the 20-word guide, but it's the comparison that only works in one breath and one of the original's standout lines. Flag accepted |
| 47.2–50.5 | "That consistency score is what the loop optimizes towards." | "That consistency score is what your loop should optimize toward." | small swap: "your loop should" keeps it a quant rule the viewer runs, not a Qube feature claim (brief; `product-truth-qube` doesn't list a consistency score). "towards" → "toward" (American) |
| 50.5–52.3 | "And here's the second check that most people skip." | Same | kept (open loop, 59%) |
| 52.3–53.6 | "Even a real strategy has a shelf life." | Same | kept |
| 53.4–57.0 | "If the signal decays in two days, you're basically just paying fees to chase noise." | Same | kept |
| 57.0–60.0 | "If it decays in 50 days, you have a real traceable edge." | "…a real tradeable edge." | small swap: Whisper fix (the screen says "TRADEABLE EDGE"). 50, as said; on screen 50, not the original's 47d |
| 60.0–61.4 | "The loop rejects these short-lived signals automatically." | "Your loop should reject these short-lived signals." | small swap: "automatically" would be a Qube feature we can't claim; "your loop should" matches line 15 |
| 61.4–62.0 | "And this is the most important part." | Same | kept (open loop, 71%) |
| 62.0–65.9 | "A loop that optimizes that same data that was built on does not find better strategies faster." | "A loop that optimizes on the same data your strategy was built on doesn't find better strategies faster." | small swap: grammar, and "your strategy" instead of "it" so the line says what was built on the data (a strategy, not the loop; `spoken-sentence-rules` #2). "your" matches lines 15 and 20 |
| 65.9–67.8 | "It just finds prettier noise faster." | Same | kept (the quotable flip) |
| 67.8–70.5 | "Every extra iteration is just another chance to accidentally fit the past data." | Same | kept |
| 70.5–72.8 | "The fix that quant uses is called an out of sample gate." | "The fix that quants use is called an out-of-sample gate." | small swap: grammar only |
| 72.8–77.6 | "Every strategy that survives the loop gets tested one final time on fresh data that is never seen." | "…on fresh data it's never seen." | small swap: grammar only |
| 77.6–79.5 | "If the consistency data holds on fresh data, then the score is real." | "If the consistency holds on fresh data, then the score is real." | small swap: one word cut so the line makes sense |
| 79.5–82.5 | "If it does not, it gets thrown out no matter how good it looked before." | "If it doesn't, it gets thrown out, no matter how good it looked before." | small swap: contraction only (payoff, 89%) |
| 82.5–85.7 | "I created a step-by-step guide on exactly how to build out this loop system to help you build trading bots that find alpha." | "We built Qube so you can run this loop on your own strategy. No code needed." | rewritten: no guide exists and the CTA can't promise one (fix-log Oct 23); "find alpha" implies returns (`finance-compliance`). The true swap is what Qube lets you do (Build, Test, Improve), in the original's spot. "We built Qube" owns the bias (`terminology`, `positioning`); "No code needed" is `positioning`'s "pro quant tools, no code" |
| 85.7–91.3 | "Just like the video and comment quant and I'll send it to you. Follow for more ways to make money and run your business with tech and AI." | "Comment QUBE and I'll send you the link for the free sign-up." | standard CTA (`cta-and-offer`, Mark Oct 23). "Like the video", "follow" and "make money" dropped: one ask, no follow line |

**Count:** 2 rewritten-or-added lines (the Qube bridge, the product line), 1 standard CTA, everything else kept or a small swap. Hook 17 · lines 411 · total 428 (`wc -w` and `tools/check-script.py`).

**Rhythm against the original (at 4.85 words a second):** Qube spoken at 18s (original's tool on screen 17.3s) · "most people don't iterate" 32–35s (32.3s) · "second check" 51s (51s) · "most important part" 62s (61.4s) · the gate and keep / throw-out 71–85s (72–82.5s) · product line and CTA in the last 6s.
