"""Turn a video's three documents into one JSON doc for the Script Room artifact.
Usage: python3 tools/scripts-to-json.py <CODE> <out.json>
"""
import json, re, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
code, out = sys.argv[1], sys.argv[2]
d = ROOT / "videos" / code


def cells(line):
    parts = [c.strip() for c in line.strip().strip("|").split("|")]
    return parts


def table(text):
    rows = []
    lines = [l for l in text.splitlines() if l.strip().startswith("|")]
    for l in lines[2:]:
        rows.append(cells(l))
    return rows


sc = (d / f"{code}-1-SCRIPT.md").read_text()
ed = (d / f"{code}-2-EDIT.md").read_text()
asx = (d / f"{code}-3-ASSETS.md").read_text()

bf = d / "brief.md"
brief_title = code
if bf.exists():
    m = re.search(r"^#\s*\S+\s*·\s*(.+)$", bf.read_text(), re.M)
    if m:
        brief_title = m.group(1).strip()
_rec = re.search(r"\*\*Recreating:\*\*\s*(.+)", sc)
rec = _rec.group(1).strip() if _rec else "Original concept (no source Reel)"
url = (re.search(r"https?://\S+", rec) or [""])[0] if re.search(r"https?://\S+", rec) else ""
if not url:
    _ov = re.search(r"\*\*Original video:\*\*\s*(https?://\S+)", sc)
    url = _ov.group(1) if _ov else ""
acct = (re.search(r"@[\w.]+", rec) or [""])[0] if re.search(r"@[\w.]+", rec) else ""
length = (re.search(r"\*\*Length:\*\*\s*(.+)", sc) or [None, ""])[1] if re.search(r"\*\*Length:\*\*\s*(.+)", sc) else ""
presenter = "Mark" if code.startswith("M") else "Joshua"

# a hook runs until the next hook, the --- rule or the end of the hook section (it can span paragraphs)
hooks = [{"id": f"h{m.group(1)}", "label": m.group(1), "text": m.group(2).strip(), "orig": m.group(2).strip()}
         for m in re.finditer(r"\*\*([A-Z]|Hook)\.\*\*\s*(.+?)(?=\n\s*\*\*(?:[A-Z]|Hook)\.\*\*|\n---|\Z)", sc.split("## Script")[0], re.S)]
body = sc.split("## Script", 1)[1] if "## Script" in sc else ""
lines = [{"id": f"l{m.group(1)}", "text": m.group(2).strip(), "orig": m.group(2).strip()}
         for m in re.finditer(r"^(\d+)\.\s+(.+)$", body, re.M)]

ed_head = ed.split("| Time")[0]
ed_notes = [l.strip() for l in ed_head.splitlines() if l.strip().startswith("**")]
ed_rows = []
for i, r in enumerate(table(ed)):
    r += [""] * (5 - len(r))
    ed_rows.append({"id": f"e{i+1}", "time": r[0], "spoken": r[1], "onscreen": r[2], "visual": r[3], "sound": r[4]})
ed_after = ed.split("\n\n")[-1].strip() if not ed.strip().endswith("|") else ""

as_head = asx.split("| ID")[0]
as_notes = [l.strip() for l in as_head.splitlines() if l.strip().startswith("**") and "Recreating" not in l]
as_rows = []
for r in table(asx.split("**Still open")[0]):
    r += [""] * (5 - len(r))
    as_rows.append({"id": r[0], "what": r[1], "who": r[2], "how": r[3], "file": r[4], "ready": False})
open_items = []
if "**Still open" in asx:
    for i, m in enumerate(re.finditer(r"^- (.+)$", asx.split("**Still open", 1)[1], re.M)):
        open_items.append({"id": f"o{i+1}", "text": m.group(1).strip(), "done": False})


def ref_dir(vid):
    """Reference folder for a Reel id: knowledge/reference/<id>, or our own video's folder (via data/video-map.csv)."""
    d = ROOT / "knowledge" / "reference" / vid
    if d.exists():
        return d
    vm = ROOT / "data" / "video-map.csv"
    if vm.exists():
        for row in vm.read_text().splitlines()[1:]:
            c = row.split(",")
            if len(c) >= 5 and c[4] == vid:
                for cand in (ROOT / "knowledge" / "own-videos" / c[0], ROOT / "knowledge" / "own-videos" / f"{c[0]}_file"):
                    if (cand / "transcript.srt").exists():
                        return cand
    return d

def original_lines(u):
    m = re.search(r"/(?:p|reel|reels)/([^/?#]+)", u or "")
    if not m:
        return []
    srt = ref_dir(m.group(1)) / "transcript.srt"
    if not srt.exists():
        return []
    segs = re.findall(r"(\d\d):(\d\d):(\d\d),\d+ --> [^\n]+\n(.+?)(?:\n\n|\Z)", srt.read_text(), re.S)
    out, buf, start = [], "", None
    for hh, mm, ss, txt in segs:
        txt = " ".join(txt.split())
        if start is None:
            start = int(mm) * 60 + int(ss)
        buf = (buf + " " + txt).strip()
        while True:
            mm2 = re.search(r"[.?!](\s|$)", buf)
            if not mm2:
                break
            out.append({"t": f"{start//60}:{start%60:02d}", "text": buf[:mm2.end()].strip()})
            buf = buf[mm2.end():].strip()
            start = int(mm) * 60 + int(ss) if buf else None
    if buf:
        out.append({"t": f"{(start or 0)//60}:{(start or 0)%60:02d}", "text": buf})
    return out


def orig_info(u):
    lines = original_lines(u)
    words = sum(len(l["text"].split()) for l in lines)
    dur = None
    m = re.search(r"/(?:p|reel|reels)/([^/?#]+)", u or "")
    if m:
        mt = ref_dir(m.group(1)) / "meta.txt"
        if mt.exists():
            mm = re.search(r"duration_s:\s*([\d.]+)", mt.read_text())
            if mm:
                dur = round(float(mm.group(1)))
    return {"account": acct, "url": u, "lines": lines, "words": words, "seconds": dur}


doc = {
    "code": code, "presenter": presenter, "title": (hooks[0]["text"] if hooks else brief_title),
    "originalTitle": (re.search(r'"([^"]+)"', rec).group(1) if re.search(r'"([^"]+)"', rec) else ""),
    "recreating": {"account": acct, "url": url.rstrip(".,"), "summary": rec},
    "length": length, "status": "In review",
    "original": orig_info(url.rstrip(".,")),
    "script": {"hooks": hooks, "lines": lines},
    "edit": {"notes": ed_notes, "rows": ed_rows},
    "assets": {"notes": as_notes, "rows": as_rows, "open": open_items},
    "updatedAt": time.time(), "updatedBy": "agents",
}
Path(out).write_text(json.dumps(doc, ensure_ascii=False, indent=1))
print(code, len(hooks), "hooks", len(lines), "lines", len(ed_rows), "edit rows", len(as_rows), "assets", len(open_items), "open", f"{len(json.dumps(doc))//1024}KB")
