SCRIPT: M14 · Grok might have just killed day trading forever (the claim vs the test)
VERDICT: Send back to Scriptwriter (3 line fixes + 3 doc fixes; everything else is clean)
Reviewer: REDPEN (script critic) · Oct 28 · round 1

Vs the original (@ashtonv.ai, DeRXZptsGOC): hook 9 · engine 8 · energy 8 · reward 9 · CTA 8 · Qube 9 · language 8 · copy 9 · **overall 8.5/10**

- **Hook:** the original's, word for word ("Grok might have just killed day trading forever."). Line 1 doesn't repeat it.
- **Engine:** claim → social proof → turn → numbered roles 1–4 → re-hook → twist → payoff → keyword CTA, in the original's order. The money counters and the 24/7 bonus are cut on purpose. Weak spot: the re-hook (line 8) lands at 42% of the runtime. The original's lands at 60%, and nothing pulls the viewer back at 60–75% before the result (fix 3).
- **Copy check:** I laid every body line over the original's line at the same beat and none reads as their sentence. Line 5 ("the news bot finds the headline behind it") is the closest, but the frame and words are new. It passes.
- **Length:** the original is 212 words (54.9s). ±10% would be 191–233 words, which is 64–78s at Mark's 3.0 words a second, so the 60s cap wins (`script-logic` #10). Ours is 165 (13A) / 162 (13B) words, about 55s / 54s. After the fixes below it's 168 / 165, about 56s / 55s. Under the cap.

Checker:
- On the real file: "Spoken words: 149 … No flags." **That 149 is wrong.** `tools/check-script.py` only reads lines that start `N. ` (regex `(\d+)\.\s+`), so it skips `13A.` / `13B.` completely: it neither counts nor checks them. I ran it on two split copies (13A only, 13B only): 165 words / 55s, no flags, and 162 words / 54s, no flags. Decision: no script flags. Tool gap goes to whoever maintains `tools/`: A/B line labels need parsing (this hits M15 and M16 too).

| Line | Problem | Rule (skill) | Fix |
|---|---|---|---|
| 7 | "And four, the skeptic tries to shoot it down." doesn't follow the pattern of 4–6 (number, the role, one verb, the object). It adds "And" and a "tries to" helper verb. Mark, Oct 28 (J029): "Exact same logic for all of the entries." | List entries use one pattern (`fix-log` Oct 28, J029) | **"Four, the skeptic picks it apart."** (6 words, fresh: the original's verb was "argue against"). EDIT row 7: cursor click on "apart", not "down". |
| 9 | Line 3 opens the loop "one job's missing" at about 10s. Line 9 pays it off about 16s later but never says that *this* is the missing job, so the viewer has to make the link alone. The "?" slot from line 3 (A3 row) also never comes back on screen. | Every sentence sells the next; close every loop you open (`script-logic` #3b, `retention-writing`) | **"The missing job? Not one bot checks if that trade ever worked before."** EDIT row 9 / A5: start from the A3 row with the grey "?" slot, flip the slot's label to `Tests on past prices` with a red ✗, then the six ✗s. EDIT row 10: on "Qube", the "?" slot fills with the Qube mark (visual payoff of the loop). |
| 12 | No second hook at 60–75% (33–41s). Line 8's pull-back is at 42%, and from 29s to 41.7s it's straight demo into the result. | Second hook at 60–75% (`script-logic` #11, `script-qa-checklist` Pass 2) | **"Qube tested it on years of real Tesla prices. Did the bots get it right?"** It lands at about 38–42s (70–76%) and works for both 13A and 13B. "Years of prices" is approved wording (`product-truth-qube`), and it stops the line from repeating M15 l4 / M16 l6 ("…up to five years of real price data") word for word. EDIT row 12: update the spoken text. The test dates stay on screen. |
| 13B | "And six bots would've argued their way right into it." says for certain what someone else's bots would have done. Our chat is a made-up EXAMPLE. 13A is honest as written: backtest labeled, losses said out loud, "simulation account with fake money" said out loud, badge on. | Honest claims about other products; both branches honest (`finance-compliance`, `claims-and-proof`) | **"It lost money. And six bots could've argued their way right into it."** (one word) |
| Hook (EDIT row 0, A1 step 5) | The on-screen title "Grok just killed day trading?" is M15's spoken first sentence plus a "?". If the two get posted close together, the first frame reads like the same video. | No repeats across our videos (`script-qa-checklist` Pass 1) | Title: **"Did 6 Grok bots kill day trading?"** ("day trading" in gold). It ties to "six" in line 1 and is clearly M14's own. |
| beatmap l28 | "after his A5 run in Qube". A5 is the "0 of 6" card. The Qube run is A6–A8. | Docs consistent | "after his A6–A8 run in Qube". |
| SCRIPT l5–6, beatmap l5/l26, EDIT times | Word counts and timings change with the fixes. | Docs consistent | SCRIPT header and beatmap: **168 (13A) / 165 (13B)**, about 56s / 55s. Re-time EDIT from line 7 on (line 7 −1.0s, line 9 +1.0s, line 12 +1.0s). The end screen still gets its full 2s. |

**Checked and clean**
- Mark's voice: "Sounds careful, right? Here's what scares me." is his set-up-then-turn move (`tqx-voice`) and raises the stakes without naming what's coming (`retention-writing` #3). "Six bots can argue all day. The test shows you what happened." is his two-beat closer, with no "not X, it's Y". Every line passes the LA-speech read. There's no "trading idea" or "test your own idea" anywhere.
- The roles (lines 4–6) follow one pattern. Line 7 is fixed above.
- Compliance: "all self-reported" said out loud, with the SELF-REPORTED stamp and no dollar figures. Mark never speaks a number; the result goes on screen from his own result screen. "Backtest, not live results" sits on every backtest, trade-list and result frame, with dates, trade count and worst drop. Tesla appears only as a typed "Example strategy" inside a labeled backtest, so it isn't a ticker call. 13A's paper step is said out loud with the badge (A9), in the right order: rules → backtest → paper. No banned phrases. No 24/7 or "without lifting a finger".
- CTA: standard, the last line.
- Docs: the EDIT times add up to 55.0s for 13A. The TSLA 4.6% / +6% / −3% numbers match across the chat mock, line 11 and the A6 check. The A6 → A8 shoot order decides line 13 before the talking takes. The brief's "BTC chart stays in the mock" note is replaced by the EDIT/ASSETS rule "TSLA only, no crypto". That's stricter and fine; no change needed.

**Repeats checked**
- **M15:** both open on "Grok… killed day trading", but they're different videos. M15 is a montage of the whole "AI killed X" genre, then Claude builds an S&P 500 strategy end to end and says "Not even close." M14 takes one viral six-bot setup apart role by role and tests the chart bot's kind of trade on Tesla. No body line is shared once fix 3 lands. The shared theme (test before money) is the TQX difference, not a repeat.
- **M13** (S-to-F app ranking) and **M16** (Claude vs Codex): no shared idea, payoff or line. M16 l6's "five years of real … prices" is cleared by fix 3.
- **J020–J033:** J028 has one Grok line (C tier); a different video. J020/J024 share only the approved Qube wording. J022/J025 share only the approved "simulation account" step. **M23/J023** (6-agent quant firm with a risk manager): different. M14 builds nothing, and its twist is what's missing, not the agent that says no. Roles stay at one line each, as the brief asked.

Facts checked:
- Hook and every original line → `knowledge/reference/DeRXZptsGOC/transcript.txt` (212 words, 54.9s per the srt).
- "Up to five years" / "years of prices", "simulation account" → `product-truth-qube` (l40, l45).
- "Thousands" → the original's claim, said as self-reported (not fact-checked, Mark Oct 23).
- The 4% / 6% / 3% rule → Mark's typed example (A6), no outside source needed.
- The result → Mark's own screen (A8), never spoken.

Mark's own lines flagged, not changed: none.
**Only Mark can decide:** how far apart M14 and M15 get posted. Both open on the same claim. The first frames now differ (stamp on a falling chart, and a new title after the hook-title fix), but posting them back to back is his call.
