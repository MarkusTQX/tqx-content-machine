SCRIPT: J033 · Day 3 of trying random side hustles: trading
VERDICT: Send back to Scriptwriter (round 3, Oct 27 fresh-body pass). **Docs only:** 2 small fixes in the EDIT and ASSETS. Every script line passes as written, so don't touch the SCRIPT.

Vs the original: hook 9 · engine 9 · energy 9 · reward 8 · CTA 7* · Qube 9 · language 9 · copy 10 · word count PASS · flow 9 · **overall 8.8 / 10** (v3: 8.6, but v3 failed the Oct 27 copy check)

\* The CTA is under 8 only because of the fixed rule. Her "my non-trading guru workflow" names a mystery offer, and ours can only promise the sign-up link (`cta-and-offer`, Mark Oct 23). That's Mark's call and doesn't block. It's already in ASSETS "Still open".

**Mark's hook** ("Trying a new side hustle everyday until I make 100 K a month ( spins a wheel it lands on trading)" + "Trading? All right, we got 15 minutes on the timer. Let's see if I can cook."): the same as in his Script Room edit, word for word. It's his, so it isn't scored down or sent back.

## Step 0 · copy check and the LA test, line by line (our line laid over hers at the same beat)

| # | Original at this beat | Ours (now) | Copied? | Sounds like an LA guy filming himself? | Sells the next line? |
|---|---|---|---|---|---|
| 1 | "okay i think i just found the cheat code" | "Hold up. This might be the move." | No. New frame and new words | Yes. "Hold up" and "the move" are how people actually talk | Yes. What's the move? |
| 2 | "if you go on this website here you can find many millionaires" | "It's this site called Qube, and you just type your strategy in plain English, like you're texting a friend." | No. v3's "If you go on this website here" is gone | Yes. "Like you're texting a friend" is Mark's own Oct 15 phrasing (`fix-log`). 19 words, one breath at her pace | Yes. You typed it, so what does it do? |
| 3 | "click on their profile you can see their win rate and how profitable they are" | "Hit backtest, and boom, there's every single trade it would've made, wins and losses." | No. v3's "Click on…, you can see…how profitable" frame is gone | Yes | Yes. If the trades are bad, then what? |
| 4 | "press mimic trade and invo will tell you when they open or close a trade" | "And if your strategy's kinda mid, Qube's AI comes back with changes and tests those too." | No | Yes. "Kinda mid" is real LA slang (see the note under the fixes) | Yes. "Mid" sets up "Let's backtest mine": is his mid? |
| 5 | "now i'm gonna mimic this guy's trade and then wait for an hour" | "Let's backtest mine. 10 grand, five years. Go." | No. v3's "Now I'm gonna…and then wait" is gone | Yes, short and punchy | Yes. Sets up both numbers |
| 6 | "wait wait i think he's closing" | "Okay, it's done. I'm scared to look." | No. v3's "Wait, wait, I think it's done" is gone | Yes | Yes. This is the second hook (~75%): what did it do? |
| 7 | "there's no way we just made 200 bro" | "Bro, are you kidding me? My strategy would've made over 8 grand." | No. v3's "There's no way…bro" frame is gone | Yes. "Would've" keeps it a backtest | Yes. How hard was that? |
| 8 | "and i don't even know what candlesticks are" | "And that's with zero code. I literally just typed what I wanted." | No | Yes. Pays off line 2's "type…like you're texting" | Yes. "I could do that" leads into the CTA |
| 9 | "and if you want my non-trading guru workflow just comment the word app and i'll send it below" | "Wanna try it yourself? Comment QUBE and I'll send you the link for the free sign-up." | No. It's the standard CTA with a qualifier | Yes | Last spoken line ✓ |

- **Copy 10:** all 6 lines v3 had copied or lightly reworded are new. No line keeps her sentence frame. The fresh-body pass worked.
- **Language 9 (was 8):** read out loud at her pace in Joshua's voice, every line makes sense on its own, cold. No "trading idea", no "rules", no written-English phrasing. Nothing a guy in LA wouldn't say to his phone.
- **Flow 9:** a side hustle a day → the wheel says trading → 15 minutes, can he cook? → "this might be the move" → type it like a text → hit backtest, every trade → if it's mid, the AI fixes it → "let's backtest mine" → "scared to look" → over 8 grand → zero code → comment QUBE. Every question gets answered and no idea comes in without a lead-in (`script-logic` #3b).
- **Engine 9:** same beats in the same order: setup → spinner → timer → silent montage → the turn → the tool + 3 steps (Qube named in the reveal, where she shows invo) → the action → time skip → result inset + reaction → "that's me" → keyword CTA.
- **Word count PASS:** "Trading?" + the timer line 16 + body 111 = **127** against her 120 (+5.8%, range 108–132). Per line: 7 + 19 + 14 + 16 + 8 + 7 + 12 + 12 + 16 = 111 ✓. Mark's setup line adds 13 (140 spoken), and the SCRIPT header and beat map both say so.

## Checker

```
python3 tools/check-script.py videos/J033/J033-1-SCRIPT.md
Spoken words: 132 (top hook 21 + script 111) · presenter: joshua · about 41s at 3.2 words/s
No flags.
```
Decision: no flags. The checker's 132 counts the first hook paragraph with the stage cue (21), so it doesn't conflict with the 127 / 140 in the header. That's explained in the beat map.

## Fixes (docs only)

| Line | Problem | Rule (skill) | Fix |
|---|---|---|---|
| ASSETS A9 step 4 | Stale cue: "Pops in on "no way"". That line is gone, and the EDIT pops the inset on "Bro", so the editor would be looking for a word that isn't in the video | Docs must match the script (`script-qa-checklist` Pass 8, `on-screen-text`) | "4. Pops in on "Bro" (scale 80→100% in 0.15s), holds to the end of the line." |
| EDIT row 33.3–35.1 (and A8) | The card "Waiting for the backtest" holds right through "Okay, it's done.", so the screen says waiting while he says it's done. In the original, her card ("Waiting for him to close") matches her line ("wait wait, I think he's closing"). With the new line 6 they clash | On-screen text adds to the voice and doesn't contradict it (`on-screen-text`) | EDIT: put the card only on a silent 0.7s pen-tap lead-in (33.3–34.0s) and drop it on "Okay". The line moves to 34.0–35.8s, and later rows move +0.7s, or take 0.7s out of the montage to keep about 45s. A8: "tapping the yellow pen on the desk, eyes on the screen, for about 1s in silence, then says…" |

Not blocking (for the Director):
- **brief.md** draft table, rows 8 and 10, still show the old lines ("Wait, wait, I think it's done.", "…a single line of code") marked "small swap". That was the Oct 23 method. The SCRIPT, EDIT, ASSETS and beat map are what count, but the brief's table should say "superseded by the Oct 27 fresh body" so nobody copies from it.
- **approval.md** (22:04) is from before this pass, so the Director has to write it again.
- Optional polish, Scriptwriter's call: lines 3–4 put "boom" and "kinda mid" back to back, the most slang in one spot (`tqx-voice`: Joshua's slang "in moderation"). It reads fine out loud, and it's a challenge-format video like hers, so it's not a send-back. If anything goes, drop "boom" ("Hit backtest, and there's every single trade it would've made, wins and losses.").

## Passes

- **Pass 1 worth making:** pass. Persona Kai. The viewer gets a tool to try and a real labeled result. Past videos are checked in the brief (J008, J022, no spinner, timer or time skip).
- **Pass 2 logic:** pass. Promise (can he cook in 15 minutes) → payoff (over 8 grand, zero code). The second hook is line 6, at about 75%. "10 grand" comes before "8 grand". "Mine" refers to the strategy he typed in A5.
- **Pass 3 facts:** pass, all unchanged from v3.
- **Pass 4 product truth:** pass. Build: type in plain English. Test: every trade, wins and losses. Improve: the AI suggests changes and tests them (`product-truth-qube` step 3). Free sign-up. No TQX OS.
- **Pass 5 compliance:** pass. "Would've" on both result lines. "Backtest, not live results" on A6 (the run shot too), A7 and A9. The A9 second line is complete. Red losses on screen. Tickers only inside "Example strategy".
- **Pass 6 spoken lines:** pass. Every sentence ends, every line fits in one breath (19 words max), contractions throughout, one term per thing ("strategy", "backtest").
- **Pass 7 hook:** pass. Mark's hook, untouched, and line 1 doesn't repeat it.
- **Pass 8 on-screen:** 2 fixes above. Everything else matches the new lines: the EDIT spoken column and the A0 takes 6–8 are word for word the SCRIPT.
- **Pass 9 CTA:** pass. Standard CTA, last spoken line, Qube placed where she shows invo.
- **Pass 10 fix log:** pass. No "trading idea", no "rules", no "practice account", Qube not in the hook, one hook, no product facts tacked on, "Original video" line present, no placeholders, and no body line copies the original (Oct 27).

Facts checked:
- "10 grand", "five years", "over 8 grand" → `claims-and-proof` row "10 biggest US stocks…Jan 2021 – Dec 2025": $18,147 (+$8,147), 607 trades, worst drop −$3,207, hindsight note, label "Backtest, not live results". The A5 typed strategy matches that row exactly, and Jan 2021–Dec 2025 is 5 years ✓
- "type your strategy in plain English" / "every single trade…wins and losses" / "AI comes back with changes and tests those too" / "zero code" / "free sign-up" → `product-truth-qube` steps 1–3, free start
- "15 minutes", "Day 3", "100 K a month" → the original and Mark's hook (taken as given)

Mark's own lines flagged, not changed: none. His hook is kept exactly ("everyday", "100 K", the stage cue). Still open for Mark (ASSETS, not blocking): line 8 replaces the candlesticks line, the backtest is the same one as J020, the timer end shot only if it's real, and CTA strength.
