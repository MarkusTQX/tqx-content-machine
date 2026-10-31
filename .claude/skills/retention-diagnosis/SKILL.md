---
name: retention-diagnosis
description: How to read the Instagram "How long people watched your reel" graph for a TQX video, split it into zones (hook, setup, middle, payoff, CTA), match every drop to the exact script line and what was on screen, name the cause from a drop-shape table, and write the fix with the skill it belongs to - with M02 and M05 worked through as examples. Use when Mark sends retention screenshots, when the Retention analyst reviews a posted video, or when deciding which part of a script to fix.
---

# Retention diagnosis

Metricool only gives average retention and the 3-second view rate (`metrics-definitions`). The drop-off curve comes from the Instagram app: Mark screenshots **Reel insights → Overview → "How long people watched your reel"** for each post. Screenshots are saved in `content-machine/data/retention/{code}_retention_{date}.jpg`.

## These are not the benchmark

M02 and M05 below are worked examples of **how to read a graph**, not what good looks like. They're our best videos so far, and they're weak (Mark, Oct 23). The point of this skill is to make every new video beat them. Never write "this is fine because M05 did the same": compare against the outside gold (`gold-standard-scripts`) for what a strong video does, and against our own last 10 (`content-scorecard`) to check we're improving. We can't see other creators' retention curves, so don't invent a "good" percentage; use the direction (better than our last ones) until real data from a strong video of ours exists.

## What you need

1. The retention screenshot. Best: a few extra screenshots with a finger held on the curve at 0:03, at the end of the setup and at the payoff, so the app shows the exact % (like M05's "53% · 0:03").
2. The video's timestamped transcript (`tools/study-video.sh` on the posted Reel; own videos are in `knowledge/own-videos/{code}/`).
3. The frames (`contact.jpg`) to see what was on screen at each drop.

## Reading the graph

- X axis: 0:00 to the video's length. Y axis: % of viewers still watching (100% at the start).
- Without tooltips, read values off the gridlines (100%, 50%, 0). Say they're estimates, ±5 points.
- "Top sources of views": when the Reels tab is 80%+ (M02 84.8%, M05 80.0%), almost everyone is a stranger seeing us for the first time. The hook is doing all the work.
- One graph is one data point. Change a skill only when the same cause shows up on 5 videos (`skill-updating`).

## The zones

| Zone | Time | What it tests | Skill |
|---|---|---|---|
| Hook | 0–3s | Did the first sentence and first frame stop the scroll? Matches Metricool's 3-second view rate. | `hook-writing` |
| Setup | 3s → the first real piece of value | Did we get to something worth staying for fast enough? | `story-structures`, `retention-writing` #2 |
| Middle | First value → payoff | Did the loops, numbers and re-hook hold people? | `retention-writing` |
| Payoff | The line that pays the hook | Did the promise land? | `script-logic` #1 |
| End | Payoff → end | Normal drop at the CTA; a big drop before the payoff is a problem | `cta-and-offer` |

## Drop shapes and what they usually mean

| Shape | Likely cause | Fix with |
|---|---|---|
| Cliff in 0–3s (more than half gone) | Hook unclear or slow, first frame shows nothing, hook too long | `hook-writing` (one sentence, done by 5s, proof in frame 1) |
| Steep slide from 3s to 20s | Setup before value: definitions, credibility, repeating the hook | Start answering in line 2; move definitions to where they're needed |
| Sudden cliff mid-video | A confusing line, an unexplained term, a dead visual, a topic switch | `spoken-sentence-rules`, `terminology`, `storyboarding` |
| Slow steady slide through the middle | No open loop, no re-hook, items with no proof | `retention-writing` #1, #3, #4 |
| Drop right when the product appears | The product came before the viewer cared, or it sounded like an ad | `cta-and-offer`, `positioning` |
| Drop in the last 5–10s | Normal: the CTA | Nothing, unless it starts before the payoff |
| A bump up | People rewound to rewatch that moment | Note the line: it's working. Do more of it. |
| Flat middle | Whoever stayed, stayed | Holds better than the rest of our curve, but at 25–30% it's still low. The fix is earlier in the video. |

## The report (one per video)

```
RETENTION: [code · title] · [length]s · read on [date] · Reels tab [x]% of views
Hook zone: [% left at 0:03] (Metricool 3-sec view rate: [x]%)

| Window | % lost | What was said | On screen | Cause | Fix | Skill |
|---|---|---|---|---|---|---|

Biggest single loss: [window and line]
One fix for the next script: [one line]
```

Save it to `content-machine/data/retention/{code}.md`. The Skill updater counts causes across reports.

## Worked example 1 · M02 "You lost to your own index fund" (90s, read Oct 23)

Readings are estimates off the gridlines.

| Window | Left | % lost | What was said | Cause | Fix | Skill |
|---|---|---|---|---|---|---|
| 0–5s | 100% → about 50% | about 50 | "Everyone says just buy the S&P 500. In 2024, the average investor didn't even come close to it." (one 8-second sentence) | Hook runs 8s and carries two ideas | One sentence, done by 5s: "In 2024, the average investor made 16.5%. The S&P 500 made 25%." | `hook-writing` |
| 5–27s | about 50% → 30% | about 20 | "...and here's why. 'Just buy the S&P 500 and you'll make what the market makes.' You've heard this a thousand times. The S&P 500 is 500 of the biggest companies..." | Repeats the hook, then a definition, before the promised numbers (they arrive at 27–36s) | Put the numbers in line 2; define the S&P 500 in a few words inside that line | `retention-writing` #2, `script-logic` #8 |
| 27–80s | about 30% → 15% | about 15 | DALBAR, the bus picture, the fix | Slow slide; no re-hook, no open loop after the numbers | A re-hook at about 60s: "And the people who lost the most did one thing." | `retention-writing` #3 |
| 80–90s | about 15% → 3% | about 12 | The CTA | Normal | | |

**Biggest loss:** 0–5s. **One fix:** say the two numbers inside the first 5 seconds.

## Worked example 2 · M05 "Quant trading tools, ranked S to F" (83s, read Oct 23)

| Window | Left | % lost | What was said | Cause | Fix | Skill |
|---|---|---|---|---|---|---|
| 0–3s | 100% → **53%** (tooltip) | 47 | "I ranked 6 tools for building a trading strategy, from S to F, so you don't have to." | Hook is good but runs 5.7s; frame 1 shows small tool logos, nothing ranked yet | Show ChatGPT already sitting in F tier in frame 1; tighten to under 5s | `hook-writing` (proof in frame 1) |
| 3–13s | 53% → about 35% | about 18 | "Quant trading just means trading with rules and data instead of your gut. And yes, I am biased because we built one." | 7 seconds of setup before the first tool (at 12.9s) | Go straight to F tier; move the bias line to the Qube reveal ("And yes, I'm biased, we built it.") | `retention-writing` #2, #8 |
| 13–64s | about 35% → 25% | about 10 | F → A tier, "Notice the pattern?" | The flattest part of our curve: the numbered tiers and the re-hook held the people who were left. Still only a quarter of viewers. | Keep the list format; fix the first 13s so more people reach it | `retention-writing` #3, #4 |
| 64–83s | about 25% → 8% | about 17 | Qube reveal, "The hard part should be the idea...", CTA | Payoff + CTA; normal end drop | | |

**Biggest loss after the hook:** the 7-second setup. **One fix:** first item by 5 seconds.

## What these two already show (2 videos, not a rule yet)

- Both lose about half the audience by 3–5 seconds, and another 15–20 points before the first real value.
- Once people reach the first real value, the curve goes almost flat until the end.
- So the biggest wins are in the first 15 seconds: a shorter hook with proof in frame 1, and **no setup lines before the first item**. Re-check this after 5 videos (`skill-updating`).
