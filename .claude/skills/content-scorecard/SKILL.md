---
name: content-scorecard
description: How TQX decides whether a video worked - four numbers (saves + shares per 1k reach, comments per 1k reach, average watch time, 3-second hold), each compared with the account's own average of its last 10 videos, where beating the average on any one number is a win, lead numbers count first, and each result points to the skill to improve. Use when the Analytics agent scores a post, when the Director reviews results, or when the Skill updater needs to know if a change helped.
---

# Content scorecard

The goal of a TQX video is **both leads and growth, leads first** (Mark, Oct 22). Leads = people who comment QUBE or GATC and sign up. Growth = views, reach and followers.

How each number is pulled is in `metrics-definitions`. This file says what counts as a win.

## The four numbers

| Number | Metricool field | What it tells you | Type | If it's low, improve |
|---|---|---|---|---|
| Saves + shares per 1k reach | (IGRE12 + IGRE21) ÷ IGRE11 × 1,000 | Was it worth keeping or sending? | **Lead** | The payoff: give them something to use, try or compare (`script-logic`, `remix-for-product`) |
| Comments per 1k reach | IGRE07 ÷ IGRE11 × 1,000 | Did it start a conversation or get the keyword? | **Lead** | The CTA and the debate line (`cta-and-offer`) |
| Average watch time | IGRE24 | Did they stay? | Growth | Structure and pacing (`story-structures`, `retention-writing`) |
| 3-second hold | IGRE28 | Did the hook stop the scroll? | Growth | The hook (`hook-writing`) |

Views, reach and followers gained are still recorded for every video. They don't decide a win.

## What counts as a win (Mark, Oct 22)

Compare each number with the **account's own average of its last 10 videos**. Don't count the video being scored. Use organic numbers only, at the same age (48h, then 7d).

| Result | When |
|---|---|
| **Big win** | Any number is at least **2x** the average |
| **Lead win** | Beats the average on saves + shares or on comments |
| **Win** | Beats the average on any one of the four numbers |
| **No win** | Beats none |

- One number is enough for a win. Always say which number it won on.
- When listing or ranking results, lead numbers come first.
- The bar moves up on its own: as videos get better, the average of the last 10 rises.

## Rules

- **Each account gets its own average.** Mark's videos are compared with Mark's, Joshua's with Joshua's.
- **Fewer than 10 videos:** use every posted video. Fewer than 5: mark every result "early, small sample".
- **Score at 48h and again at 7d.** The 7d score is the one the Skill updater uses.
- **Average watch time favors longer videos.** Once Metricool returns the video length (IGRE26), score watch-through (watch time ÷ length) instead of raw seconds. Until then, note the video's length next to its score.
- **Never boost a video's score with paid numbers.** Boosted Reels get scored on organic numbers only.

## What a result tells you

| Pattern | What it means | Look at |
|---|---|---|
| High 3-second hold, low watch time | Good hook, then lost them | `retention-diagnosis`, `story-structures` |
| High watch time, low saves and shares | They watched, but got nothing to keep | The payoff (`script-logic` check 1, "what they walk away with") |
| High saves, low comments | Useful, but no reason to speak up | The CTA or a debate line (`cta-and-offer`) |
| Low 3-second hold, everything else high | Great video behind a weak hook | `hook-writing` |

## Score report (one per video)

```
SCORE: [code · title] · [account] · [48h / 7d]
Baseline: average of last [n] videos [· early, small sample]

| Number | This video | Average | Result |
|---|---|---|---|
| Saves + shares / 1k reach | | | |
| Comments / 1k reach | | | |
| Average watch time | [s] (video is [s] long) | | |
| 3-second hold | | | |

Verdict: Big win / Lead win / Win / No win, on [numbers]
Also: views [n] · reach [n] · followers gained [n]
What to look at: [from the pattern table]
```

## Baseline, Oct 22 2026 (markus_ai_quant, 6 videos, early, small sample)

This is the floor we're climbing from, not a standard. None of these videos performed well; "Big win" here only means better than our other videos (Mark, Oct 23). The real bar is the outside gold in `gold-standard-scripts`.

Totals pulled Oct 22. The videos are 2 to 8 days old, so they aren't the same age yet.

| Number | Average |
|---|---|
| Saves + shares per 1k reach | 17.7 |
| Comments per 1k reach | 5.4 |
| Average watch time | 13.5s |
| 3-second hold | 53.2% |

Scored against the other five videos:

| Video | Saves + shares / 1k | Comments / 1k | Watch time | 3-sec hold | Verdict |
|---|---|---|---|---|---|
| M05 Tool tier list | 76.7 (**big**) | 22.0 (**big**) | 24.5s (**big**) | 50.2% | **Big win**, on 3 numbers |
| M06 Sports betting | 13.0 | 8.7 (win) | 14.6s (win) | 65.1% (win) | **Lead win**, on comments, watch time and hook |
| M02 S&P 500 | 0 | 1.8 | 18.4s (win) | 60.8% (win) | **Win**, on watch time and hook |
| M03 India 93% | 16.4 | 0 | 11.1s | 52.0% | No win |
| M04 Day traders | 0 | 0 | 7.0s | 51.2% | No win |
| M01 Men vs women | 0 | 0 | 5.4s | 40.0% | No win |

What this already shows: M05 won on the numbers after the hook (saving, commenting, watching), not on the hook itself. M02 and M06 had the strongest hooks but gave people nothing to keep.

Replace this section with a fresh baseline once there are 10 videos, and add Joshua's account once it's connected to Metricool.
