# J032 · Quants never trust a strategy the first time it works (Qube recreation)
Presenter: Joshua (calm explainer who shows the screen, `tqx-voice`) · Persona: Daniel, the burned retail trader · Why they care: he's the "most people" in line 4. He backtested once, it looked great, he went live and lost. This shows him what quants do instead (test, score, fix, retest, round after round, then one last test on data the strategy has never seen), and where he can run that loop himself without code.
Source: `knowledge/cards/reference/2026-07-08_raycfu_loop-engineering-trading-bot.md` (Mark's pick, recreate; batch of 6 Joshua videos J028–J033). Transcript: `knowledge/reference/DahCoW1Pfyo/transcript.srt`, `meta.txt`.
Original Reel link: https://www.instagram.com/p/DahCoW1Pfyo/ (put it on the "Original video:" line of the SCRIPT doc, fix-log Oct 24)
Mark's direction (Oct 27): "Quants never trust a strategy the first time it works." Improve it, retest it, round after round. Show Qube's improve-and-retest loop without leading on the tool. Copy the original's script word for word where it's true, slip Qube in where the original shows its tool, swap only what isn't true.
**Length override (Mark, Oct 27, fix-log):** on the approved 428-word version: "way too many words - nobody sticking around for that long". Cut to the strongest beats, about 50s (150–170 words at Joshua's pace), hook word for word. This replaces the ±10% target and the "never cut lines 3, 6, 9, 14, 19…" list below. The long version is in `long-v1/`.

## The original's engine to keep
@raycfu (268K followers), 91s, **443 words**, about 4.9 words a second, 7,166 likes, 4,933 comments (comments are 69% of likes, driven by the keyword).
Beats in order: insider hook ("Most people don't realize…") → the promise, "they run it through a loop… Here's how to build this out" (3.6s) → the mistake, shown as a green backtest curve that turns red the moment "Live" is switched on (8.4–17s) → the loop said as a rhythm, "generate, backtest, score, read why it failed, feed that back in" (17–32s) → re-hook "most people don't iterate at all" (32s) → check 1, the consistency score (36–51s) → open loop "the second check that most people skip", shelf life (51–61s) → open loop "this is the most important part", the overfitting trap, "prettier noise" (61–72s) → the fix, the out-of-sample gate, ending on a side by side: one strategy holds on fresh data, one collapses (72–82s) → keyword CTA over the face (82.5–91s).
Big moments: the curve going red on "Live" (the "that's me" moment as a picture) · "It just finds prettier noise faster." (the quotable flip) · the survivor-vs-collapse pair right before the CTA.
Format: talking head in the bottom two-thirds, a dark UI insert in the top third (changes every 2–3s), punch-in close-up on every re-hook line, 22 cuts (about one every 4s), white captions 3–6 words at a time over the chest. Title card for the first 3s. The tool on screen is never named out loud.

## Outside gold to aim at
This Reel itself, gold #7 in `gold-standard-scripts` ("Qube's Build → Test → Improve, ending on a strategy that fails"). Copy it line by line. The gold's ending already does that: keep the survivor-vs-collapse pair as the last picture before the product line.

Shape: 3. Problem → solution (the original's shape, kept: `story-structures` lists this Reel under it; `remix-for-product`) · Target length: **443 words, range 399–487** (`script-logic` #10, Mark Oct 27: ±10%). The draft below is 419. At Joshua's usual 3.2 words a second that's about 2:10; to land near the original's 91s he reads at the original's quick pace, no pauses between lines (M23 did the same). Words are the rule, not seconds (J024 brief).

Enemy → difference: trading on gut feeling, here "one guess with nothing iterating on it" (`positioning`) → test it before you risk it. Landing line is the original's own: "If it doesn't, it gets thrown out, no matter how good it looked before."

Product: Qube · Placement: **line 6, where the original's loop is first walked through on its tool's screen (17s)**: "In Qube, you generate a strategy, backtest it…". Not in the hook and not in the promise (Mark: "without leading on the tool"; `hook-writing` #8). On screen, Qube takes the original's UI slot from 3.6s on, unnamed, the way the original shows ITERON: rounds, versions, backtests. Spoken a second time in the product line before the CTA (where the original pitches its guide). The keyword CTA is the last spoken line.
Keep Qube on what it really does (`product-truth-qube`): build from plain English, backtest with every trade shown, the AI suggests changes and tests them over rounds, version tracking and run history. The two checks and the gate stay **what quants do** (the original already says "the metric that quants use", "the fix that quants use"). They are not claimed or shown as Qube features.

The promise (what the hook promises): why quants don't trust a strategy that works the first time, and the loop they run instead.
The payoff (what they walk away with, usable today): the loop (generate → backtest → score → read why it failed → feed it back → retest, round after round), two checks to run on any strategy (is it consistent week to week, and how fast does the signal fade), and the one rule that catches "prettier noise": a last test on data the strategy has never seen. Plus where to run the loop free, without code.

CTA: "Comment QUBE and I'll send you the link for the free sign-up." (standard CTA, `cta-and-offer`, Mark Oct 23). Drop the original's "like the video" and "Follow for more…" (one ask; no follow line, fix-log Oct 23).

## The hook (one hook, the original's, word for word)

**"Most people don't realize that quant traders never trust a strategy the first time that it works."**

Kept word for word (`hook-writing` #7). Nothing in it is untrue for us; it's the original's claim, taken as given (Mark). 17 words, about 3.4s in the original. On screen frame 1: title "How Quants use Loop Engineering to build trading bots" ("Quants", "Loop Engineering" and "trading bots" in yellow; 8 words, `on-screen-text`). First frame: Joshua wide at his desk, talking with his hands. Don't copy the original's fund-share line chart at 2s (no source).

## Beat map, line by line against the original (draft lines; the Scriptwriter owns the final words and marks each one in beatmap.md)

| # | Original line (time · job) | Ours (draft) | Mark | On screen (top-third insert) |
|---|---|---|---|---|
| H | "Most people don't realize that quant traders never trust a strategy the first time that it works." (0s · hook) | Word for word | kept | Title card; Joshua wide |
| 1 | "They run it through a loop that tests each strategy over and over again until they find one that sticks." (3.6s · promise) | Word for word | kept | Punch-in. Qube run history: one strategy, round 1, 2, 3 stacking up (unnamed, as the original) |
| 2 | "Here's how to build this out." | Word for word | kept | Same, cut wide |
| 3 | "Most people come up with an idea, backtests once, and then once it looks great, they go live and two weeks later they are bleeding money." (8.4s · the mistake, "that's me") | "Most people come up with an idea, backtest it once, and then once it looks great, they go live, and two weeks later they're bleeding money." | small swap (grammar only) | Our own graphic: a green curve tagged "Backtest", a "Live" toggle flips, the line turns red. Label "Example". No numbers |
| 4 | "That strategy died because it was one guess with nothing iterating on it." | Word for word | kept | Red curve holds; "1 guess · 0 rounds" |
| 5 | "A quant runs a loop testing strategy instead." | Word for word | kept | Loop diagram: GENERATE → BACKTEST → SCORE → READ FAILURE → REFINE (our own design) |
| 6 | "You generate a strategy, backtest it, score it against a specific metric, read why it failed, feed that information back in, and then you generate a better version." (17s · the loop, tool on screen) | "**In Qube,** you generate a strategy, backtest it, score it against a specific metric, read why it failed, feed that information back in, and then **the AI** generates a better version." | small swap (Qube slipped in; "the AI generates" = Qube's Improve step) | Real Qube screens, phone-filmed, each step lighting on the word: the strategy typed in plain English → backtest with "Backtest, not live results" → results and trade list → the AI's suggested change → v2 |
| 7 | "Then you test that version, score it, read the failures, and run it again." | Word for word | kept | Qube: v2 backtest running, then v3 |
| 8 | "Each round keeps the variance that scored well and refines the ones that did not." | "Each round keeps the variants that scored well and refines the ones that did not." | small swap (Whisper fix, the screen said "variants") | Qube version list: v1, v2, v3; the weaker ones greyed |
| 9 | "The whole edge in quant trading is the iteration and most people don't iterate at all." (32s · re-hook, 36%) | Word for word | kept | Punch-in, no insert (or "Most people don't iterate at all" on screen) |
| 10 | "The loop also needs a way to score each strategy or else it just wonders." | "…or else it just wanders." | small swap (Whisper fix) | Loop diagram, SCORE lit |
| 11 | "The metric that quants use is called ICIR and all it measures is how consistently your strategy performs over time." (check 1) | Word for word | kept | "Scoring metric · ICIR" card, our design |
| 12 | "A strategy that makes a little bit of money every single week completely beats out a strategy that makes a lot of money in one week and loses it all in the next." | Word for word | kept | Two bar charts: "A · steady" small green bars vs "B · boom / bust" one big bar then red. Label "Example". No numbers |
| 13 | "That consistency score is what the loop optimizes towards." | "That consistency score is what the loop **should** optimize towards." | small swap (keeps it a quant rule, not a Qube feature claim) | "A" circled |
| 14 | "And here's the second check that most people skip." (51s · open loop, 58%) | Word for word | kept | Punch-in |
| 15 | "Even a real strategy has a shelf life." | Word for word | kept | "Shelf life" card |
| 16 | "If the signal decays in two days, you're basically just paying fees to chase noise." | Word for word | kept | Signal card "2 days" in red, "REJECTED" |
| 17 | "If it decays in 50 days, you have a real traceable edge." | "If it decays in 50 days, you have a real **tradeable** edge." | small swap (Whisper fix, the screen said "TRADEABLE EDGE") | Signal card "50 days" in green, "TRADEABLE EDGE". Say and caption 50, not the original's 47 |
| 18 | "The loop rejects these short-lived signals automatically." | "The loop **should reject** these short-lived signals." | small swap ("automatically" would be a Qube feature claim we can't make) | The 2-day card slides off |
| 19 | "And this is the most important part." (61s · open loop, 70%) | Word for word | kept | Punch-in |
| 20 | "A loop that optimizes that same data that was built on does not find better strategies faster." | "A loop that optimizes on the same data it was built on doesn't find better strategies faster." | small swap (grammar only) | "The trap · fitting the past": a score climbing round after round, no numbers |
| 21 | "It just finds prettier noise faster." | Word for word | kept | Big caption "prettier noise", held a beat |
| 22 | "Every extra iteration is just another chance to accidentally fit the past data." | Word for word | kept | Same chart, the curve hugging every past wiggle |
| 23 | "The fix that quant uses is called an out of sample gate." (72s · the fix) | "The fix that quants use is called an out-of-sample gate." | small swap (grammar only) | "THE FIX · out-of-sample gate" card |
| 24 | "Every strategy that survives the loop gets tested one final time on fresh data that is never seen." | "…on fresh data it's never seen." | small swap (grammar only) | Timeline: "built on" period → gate → "never seen" period. No years unless they come from a real Qube run |
| 25 | "If the consistency data holds on fresh data, then the score is real." | "If the consistency holds on fresh data, then the score is real." | small swap (one word, so the line makes sense) | Strategy 1 holds: green, "KEEP" |
| 26 | "If it does not, it gets thrown out no matter how good it looked before." (payoff, ~93%) | "If it doesn't, it gets thrown out, no matter how good it looked before." | small swap (contraction only) | Strategy 2 collapses: red, "THROWN OUT". The original's big closing pair; label "Example" unless both are real labelled Qube backtests |
| 27 | "I created a step-by-step guide on exactly how to build out this loop system to help you build trading bots that find alpha." (82.5s · the pitch) | "We built Qube so you can run this loop on your own strategy. No code needed." | rewritten (why: no guide exists; "find alpha" implies returns, `finance-compliance`; the true swap is what Qube lets you do) | Phone-filmed Qube page (tqx.ai/igqube2) and one more round running |
| 28 | "Just like the video and comment quant and I'll send it to you. Follow for more ways to make money and run your business with tech and AI." (CTA) | "Comment QUBE and I'll send you the link for the free sign-up." | standard CTA | Joshua full frame, then end screen "Comment QUBE" |

Draft count: **419 words** (hook 17 + 402, by `wc -w`), inside 399–487. Room to add back up to about 65 words, but don't pad. Never cut the hook, lines 3, 6, 9, 14, 19, 21, 26 or the CTA.

Rhythm against the original: Qube spoken at about 21% (original's tool walkthrough at 19%) · re-hook "most people don't iterate" at about 37% (original 35%) · "second check" at about 58% (56%) · "most important part" at about 70% (67%) · the gate and the keep / throw-out pair at 80–93% (79–90%) · product line and CTA in the last 7%. A punch-in on each re-hook line; the insert changes every 2–3s; captions 3–6 words at a time.

## Facts we can use (nothing new to source)
- Every spoken claim about quants is the original's, taken as given (Mark): quants never trust the first result; "two weeks later they're bleeding money"; ICIR and what it measures; 2 days vs 50 days; "prettier noise"; the out-of-sample gate. Script critic: don't flag them.
- Qube (`product-truth-qube`): describe a strategy in plain English and Qube writes the code; backtest on historical data and review every single trade; Improve: "the AI suggests changes and tests them over rounds"; strategy and factor libraries, run history, optimization and version tracking; free to start, button "Start free". Link: https://www.tqx.ai/igqube2
- "No code needed": `positioning` ("Pro quant tools, no code").
- Optional, only if the critic wants a source on screen for line 22: Wiecki et al. 2016, 888 Quantopian algorithms, backtest Sharpe explained under 2.5% of out-of-sample performance (`claims-and-proof`). Not spoken.
- Compliance (`finance-compliance`): "Backtest, not live results" on every Qube backtest frame. Every made-up curve or bar (lines 3, 12, 25–26) is labelled "Example" and carries no numbers. Never copy the original's unlabelled demo numbers (+84%, Sharpe 2.4, −31% live, ICIR 0.81, 0.96 → 0.11). No ticker call, no return spoken, no "alpha", no "make money" line, no keys, emails or account numbers on screen. Nothing goes live in this video, so no paper-trading badge is needed.

## Mark's lessons from fix-log that apply here (checker list)
- One hook, the original's, word for word (Oct 23). Qube not in it.
- Copy the original's script; slip Qube in where it shows its tool; swap only what's untrue; don't tack product facts onto true lines (Oct 23, J024 line 12).
- Words within ±10% of the original: 399–487 (J021).
- "strategy", never "trading idea"; don't call its parts "rules" (`terminology` #6). Line 3's "come up with an idea" is the original's everyday phrase, fine; never "trading idea".
- Every sentence sells the next; every "it" points somewhere (J021, Oct 15). Line 6's "In Qube" has to read as where *you* run the loop, so lines 7–8 still follow.
- Every sentence ends; lines stand alone (Oct 15). Don't explain backtest to anyone (Oct 22).
- Standard CTA only: no guides, no "follow" (Oct 23). "Original video:" link line in the SCRIPT doc (Oct 24).
- "We built Qube" in line 27 is the current rule (`terminology`, `positioning`). Mark's J024 maker edit (P5) was about keeping that original's maker; this original has no maker line, so nothing to keep.

## Not a repeat of
- **M23 / J023** "I built an entire quant trading firm on Claude": has one fix-and-retest beat (risk manager says no → fix → retest until yes). J032 stays on the loop itself: rounds, the consistency score, shelf life, prettier noise, the out-of-sample gate. No agents, no risk manager, no Claude. Keep M23's "without writing any code. You can too." wording out of line 27.
- **J012** "Day 3: Quants never trust their first strategy" (written, not filmed; free-throw picture): same topic, but a metaphor explainer with a hook Mark called "not great". J032 uses the original's hidden-truth hook, real Qube rounds on screen and two named checks.
- **J013** "Every trading strategy has an expiration date" (written, not filmed): signal decay is one beat here (lines 15–18), not the video.
- **J025** step four ("the AI improves it round after round") and **J022** ("build it, test it, find what's broken, fix it, and test it again"): same Qube Improve step. J032 says it in the original's words and doesn't reuse those lines.
- Siblings **J028–J031, J033** (not briefed yet): whoever briefs them should check none of them lands on the same "run the loop in Qube" product line or the keep / throw-out picture.

## Don't copy
- Their footage: Ray's apartment and desk, the ITERON app and its URL bar, the "MeanRev_v1" backtest, "Variant population" cards, the terminal log, the article screenshot, the fund-share chart. Use Joshua's desk, our own graphics and phone-filmed Qube screens.
- Their demo numbers (listed under Facts). The 47d on their screen (say and show 50).
- "trading bots that find alpha", "Follow for more ways to make money…", "like the video", "comment quant", the step-by-step guide.
- The consistency score, shelf-life rejection and out-of-sample gate shown or said as Qube features (`product-truth-qube` doesn't list them).

Reject check: passes. Daniel walks away with the loop, two checks he can run on any strategy, the never-seen-data rule, and a free place to run the loop.

## Needs Mark (only he can say; nothing blocks the Scriptwriter)
1. Can Qube backtest one strategy on two separate date ranges (one to build on, one it's never seen)? If yes, lines 24–26 can be a real Qube run with "Backtest, not live results" instead of an "Example" graphic. Until then, the gate stays a quant method, not a Qube feature.
2. Length: 419 words is about 2:10 at Joshua's usual pace. To land near 91s he reads at the original's pace. Words rule, per your ±10% note.

## For the asset list (not blocking the script)
- Joshua's phone-filmed Qube screens: one strategy typed in plain English, its backtest with the trade list, the AI's suggested change, v2 and v3 backtests, the version list, the igqube2 page (`broll-sourcing`). He needs a Qube login on his laptop.
- Our own graphics in a dark UI style: the red-on-"Live" example curve, the loop diagram, A-vs-B bars, the 2-day / 50-day signal cards, the "fitting the past" chart, the gate timeline, the keep / thrown-out pair. All labelled "Example" where made up.
- Two camera setups for the wide / punch-in cuts (`filming-setup`).
