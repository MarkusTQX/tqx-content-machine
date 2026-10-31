# J027 · Pass 0 beat map (the original, line by line)

**Original:** @ai.honeycove · https://www.instagram.com/p/Dao8zl4Of3I/ · 37.8s · 133 words (transcript `knowledge/reference/Dao8zl4Of3I/transcript.srt`)
**Ours:** 144 words (range 120–146) · about 45s at Joshua's 3.2 words a second · Presenter: Joshua · Persona: Daniel

| Time | Original line (exact) | Our line | kept / small swap / rewritten (why) |
|---|---|---|---|
| 0.0–5.4 | "A Hong Kong university just open sourced an entire AI hedge fund and it runs on your laptop for free." | "A trading company just released an entire AI hedge fund, and it runs on your laptop for free." | small swap: "A Hong Kong university" → "A trading company" (TQX built it), "open sourced" → "released" (Qube isn't open source in `product-truth-qube`). Rest word for word |
| 5.4–7.5 | "It's called Vibe Trading and this is insane." | "It's called Qube. Yes, we built it, and this is insane." | small swap: name → Qube, plus "Yes, we built it" (Joshua is TQX's COO; the hook reads as outside news, so this line owns the bias, `finance-compliance` #6, M05). "and this is insane" kept |
| 7.5–11.7 | "You type what you want in plain English and a whole team of AI agents goes to work." | "You type what you want in plain English, and Qube goes to work." | small swap: "a whole team of AI agents" → "Qube" (agents aren't a Qube feature, and they're J023's video) |
| 11.7–15.7 | "One researches, one builds the strategy, one runs the backtest, another reviews the risk." | "It writes the code, runs the backtest, shows you every trade, then suggests changes and tests them again." | small swap: same one-breath list of four jobs, now Qube's own steps in reality's order (Build → Test → Improve, `product-truth-qube`). "runs the backtest" kept |
| 15.7–17.4 | "A real trading desk in your terminal." | "A real trading desk, right on your laptop." | small swap: "in your terminal" → "right on your laptop" (echoes the hook; no terminal in this video) |
| 17.4–25.9 | "It pulls live data from 18 sources across stocks, crypto and forex, and stress tests every strategy with Monte Carlo before you risk a single dollar." | "It tests every strategy on up to five years of real price data before you risk a single dollar." | small swap: 18 sources, crypto, forex and Monte Carlo aren't in `product-truth-qube`; "up to five years of real price data" is Mark's J020 wording. "every strategy" and "before you risk a single dollar" kept word for word |
| 25.9–32.1 | "And the part nobody's talking about, upload your real broker history and it tells you exactly which of your own habits are bleeding you money." | "And the part nobody's talking about? Type in how you already trade, and Qube tells you exactly which trades would've been bleeding you money." | small swap: broker-history upload isn't a Qube feature; Qube backtests what you describe and shows every trade, losses included. "And the part nobody's talking about", "tells you exactly which" and "bleeding you money" kept ("of your own habits" → "trades": after "how you already trade" they're clearly his). Split into two sentences so neither runs over 20 words (`spoken-sentence-rules` #9); the "?" is the Kronos "And the model?" move |
| 32.1–36.7 | "More than 400 pre-built quant strategies, 15,000 developers already on it." | "Ready-made strategies for US and Hong Kong stocks, and it connects to Claude and Codex." | small swap: no template count or user count we can source, so breadth instead of scale. "pre-built quant strategies" → "ready-made strategies" (`terminology`). Brief's "factor research" left out: Daniel doesn't know "factor" and there's no room to explain it (`terminology` #2); "US and Hong Kong stocks" moved here from line 5 so line 5 stays one breath |
| 36.7–37.8 | "Open source and free." | "No code, and free to start." | small swap: same 2-part close that echoes the hook's "for free"; "free to start" is the page's own claim (`product-truth-qube`) |
| none | (no CTA in the original) | "Comment QUBE and I'll send you the link for the free sign-up." | added: standard CTA (`cta-and-offer`, Mark Oct 23), straight after "free" like the Kronos gold |

**Count:** hook 18 · lines 11 + 13 + 18 + 8 + 19 + 24 + 15 + 6 + 12 = 126 · total 144 (`wc -w` and `tools/check-script.py` agree).

**Rhythm against the original (at 3.2 words a second):** name at 5.6s (original 5.4s) · line 4 re-hook at 18.8s, 42% (original 42%) · "the part nobody's talking about" at 27.2s, 60% (original 68%) · payoff, the viewer's own losing trades, 29–35s (65–77%) · lines 7–8 stack fast · CTA 1.9s after "free".

**Every sentence sells the next:** hook (big thing, free) → name + "this is insane" (why should I care?) → how it works in one line → the four jobs → "a real trading desk" (re-hook) → the safety stake "before you risk a single dollar" → "the part nobody's talking about?" (open loop) → your own losing trades (closes it) → what else is in it → "free to start" → the link.

**One enemy, one difference:** trading on gut feeling ("which of your trades would've been bleeding you money") → test it before you risk it ("before you risk a single dollar").

## Not a repeat: on-screen runs

| | J023 (six-agents firm) | J024 ($30,000 software) | J027 (this one) |
|---|---|---|---|
| Layout | Top third (1080×640) inserts over Joshua | Top third, phone-filmed screens | Split in half like honeycove: top half 1080×960 B-roll, Joshua bottom half; full-screen rounded screenshot cards on one gold background between them |
| Thread on screen | Org chart, 6 boxes lighting up; red rule cards | "$30,000 worth of software" title; ChatGPT logo; sections lighting up | Yellow highlighter swipe on the key phrase of every screenshot card |
| Where Qube is shown | Claude in the terminal driving Qube | Phone filming a laptop screen | Clean desktop screen captures of Qube in Chrome, as cards; one over-the-shoulder laptop shot for "right on your laptop" |
| Example | NVDA, typed into Claude | Plain-English buy/sell/how much/get out sentence | Tencent (0700.HK) breakout, typed into Qube itself (no Claude, no terminal) |
| Big moment | Risk manager's red "NO" | ChatGPT logo; "Completely free. No card." | Zoom into one real losing trade, boxed in yellow |
| B-roll | none (UI only) | Trading desk monitors | Glowing ticker numbers |
| Path / steps graphic | BACKTEST → SIMULATION ACCOUNT → LIVE path | none | none (nothing goes live in J027) |
