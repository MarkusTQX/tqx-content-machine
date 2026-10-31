# M16 · Beat map (original concept, beat by beat from the brief)

**Original video:** none, original concept (Director, Oct 28). There's no source Reel, so there's no transcript to map against. The rows below follow the Director's beat list in `videos/M16/brief.md`, and the hook is the brief's, word for word.
**Ours:** 157 words, about 52s at Mark's 3.0 words a second, inside 35–60s. The other line 8 reasons make it 158–159 (about 53s); the same-strategy lines make it 149 (about 50s). The critic's fixes (review.md, round 1) take it past the brief's 130–150; the Director accepts or trims. · Presenter: Mark · Persona: Priya, the AI-curious tinkerer
**Shape:** 7, experiment / challenge (`story-structures`): the attempt (same sentence into both) → Round 1 (the strategies) → Round 2 (the backtests) → honest verdict with one reason → the habit → CTA.
**Outside gold aimed at:** #4 @copyandrea (the attempt on screen, a time skip, the honest reaction) · #1 @samin_yasar12 (names people know in the first words, the prompt typed live). M05 is only the floor: the Round 1 / Round 2 scoreboard chip.
**v2 (Oct 28, critic round 1):** each line 8 pick now has one reason from one strategy section, all in the same shape, "[Pick]. It [X]. [Other] [doesn't].", with every version written out in full. Line 1 introduces Claude the same way it introduces Codex. Line 5's same-strategy version is "down to the numbers". Line 6 says "the backtests". Line 8's same-strategy version is "Which one should you use? Honestly, whichever one you already use." The second hook is relabelled to line 8. The EDIT and ASSETS docs carry the fixes for the labels, the yellow boxes, the fast-forward and the model.

## Outline (`script-logic`)

- **Promise (hook):** which one, Claude or Codex, builds the better trading strategy from the same sentence, judged by the same test.
- **One idea:** give two AIs the same loose sentence and each fills in what you didn't say, so read what yours wrote before you trust the test.
- **Second hook:** line 8, "Which one would I use?" (36.0s, about 69%)
- **Payoff:** line 8, Mark's pick plus one concrete reason from one strategy section (36.0–41.3s, about 69–79%), then the habit in lines 9–10 (41.3–48.3s, about 79–92%).
- **What she walks away with:** a fair head-to-head, a verdict with a reason she can see on screen, and one habit for tonight with whichever AI she already has.
- **Enemy → difference:** trusting whatever the AI wrote without reading or testing it → test it before you risk it (`positioning`).
- **CTA:** standard (`cta-and-offer`).

## Beats

| Time | Beat (what it does) | Our line |
|---|---|---|
| 0.0–4.7 | Hook: A vs B, two names Priya knows, then the fair-test promise (brief, word for word) | "Claude or Codex: which one builds the better trading strategy? Same idea, same test." |
| 4.7–9.7 | Setup: who makes each one, in the same pattern for both, and Qube connected as an action Mark did (`product-truth-qube`) | "Claude's from Anthropic, Codex is from the ChatGPT people, and I connected Qube to both." |
| 9.7–14.7 | The attempt: the exact sentence typed into both, said and shown (gold #1, prompt typed live) | "I typed this into each one. "Buy Apple when it's oversold, sell when it recovers."" |
| 14.7–18.7 | Explains the one term Priya won't know, then opens the loop: the loose part is on purpose | "Oversold means it dropped hard and fast. How hard? I didn't say." |
| 18.7–24.0 | Round 1: the strategy each one wrote, the same four sections on each side | "Round one, the strategies. When to buy, when to sell, how much, when to get out." |
| 24.0–28.0 | Content beat: same words in, different strategies out, and the yellow marks the numbers each AI chose | "Same sentence, two different strategies. Every word in yellow, I never typed." · *Or, if the same:* "Same sentence, same strategy, down to the numbers." |
| 28.0–33.3 | Round 2: both backtests, explained in the same breath for Priya, with Mark's approved wording for the data | "Round two, the backtests. Qube tests both on up to five years of real Apple prices." |
| 33.3–36.0 | The result: the gap from Round 1 changed the outcome (results on screen, labelled, losses in red) | "Those yellow words gave me two different results." · *Or, if the same:* "The test came back the same, trade for trade." |
| 36.0–41.3 | Second hook and verdict: Mark's pick as his opinion, with one reason from one strategy section, never the money (`positioning`) | "Which one would I use? Claude. It sells if Apple keeps falling. Codex just holds on." · or one of the other versions in the table below |
| 41.3–45.7 | The habit, whichever AI she picks | "Either way, read the strategy your AI wrote before you trust the test." |
| 45.7–48.3 | The reason, closing the line 3 loop ("I didn't say" → "you didn't say") | "The AI fills in everything you didn't say." |
| 48.3–52.3 | CTA (standard), end screen the last 2s | "Comment QUBE and I'll send you the link for the free sign-up." |

**Which lines Mark picks after his run:** lines 5, 7 and 8. Every version is written out in full, so nothing is left blank.

| What Mark's run shows | Line 5 | Line 7 |
|---|---|---|
| Different strategies (likely, because the sentence is loose on purpose) | "Same sentence, two different strategies. Every word in yellow, I never typed." | "Those yellow words gave me two different results." |
| The same strategy | "Same sentence, same strategy, down to the numbers." | "The test came back the same, trade for trade." |

If the strategies are different but the test result is exactly the same, use line 5 from the first row and line 7 from the second.

**Line 8: where the two strategies differ most → the reason.** Every version uses the same shape. For a Codex pick, swap the two names; all eight versions are written out in the SCRIPT doc.

| Section | Line 8 (Claude pick) | Words |
|---|---|---|
| When to get out | "Which one would I use? Claude. It sells if Apple keeps falling. Codex just holds on." | 16 |
| How much | "Which one would I use? Claude. It only puts in part of the cash. Codex goes all in." | 18 |
| When to buy | "Which one would I use? Claude. It waits for a real drop. Codex buys almost any dip." | 17 |
| When to sell | "Which one would I use? Claude. It knows when to take the win. Codex never says when." | 17 |
| Same strategy | "Which one should you use? Honestly, whichever one you already use." | 11 |

"Codex never says when." adds "when" to the critic's "Codex never says" so the sentence ends (`spoken-sentence-rules` #1).

**Count:** hook 14 · lines 15 + 15 + 12 + 16 + 12 + 16 + 8 + 16 + 13 + 8 + 12 · total 157 (about 52s). `tools/check-script.py` finds nothing to flag on all five versions (get out 157, how much 159, buy 158, sell 158, same strategy 149).

**Every sentence sells the next:** Claude or Codex, same idea, same test → who makes each one, and both connected to the same test bench → the exact sentence → what "oversold" means, and the part left loose on purpose → so what did each one build? Round 1 → same words in, two strategies out, and the yellow is the numbers each AI chose → do those choices matter? Round 2, the tests → yes, two different results → so which one would Mark use, and the one section that decided it → whichever she uses, read it first → because the AI fills in what she didn't say → the link.

**Every compared item follows the same pattern (Mark, Oct 28):** both AIs get the same treatment in every round, with Claude always on the left and Codex always on the right. Line 1 says who makes each one, in the same shape, and each gets a grey maker line on screen. In Round 1, each side shows the same four sections in the same order (buy · sell · how much · get out), and the yellow rule is the same on both sides. In Round 2, each side shows the same Qube result card, then the same every-trade scroll. Line 8's reason names one section and says what each side did in it.

## Pass 3 · self-check (no original transcript, so against the outside gold and the fix log)

| Check | Ours |
|---|---|
| Gold #1: names people know in the first words, prompt typed live | "Claude or Codex" are the first two words; line 2 is the typed sentence, on screen letter by letter on both sides |
| Gold #4: the attempt, a time skip, the honest reaction | Line 2 is the attempt; both builds are sped up to the same 2s; line 8 is Mark's pick with a reason the viewer can see; the same-strategy version is just as honest |
| Hook paid off (`script-logic` #1) | Line 8 says which one and why, from one strategy section on screen |
| LA speech (fix-log Oct 15, Oct 23) | "the ChatGPT people", "How hard? I didn't say.", "Codex just holds on.", "goes all in". No "trading idea", no "rules" for what the AI built (`terminology` #6), no "hooked up" (`product-truth-qube`: "I connected Qube to both"). "Actually" is cut from line 8 (J031) |
| 35–60s hard limit (Oct 27) | 149–159 words, about 50–53s, across every version |
| Price history (Mark, J020) | "up to five years of real Apple prices" |
| Standalone lines (`spoken-sentence-rules` #4) | Line 8 names Apple and both AIs; line 9 says "the strategy your AI wrote"; line 10 says "The AI"; the same-strategy line 8 says "you" in both the question and the answer |
| No "X makes more money" (`positioning`) | Line 7 says "two different results", with no winner by money; every line 8 reason is about how the strategy works, never about returns |
| Compliance | Apple appears only inside a labelled backtest; every result card carries "Backtest, not live results"; losses are in red as openly as wins; no numbers are spoken that aren't on Mark's screen; "pay for" is gone, so no plan claims |
| Past videos (brief + critic) | No repeat of an idea or payoff from J028, J008, J022/J030 or M13–M15. Line 4's four parts and "up to five years" are approved house product wording |
