# J031 · Beat map (Pass 0)

**Original:** @julias.algos · "Let's code a trading strategy based on this quantitative trading research paper" (Codex, sponsored) · https://www.instagram.com/p/DYOCsS0tU_k/ · 46.3s · 125 words (2.7 words a second) · 13,045 likes, 172 comments, 152K followers
**Transcript:** `knowledge/reference/DYOCsS0tU_k/transcript.srt` · **Card:** `knowledge/cards/reference/2026-05-12_julias.algos_research-paper-to-strategy-with-codex.md` · **Brief:** `videos/J031/brief.md`
**Presenter:** Joshua (about 3.2 words a second) · **Persona:** Marcus, the quant competitor who reads papers but loses a weekend turning one into tested code
**Paper:** Mebane T. Faber, "A Quantitative Approach to Tactical Asset Allocation" (2007), free on SSRN: https://ssrn.com/abstract=962461. Only its rule is used (monthly close above the 10-month simple moving average = in, below = cash). None of its numbers are said or shown.
**Method:** `remix-for-product` "The method" (Mark, Oct 23). The original transcript is the draft. Claude goes where it names Codex for reading; Qube goes where Codex writes, builds and tests. Only what's untrue for us is swapped.
**Hard cuts in the original:** 1.6, 3.9, 4.0, 4.9, 7.9, 9.0, 10.4, 12.4, 15.5, 15.5, 19.9, 20.0, 20.7, 22.5, 22.6, 25.0, 26.9, 28.5, 31.2, 32.3, 32.3, 34.9, 35.1, 36.2, 37.5, 39.2, 41.3, 44.6 (28 cuts, about one every 1.6s).

## Line by line

| Time (orig.) | Original line (exact) | Our line | kept / small swap / rewritten (why) | Our time |
|---|---|---|---|---|
| 0.0–4.8 | "Let's code a trading strategy based on this quantitative trading research paper using Codex." | Hook: "Let's code a trading strategy based on this quantitative trading research paper using Claude." | **small swap.** Codex → Claude (Mark's direction: Claude + Qube). "Let's code" stays: Qube writes the code, so it's true. Known name in the hook, Qube not (`hook-writing` #7, #8). | 0.0–4.4 |
| 4.9–12.4 | "Usually, turning a research paper into something tradable means hours of reading, decoding equations, and manually implementing the strategy." | 1. "Usually, turning a research paper into something tradable means hours of reading, decoding equations, and manually implementing the strategy." | **kept**, word for word. The "that's me" line for Marcus. 19 words, under the 20-word line. | 4.4–10.3 |
| 9.2–14.6 | "Instead, I drop the raw PDF directly into Codex." | 2. "Instead, I connect Qube to Claude and drop in the PDF." | **small swap.** Qube slipped in at the flip, said as an action Joshua does (Mark, Oct 23: "I start by connecting Qube to Claude"). "Directly into Codex" → "drop in": the PDF goes into Claude, named two words earlier. "Raw" cut (the brief's first trim) to make room for line 5. Same point as the original's tool screen (12.4s). | 10.3–14.1 |
| 14.6–19.7 | "I'm asking Codex to act like a quant researcher instead of just summarizing the paper." | 3. "I'm asking Claude to act like a quant researcher instead of just summarizing the paper." | **small swap.** Codex → Claude. The re-hook and the save moment: the full prompt readable on screen. | 14.1–18.8 |
| 20.2–24.9 | "Codex actually reads the methodology section, then translates it into implementable code." | 4. "Claude actually reads the methodology section, then Qube translates it into implementable code." | **small swap.** Claude reads (true: Claude reads the PDF), Qube writes the code (true, `product-truth-qube`). Never says or shows Qube reading a PDF. "It" = the methodology, heard in the same sentence. | 18.8–22.8 |
| 24.9–31.2 | "Normally, this would mean stitching together signal processing libraries, reinforcement learning frameworks, and backtesting the code." | 5. "Normally, this would mean stitching together data, charting tools, and backtesting frameworks." | **small swap.** No signal processing or reinforcement learning in a moving-average paper, so the list becomes the three kinds of tool a moving-average backtest really needs. Un-folded so each logo wave lands on a noun; "frameworks" kept from the original, and it ends on the heaviest item, as the original does. Still three items, still a logo pile. Round 2: "libraries" cut after "data" to bring the count inside ±10%. | 22.8–26.3 |
| 29.9–34.6 | "But Codex built the entire workflow automatically." | 6. "But Qube built the entire workflow automatically." | **small swap.** Codex → Qube. The original's claim, taken as given. Second hook at about 61%. | 26.3–28.4 |
| 35.0–39.4 | "Then it ran the backtest, generated the charts, and even flagged weaknesses." | 7. "Then it ran the backtest, showed every trade, and Claude even flagged weaknesses." | **small swap.** "It" = Qube from line 6. "Generated the charts" isn't a Qube fact → "showed every trade" (`product-truth-qube`). The weaknesses are Claude's answer to prompt step 7, so Claude is named for that part (brief; every "it" points at Qube, J021). | 28.4–32.5 |
| 39.4–44.9 | "Reading quant papers is extremely useful, but having AI turn them into executable strategies in minutes?" | 8. "Reading quant papers is extremely useful, but having AI turn them into executable strategies in minutes?" | **kept**, word for word. The original's claim, taken as given; the real run time is on screen. | 32.5–37.5 |
| 44.9–46.0 | "That's where things get interesting." | 9. "That's where things get interesting." | **kept**, word for word. | 37.5–39.1 |
| — | none (caption-only sponsor link) | 10. "Comment QUBE and I'll send you the link for the free sign-up." | **added:** the standard CTA (`cta-and-offer`, Mark Oct 23), the last spoken line. | 39.1–42.8 |

## Tally

11 spoken units (hook + 10 lines): **3 kept** (1, 8, 9) · **7 small swaps** (hook, 2, 3, 4, 5, 6, 7) · **0 rewritten** · **1 added** (CTA).

## Length

Original 125 words (46.3s). Ours 137 words (hook 14 + body 123), +9.6%, inside ±10% (112.5–137.5). About 43s at Joshua's 3.2 words a second; the original reads slower (2.7), so Joshua can take it unhurried, no rush between lines.

**Rhythm against the original:** hook done by 4.4s · pain line to 10.3s · Qube said at about 11s (original's tool screen 12.4s) · prompt readable 14–19s · logo pile 22.8–26.3s · "But Qube built..." at 26.3s (61%) · weaknesses on screen at about 31s (73%) · teaser at 37.5s · CTA in the last 4s.

## Pass 3 · side by side

| # | Ours as strong as the original? |
|---|---|
| Hook | Same words; Claude is a name the viewer knows as well as Codex. |
| 1 | Identical. |
| 2 | Adds the Qube connection as an action; one beat, same "Instead" flip. "Drop in" lands on the PDF on screen. |
| 3 | Identical apart from the name. |
| 4 | Two names in one line, but each does what's true; the screen shows Claude's reading, then Qube's strategy. |
| 5 | Same shape as the original ("...libraries, ...frameworks, and backtesting..."), same heavy word "frameworks", three logo waves each on a noun. |
| 6–7 | Same re-hook; "showed every trade" is a stronger proof for Marcus than "generated the charts". |
| 8–9 | Identical. |
| 10 | Added; standard CTA. |

Phrases a guy from LA wouldn't say: none found ("tradable", "implementable", "methodology section" are the original's own, and Marcus's words).
