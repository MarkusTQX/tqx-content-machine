---
name: script-logic
description: The reasoning checks a TQX script must pass as a whole - the hook's promise gets paid off, one main idea, no skipped steps, correct cause and effect, pictures that don't contradict the point, claims that match their source, and consistency across a series. Use when outlining, drafting, reviewing or approving any TQX script, especially when every line sounds fine but the script doesn't add up.
---

# Script logic

A script can sound fine line by line and still not make sense as a whole. Check the logic before polishing the words: outline first (promise, beats, payoff), then draft.

## The checks

### 1. The hook's promise gets paid off
Write down what the hook promises. Find the line that pays it off. If you can't point to it, fix the hook or the script.

| Bad | Fixed |
|---|---|
| Hook: "Watch me build a trading bot. You'll have one by the end." (The viewer won't have one.) | Hook: "Watch me build a trading bot in 60 seconds. No code." (Paid off when the timer hits zero.) |

### 2. One main idea
If the script needs a second idea to make sense, it's two videos.

| Bad | Fixed |
|---|---|
| A video on "the quant loop" that adds "steady beats spiky returns" in the middle. | Cut the second idea. Keep the loop: build, test, score, fix, repeat. |

### 3. Every line earns its place
Each line answers "so what?" or "how?" for the line before it. If a line only restates, cut it.

### 3b. Every sentence sells the next one (Mark, Oct 23)
Read the script top to bottom. Each line has to lead into the next: it answers the line before, or sets up the line after. A new idea (fees, a new number, a new stock) needs a line that brings it in. Never drop a twist into the gap after a question.

| Bad (J021 draft) | Fixed |
|---|---|
| "So what's actually going on?" → "Those tests had zero trading fees." (the question is never answered; fees come from nowhere) | "So what's actually going on?" → answer it, the way the original does ("There's two different crowds trading at two different times...") → only then any twist, with a line that leads into it |

If a recreation cuts the original's answer to its own question, the script breaks. Keep the original's answer.

### 4. No skipped steps
The viewer must be able to follow from A to B without filling a gap.

| Bad | Fixed |
|---|---|
| "$10,000" appears with no setup. | "Say I'd put in $10,000." comes first. |
| The S&P 500 is used before anyone says what it is. | "When the S&P 500, that's about 500 of the biggest US companies, drops 2% in one day..." |

### 5. Cause and effect are correct, and the order matches reality
| Bad | Fixed |
|---|---|
| Steps run paper trading → rules → backtest. | Rules → backtest → paper trading → live. Same order in every video. |
| "The researchers think all of that drop came from people copying them." | "The researchers say a lot of that drop came from people copying them." (Matches what the source measured.) |

### 6. A picture can't contradict the point
If you explain with an everyday picture, map each part once and check it holds all the way through.

| Bad | Fixed |
|---|---|
| The spam filter "learned" from old emails (that's AI), then two lines later "before, a human had to write every rule by hand". | First show people writing rules by hand ("free money" in the subject line? Spam). Then show the filter learning them on its own. |
| A menu used for "how much goes into each trade". A menu doesn't decide portions. | "That's your portion sizes." |

A picture is optional. Don't force one where a real example, a real screen or a real number says it better.

### 7. Claims say what the source said
No line can claim more than the source measured: who, where, which years. (See `claims-and-proof`.)

| Bad | Fixed |
|---|---|
| "Researchers built a trading firm where every job is done by AI." | "Researchers built a pretend trading firm where every job is done by AI." |
| "Less than 1% of day traders make money." | "In one study, fewer than 1 in 100 day traders kept making money year after year, after fees." |

### 8. Hooks make sense cold
Every hook must make sense to someone who hasn't seen the video and doesn't know our terms.

| Bad | Fixed |
|---|---|
| "Level 3 is already here." | "AI can trade your account now. Should you let it?" |
| "You're skipping step 6." | "You're probably skipping five steps before you buy a stock." |

And a hook can't be repeated word for word by the next line.

### 9. Consistency across a series
- Numbers carry across episodes and add up (Day 2's total = Day 1's total + Day 2's trades).
- References to other episodes are correct ("Tomorrow, Day 4", not "over the next 30 days" on Day 2).
- Facts and step orders match what earlier videos taught.

### 10. Length: 35–60 seconds, a hard limit (every script)
Every script, recreation or not, runs **35–60 seconds** spoken (hook + every spoken line): **Joshua about 110–190 words, Mark about 105–180**, at the measured pace in `tqx-voice`. **Aim for about 40–50 seconds.** This is a hard limit, not a preference (Mark, Oct 27, on J028 at about 81s: "We have literally gone over this saying that ideal scripts are between [35 and 60] seconds. Now we are doing more than 1 minute long videos again."). Nothing overrides it: not ±10% of the original's word count, not matching the original's length, not matching one of our own past videos.

**Recreations: ±10% of the original's word count, only inside 35–60s.** Keep our script within ±10% of the original's word count (Mark, Oct 23: "we do our best to keep the words in the same range") when that lands inside 35–60 seconds. Example: the original has 150 words, so ours is 135–165. If ±10% would go past 60s, the 60s cap wins.

**Long originals get cut (Mark, Oct 27, on J032 at 428 words against 443: "way too many words - nobody sticking around for that long").** If the original runs past 60 seconds, don't match it. Cut it to its strongest beats, aiming for about 40–50 seconds and never past 60. Keep the hook word for word and the beats you keep in the original's order. Say it in the SCRIPT header: "original 443 words (91s) · cut to strongest beats · ours 150 words (47s)".

**Short originals:** under 35s, build ours up to 35s with the original's own beats, never padding. The one exception is a short text-only format where nothing is spoken (J026: on-screen text over music, 14s like its original); it keeps the original's length.

| Bad | Fixed |
|---|---|
| J028: "original 250 words (83.7s) · ours 259 words · about 81s at Joshua's pace, matches M05" | Hook word for word + M05's strongest beats: about 130–160 words, about 40–50s at Joshua's pace. Mark asked for J028 at about 40s. |

### 10b. Videos that aren't recreations: the same hard limit
35–60 seconds, aim for about 40–50 (#10): Joshua about 110–190 words, Mark about 105–180. 14 of the 19 viral Reels Mark picked ran 35–62s; ours ran 75–112s (Mark, Oct 22). If the draft is longer, cut the weakest beat, not the payoff.

### 11. A second hook at 60–75%
Around two-thirds in, one line that pulls attention back before the payoff ("here's where it gets crazy" style, in our words, e.g. "Notice the pattern?" in M05). 9 of the 19 viral Reels had one (Mark, Oct 22).

| Bad | Fixed |
|---|---|
| The payoff just arrives after the third step. | "And this is the part nobody checks." → then the payoff. |

### 12. Region and audience fit
If the claim, feature or reference only applies to one country, say so ("in the US").

## The explain-it-to-a-friend test

Before drafting, explain the whole video to a friend in three sentences: the problem, what you show, what they walk away with. If you can't, the outline isn't ready.

## Outline template (do this before writing lines)

```
Promise (hook): [what the viewer is promised]
One idea: [one sentence]
Beats: [3–6 beats, each with what changes on screen]
Second hook (60–75%): [the line]
Payoff: [the line that delivers the promise]
Length: [words] → [seconds] (hard limit 35–60s, aim 40–50s)
What they walk away with: [usable thing / answer / result]
CTA: [from cta-and-offer]
```
