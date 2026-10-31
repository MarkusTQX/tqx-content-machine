# TQX content machine

A multi-agent system that writes, reviews and improves short-form video scripts for TQX, and gets better from the data. Owner: Mark (Head of Growth). Presenters: Mark and Joshua (COO). Editing is done by a human.

## The products (details only in the product-truth skills)
- **Qube:** build, backtest, improve and run AI trading strategies without code. Free to start, no card. Connects to Claude and Codex.
- **GATC:** the Global AI Trading Championship. Only AI agents trade. 55% return / 45% risk scoring. HK$14M prize pool. Season 1: Jul 2026 – Jun 2027.
- Never mention TQX OS.

## The standard
The bar is other creators' viral Reels that Mark picked (`gold-standard-scripts`, `knowledge/cards/reference/`). TQX's own posts are the floor we're climbing from, never the benchmark.

## Where things live
| What | Where |
|---|---|
| Skills (the knowledge) | `.claude/skills/` |
| Agents (the workers) | `.claude/agents/` |
| One folder per video: brief, outline, script, review, approval | `videos/<CODE>/` |
| Lesson cards (viral Reels), teaching cards, structure cards | `knowledge/cards/` |
| Rule ledgers and pattern summaries | `knowledge/rules/` |
| Transcripts and frames of studied videos | `knowledge/reference/`, `knowledge/hook-study/`, `knowledge/own-videos/` |
| Video code → Reel map, metric snapshots, retention reports, skill changelog | `data/` |
| Tools: study a video, check a script, progress windows | `tools/` |

## The script pipeline (run with /make-script)
Director (brief) → Scriptwriter (outline → draft → voice pass → checker) → Script critic (review) → back to the Scriptwriter until clean (max 3 rounds) → Director (approve) → Mark.

## Script Room
Every script lives in the Script Room artifact (https://claude.ai/artifact/NL5inALCXYhUiwriYGCnYy): grouped under Joshua and Mark, code at the top, three tabs per script (1 Script · 2 For the editor · 3 Asset list), every line editable. Mark's edits are logged in its `edits/<CODE>` docs; read them before any revision and log them in `fix-log`.

## Learning from Mark
At the start of every session, before any new script or revision, and whenever Mark says he saved changes: run the `learn-from-edits` skill. It pulls his Script Room edits into fix-log and has the `skill-updater` agent turn them into rules, so he never fixes the same thing twice.

## Working with Mark
- Short replies, tables when listing. Plain words.
- Ask him only what only he knows; read the skills and docs first.
- Never change Mark's own lines or decisions; flag instead.
- Files he needs go to `~/Downloads`. Long jobs get a live progress window in the Terminal panel.
- Skills change only through `skill-updating`. Log every correction he makes in `fix-log`.
- Skills cover how to write, what's true and what's allowed. Never what to make or how often to post.
