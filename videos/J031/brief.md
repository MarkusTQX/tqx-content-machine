# J031 · Let's turn this research paper into a trading strategy (Claude + Qube)
Presenter: Joshua (calm explainer who shows the screen, about 3.2 words a second, demos are his strongest mode; one slang word at most, `tqx-voice`) · Persona: Marcus, the quant competitor · Why they care: he reads papers and knows what a backtest and Sharpe are, but turning a paper into tested code costs him a weekend. Here a famous paper goes from PDF to a labelled backtest, every trade shown, with the weaknesses listed. Don't explain basics to him.
Source: `knowledge/cards/reference/2026-05-12_julias.algos_research-paper-to-strategy-with-codex.md` (Mark's pick, recreate; batch of 6 Joshua videos J028–J033; Mark's direction Oct 27: "Let's turn this research paper into a trading strategy" with Claude + Qube, a real tool demo). Transcript: `knowledge/reference/DYOCsS0tU_k/transcript.srt`, frames in `knowledge/reference/DYOCsS0tU_k/frames/`.
Original Reel link: https://www.instagram.com/p/DYOCsS0tU_k/ (@julias.algos, 152K followers, 13,045 likes, 172 comments, 46.3s, **125 words**). Put it on the "Original video:" line of the SCRIPT doc (fix-log Oct 24).

## The paper we use (real, public, buildable in Qube)

**Mebane T. Faber, "A Quantitative Approach to Tactical Asset Allocation", The Journal of Wealth Management, Spring 2007** (free working paper on SSRN: https://ssrn.com/abstract=962461).

Why this one:
- **Public:** free PDF on SSRN, so Joshua can download it and drop it into Claude on camera. (First pick was Brock, Lakonishok & LeBaron 1992, "Simple Technical Trading Rules...", but it's behind JSTOR, so it's out.)
- **Qube can build and test it:** the method is one moving-average rule: buy when the monthly price is above its 10-month simple moving average; sell and go to cash when it's below; check once a month, at the last close. Moving-average strategies on US stocks are Qube's own templates (`product-truth-qube`), so the build and backtest are things Qube really does.
- **Honest weaknesses to end on**, the way the original does: a monthly signal gives few trades in up to five years; sideways markets cause whipsaws; the paper tested a different period and five asset classes, and we test US stocks only.

On screen at about 1.6s, as the original: the paper's real first page pinned top, with **the paper's own title and author** readable ("A Quantitative Approach to Tactical Asset Allocation" · "Mebane T. Faber"), and the journal name if it's on the page Joshua downloads. **No number from the paper is said or shown** (none of its returns, Sharpe or drawdown figures). Only our own labelled backtest.

## The original's engine to keep

Beats in order: hook names the hard thing and a known tool in one sentence, with the paper on screen by 1.6s → "that's me" pain, the old way (4.9s: "hours of reading, decoding equations..."), seen as stock photos pinned top (someone buried in books, a multi-monitor desk) → **"Instead"** flip at 9.2s, drop the PDF in → "act like a quant researcher instead of just summarizing" (14.6s), with **the full prompt readable on screen** (about 16s, the save/screenshot moment) → it reads the method and writes the code (20.2s), real output on screen → **logo pile** of everything you'd normally stitch together (24.9–31s) → "But [tool] built the entire workflow automatically" (29.9s, re-hook) → reward at 35s: backtest, chart, **"and even flagged weaknesses"** with the "Where the strategy might fail" list on screen (37s) → teaser close "That's where things get interesting." (no CTA in the original).
Length and rhythm: 46.3s, 125 words, 2.7 words a second, average sentence 12.5 words, 28 cuts (a visual change about every 1.6s). Presenter in the bottom two-thirds, inserts pinned in the top third (paper page, stock photos, Claude/Qube windows, logo stacks). Captions 3–5 words at a time, white with dark outline, lower third.

## Outside gold to aim at
This Reel itself (`remix-for-product`, Oct 27 method: only the hook is copied word for word; every body line is written fresh in natural LA speech, keeping the original's beats, order and length). It sits in `story-structures` shape 3 as the julias.algos (Codex) example. Same creator as gold #9 (@julias.algos, the J025 source), so we already know her rhythm works for Joshua. One borrow from gold #1 (@samin_yasar12): the tool name lands on screen on the same word it's said.

Shape: **3. Problem → solution** (the original's own: pain → "Instead" → fix shown → result → close) · Target length: **125 words, range 113–137** (`script-logic` #10, ±10% = 112.5–137.5; 138 is over, critic round 2). At Joshua's 3.2 words a second that's about 40–43s (the original runs 46s because it's read slower; match the words, not the seconds).

Enemy → difference: Wall Street gatekeeping (quant research sits in dense papers that only people who can code it ever test) → **Pro quant tools, no code**. Landing: line 8 (fresh) asks the "in minutes?" question and Mark's line 9 answers it: "That's when everything changes."

## Product and placement

Product: Qube (with Claude, per Mark) · Placement: **exactly where the original uses Codex to code and test.**
- Hook: "Codex" → "Claude" (the known name stays in the hook; Qube is not in the hook, `hook-writing` #8: nobody knows Qube yet).
- Line 3, the "Instead" flip (~10s): "Instead, I connect Qube to Claude and drop in the raw PDF." The connection is said as an action Joshua does (Mark, Oct 23: "I start by connecting Qube to Claude"; never "hooked up" / "plugged in").
- Line 5: Claude reads the method (true: Claude reads the PDF), **then Qube writes the code** (true: "Qube writes the code"). Don't say or show Qube reading PDFs (lesson card).
- Line 7: "But Qube built the entire workflow automatically." (Codex → Qube).
- Line 8: Qube ran the backtest and showed every trade; **Claude** flagged the weaknesses (the "where it might fail" answer is Claude's reply).
- Qube or the Claude/Qube screen is on screen from line 3 to the end (demo exception, `cta-and-offer`). Keyword CTA is the last spoken line, added after the original's teaser close.

Qube is first said at about 10s, not inside 8s: the original names Codex in the hook at 4s and shows it from 12.4s. Ours names Claude in the hook and Qube at the same point the original's tool screen appears.

The promise (what the hook promises): we take a real quant research paper and turn it into a working, tested trading strategy with Claude, on camera.
The payoff (what they walk away with, usable today): the paper's name (one they can read tonight), the exact prompt to reuse with any paper (on screen, screenshot-able), proof it works (Qube's labelled backtest with every trade), the weaknesses Claude found, and a free tool to do the same.

CTA: **"Comment QUBE and I'll send you the link for the free sign-up."** (standard CTA, `cta-and-offer`, Mark Oct 23). The original has no spoken CTA, so it's added after "That's where things get interesting." P6 ("full breakdown") is still open; don't use it here.

## The hook (one hook, the original's, word for word except the untrue part)

**"Let's code a trading strategy based on this quantitative trading research paper using Claude."**

Only swap: "Codex" → "Claude" (Mark's direction: Claude + Qube). "Let's code" stays: Qube writes the code, so it's true. 14 words, about 4.4s (original 4.8s). On screen: caption "let's code a trading strategy", then "based on this quantitative trading research paper" with the Faber paper's first page pinned top from about 1.6s. First frame: Joshua to camera, holding a mic, plain office wall, no insert yet (as the original).

## Beat map, line by line against the original (draft lines; the Scriptwriter owns the final words and marks each in beatmap.md)

| # | Original line (job) | Ours (draft) | Mark | On screen |
|---|---|---|---|---|
| H | "Let's code a trading strategy based on this quantitative trading research paper using Codex." (hook) | "Let's code a trading strategy based on this quantitative trading research paper using Claude." | small swap (Codex → Claude) | Joshua, then the paper's first page pinned top (title + author) |
| 2 | "Usually, turning a research paper into something tradable means hours of reading, decoding equations, and manually implementing the strategy." (pain, "that's me") | Kept word for word | kept | Our own stock photos pinned top: someone reading among piles of books; a multi-monitor trading desk |
| 3 | "Instead, I drop the raw PDF directly into Codex." (the flip) | "Instead, I connect Qube to Claude and drop in the raw PDF." | small swap (Qube slipped in at the flip, as an action; Mark Oct 23 wording) | Claude window with the Faber PDF attached; "Qube" connection visible in the session |
| 4 | "I'm asking Codex to act like a quant researcher instead of just summarizing the paper." (re-hook) | "I'm asking Claude to act like a quant researcher instead of just summarizing the paper." | small swap | **The full prompt, readable** (see below), held 2–3s |
| 5 | "Codex actually reads the methodology section, then translates it into implementable code." (it works) | "Claude actually reads the methodology section, then Qube translates it into implementable code." | small swap (Claude reads, Qube writes the code) | Claude's reply quoting the rule (10-month moving average, monthly check, cash when below); then the strategy in Qube with its sections (when to buy, when to sell, how much, when to get out) |
| 6 | "Normally, this would mean stitching together signal processing libraries, reinforcement learning frameworks, and backtesting the code." (contrast) | "Normally, this would mean stitching together data libraries, charting libraries, and backtesting code." | small swap (no signal processing or RL in a moving-average paper; same three-item list) | Logo stacks, two waves as the original: Python, pandas, NumPy · then matplotlib, plotly, Backtrader |
| 7 | "But Codex built the entire workflow automatically." (re-hook, ~65%) | "But Qube built the entire workflow automatically." | small swap | Qube with the finished strategy and its code |
| 8 | "Then it ran the backtest, generated the charts, and even flagged weaknesses." (reward, ~78%) | "Then it ran the backtest, showed every trade, and Claude even flagged weaknesses." | small swap ("generated the charts" → "showed every trade", the Qube fact; the weaknesses are Claude's answer) | Qube backtest with **"Backtest, not live results"**, the period and the trade count; the trade list scrolling; then Claude's "Where the strategy might fail" answer, readable |
| 9 | "Reading quant papers is extremely useful, but having AI turn them into executable strategies in minutes?" | Kept word for word | kept | Joshua to camera; Claude/Qube window with the run time visible |
| 10 | "That's where things get interesting." (teaser close) | Kept word for word | kept | Joshua to camera |
| 11 | none (caption-only sponsor link) | "Comment QUBE and I'll send you the link for the free sign-up." | added (standard CTA) | Joshua full frame, end screen "Comment QUBE" (last 2s) |

Draft count: **138 words** (by `wc -w`), over the 137 max (critic round 2); final script is 137 after cutting "raw" and "libraries". If any swap adds a word, trim in this order: "raw" (line 3), then "Claude" in line 8 ("and even flagged weaknesses", with Claude's reply on screen). Never trim the hook, lines 2, 4, 9, 10 or the CTA.

Rhythm against the original: hook done by ~4.5s · pain line by ~10s · Qube said at ~10–11s (original's tool screen 12.4s) · prompt on screen at ~14–17s · logo pile at ~22–27s · "But Qube built..." at ~65% · weaknesses at ~78% · close and CTA in the last 6s. A visual change about every 1.5s, inserts pinned top, Joshua bottom two-thirds, like the original.

### The prompt on screen (line 4; readable, the save moment)

> Read this research paper and:
> 1. Extract the trading logic
> 2. Identify when to buy, when to sell, how much, and when to get out
> 3. Build the strategy in Qube
> 4. Backtest it on up to five years of real price data
> 5. Show me the results
> 6. Show me every single trade
> 7. Explain where the strategy might fail

Same seven-step shape as the original's prompt, with Qube's real steps and Mark's J022 list in step 2. Joshua types exactly this in the real run, so the screen and the script match.

## Facts we can use (each from a skill or the paper itself; nothing to source)

- The paper: Faber (2007), title and author as above, free on SSRN (https://ssrn.com/abstract=962461). Its rule: monthly price above the 10-month simple moving average = in; below = out, to cash; updated once a month. Only the rule is used; none of its results.
- Qube: describe a strategy in plain English (or send it from Claude), Qube writes the code, backtests it on historical data, shows the results and every single trade. "up to five years of real price data", never a fixed length. Free to start, no card. Link: https://www.tqx.ai/igqube2 (`product-truth-qube`).
- Qube connects to Claude and Codex (`product-truth-qube`). Say it as "I connect Qube to Claude" (Mark, Oct 23).
- The original's claims are kept as given (Mark, Oct 23 and Oct 27): "hours of reading", "built the entire workflow automatically", "executable strategies in minutes". Script critic: don't flag them. For "in minutes", show the real run time from Joshua's session on screen (the lesson card's honest version); no timer needed in the spoken line.
- What it's tested on: US stocks. If SPY (the S&P 500 fund) is in Qube, use it (closest to the paper's US stock test); if not, the 10 biggest US stocks (J020's set). Say neither out loud; the backtest frame shows it.
- Compliance (`finance-compliance`): every backtest frame carries "Backtest, not live results" plus the period and trade count; no return spoken; no paper numbers; no ticker call; no keys, emails or account numbers on screen (blur the Claude session sidebar). Nothing goes live in this video, so no paper-trading line or badge is needed. The weaknesses list stays on screen as Claude wrote it (losses and limits shown openly).

## Mark's lessons from fix-log that apply here (checker list)

- One hook, the original's, word for word except the untrue part (Oct 23). Qube not in the hook.
- Only the hook is copied; every body line is fresh, natural LA speech, same beats, order and length as the original (Mark, Oct 27; replaces the Oct 23 copy-line-by-line rule). Mark's own Script Room lines (1–7, 9) stand as he wrote them.
- Words within ±10% of the original: 113–137 (J021; 138 is over).
- "I connect Qube to Claude", never "hooked up" (Oct 23). "strategy", never "trading idea"; its parts aren't "rules" (J020, `terminology` #6), including on screen.
- "up to five years of real price data" (J020). Mark's J022 list in the prompt.
- Every sentence sells the next; every "it" points at Qube (J021). Line 7's "it" = Qube: Mark gives Qube the weakness check and the optimize step (Oct 27).
- Every sentence ends; lines stand alone (Oct 15). Don't explain basics like backtest (Oct 22).
- Standard CTA only (Oct 23). "Original video:" link line in the SCRIPT doc (Oct 24). TQX, if said, as "T-Q-X".

## Not a repeat of
Past videos checked (Director step 1, Oct 27): `data/video-map.csv`, every `knowledge/own-videos/*/transcript.txt`, every `videos/<CODE>/` brief and script incl. `_archive`, and `slop`, searched for "research paper", "paper", "PDF", "Faber". No overlap: no other video takes a paper or PDF as its input (closest: J022 and J021, below).
- **J022** "Claude can now build and backtest your trading idea in Qube" (Joshua): same Claude + Qube path. J031 differs: the input is a named research paper (PDF in), the prompt is the save moment, and it ends on weaknesses, not on going live. Same presenter and same tools: space them apart in posting.
- **J021** "I tested the overnight trick in Qube": also leans on research (overnight returns), but it's a shock-number video with no paper on screen and no Claude.
- **J008** "Turn your idea into rules with AI", **J016** 60-second build, **J020** "Watch Qube trade your idea 607 times": Qube build/test demos, but the idea is typed, not taken from a paper.
- **J026** "10 ways to trade with Claude": a list, not one build.
- Siblings **J028–J033** (no briefs yet besides this one): whoever briefs them should check none uses the Faber paper or a "drop the PDF into Claude" flip.

## Don't copy
- Their footage: the creator, her room, her stock photos, the Codex windows, the PPO paper and its pages, the "FSRPPO-style equity curve". Use our own stock photos, Joshua's own phone-filmed Claude and Qube screens, our own logo stacks.
- What's untrue for us: "Codex" as the tool (Mark wants Claude), "signal processing libraries, reinforcement learning frameworks" (not in this paper), "generated the charts" as a Qube feature (not in `product-truth-qube`), any claim that Qube reads PDFs.
- The unlabelled equity curve: ours always carries the label, period and trade count.
- "#ChatGPT_Partner" / sponsor framing: this is TQX's own tool. No "we're partners" line.

Reject check: passes. Marcus gets a paper to read, a prompt to reuse with any paper, a labelled test with every trade, the weaknesses, and a free tool to try tonight.

## For the asset list (not blocking the script)
- Joshua's real run, phone-filmed or screen-recorded: download the Faber PDF from SSRN → Claude with Qube connected → paste the prompt above exactly → Claude's reading of the method → the strategy in Qube → backtest with label, period and trade count → trade list → Claude's "where it might fail" answer → the run time. He needs Qube connected to Claude on his laptop (setup commands aren't documented, so no install commands on screen, `product-truth-qube`).
- Stock photos (not the original's): someone reading among piles of books; a multi-monitor trading desk.
- Logo stacks: Python, pandas, NumPy · matplotlib, plotly, Backtrader.
- Claude logo for the hook caption; Qube logo on its first mention.

## Needs Mark (only he can say; nothing blocks the Scriptwriter)
1. Paper pick: Faber (2007) is my choice (free, one rule Qube can build). Swap it if you have a paper you'd rather show.
2. Recording: is Qube connected to Claude on Joshua's laptop, and is SPY in Qube? If not SPY, the backtest uses the 10 biggest US stocks.
