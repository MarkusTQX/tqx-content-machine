# Approval · M14
Verdict: APPROVED for Mark (Oct 28, round 2): the length cuts below landed. 157 words / about 52s (13A) and 147 / about 49s (13B). Checker clean on both split copies.
Director: MAX · Oct 28 · round 1 sent back for length, round 2 approved

## Round 2 (Oct 28): approved
All 5 cuts are in the SCRIPT, EDIT, ASSETS and beatmap, word for word (previous versions are the `*-v2-prev.md` files):
- **Script:** lines 3, 9, 10, 13A and 13B as listed below.
- **SCRIPT header:** 157 / 147 words, about 52s / 49s.
- **EDIT:**
  - Re-timed from line 3 on, to 52.0s / 48.7s. End screen keeps its 2s.
  - Music cue moved to "worked".
  - 13A's A9 lands on "simulation account".
  - 13B's left-side return moved to line 14's "Six bots".
- **ASSETS:**
  - A0 aim changed to about 52s / 49s.
  - A8 step 5 has the new texts.
  - A9 carries "Simulation account · fake money" on screen.
- **beatmap:** counts, rows, side-by-side table and "Every sentence sells the next" all updated.

One leftover fixed by the Director: EDIT row 13's movement column still said "13B: the left side slides back in on 'six bots'", a phrase 13B no longer has. It now reads "hold the punch-in on the result (the left side comes back on line 14)". The second hook lands at 72% (13A) / 77% (13B). The re-hook lands at about 22s. Nothing else changed: compliance, repeats, hook and voice are as checked in round 1.

## Round 1: the 6 critic fixes, all landed
| Fix | Check |
|---|---|
| Line 7 pattern | "Four, the skeptic picks it apart." Same shape as 4–6. EDIT click on "apart" ✓ |
| Line 9 closes line 3's loop | "The missing job? …" + A5 "?" slot flips, fills with Qube on line 10 ✓ |
| Line 12 second hook | "…Did the bots get it right?" at 38–43s (68–76%) ✓ |
| 13B honest | "could've" ✓ |
| Hook title | "Did 6 Grok bots kill day trading?" in EDIT row 0 and A1 step 5 ✓ |
| Docs | beatmap "A6–A8", counts 168 / 165, EDIT re-timed to 56.0 / 55.0s, A0 "about 56s", A8 step 5 texts ✓ |

## Everything else: clean
- **Hook:** word for word vs `knowledge/reference/DeRXZptsGOC/transcript.txt` ("Grok might have just killed day trading forever.").
- **Body fresh:** every line laid over the original's line at the same beat. None copies or lightly rewords it. Beats in the original's order (claim → proof → turn → roles 1–4 → re-hook → twist → payoff → keyword).
- **Mark's voice:** "Sounds careful, right? Here's what scares me." and the two-beat closer are his moves. No "not X, it's Y".
- **Bot lines:** 4–7 all "Number, the [role] [verb] [object]" (`fix-log` Oct 28, J029).
- **Loop:** line 3 opens it, line 9 says it out loud, line 10's slot fills with Qube, 13A/13B answers line 12's question. Promise (did six bots kill day trading?) is paid off. Payoff is usable: the viewer can type the same rule and test it free.
- **Compliance:** "all self-reported" said out loud + SELF-REPORTED stamp, no dollar figures anywhere. Mark never speaks a result number. "Backtest, not live results" + dates, trades, worst drop on every Qube result frame. Tesla only as a labelled "Example strategy". No crypto in Qube. No 24/7 / hands-off. Order rules → backtest → simulation account.
- **Repeats:** M13 (S–F app ranking), M15 ("AI killed X" montage, Claude S&P 500 strategy), M16 (Claude vs Codex on Apple) share no idea, payoff or line. Only shared wording is approved product wording ("years of … prices", M13 l9 / J027 l5; "simulation account", J022). J020–J033: J028 has one Grok line (C tier), different video. M23/J023 (6-agent firm): M14 builds nothing; twist is what's missing. `data/video-map.csv` and own-video transcripts: no Grok / group-chat video. Brief's "Past videos checked" line is there and true.
- **Docs:** EDIT times add up, TSLA 4.6% / +6% / −3% match across A3, line 11 and A6.

## Round 1 send-back: length
168 / 165 words is about 56s / 55s. Under the cap, but the aim is 40–50s (`script-logic` #10) and Mark cuts long scripts. Four lines can lose words without touching the payoff, and one cut also fixes a repeat: 13B says "six bots could've argued" and line 14 says "Six bots can argue" right after it.

### Exact cuts (round 1 send-back, applied in round 2)
| # | Line | Now | Change to | Words | Why (skill) |
|---|---|---|---|---|---|
| 1 | 3 | "Each bot has a job, but one job's missing." | **"Each bot has a job, but one's missing."** | 9 → 8 | "job" twice in 9 words (`spoken-sentence-rules`). |
| 2 | 9 | "The missing job? Not one bot checks if that trade ever worked before." | **"The missing job? Checking if that trade ever worked."** | 13 → 8 | Still closes line 3's loop out loud (REDPEN fix 2 kept). The answer is said straight, and the A5 "0 of 6 bots" ✗s show none of them do it. "ever worked before" doubled up. |
| 3 | 10 | "So I typed that kind of trade into Qube." | **"So I typed it into Qube."** | 9 → 6 | "It" is line 9's trade. Line 11 says the exact rule. |
| 4 | 13A | "It made money, losses and all. Next, it runs on a simulation account with fake money." | **"It made money, losses and all. Next, it goes on a simulation account."** | 16 → 13 | Keeps Mark's J022 word "simulation account" (`terminology` #5). "Fake money" moves on screen (A9). |
| 5 | 13B | "It lost money. And six bots could've argued their way right into it." | **"It lost money."** | 13 → 3 | Line 14 ("Six bots can argue all day…") makes the bots point one beat later. "argue" twice in a row goes. Mirrors 13A's "It made money" (`script-logic` #3, every line earns its place). |

**After the cuts:** 157 words (13A) / 147 (13B), about 52s / 49s. I ran `tools/check-script.py` on split copies of both: no flags. Second hook "Did the bots get it right?" lands at 37.7s, so 72% (13A) / 77% (13B). Re-hook (line 8) lands at about 22s.

### Docs to update with the cuts
- **SCRIPT:** header words 157 / 147, length about 52s.
- **EDIT:** re-time from line 3 on.
  - Row 9: move the music cue "back in on 'before'" to "worked".
  - Row 13A: the A9 badge lands on "simulation account".
  - Row 13B: the "on 'argued their way'" left-side return moves to line 14's "Six bots".
  - End screen keeps its full 2s.
- **ASSETS:**
  - A0: change "Aim for about 56s" to about 52s.
  - A8 step 5: new 13A / 13B text.
  - A9 graphic: middle box `SIMULATION ACCOUNT · fake money`, so the term is explained on screen (`terminology` table).
- **beatmap:** count row, the line 3 / 9 / 10 / 13 rows, the side-by-side rows, and "Every sentence sells the next".

No line here is Mark's own (no Script Room edits on M14), so nothing of his is changed.

## Flags for Mark (not send-back reasons)
- **"Qube" vs "TQX.ai":** on Oct 28 Mark changed J033 l2 "called Qube" to "called TQX.ai" (and J031 "Connect TQX to Claude"). The lesson isn't written yet. M14 says "Qube" in lines 10 and 12 and in the standard CTA. I left it as is, per `fix-log`: flag it, don't hard-rail it.
- **M14 and M15** both open on "Grok… killed day trading". The first frames now differ. How far apart they get posted is Mark's call.

Score vs the gold: as strong as the original line by line, with a stronger twist (a real test with every losing trade vs a demo graphic). Softer stakes at 6–9s with no money counters. After the cuts it's tighter than the original (about 52s vs 55s), with the same beats.
