# How quants use loop engineering to build a trading bot · @raycfu · Instagram
Link: https://www.instagram.com/p/DahCoW1Pfyo/
Posted: 2026-07-08 · Length: 91s (91.35s) · Views: not visible · Likes: 7,166 · Comments: 4,933 · Shares/Saves: not visible
Account followers: 268K · Outperformance: likes = 2.7% of followers; comments = 1.8% of followers (comments are 69% of likes, driven by the keyword CTA)
Found by: Mark · Why he flagged it: not given · Goal: recreate

## Hook (0–3s)
Spoken: "Most people don't realize that quant traders never trust a strategy the first time that it works."
On screen: "How Quants use Loop Engineering to create a trading bot" ("Quants", "Loop Engineering" and "trading bot" in yellow). Captions below: "most people don't realize that", then "the first time that it works".
First frame shows: Ray sitting at his desk in a bright apartment, wide shot, talking and gesturing with both hands. At 2s a small white line chart appears over his chest (lines labelled "Hedge funds", "Quant funds", "Asset managers", "Banks", 2010 to 2019; no source visible).
Hook type: insider + contrarian ("Most people don't realize...")

## The skeleton (the part we copy)
Insider claim ("quants never trust the first result") → the common mistake (backtest once, go live, bleed) → the method as a 5-step loop → check 1: a consistency score → check 2: signal shelf life → "most important part": the overfitting trap → the fix (out-of-sample gate) → keyword CTA for the full guide.

## Structure (by timestamp)
| Time | Beat | What's said (short) | What's on screen |
| 0–3.4s | Hook | "quant traders never trust a strategy the first time that it works" | Title card; Ray at desk; small fund-share line chart at 2s |
| 3.6–8.4s | Promise | "They run it through a loop... until they find one that sticks. Here's how to build this out." | Close-up of Ray; "ITERON · Strategy loop" app: GENERATE → BACKTEST → SCORE → READ FAILURE → REFINE, "Generation 01", score 0.31 |
| 8.4–17.3s | The mistake | "come up with an idea, backtests once... two weeks later they are bleeding money... one guess with nothing iterating on it" | "MeanRev_v1 · BTC-USD · 1h", "BACKTEST PASSED", equity curve climbs to +84%, Sharpe 2.4, max drawdown -12%, then the line turns red after a "Live" toggle. Pop-up "Live P&L diverging", +19%, -0.4, -31% |
| 17.3–32.3s | The loop | "generate a strategy, backtest it, score it against a specific metric, read why it failed, feed that information back in..." | Loop diagram again; a white document page; score "0.31"; terminal log "gen3 · diagnose failure... 3 generations complete · best ICIR 0.81"; "Variant population" cards 0.52, 0.63, 0.34, 0.54, 0.53 ("kept", "elite", "culled") |
| 32.3–35.8s | Re-hook | "The whole edge in quant trading is the iteration and most people don't iterate at all." | Close-up; a white article page with "Most people don't iterate trading" highlighted and "The "Silver Bullet" Fallacy" |
| 35.8–51s | Check 1: score | "The metric that quants use is called ICIR... how consistently your strategy performs over time" | "Scoring metric · ICIR"; Strategy A (small steady green bars) vs "Strategy B · boom / bust · big win, then gives it back"; caption in the app: "The loop optimizes toward A, consistency compounds, spikes don't" |
| 51–61.4s | Check 2: shelf life | "If the signal decays in two days, you're basically just paying fees to chase noise. If it decays in 50 days, you have a real traceable edge." | "SIGNAL" cards "2d" (red, "REJECTED") and "47d" ("TRADEABLE EDGE"); decay curve falling below a "noise floor" line, axis 0 to 40d |
| 61.4–72s | Re-hook: the trap | "And this is the most important part... It just finds prettier noise faster." | Close-up; "The trap · fitting the past" chart, score climbing 23 → 31 over rounds |
| 72–82.5s | The fix | "an out of sample gate... tested one final time on fresh data that is never seen" | "THE FIX · Test survivors on data they've never seen. An out-of-sample gate."; "Out-of-sample gate · final check", "in-sample 2021-2023 → gate → out-of-sample 2024-2025"; "carry_34d · loop survivor" 0.81 → 0.77 "VERIFIED · REAL EDGE → DEPLOY"; "momo_tuned" 0.96 → 0.11 "Δ -0.85 · it was noise all along", "COLLAPSED ON FRESH DATA · DISCARD" |
| 82.5–91.3s | CTA | "I created a step-by-step guide... comment quant and I'll send it to you. Follow for more ways to make money..." | Close-up of Ray, no insert. Captions only. |
Build-up: the hook promises a method; the mistake (8s) shows the cost of not having it. Two open loops: "Here's the second check that most people skip" (51s, paid off by 61s) and "this is the most important part" (61s, paid off by the out-of-sample gate at 72 to 82s). The full build is held back for the DM.
Re-hooks: 3.6s (cut to close-up), 13.7s ("bleeding money" + red live curve), 32.3s ("most people don't iterate at all"), 51s ("the second check that most people skip"), 61.4s ("the most important part"), 72s ("The fix...").
Reward: a clear mental model of a test loop plus two real checks (consistency over time, out-of-sample testing), delivered between 17s and 82s. Pays off the hook? Mostly yes on the "why", no on the "how" (the step-by-step build is in the DM).

## Writing style
Words per second: about 4.9 (443 words in 91s) · Average sentence length: about 17 words
Tone: calm insider, slightly urgent, teacher explaining a secret
Talks to the viewer as: "you" and "most people" (with "quants" as the in-group)
Slang and signature phrases: "Most people don't realize", "bleeding money", "prettier noise", "alpha", "edge", "Follow for more ways to make money and run your business with tech and AI."
Lines that stand out: "It just finds prettier noise faster." (65s); "A strategy that makes a little bit of money every single week completely beats out a strategy that makes a lot of money in one week and loses it all in the next." (42s); "two weeks later they are bleeding money" (12s)
(Whisper fixes from context: "wonders" = "wanders", "variance" = "variants" (screen says "Variant population"); "comment quant" is captioned "comment Quan".)

## Proof
How they make you believe it: a polished app UI ("ITERON", URL bar "iteron.research") that acts out every step, with numbers moving on screen. No real account, no source, no named study.
Exact proof shown: "MeanRev_v1" backtest +84%, Sharpe 2.4, max drawdown -12% then live -31% (9–16s); "best ICIR 0.81" (25s); "47d" vs "2d" signals (54–60s); "momo_tuned" 0.96 in-sample → 0.11 out-of-sample (79s). All look like a built demo. None is labelled as a demo, a simulation or real. The fund-share chart at 2s has no source on screen.

## Relatability, emotion and stakes
Aimed at: retail traders and AI builders who've tried a bot or a backtest. · Pain it hits: a strategy that looked great in testing and lost money live.
"That's me" moment: "Most people come up with an idea, backtests once, and then once it looks great, they go live and two weeks later they are bleeding money." (8.4–13.9s)
Main emotion: being let in on a secret (insider curiosity), plus fear of being "most people".
What's at stake for the viewer: money lost live; wasted time on a strategy that was noise.

## Product placement
Product: Ray's "step-by-step guide" (DM). The ITERON app is on screen throughout but never named out loud. · First mention or appearance: ITERON UI at 3.6s; guide at 82.5s · Share of the video it takes: the UI is on screen about 70% of the time; the guide pitch is about 10%
How it's brought in: the UI is a demo that illustrates each step; the guide is the answer at the end.
Does it feel earned? Yes. The guide is the natural next step after 80 seconds of method. The UI is never sold, so it reads as teaching.

## Comments and shares
Comment trigger: keyword CTA ("comment quant").
Share or save trigger: a method with named checks (ICIR, out-of-sample gate) that people want to keep and send to a friend who trades or builds bots.

## CTA
Exact words: "I created a step-by-step guide on exactly how to build out this loop system to help you build trading bots that find alpha. Just like the video and comment quant and I'll send it to you. Follow for more ways to make money and run your business with tech and AI."
Where: 82.5–91.3s · Type: comment keyword + like + follow
What it promises: a step-by-step guide to building the loop · Funnel after the CTA (if known): DM (contents not visible)

## The ending
Last line: "Follow for more ways to make money and run your business with tech and AI." · Ends on: CTA
Loops back to the start for a rewatch? No. The last shot is a close-up, the first is a wide shot with the title.

## Format, visuals and sound
Presenter: face, talking head · Energy: medium, steady, lots of hand gestures · Why they're believable: calm delivery, clean home office, the app UI makes it look like he built the system.
Shot type: talking head with a UI insert on top
Layout: UI insert in the top third, Ray in the bottom two-thirds, captions over his chest. Alternates between a wide shot (at the desk) and a close-up (punch-in to his face).
Cut rhythm: 22 cuts in 91s, about one every 4s; the UI insert changes more often, about every 2 to 3s.
On-screen text and graphics: dark app UI with green and red numbers, a loop diagram, bar charts, decay curves, terminal log; title card in the first 3s.
Captions: white serif, 3 to 6 words at a time, centred over his chest
Sound: voice only is audible in the transcript; any music is not detectable from the files.
Post caption: "How Quants use Loop Engineering to create a trading bot with alpha #ai #tech" · Cover/title text: "How Quants use Loop Engineering to create a trading bot"

## What the viewer gets
An explanation plus a how-to outline (generate, backtest, score, read failure, refine; then an out-of-sample gate).
Can the viewer use something from it today? Yes: "test on data the strategy has never seen" and "prefer steady over boom-and-bust" are usable right away.

## Claims made
| Claim | Source given? | Looks true? |
| "quant traders never trust a strategy the first time that it works" | No | Generalisation; reasonable as a principle but not sourced |
| "two weeks later they are bleeding money" | No | A made-up example, not labelled as one |
| "The whole edge in quant trading is the iteration" | No | Opinion stated as fact |
| "The metric that quants use is called ICIR... how consistently your strategy performs over time" | No | ICIR is a real measure (for factor signals), but "the metric quants use" overclaims, and the definition is simplified |
| "If the signal decays in two days... If it decays in 50 days, you have a real traceable edge" | No | Unsourced thresholds; on screen it's 47d, not 50 |
| Overfitting: "Every extra iteration is just another chance to accidentally fit the past data" | No | True as a general principle |
| Out-of-sample testing makes "the score real" | No | Out-of-sample testing is standard practice; "real" overclaims, it can still fail live |
| UI numbers: +84%, Sharpe 2.4, -31% live, ICIR 0.81, 0.96 → 0.11 | No | Look like demo numbers. Not labelled as demo or backtest. Flag. |
| "trading bots that find alpha" | No | Implied returns. Overclaim. |

## Why it works (observations, not guesses)
- "Most people don't realize" is the first line (0s): a known opener from the earlier batch, and it splits the viewer from "most people" at once.
- The mistake is shown, not told: the green curve turns red the moment "Live" is switched on (13–16s). That's the "that's me" moment as a picture.
- The loop is said as a rhythm, "generate, backtest, score, read why it failed, feed that back in" (17–25s), and the on-screen loop diagram lights each step.
- Two explicit open loops: "here's the second check that most people skip" (51s) and "this is the most important part" (61s). Each restarts attention 10 seconds apart.
- "It just finds prettier noise faster" (65s) is a one-line flip that's easy to quote in comments.
- The final proof is a before/after pair: "carry_34d" holds (0.81 → 0.77) and "momo_tuned" collapses (0.96 → 0.11, "it was noise all along") (75–82s). A winner and a loser side by side.
- The CTA (82.5s) offers the missing build steps right after the payoff, so the comment is the next logical move. Comments landed at 69% of likes.

## Patterns to reuse (structure only)
- Insider opener → the common mistake shown as a chart turning red → the method as a named loop → two "checks most people skip" → the trap → the fix → keyword CTA for the full guide.
- UI insert top third, talking head bottom two-thirds, punch-in close-ups on each re-hook line.
- Name each check with a label ("consistency score", "shelf life", "out-of-sample gate") so it feels like a system.
- End the teaching on a side-by-side: one that survives the test, one that collapses.

## What we can't copy, and the honest TQX version
| In the original | Why we can't | TQX version |
| "trading bots that find alpha" | Implies returns (`finance-compliance`) | "a way to test whether your idea holds up on data it's never seen" |
| "Follow for more ways to make money..." | "make money" framing; implied returns | "Follow for more ways to test your trading ideas before you risk money." |
| Unlabelled demo numbers (+84%, Sharpe 2.4, -31% live, ICIR 0.81) | Unsourced numbers; a backtest shown without a label | Real Qube backtest screens with "Backtest, not live results", the period and trade count. Or the page's sample backtest (+55.43%, 814 trades, Sharpe 1.22) with its label and "sample backtest from the page". |
| "two weeks later they are bleeding money" | Made-up example said as fact | "Say you backtest once, it looks great, and you go live. Two weeks later..." (called an example) |
| "If it decays in 50 days, you have a real traceable edge" | Unsourced threshold | Drop the number, or source it via `claims-and-proof` |
| Out-of-sample gate shown as a product feature | Qube's product-truth doesn't list an out-of-sample gate | Say Qube does what's documented: backtest, every trade shown, AI optimization over rounds. Ask Mark before showing out-of-sample testing as a Qube feature. |
| Going "live" right after one backtest, shown as the normal path | TQX order is backtest, then paper trading, then live | "Test it on past prices, then on paper. Go live only once you've seen how it behaves." |

## Recreate for TQX (one line)
Same insider talking head with a UI insert top third ("Most people backtest once. Here's the loop that catches the bad ones"), but the loop is Qube's real Build → Test → Improve rounds on a real labelled backtest, ending on a strategy that fails the test, CTA "comment QUBE"; suits Daniel (burned by a pretty backtest that lost money live), with Marcus as a second fit.
