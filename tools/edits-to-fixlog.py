"""edits-to-fixlog: turn Mark's saved Script Room edits into fix-log rows the agents learn from.

Usage: python3 tools/edits-to-fixlog.py <dir-with-edits-json>
  <dir> is where `ArtifactData list collection=edits out_dir=...` saved the docs
  (it contains edits/<CODE>.json). Only edits newer than the last run are used
  (state: data/mark-edits/processed.json).

Writes:
  data/mark-edits/<CODE>.md       every edit Mark made, readable
  data/mark-edits/new-lessons.md  just the new ones, for the Skill updater
  .claude/skills/fix-log/SKILL.md new rows under "## Mark's edits in the Script Room"
"""
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "data" / "mark-edits" / "processed.json"
FIXLOG = ROOT / ".claude" / "skills" / "fix-log" / "SKILL.md"
SECTION = "## Mark's edits in the Script Room"
PARTS = {"line": "Script line", "hook": "Hook", "edit-spoken": "Editor sheet · spoken", "edit-onscreen": "Editor sheet · on-screen text",
         "edit-visual": "Editor sheet · visual", "edit-sound": "Editor sheet · sound", "edit-time": "Editor sheet · time",
         "assets-what": "Asset · what", "assets-how": "Asset · steps", "assets-who": "Asset · who", "assets-file": "Asset · file",
         "open": "Open question", "status": "Status"}


def cell(s, n=220):
    s = " ".join(str(s or "").split()).replace("|", "/")
    return s if len(s) <= n else s[: n - 1] + "…"


def main():
    src = Path(sys.argv[1])
    files = list(src.rglob("*.json"))
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    STATE.parent.mkdir(parents=True, exist_ok=True)
    new_rows, lesson_lines = [], []
    for f in files:
        doc = json.loads(f.read_text())
        body = doc.get("data", doc)
        code = body.get("code") or f.stem
        log = sorted(body.get("log", []), key=lambda e: e.get("at", 0))
        (ROOT / "data" / "mark-edits" / f"{code}.md").write_text(
            f"# Mark's edits · {code}\n\n| When | Where | Agents wrote | Mark changed it to |\n|---|---|---|---|\n" +
            "".join(f"| {time.strftime('%b %d %H:%M', time.localtime(e.get('at', 0)/1000))} | {PARTS.get(e.get('part'), e.get('part'))} {e.get('ref','')} | {cell(e.get('before'))} | {cell(e.get('after'))} |\n" for e in log))
        last = state.get(code, 0)
        for e in log:
            if e.get("at", 0) <= last or e.get("part") in ("status", "assets-ready", "open-done"):
                continue
            when = time.strftime("%b %d", time.localtime(e["at"] / 1000))
            where = f"{code} · {PARTS.get(e.get('part'), e.get('part'))} {e.get('ref', '')}"
            new_rows.append(f"| {when} | {where} | {cell(e.get('before'))} | {cell(e.get('after'))} | (Skill updater: write the lesson) | 1 |")
            lesson_lines.append(f"- {where}\n  - Agents wrote: {e.get('before')}\n  - Mark changed it to: {e.get('after')}")
        if log:
            state[code] = max(e.get("at", 0) for e in log)
    if new_rows:
        t = FIXLOG.read_text()
        if SECTION not in t:
            t = t.replace("## Asset lists and production",
                          f"{SECTION}\n\nEvery change Mark saves in the Script Room lands here (tools/edits-to-fixlog.py). The Skill updater fills in the lesson and, when the same kind of change shows up twice, proposes a rule (`skill-updating`).\n\n| Date | Where | Agents wrote | Mark changed it to | Lesson | Seen |\n|---|---|---|---|---|---|\n\n## Asset lists and production", 1)
        head = t.index(SECTION)
        end = t.index("\n\n## ", head + len(SECTION))
        t = t[:end] + "\n" + "\n".join(new_rows) + t[end:]
        FIXLOG.write_text(t)
        (ROOT / "data" / "mark-edits" / "new-lessons.md").write_text("# New edits from Mark to learn from\n\n" + "\n".join(lesson_lines) + "\n")
    STATE.write_text(json.dumps(state, indent=1))
    print(f"{len(new_rows)} new edit(s) from Mark logged" + (" → data/mark-edits/new-lessons.md" if new_rows else ""))


if __name__ == "__main__":
    main()
