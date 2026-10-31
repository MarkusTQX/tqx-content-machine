"""room-to-script-doc: write Mark's saved Script Room version back into <CODE>-1-SCRIPT.md (hook + numbered lines),
so the files on disk never fall behind his edits. Keeps the doc's header.
Usage: python3 tools/room-to-script-doc.py <CODE> <live-json>   (live-json from ArtifactData list/get out_dir)
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
code, src = sys.argv[1], Path(sys.argv[2])
d = json.loads(src.read_text()); d = d.get("data", d)
p = ROOT / "videos" / code / f"{code}-1-SCRIPT.md"
t = p.read_text()
head = t.split("## Hook")[0]
hooks = d["script"]["hooks"]
lines = [l for l in d["script"]["lines"] if l.get("text","").strip()]
out = head + "## Hook (the original's, word for word)\n\n" + "".join(f"**Hook.** {h['text'].strip()}\n\n" for h in hooks[:1]) + "---\n\n## Script\n\n" + \
      "".join(f"{i+1}. {l['text'].strip()}\n\n" for i, l in enumerate(lines))
words = sum(len(h["text"].split()) for h in hooks[:1]) + sum(len(l["text"].split()) for l in lines)
og = d.get("original", {}).get("words")
out = re.sub(r"(?m)^\*\*Words:\*\*.*$", f"**Words:** original {og} words · ours {words} words", out) if og else out
p.write_text(out.rstrip() + "\n")
print(code, "synced from the Script Room:", len(lines), "lines,", words, "words")
