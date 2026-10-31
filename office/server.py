#!/usr/bin/env python3
"""TQX Content Studio: a live view of the agents at work.

Serves office/index.html and /status (JSON built from the videos/<CODE>/ folders
and the event log data/office-log.jsonl). Run: python3 office/server.py [port]
"""
import json
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VIDEOS = ROOT / "videos"
LOG = ROOT / "data" / "office-log.jsonl"
STAGES = [("brief", "director"), ("outline", "scriptwriter"), ("script", "scriptwriter"),
          ("review", "script-critic"), ("approval", "director")]


def tail(path, n=9):
    try:
        lines = [l for l in path.read_text(errors="ignore").splitlines() if l.strip()]
        return lines[-n:]
    except Exception:
        return []


def verdict(path):
    try:
        for l in path.read_text(errors="ignore").splitlines():
            u = l.upper()
            if u.startswith("VERDICT"):
                return l.split(":", 1)[-1].strip()
    except Exception:
        pass
    return None


def status():
    now = time.time()
    videos = []
    files = []
    if VIDEOS.exists():
        for d in sorted(p for p in VIDEOS.iterdir() if p.is_dir()):
            title = d.name
            stages = []
            for name, agent in STAGES:
                f = d / f"{name}.md"
                if f.exists():
                    st = f.stat()
                    stages.append({"stage": name, "agent": agent, "done": True,
                                   "mtime": st.st_mtime, "size": st.st_size,
                                   "verdict": verdict(f) if name in ("review", "approval") else None})
                    files.append((st.st_mtime, d.name, name, agent, f))
                    if name == "brief":
                        first = f.read_text(errors="ignore").splitlines()[:1]
                        if first:
                            title = first[0].lstrip("# ").strip()
                else:
                    stages.append({"stage": name, "agent": agent, "done": False})
            videos.append({"code": d.name, "title": title, "stages": stages})
    events = []
    if LOG.exists():
        for l in LOG.read_text(errors="ignore").splitlines()[-200:]:
            try:
                events.append(json.loads(l))
            except Exception:
                pass
    agents = {}
    for e in events:
        agents[e.get("agent")] = e
    # The most recent file each agent touched, so its monitor can show it live
    monitors = {}
    for mtime, code, name, agent, f in sorted(files, key=lambda x: x[0]):
        monitors[agent] = {"code": code, "file": f"{name}.md", "mtime": mtime,
                           "lines": tail(f), "fresh": now - mtime < 25}
    return {"now": now, "videos": videos, "events": events[-40:], "agents": agents, "monitors": monitors}


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_GET(self):
        if self.path.startswith("/status"):
            body = json.dumps(status()).encode()
            ctype = "application/json"
        else:
            body = (Path(__file__).parent / "index.html").read_bytes()
            ctype = "text/html; charset=utf-8"
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    print(f"TQX Content Studio on http://localhost:{port}")
    ThreadingHTTPServer(("127.0.0.1", port), H).serve_forever()
