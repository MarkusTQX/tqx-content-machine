---
name: learn-from-edits
description: Pulls every change Mark saved in the Script Room artifact, logs each one in fix-log, and runs the Skill updater to turn them into lessons and rules, so the agents stop repeating what Mark corrected. Run at the start of every TQX session, before any new script or revision, and whenever Mark says he saved changes.
---

# Learn from Mark's edits

The Script Room (https://claude.ai/artifact/NL5inALCXYhUiwriYGCnYy) logs every change Mark saves in its `edits/<CODE>` documents (what the agents wrote → what Mark changed it to).

## Steps (the producer runs these)
1. **Pull the edits:** `ArtifactData` action `list`, url above, collection `edits`, `out_dir` = `data/mark-edits/raw`.
2. **Log them:** `python3 tools/edits-to-fixlog.py data/mark-edits/raw`. New edits become rows in `fix-log` and `data/mark-edits/new-lessons.md`; already-processed ones are skipped.
3. **If there are new edits,** run the `skill-updater` agent: "Turn data/mark-edits/new-lessons.md into lessons and rules." It writes the lesson for each row and adds rules where the same kind of change has happened twice.
4. **Sync the files:** `ArtifactData` list `scripts` to `data/script-room/live`, then `python3 tools/room-to-script-doc.py <CODE> data/script-room/live/scripts/<CODE>.json` for each script Mark edited, so the SCRIPT docs on disk match his version.
5. **Keep Mark's version:** the Script Room script stays as Mark saved it. Any revision starts from it (`make-script` step 7b), and the agents regenerate their files from his text.
6. Tell Mark in one or two lines: how many changes were learned, and which new rules went in.

Mark shouldn't have to explain an edit. The change itself is the lesson.
