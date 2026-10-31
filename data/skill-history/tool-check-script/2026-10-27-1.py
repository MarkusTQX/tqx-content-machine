#!/usr/bin/env python3
"""check-script: automatic checks on a TQX script (Pass 0 of script-qa-checklist).

Usage: python3 tools/check-script.py videos/<CODE>/script.md

Checks every spoken line (hooks + numbered script lines) and on-screen text for:
em dashes, AI patterns, banned finance phrases, "never say" terms from the
terminology skill, sentences over 20 words, placeholders, and the length.
Every flag is for a human (or the Script critic) to decide on; it never edits.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TERMS = ROOT / ".claude/skills/terminology/SKILL.md"
WPS = {"mark": 3.0, "joshua": 3.2}

PATTERNS = [
    ("Em dash", r"—"),
    ("It's not X, it's Y", r"\b(it'?s not|it isn'?t|it wasn'?t|this is not|this isn'?t|this wasn'?t|that'?s not|that isn'?t|that wasn'?t|they'?re not|they aren'?t|you'?re not|you aren'?t)\b.{0,60}?[.,;]\s*(it'?s|it was|this is|that'?s|they'?re|you'?re)\b"),
    ("Stock opener", r"here'?s the thing|let'?s dive in|let'?s break it down|buckle up|in today'?s|picture this|here'?s why that matters"),
    ("Buzzword", r"game[- ]changer|revolutioni[sz]|\bunlock|supercharge|seamless|cutting[- ]edge|next level|\bdelve|\bharness|\bempower|\belevate"),
    ("Hedging", r"might potentially|could potentially|arguably|it could be said|generally speaking"),
    ("Summary ending", r"to sum up|in short,|at the end of the day|the bottom line is"),
    ("Motivational filler", r"you'?ve got this|future self|your journey"),
    ("Banned finance phrase", r"guarantee|risk[- ]free|passive income|can'?t lose|easy money|get rich"),
    ("Never mention", r"\bTQX OS\b"),
    ("Placeholder", r"\[[^\]]*\]|\bTBD\b|\bXX+\b|\bFILL\b|\bREAL FIGURE\b"),
]
# "Never say" terms that are too common to flag automatically (the critic still checks them by reading)
SKIP_TERMS = {"stop", "sl", "dip", "loss", "results", "returns", "simulation", "system", "setup",
              "qube", "the qube app", "accuracy", "secrets", "preset", "margin", "agent team",
              "agent", "bot", "ready-made strategy"}


def never_say_terms():
    terms = set()
    if not TERMS.exists():
        return terms
    for row in TERMS.read_text().splitlines():
        cells = [c.strip() for c in row.split("|")]
        if len(cells) < 5 or cells[1] in ("Approved term", "---", "Approved", "Term"):
            continue
        for q in re.findall(r'"([^"]+)"', cells[3]):
            q = q.strip()
            if q.lower() not in SKIP_TERMS and len(q) > 2:
                terms.add(q)
    return terms


def parse(path):
    text = Path(path).read_text()
    presenter = "mark"
    m = re.search(r"(?:Presenter:\s*|for |\()(Joshua|Mark)\b", text, re.I)
    if m and m.group(1).lower() in WPS:
        presenter = m.group(1).lower()
    hooks, lines, onscreen = [], [], []
    section = None
    for raw in text.splitlines():
        s = raw.strip()
        if s.startswith("## "):
            section = s[3:].strip().lower()
            continue
        if section and section.startswith("hook"):
            m = re.match(r'(\d+)\.\s*"([^"]+)"', s) or re.match(r'\*\*([A-C]|Hook)\.\*\*\s*(.+)', s)
            if m:
                hooks.append((f"Hook {m.group(1)}", m.group(2).strip('" ')))
            for t in re.findall(r'On screen:\s*"([^"]+)"', s):
                onscreen.append((f"Hook on-screen", t))
        elif section == "script":
            m = re.match(r"(\d+)\.\s+(.*)", s)
            if m:
                lines.append((f"Line {m.group(1)}", m.group(2)))
            for t in re.findall(r'On screen:\s*"([^"]+)"', s):
                onscreen.append((f"On-screen", t))
    return presenter, hooks, lines, onscreen


def sentences(t):
    return [x for x in re.split(r"(?<=[.!?])\s+", t) if x.strip()]


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    presenter, hooks, lines, onscreen = parse(sys.argv[1])
    terms = never_say_terms()
    flags = []
    spoken = hooks + lines
    for where, t in spoken + onscreen:
        for name, pat in PATTERNS:
            for m in re.finditer(pat, t, re.I):
                flags.append((where, name, m.group(0)))
        for term in terms:
            if re.search(r"(?<![\w-])" + re.escape(term) + r"(?![\w-])(?! 500)", t, re.I):
                flags.append((where, "Never-say term (terminology)", term))
    for where, t in spoken:
        for sn in sentences(t):
            n = len(re.findall(r"[\w'$%.,-]+", sn))
            if n > 20:
                flags.append((where, f"Long sentence ({n} words)", sn[:60] + "..."))
    for where, t in onscreen:
        n = len(t.split(" · ")[0].split())
        if n > 8:
            flags.append((where, f"On-screen main line over 8 words ({n})", t[:50]))
    # Question chains
    prev_q = False
    for where, t in lines:
        q = t.rstrip().endswith("?")
        if q and prev_q:
            flags.append((where, "Question chain (2 lines in a row end in ?)", t[:50]))
        prev_q = q

    words = sum(len(t.split()) for _, t in lines)
    top = re.search(r"Top 3:\s*\[?#?(\d+)", Path(sys.argv[1]).read_text())
    hook_words = 0
    if not top and hooks and hooks[0][0] in ("Hook A", "Hook Hook"):
        hook_words = len(hooks[0][1].split())
    elif top:
        for where, t in hooks:
            if where == f"Hook {top.group(1)}":
                hook_words = len(t.split())
    elif hooks and not hook_words:
        hook_words = len(hooks[0][1].split())
    total = words + hook_words
    secs = total / WPS[presenter]
    print(f"Spoken words: {total} (top hook {hook_words} + script {words}) · presenter: {presenter} · about {secs:.0f}s at {WPS[presenter]} words/s")
    if secs > 60:
        print("  LENGTH: over 60s. Fine only if it recreates a longer original and the Notes say why (script-logic #10).")
    if secs < 30:
        print("  LENGTH: under 30s. Check the payoff has room.")
    if not flags:
        print("No flags.")
    else:
        print(f"{len(flags)} flag(s):")
        for where, name, what in flags:
            print(f"  {where:<16} {name}: {what}")
    sys.exit(0)


if __name__ == "__main__":
    main()
