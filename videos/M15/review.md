SCRIPT: M15 · Everybody says AI killed trading. Nobody shows proof. (Mark)
VERDICT: Send back to Scriptwriter (one round: 3 line fixes + 4 asset/doc fixes; 1 flag for Mark)
Score: 7.5 / 10

No original Reel (Mark's own concept), so it's scored against the gold named in the brief (#4 @copyandrea, #5/#6 @svermm/@markvictorn, #10 @erickjablonski).

Vs the gold: hook 8 · engine 9 · energy 8 · reward 8 · CTA 8 · Qube 9 · language 8 · copy/repeats 6 (line 5)

What works: the three-claim stack, then a dead stop on Mark's "Everybody says this. Nobody shows proof. I'm gonna change that.", is a strong open. The first frame is already stamped, and all three claims land inside 5s. Each beat sells the next one: prompt → build → run → reveal → "the part nobody on your feed shows you" → losses → answers the hook → why → CTA. Both result versions are honest. "Beat holding" (A) only goes in after A9 checks the same dates and the same $10,000. "Backtest, not live results", Qube's period and its trade count stay on screen from 24.3s. The worst drop is shown in A and in B. Losses are shown in A too, and the claim cards carry no numbers.

Checker:
- Version A: 148 spoken words (hook 15 + script 133), about 49s, no flags.
- Version B (lines 6B/8B swapped in): 149 words, about 50s, no flags.
- Both are inside 35–60s and the brief's 130–150. After the fixes below: A 148, B 149.

| Line | Problem | Rule (skill) | Fix |
|---|---|---|---|
| 5 | "I'm scared to look" repeats J033 line 6 ("Okay, it's done. I'm scared to look."), which is itself the @copyandrea line (brief gold #4). It's a repeat of a past video and a creator's sentence. | No repeats with past videos (Mark Oct 27–28); copy check (script-critic) | "I hit run. No clue how this ends." (8 words, -1). Keep the hand-over-eyes shot. |
| 10 | "before risking a single dollar" repeats J020's hook and J027 line 5 ("before you risk a single dollar"). "Risking" also reads written. "In minutes" isn't in `product-truth-qube`. | No repeats; `spoken-sentence-rules`; `claims-and-proof` | "But now anyone can build a strategy and test it before their money's on the line." (16 words, +1). Keep "in minutes" only if Mark's own run shows it, e.g. "test it in minutes, before…". |
| 8B | "its" has no clear owner after "every losing trade". "That's the proof those claims skip" repeats line 7's point one line later and sounds written. | `spoken-sentence-rules`; `script-logic` #3b | "Here's every trade it lost. And here's its worst drop." (10 words, -3). |
| 9 (A only, optional) | After "It even beat just holding the S&P 500", "Not even close" overshoots. The drop in line 8A carries it, so it's not a blocker. | `script-logic` | Optional 9A: "So did AI just kill trading? Nope." Keep "Not even close" for B. |
| Asset A9 | Pick rule hole: "below $10,000 = B". If Claude's strategy lost money but holding lost more, 6B ("did worse than just… holding") is false. A tie isn't covered either. | `finance-compliance` (no false performance claim) | "A8 final value above A9 = A. Below A9 = B. Equal, or anything else: stop and send Mark both screenshots." |
| Asset A10 | 8A says "here, here, and here", which needs at least three losing trades. Zero losing trades breaks 8A completely. | `claims-and-proof` | Add: "Fewer than three losing trades: tell INK the count and 8A says 'here' that many times. None: send Mark the screenshot before filming." |
| Asset A7 | "(or let Claude run it)" contradicts line 5's "I hit run". | Docs consistency | "Mark clicks Run in Qube himself." |
| Docs | Brief says the hook is 14 words; it's 15. The beat map says "played straight and loud", but EDIT says "Mark in mock-hype". Card timing differs: the brief says 1–1.5s per card over about 6s, EDIT says 1.6s over 5.0s. EDIT's label window ends at "37.3s" but the row ends at 37.0. | Docs consistency | Brief → "15 words". EDIT rhythm → "Mark sells each claim dead serious, like a hype ad, no wink" (a wink kills the stop). Brief → "1.6s per card, 0–5s". EDIT labels → "24.3s to 37.0s". |

Facts checked:
- "connecting Qube to Claude" → `product-truth-qube` l.49
- "up to five years of real price data" → `product-truth-qube` l.40/45
- "Backtest, not live results" + period + trade count → `finance-compliance` Always #1
- Losses shown → `finance-compliance` Always #3
- "Beat holding" → A8 vs A9, same dates and the same $10,000
- Result numbers come from Mark's run only (A8–A11, no reruns)

Repeats checked (J020–J033, M13, M14, M16, all script versions):
- Repeats found: line 5 (J033) and line 10 (J020, J027). Fixes are above.
- Line 2 ("I start by connecting Qube to Claude", J020/J023) and line 4 ("up to five years of real price data", J020/J024/M14/M16) are the mandated product-truth wording, so they stay.
- Optional for line 4, since three Mark videos in this batch say it: the allowed short form "Qube tests it on years of real prices".
- No other overlaps. M16 (Claude vs Codex) and M14 (six Grok bots) are different concepts.

Mark's own lines flagged, not changed:
- The hook's first claim, "Grok just killed day trading.", sits beside M14's hook, "Grok might have just killed day trading forever.". Both are Mark videos in the same batch.
- Option for Mark: open on "Claude just killed finance." and swap Grok for "Codex just killed Wall Street.". The full stack becomes "Claude just killed finance. ChatGPT just killed the financial advisor. Codex just killed Wall Street." (15 words, same length).
- Or keep it, with the different first frames already planned.
- Line 1 is untouched.
