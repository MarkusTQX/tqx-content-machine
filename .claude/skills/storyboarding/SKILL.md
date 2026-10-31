---
name: storyboarding
description: How to turn a locked TQX script into a storyboard and shot list - one row per line with timing, framing, the top-third visual, on-screen text, movement and sound - using the layouts TQX already edits in (talking head with a top-third insert, and screen-first builds). Use when the Production agent or anyone plans the shots and edit for a TQX video.
---

# Storyboarding

Input: a locked script (numbered lines with cues). Output: a storyboard table the presenter can film from and the creator can edit from. Every line gets a row. Something on screen changes on every line.

This is a first version built from how TQX videos have been edited so far. Lessons from the link database (pacing, shot types, pattern breaks) get added here later.

## Timing

- Spoken pace: about 3 words a second for Mark and about 3.2 for Joshua (measured across all their posted Reels, Oct 2026; see `tqx-voice`). Mark has faster cuts and no pauses between lines.
- Estimate each line's length from its word count and write the timestamp range.
- A visual change every 2 to 3 seconds. If a line runs longer than 4 seconds, plan two visuals for it.

## The two layouts

### A. Talking head + top-third insert (default)
- Canvas 1080×1920. Presenter in the bottom two-thirds, head just below the 640px line.
- The top third (1080×640) holds the visual for that line: on-screen text, a graphic, a chart, a screen recording or a stock clip.
- Lines with no graphic get a 110% punch-in on the presenter so the frame still changes.
- Captions at chest height, 1 to 3 words at a time.

### B. Screen-first (builds and demos)
- The screen recording fills the whole 1080×1920 frame.
- Presenter in a circle, 300px wide, bottom-left (x 40, y 1540), 6px white border.
- Use it for anything where watching the product or the terminal is the point.

Pick one layout per video. Switch only if the script moves from talking to building.

## Storyboard row

| Field | What to write |
|---|---|
| Line # | Script line number (hook = line 1) |
| Time | Estimated start–end, e.g. 0:04–0:07 |
| Spoken | The line, word for word |
| A-roll | Framing (medium, close, punch-in 110%), angle (eye level), presenter action |
| Top-third / screen | The visual, named exactly as in the asset list (e.g. "J016-02 Claude → Qube recording, 0:00–0:05 of the clip") |
| On-screen text | Exact words in quotes, and the word it pops in on |
| Movement | Zoom, slide in, stamp, counter ticking, highlight. Something always moves. |
| Sound | Music level, a hit or effect on a beat, where the music peaks |

## Example rows

| Line | Time | Spoken | A-roll | Top third | On-screen text | Movement | Sound |
|---|---|---|---|---|---|---|---|
| 1 | 0:00–0:03 | "I ranked 6 tools for building a trading strategy, from S to F." | Medium, eye level, Mark leaning in | Empty tier board S A B C D F | "Quant trading tools, ranked S to F" | Board slides down | Music in |
| 3 | 0:05–0:09 | "F tier: asking ChatGPT what to buy..." | Punch-in 110% | ChatGPT logo | "F: asking ChatGPT what to buy" | Logo drops into F with a bounce | Thud effect |
| 9 | 0:30–0:35 | "S tier: Qube. You describe the idea in plain English..." | Medium | Qube logo, then 2s of Qube screen recording | "S: Qube · no code" | Logo drops into S, gold flash | Music peak |

## Rules

- Only plan shots that can be filmed with what's in `filming-setup`, and screens that exist in `broll-sourcing`.
- Every visual must match the spoken line it sits under. If the line is about fees, the screen shows fees.
- Labels from `on-screen-text` are always included (backtest, paper trading, sources).
- The last 2 seconds are the end screen with the CTA keyword.
- Timers, counters and running totals (a countdown, a P&L number) stay in the same spot for the whole video.
