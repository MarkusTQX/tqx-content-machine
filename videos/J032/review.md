SCRIPT: J032 · The 5 most powerful Claude connectors (for trading, Qube is #3)
VERDICT: Ready for Director (round 3, final). Every fix from my round 2 and from the Director's approval.md (1–5) landed. Nothing in the spoken script broke. No line repeats J020–J033 or M05, and every claim checks out. Two small doc fixes are left that don't change any spoken word. The Director can make them at approval (below).

Vs the original: hook 9 · engine 9 · energy 8 · reward 8 · CTA 8 · Qube 8 · language 8 · copy vs original 9 · batch repeats 9 · word count PASS (180, −1.6%) · flow 8 · **overall 8.4 / 10**

## Checker

```
python3 tools/check-script.py videos/J032/J032-1-SCRIPT.md
Spoken words: 180 (top hook 8 + script 172) · presenter: joshua · about 56s at 3.2 words/s
No flags.
```
Decision: no flags. That's 180 against 183, inside 165–201. The EDIT ends at 58.7s, so it's inside Mark's 50–60s.

## Did everything land?

| Fix | Now | Landed? |
|---|---|---|
| Round 2: #5 needs a connector job | l15 "And with Google Calendar connected, Claude lists every earnings date coming up." EDIT 51.5–55.0 has the A9 read-back clip, tagged "Google Calendar connector · read-only" | Yes. True: the connector reads your calendar (`claims-and-proof`, claude.com docs) |
| Director 1: l8 echoed J027 l5 and the J020 hook ("before you risk a single dollar") | "Tell Claude what you'd buy and when, and Qube tests it on years of prices, trade by trade." | Yes. "Before you risk…" is gone. "Trade by trade" leads straight into l9 ("Even the losing trades show up…") |
| Director 2: l2 "has no clue" isn't true (web search) | "Claude can search the web, but it's got no real market data feed." | Yes. True, and it says what's missing. Frank's "just Google it" is answered before he can type it |
| Director 3: l15 "earnings week" didn't match the 3-month read-back | "…lists every earnings date coming up." | Yes. It matches A9 step 14 ("next three months"), and the EDIT holds on "coming up" |
| Director 4: l9 vs A7 "even if it's worse" | A7 has a new CHECK: if the optimized version doesn't beat the first one on the flagged weakness, stop and tell Mark, and don't rerun | Yes. Line and screen can't contradict each other now |
| Director 5: A0 "lines 1–17", brief "live" for Alpha Vantage | A0 "lines 1–16". Brief #1 row is "stock market data" | Yes, both |
| Trim to under 60s | "Claude can keep your trading journal for you." and "Every company on your watchlist has a day it reports earnings." are cut. By-hand line rewritten: "Typing every earnings date on your watchlist into your calendar takes forever." | Yes. Flow still holds (below) |

## Batch-repeat check (J020–J033 scripts, posted transcripts, M05)

I grepped all 13 other scripts (J020–J031, J033) and every `knowledge/own-videos` transcript for each J032 phrase: search the web, data feed, trade by trade, losing trades, weak spots, neutral, my team, what you'd buy, log that, try next, takes forever, one prompt, calendar, coming up, same deal, side by side, trending, connect it, last earnings, earnings date, risk a.

- **No repeats**, except "years of prices" in l8. That's Mark's locked wording (`product-truth-qube`), also in J022, J025, J026, J028 and J030. Kept on purpose: the line around it is fresh.
- Closest echo, and it passes: J025 l7 "Three, it tests your strategy on years of prices. And it shows you every single trade…". J032 also puts Qube at "Three", but l7 is the bias line and l8 opens on "Tell Claude what you'd buy and when". The sentence is different, the frame is different and the word "every" isn't there.
- The "biased / built / ours" line, "type your strategy" and the J031 l7 chain are all still gone.

## Copy check vs the original

The hook is word for word (transcript.srt 0–3.08s). No body line lays over David's sentence at its beat. The new l2 vs "This gives Claude access to the most powerful research engine on the planet.": different frame and job (what's missing, not what's added). The new l13 vs "So instead of wasting your time installing apps one by one…": different. Pass.

## Read-aloud (Joshua, LA test) and flow

- Every line passes. Strongest: "Same deal, but for crypto." · "My team makes it, so I'm not exactly neutral." · "Now it's one prompt." · "Typing every earnings date on your watchlist into your calendar takes forever."
- Flow: hook → One, Alpha Vantage → web search but no data feed (so what fixes it?) → connect it, ask, get price, earnings, news → Two, CoinGecko → same for crypto → prices, volume, trending, three coins → Three, Qube, bias owned → tell Claude, Qube tests it trade by trade → even the losers, then the weak spots fixed → Four, Notion → "log that test" (the Qube test we just saw) → Five, Google Calendar → by hand takes forever → one prompt, one file → the connector lists them back → CTA. Every line sells the next.
- Second hook: the #4 and #5 punch-ins and the stopwatch carry it, same as the original. Accepted.

Optional polish, writer's or Director's call (not required):

| Line | Note | Option |
|---|---|---|
| 2 | "it's got no real market data feed" is fine, but "data feed" is a little techy for Priya | "Claude can search the web, but it doesn't have real market data." (12 words, −1) |
| 13–15 | "every earnings date" (l13), "every date" (l14), "every earnings date" (l15): three "every"s in three lines | l15: "And with Google Calendar connected, you can just ask Claude what's coming up." (13 words, +1, still true; the screen shows the list) |

## Doc fixes (no spoken change; the Director can apply them at approval)

| Doc | Fix |
|---|---|
| EDIT 3.9–7.7, Movement column | "Hard cut on "On"" → **"Hard cut on "Claude""** (l2 no longer starts with "On") |
| Beatmap, "Every sentence sells the next" | The end still says "Claude knows your earnings week" → **"Claude lists every earnings date coming up"** |

## Facts checked

- Hook → transcript.srt line 1, word for word.
- l2: Claude has web search but no market data feed. True. ASSETS turns web search off, so the demo answers come from the connectors.
- Alpha Vantage: in Claude's directory; GLOBAL_QUOTE, EARNINGS, EARNINGS_CALENDAR, NEWS_SENTIMENT; 25 free requests a day, so a two-day shoot; "live" never said (`claims-and-proof` row 80; github.com/alphavantage/alpha_vantage_mcp, alphavantage.co/support). l3 and l14 are true.
- CoinGecko: keyless server, live prices, volume, market cap, trending (row 81). l6 is true.
- Qube: years of prices, every trade, weak spots fixed through optimisation (`product-truth-qube`). Backtest label and test period on every Qube frame. A7 CHECK guards l9.
- Notion: creates and updates pages (row 82). l11 is true.
- Google Calendar: read-only (row 83). l14 makes no write claim, and l15 uses only the read job. True.
- Compliance: neutral prompts, example tags, bias owned, no keys or emails on screen, losses shown, no live trading, standard CTA. Clean.

Mark's own lines flagged, not changed: none.
