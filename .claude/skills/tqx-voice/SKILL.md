---
name: tqx-voice
description: How TQX's two presenters actually talk on camera, from transcripts of all their posted Reels (Mark: 6, Joshua: 9, plus raw takes, Oct 2026) - the shared TQX voice, then Mark's and Joshua's own openers, moves, phrases, pace and watch-outs, with real lines, and the casual voice of the Instagram post captions. Use when writing or reviewing any line a presenter will say, so the script sounds like the person filming it. This describes voice only; the quality bar is in gold-standard-scripts.
---

# TQX voice

Built from what Mark and Joshua actually said in their posted Reels (transcribed with `tools/study-video.sh`, Oct 22 2026; transcripts in `content-machine/knowledge/own-videos/`). This file is about *how they sound*. It is not a quality bar: none of these videos has broken through yet. For what good looks like, use `gold-standard-scripts`.

Write every script for one presenter (`filming-setup`). Name them at the top of the script.

## The shared TQX voice (both presenters)

- **Talk to "you".** The presenter says "I" only for his own experience or test.
- **A real number in the first line, with who measured it.** "Two US professors looked at trading accounts from more than 35,000 households." "India's market regulators studied over 10 million people."
- **Explain a term in the same breath.** "Futures and options are contracts that let you bet big on where the price is going." No pause, no "so basically".
- **One question, then the answer.** "So who was making the money? Big foreign investors and professional trading firms."
- **End on a lesson the viewer can act on, then the CTA.** "If it can't survive that, it won't survive real life."
- **Plain American speech, contractions, no hype words.** Both presenters slip into "revolutionary" and similar when ad-libbing; cut them (`anti-ai-patterns`).

## Mark

**On camera:** picks a fight with something the viewer believes and wins it with a number. Fast, no pauses between lines.
**Pace:** about 3 words a second (measured across 6 Reels: 227–267 words in 74–90s).

**Signature moves (real lines):**

| Move | Example |
|---|---|
| Stat hook + "I'm going to tell you exactly why" | "Over 93% of Indian traders lose money, and I'm going to tell you exactly why." · "Only 1 out of 100 day traders actually make money, and I'm going to tell you exactly why." |
| Name the advice the viewer has heard | "Quit your job and start day trading for a living. I'm sure you've seen one of these videos." · "Everyone says just buy the S&P 500." |
| Flip with a short line | "You'd think more trading means more money. It meant less." · "It wasn't the fund. It was them." |
| Two-beat closer | "Same feeling, different application." · "Not a Tuesday night game." |
| "The surer you are..." chains | "The surer you are, the more you trade. And the more you trade, the more you pay." |
| The fix, stated plainly | "Here's the fix. Before every trade, write down the rules it should follow." |
| CTA with a qualifier | "If you're interested in algo trading, comment QUBE and I'll send you..." (keep the qualifier; the promise now names what they get, see `cta-and-offer`) |

**Words and phrases he uses:** "exactly", "here's the fix", "so", "say you had $10,000", "that's called...", "the results shocked everybody".
**Don't write for Mark:** long setups, soft openers, lines that explain before they provoke, analogies that run more than two lines (his best line in M03 is the chess picture in two sentences, then straight back to the numbers).

| Bad (not Mark) | Fixed (Mark) |
|---|---|
| "Today I want to talk about a really interesting study on gender and trading." | "Men trade 45% more than women, and it's costing them money." |

## Joshua

**On camera:** the calm explainer who shows you the screen. Credible, a bit of slang, likes numbered lists.
**Pace:** about 3.2 words a second (measured across 9 Reels: 129–377 words in 44–112s). Faster than people assume; time his scripts like Mark's.

**Signature moves (real lines):**

| Move | Example |
|---|---|
| "If you [do X], [warning]" opener | "If you're still asking ChatGPT what stocks to buy, you need to watch this video." · "If you trade, you need to hear this." · "If you're asking ChatGPT what stock to buy, you're cooked." |
| His own credibility | "I helped launch TikTok in Australia and New Zealand, from zero to two million daily active users. I've seen this movie before." |
| Numbered breakdowns | "One, it doesn't panic. Two, it doesn't sleep. Three, it can test thousands of strategies..." · "Here are three prompts." |
| Show the screen | "Let me show you. This is Qube, and I'm gonna type in a sentence. And here's the rules it gives me." |
| Personal detail | "For me, that's a large flat white with two extra shots." |
| Set up, then turn | "Sounds perfect, right? But here's the problem." · "So where are we?" |
| Honest closer | "I tested it on past prices, not my real money, and it didn't even cost me a thing." |

**Slang he uses naturally:** "you're cooked", "20 grand", "gonna". Fine in moderation; one per video.
**Strongest mode:** demos. His Qube walkthrough ("build your first trading system") is the most *him*: showing, typing, reacting.

**Watch-outs (seen in his posted Reels):**
- **Analogies take over.** The bus-and-red-cars backtest video spends most of its 112 seconds on the picture. Keep a picture to two or three lines, then go to the real screen or number (`slop`, `script-logic` #6).
- **Ad-libbed hooks add made-up stakes.** Raw take: "If you trade, you should screenshot this, or you might lose $10 million." Every number in a hook needs a source (`claims-and-proof`), even when he ad-libs. Give him 3 written hook options so he doesn't need to invent one.
- **The CTA keyword drifts.** He has said "comment GATC", "comment Jev", "comment TQX", "comment Q". Only QUBE has a live ManyChat flow (`cta-and-offer`). Write the exact keyword and nothing else.
- **Hype when ad-libbing.** "We're weeks away from launching something revolutionary." Cut it, and never mention unlaunched products (`product-truth-*`).

| Bad (not Joshua) | Fixed (Joshua) |
|---|---|
| "Today we'll explore why AI-driven strategies can outperform discretionary traders." | "If you trade on gut feeling, you need to hear this. AI beats you in three ways, and the last one can wipe out your account." |

## How they record

Raw takes (J10, J11) show the presenter records several hook options back to back, then the body in one take. So:
- Give every script 3 to 5 hooks, each a complete sentence that works on its own.
- Line 1 of the body must work after any of the hooks.

## Instagram post captions (not spoken)

The captions under the Reel are much more casual than the spoken script: lowercase, slang, trailing dots.

| Mark (real) | Joshua (real) |
|---|---|
| "you probs should just buy the sp500 bro damn…." | "chatGPT traders are actually cooked" |
| "only 1 in 100 day broskis make it in the long run…" | "everybody talks about backtesting but nobody explains it." |
| "ranking the best quant tools so you don't have to" | "wanna build your first ai trading system?" |

Caption rules: one line, lowercase, the hook's idea in slang, then hashtags (#quant #trading #algotrading #aitrading #tqx). Captions still follow `finance-compliance`: slang, never a promise. And the caption and the spoken hook must both say only what the source says (M06's spoken hook said "addiction" when the stat is about having a betting account; see `fix-log`).

## Checks

- [ ] One presenter named, and the lines sound like *him* (read them in his voice).
- [ ] Mark: provokes in line 1, a number by line 2, short flips, fast.
- [ ] Joshua: an "If you..." or numbered setup, shows the screen where possible, analogy kept short.
- [ ] Timing at about 3 words a second for both.
- [ ] 3 to 5 hooks that each stand alone.
- [ ] The exact CTA keyword from `cta-and-offer`.
