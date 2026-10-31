# J033 · Pass 0 beat map (the original, line by line)

**Original:** @copyandrea · https://www.instagram.com/p/DdCo8_CPs-a/ · 38.3s · 120 words (transcript `knowledge/reference/DdCo8_CPs-a/transcript.srt`)
**Ours:** 128 words (range 108–132) · about 40s spoken at Joshua's 3.2 words a second, plus the spinner and the silent montage, about 50s in all · Presenter: Joshua · Persona: Kai

| Time | Original line (exact) | Our line | kept / small swap / rewritten (why) |
|---|---|---|---|
| 0–6.7s | "Trading?" | "Trading?" | kept |
| 6.7–9.5s | "All right, we got 15 minutes on the timer. Let's see if I can cook." | "All right, we got 15 minutes on the timer. Let's see if I can cook." | kept (part of the hook, Mark Oct 23 and Oct 27) |
| 9.5–14.4s | (silent montage) | (silent montage) | kept |
| 14.4s | "Okay, I think I just found the cheat code." | "Okay, I think I just found the cheat code." | kept (Mark: copy it) |
| 17.3–18.9s | "if you go on this website here, you can find many millionaires" | "If you go on this website here, you can type out a strategy in plain English." | small swap: no millionaires to copy; Qube's Build step (`product-truth-qube`). "If you go on this website here, you can" kept |
| 21.8s | "click on their profile, you can see their win rate and how profitable they are" | "Click on backtest, you can see every trade and how profitable it would've been." | small swap: Qube's Test step, every trade. "Click on…, you can see… and how profitable" kept; "would've been" because it's a backtest. "It" = the strategy from the line before |
| 24.5s | "press mimic trade and invo will tell you when they open or close a trade" | "Ask the AI to improve it, and Qube will suggest changes and test them for you." | small swap: Qube's Improve step; Qube said where she says "invo" |
| 26.9s | "now I'm gonna mimic this guy's trade and then wait for an hour" | "Now I'm gonna backtest mine with 10 grand, and then wait." | small swap: his own strategy backtested, nobody's trade copied (`positioning`). "10 grand" sets up the result number (`script-logic` #4). "for an hour" cut: a backtest doesn't take an hour |
| 28.4s | "wait wait I think he's closing" | "Wait, wait, I think it's done." | small swap |
| 30.6s | "there's no way we just made 200" | "There's no way my strategy would've made over 8 grand, bro." | small swap: our real backtest, +$8,147 (`claims-and-proof`, 10 biggest US stocks); "would've made" keeps it a backtest. "bro" moved to the end of this sentence |
| 32.6s | "bro and I don't even know what candlesticks are" | "And I didn't write a single line of code." | rewritten: Joshua runs a trading platform, so "I don't know candlesticks" isn't true for him (brief, flagged to Mark). The no-code point is the true version and TQX's difference ("you bring the idea, AI builds it") |
| 34.6–38.3s | "and if you want my non-trading guru workflow just comment the word app and I'll send it below" | "Want to try it yourself? Just comment the word QUBE and I'll send you the link for the free sign-up." | small swap: standard CTA (`cta-and-offer`). "just comment the word… and I'll send" kept; "And if you want to try it yourself," became a question so the line isn't one 23-word sentence (checker flag, `spoken-sentence-rules` #9; one question, then the answer, `tqx-voice`). No "workflow": the QUBE flow sends the sign-up link only |

**Count:** hook 16 · lines 9 + 16 + 14 + 16 + 11 + 6 + 20 + 20 = 112 · total 128 (`wc -w` and `tools/check-script.py` agree). Two words cut from the brief's draft wording ("and" in "Click on backtest", "Then" before "Ask") to stay inside 132 after "my strategy" went into the result line; the CTA question saves 3 more.

**Rhythm against the original:** spinner lands ~4.5s (same) · timer 5.2s (6.7s) · silent montage to ~14.9s (14.4s) · "cheat code" ~14.9s · Qube page ~17.7s (17.3s) · 3 steps at ~19.7 / 22.7 / 27.1s (18.9 / 21.8 / 24.5s) · time skip ~35.5s (28.4s) · result inset ~37.4s (30.6s) · CTA ~43.7s (34.6s). Ours runs about 11s longer because Joshua reads slower than she does and the steps carry more words; same beats, same order.

**Every sentence sells the next:** "Trading?" (what will he do with it?) → 15 minutes, can he cook? → "cheat code" (what is it?) → the website: type a strategy → click backtest: every trade → the AI improves it → now he runs his own and waits → "Wait, wait, I think it's done" (what did it do?) → "over 8 grand" and no code (can I do that?) → comment QUBE to try it.

**One enemy, one difference:** copy-trading and gurus (the original's "copy millionaires' trades", never named) → you bring the idea, AI builds it ("I didn't write a single line of code").

**Pass 3 side by side:** each of our lines keeps the original's frame words and does the same job. Weaker than the original: "I didn't write a single line of code" is a calmer "that's me" line than "I don't even know what candlesticks are"; it stays because the original's isn't true for Joshua (Mark can have it back). Stronger than the original: the result number matches the screen, the losses are on screen, and the timer comes back at the end.
