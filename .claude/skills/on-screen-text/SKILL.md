---
name: on-screen-text
description: What goes on screen versus what's spoken in a TQX video, how to write on-screen text and labels, when each piece pops in, and the house style (top third, fonts, colors, captions, badges). Use when writing the on-screen layer of a TQX script, the cues, or the editing instructions for the creator.
---

# On-screen text

The voice tells the story. The screen gives the exact proof: the precise number, the source, the key term, the label. Every spoken line gets a visual of some kind; on-screen text is one of those visuals.

## What goes on screen, what's spoken

| Spoken | On screen |
|---|---|
| Rounded, natural numbers: "about $4,400" | The exact number: "+$4,428" |
| "In one study..." | The scope and source: "Taiwan day traders, 1992–2006 · Barber, Lee, Liu & Odean" |
| The explanation of a term | The term, short: "Drawdown = biggest drop from a high" |
| A list said as sentences | The list as it builds: "1. Playbook = written rules" |
| Nothing (labels are never read out) | "Backtest, not live results" / "Paper trading · simulated results" |

Never put the whole spoken sentence on screen; captions already do that. On-screen text adds something.

| Bad (duplicates the voice) | Fixed (adds proof) |
|---|---|
| Spoken: "The men traded 45% more." · On screen: "The men traded 45% more." | On screen: "Men traded 45% more than women · 35,000+ US households, 1991–97" |

## How to write it

- **Exact words in quotes**, with the same symbols the creator must type: `"+$4,428 · 2015–2024 · 62 trades · Backtest, not live results"`.
- **Main line: 8 words or fewer.** A second, smaller line can hold the source or label.
- **Say which spoken word it pops in on**, and how long it holds: "pops in on 'drawdown', holds to the end of the line".
- Use the middle dot ( · ) to separate short parts. No em dashes.
- In the script, write cues in brackets under the spoken line:
  - `(On screen: "...")` for text.
  - `(Visual: ...)` for anything else: a screen recording, a chart, a stock clip, a graphic.

## Required labels

| When | Label | Where |
|---|---|---|
| Any backtest result | "Backtest, not live results" | On the clip, top-left |
| Any paper or simulated result | "Paper trading · simulated results" | Top-right corner, the whole video (top-left is kept for the backtest and terminal labels) |
| Any sourced number | Author and year, or the body ("SEBI", "DALBAR") | Small line under the number |
| Terminal recordings of Claude or Codex | "Claude · Codex" (or "Claude · Codex → Qube") | Top-left of the clip |

## House style (set Oct 2026; update here if the brand changes)

| Element | Spec |
|---|---|
| Canvas | 1080×1920, 9:16, 30 fps |
| Top third | The 1080×640 box above the presenter's head. Almost every visual goes here. |
| On-screen text | Inter Bold 48px, white, on a #0B0F14 box at 85% opacity, 24px padding, 16px rounded corners. Key number or word in gold #E8B04B. |
| Titles and end screens | Instrument Serif 88px, white |
| Captions | Inter Bold 58px, white, black stroke 6px, 1 to 3 words at a time, at chest height (y = 1380). CapCut preset "TQX Captions". Spell Qube, GATC and S&P 500 exactly. |
| Colors | Dark #0B0F14 · Grey (off) #2A2F37 · Light grey #9AA3AE · Gold (highlight) #E8B04B · Green (money up) #22C55E · Red (money down) #EF4444 |
| End screen | Last 2 seconds, full-screen #0B0F14, the CTA keyword centered, e.g. "Comment QUBE" |

These fonts, colors and sizes were set by Claude for the first asset sheets. If TQX has official brand fonts or colors, replace them here and everything downstream follows.
