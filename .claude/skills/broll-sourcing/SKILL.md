---
name: broll-sourcing
description: How to turn a locked TQX script into an asset list the creator can follow with zero questions - which Qube, GATC and terminal screens exist, how to capture each (settings, crop, what to hide), how to source stock, charts and fake screens, and how to write each step. Use when building the B-roll or asset list for any TQX video.
---

# B-roll and asset sourcing

The person reading the asset list does exactly what it says and nothing else. Mark's standard: "so precise that nobody could mess it up." If a step can be read two ways, rewrite it.

## How to write an asset row

Every row has: ID, video, script line, what it is (one plain sentence), numbered steps, deliverable file name and size, who does it, ready-by date, status.

Rules, each from a real correction:

| Bad | Why Mark rejected it | Fixed |
|---|---|---|
| "Screen recording" | Of what? Gmail? | "Screen recording of Qube in Chrome: type exactly '...' into the prompt box, wait for the rules, hold 2 seconds." |
| "Day N badge", "4 stat cards" | Vague placeholders | "A label in the top-left corner that says exactly: Day 1 / 30" and "4 numbers, one at a time: +$4,428 · 62 trades · −$2,606 · 2015–2024" |
| "Text card" | Jargon | "On-screen text: these exact words pop up..." |
| Rows out of order, other presenter's assets mixed in | Hard to work through | One presenter per list, in video order, then script-line order |
| "Use a real inbox" | Privacy, brand risk | "Build a fake inbox in Canva with these 5 rows, exactly: ..." |

- Steps are numbered: 1. Open... 2. Type exactly... 3. Export as...
- Every word that appears on screen is written out exactly, in quotes, with the same symbols.
- Every number is written out exactly. Add a CHECK step: "The result must say $10,000 → $14,428, 62 trades. If it doesn't, stop and send Mark a screenshot. Don't change any number yourself."
- Every file name is given: `{ID}_qube_full_build.mp4 · 1080×640 · 6s`.
- Reused assets say which row they come from: "Reuse J014-11."
- Anything typed on screen is typed, never pasted, so the typing shows.

## Screens that exist (capture only these)

| Screen | Where | Hide |
|---|---|---|
| tqx.ai homepage ("AI that creates, tests & trades for you all in one platform") | tqx.ai | — |
| Sign-up page (Google button, username, email, password) | tqx.ai → Log in | Any real email or password |
| Q menu → Competition → Join | TQX workspace | — |
| Simulation account creation | TQX workspace | — |
| Agent creation with two API keys | TQX workspace | Both keys, always |
| Workshop setup page | c.tqx.ai/set (confirm it's still live) | — |
| Qube: prompt box, generated rules, backtest result, trade list, templates, factor tools | Qube (login from Mark) | Account email |
| Qube public page | tqx.ai/igqube2 | — |
| Terminal with Claude Code (or Codex) connected to Qube or GATC | Presenter's laptop; Mark and the Qube team set up the connection before recording | API keys, emails, file paths with names |

Never ask for a screen that isn't in this table. If a script needs one, ask Mark whether it exists.

## Capture settings

- **Screen recordings:** OBS or QuickTime, 1920×1080, 30 fps. Browser full screen, zoom 125%, no other tabs, no bookmarks bar, notifications off.
- **Terminal recordings:** Terminal app, dark theme, font size 22, full screen. Start Claude Code by typing `claude` and pressing Enter. Type the prompt exactly as written in the asset row. Keep recording until the result is on screen; speed up waiting parts (4x) in the edit.
- **Crop:** most visuals go in the top third, 1080×640. Screen-first videos fill the 1080×1920 frame.
- **Labels on product screens:** "Backtest, not live results" on any backtest; "Claude · Codex" or "Claude · Codex → Qube" on terminal clips.

## Other sources

| Need | Source | Rules |
|---|---|---|
| Price charts | TradingView (free), dark theme, no indicators | Say the symbol, timeframe and date range exactly |
| Stock video | Pexels first (free), then Storyblocks (TQX account) | Exact search words; no brand logos, no watermarks, no faces looking into the camera |
| Graphics | Canva (free), 1080×640 | Exact text, colors and sizes; export PNG |
| Fake app screens, inboxes, DMs | Canva | Made-up names and content; never a real person's account |
| Logos of other tools | The tool's own site | Only when the script names the tool |
| Sources on screen | Small text | Author and year, e.g. "Barber & Odean, 2001" |

## Where files go

Shared Drive: "TQX Content / [month] / Assets", one subfolder per video code. File names exactly as given in the list.
