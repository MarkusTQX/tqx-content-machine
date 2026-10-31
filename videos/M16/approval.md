# Approval · M16
Verdict: APPROVED for Mark (round 2 fix checked against the diff, Oct 28)

## Round 2 re-check (line 8)
| Fix | Now (diff vs *-v2-prev.md) | Landed? |
|---|---|---|
| "Codex never says when" (false, since the sentence says "sell when it recovers") | "It takes the win sooner. Codex waits for more." Only if the pick sells at a smaller gain | Yes |
| "Codex buys almost any dip" (overstated) | "It waits for a bigger drop. Codex buys smaller ones." Only if the pick buys after a bigger % fall or a lower oversold number | Yes |
| Absolute get out / how much lines | Kept, but only if the other side has no get-out at all / uses 100% of the cash | Yes |
| Degree versions for the likely case | "It gets out sooner if Apple keeps falling. Codex waits longer." (the default, since it's the likely result) and "It puts in less of the cash. Codex puts in more." | Yes |
| "Say it only if" column + A5 rule | In the SCRIPT table and the beatmap table. A5 CHECK says both halves must be true on the two screenshots, otherwise use the fallback. The fallback now also covers "you'd follow the side that waits longer" | Yes |
| Same shape, both picks, counts | All 7 rows follow "[Pick]. It [X]. [Other] [Y]." and every row is written for both a Claude pick and a Codex pick. My counts: 158 / 157 / 158 / 159 / 157 / 156 / 149. Checker: 158 words, about 53s, no flags. EDIT re-timed (line 8 36.0–41.7s, end 52.7s). Beatmap and header match | Yes |
| Extra (EDIT row 36.0s) | The punch-ins have to show the numbers that make both halves true (both stop-loss levels, both shares of cash) | Good addition |

No stale lines are left in any doc ("never says", "almost any", "real drop" only show up in the history notes). The sell row only works when both sell rules are a % gain. If one sells on an indicator instead, the fallback covers it, so nothing is left blank.

Still to do after approval: sync the Script Room (`data/script-room/M16.json` is still the v1 text). Keep the "[IF …]" labels on the alternate lines.

Score vs the gold: about 8/10. The verdict now has a reason the viewer can check on screen, every version is true, and the format is gold #1 + #4 with a scoreboard on top.

---

## Round 1 record (kept for history)
Verdict then: SEND BACK (line 8's pick versions only).

## The critic's fixes: did they land?
| Review item | Now | Landed? |
|---|---|---|
| Line 8 pick had no reason | Four reasons, one per section, in one shape "[Pick]. It [X]. [Other] [Y].", each written for a Claude pick and a Codex pick (8 versions) | Yes, but two of the reasons can't be true as written (fix 1) |
| Line 8 same-strategy "I / you" + "pay for" | "Which one should you use? Honestly, whichever one you already use." | Yes |
| Line 1 introduced Codex only | "Claude's from Anthropic, Codex is from the ChatGPT people, and I connected Qube to both." On screen "Made by Anthropic" / "Made by OpenAI", same style, A6 has both PNGs | Yes |
| Line 5 same-strategy set up an impossible contest | "Same sentence, same strategy, down to the numbers." | Yes |
| Line 6 "the backtest" | "Round two, the backtests." | Yes |
| Second hook mislabelled | Beatmap: line 8, 36.0s, about 69% | Yes |
| "Claude · Codex → Qube" on both sides | "Claude → Qube" left, "Codex → Qube" right (EDIT row, labels list, ASSETS) | Yes |
| Yellow rule said two things | Numbers and settings each AI chose only, same on both sides (EDIT header + ASSETS A5) | Yes |
| Fixed "8x" chip | Both builds fit the same 2s, "sped up" chip on both; A1/A2 "sped up to fit 2s" | Yes |
| Model not fixed | Default model, no switching, model name written down and sent with A5 | Yes |
| Nothing told Mark how to pick line 8 | A5 CHECK line 8 + A0 step 5 | Yes |
| Em dash in headers | Gone in all four docs | Yes |
| Counts and times | 157 words, about 52s; 149–159 across versions; EDIT re-timed to 52.3s | Yes |

Checker (`tools/check-script.py`): 157 words, about 52s, no flags. My count of every version: get out 157 · how much 159 · buy 158 · sell 158 · same strategy 149. All about 50–53s, inside 35–60s. I've accepted the extra words over the brief's 130–150 and updated my brief to 130–160.

## Send back: the fix
1. **Line 8 pick versions: each one has to be literally true on Mark's two screenshots, and two of them can't be.** The pick rule says "the section where they differ most is your reason" and "pick the AI whose version you'd follow". It never says the line has to be true on screen. Most versions describe the other AI in absolutes ("just holds on", "goes all in", "never says when"). But the likely result of Mark's run is a difference of degree: both have a stop-loss at different levels, or both put in part of the cash in different amounts. Then the line Mark picks would be false, and Frank would spot it on the screenshot straight away. (`finance-compliance`: describe each tool accurately; `claims-and-proof`; brief: "every version honest".)
   - **When to sell, "Codex never says when."** The typed sentence says "sell when it recovers", so both AIs will set a sell point. This version is false almost by construction. Replace it with a difference-of-degree line in the same shape, for example "It takes the win sooner. Codex waits for more."
   - **When to buy, "Codex buys almost any dip."** "Almost any" overstates something the screen shows as a number. Say a checkable difference, for example "It waits for a bigger drop. Codex buys smaller ones."
   - **When to get out / how much:** keep the absolute versions ("just holds on", "goes all in"), but only for when the other side really has no get-out or really uses all the cash. Add a degree version of each for the likely case, for example "It gets out sooner if Apple keeps falling. Codex waits longer." and "It puts in less of the cash. Codex puts in more."
   - **Add a "Say it only if your screenshots show" column** to the SCRIPT "Pick after your run" table, with one plain condition per row (e.g. "the other side has no stop-loss", "the other side uses 100% of the cash", "your pick's buy needs a bigger drop"). Add the same rule to the A5 CHECK for line 8: "Both halves of the line must be true on the two screenshots. If they aren't, use the fallback." Keep the fallback as it is.
   - Keep every version in the "[Pick]. It [X]. [Other] [Y]." shape, Claude and Codex picks both written out, and keep each one 15–19 words, so the total stays at 160 words or under (about 53s). Update the counts in SCRIPT, beatmap and EDIT row 36.0s, and the row label list ("GET OUT", "HOW MUCH", "BUY", "SELL") if a section changes.

Once that's done, M16 is APPROVED for Mark. No new critic round is needed: the Scriptwriter makes the change and I check the diff.

## Not blockers (no change needed)
- **Line 1 says the two makers in different ways** ("from Anthropic" vs "from the ChatGPT people"). Both say who makes it, and that's the same logic for both. The ChatGPT name is the one Priya knows. The screen evens it out with "Made by Anthropic" / "Made by OpenAI" in the same style. It stays.
- **Script Room** (`data/script-room/M16.json`) still has the v1 text ("I'd actually follow its strategy", line 1 without Claude). Sync it after this round, and keep the "[IF …]" labels on the alternate lines. Nothing in it has a Mark edit to protect.
- I updated my own brief: the target is now 130–160 words, the same-strategy payoff no longer says "pay for", and "rules" is now "strategy" (`terminology`), which matches the script.

## Checked and clean
- **Fair, same-pattern comparison:** Claude is always left and Codex always right. The same sentence is typed, not pasted. Each gets the same reply if it asks back, the same default model, the same dates and the same $10,000. Both show the same four sections in the same order, the same yellow rule, the same result card and the same trade scroll, and both get a maker line. In both directions, the pick shows a chip, a punch-in on the same section on both sides, then a dim. Every line 8 version names the same section for both AIs.
- **Honest everywhere but fix 1:** line 5 and line 7 are chosen by a plain screenshot check (different anywhere / word for word the same), and the mixed case (different strategies, same result) is covered. No numbers are spoken. "Backtest, not live results" shows from 28.0s through line 8, with the period and trade count on Qube's own cards and losses in red. "MARK'S PICK · My opinion" is on screen. Every reason is about how the strategy works, never the money (`positioning` never-table).
- **Product truth:** "I connected Qube to both" is the approved action wording. Qube connects to Claude and Codex from the command line. "Up to five years of real Apple prices" is Mark's J020 wording. Apple is a US stock, not crypto. No TQX OS, install commands, keys or file paths. The CTA is the standard one.
- **Repeats (M13–M15, J020–J033, own-videos, `slop`):** none. Codex only ever got a one-line "connects to Claude and Codex" before (J025, J027, J10_raw; M13 l8 now says only Claude). M15 shares the "connect Qube to Claude, it builds and tests" mechanic, but its idea is AI-hype claims vs a full test, not a head-to-head. "Fills in everything you didn't say", "before you trust the test", "down to the numbers" and "trade for trade" appear nowhere else. Line 4's four parts and "up to five years" are approved house product wording.
- **Mark's voice:** fast, short flips ("How hard? I didn't say.", "Which one would I use? Claude."), casual LA ("the ChatGPT people"). "Actually" is cut. No AI patterns. Line 10 closes line 3's loop.
- **Structure:** one persona (Priya), shape 7, one idea (same loose words, two AIs fill the gaps differently), enemy → difference ending on "test it before you risk it". The hook's promise is paid off by line 8's pick and reason. The usable habit is lines 9–10. The second hook is at about 69%.

Score vs the gold: about 8/10 once line 8 is fixed. It has #1's names in the first words with the prompt typed live, and #4's attempt, time skip and honest verdict, with a scoreboard on top. Line 8's reason is the line that makes it gold or not, which is why it has to be true on screen.
