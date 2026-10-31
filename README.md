# TQX Content Machine

A multi-agent system (built for Claude Code) that writes, reviews and improves short-form video scripts for TQX (Qube and GATC), and learns from Mark's edits.

## How it works
Director (brief) → Scriptwriter (beat map, script, editor sheet, asset list) → Script critic (review) → revise until clean → Director (approve) → Mark.

- **Agents:** `.claude/agents/` (director, scriptwriter, script-critic, skill-updater)
- **Skills (the knowledge):** `.claude/skills/` (hooks, voice, compliance, product truth, retention, fix log, and more)
- **Project brief:** `CLAUDE.md`
- **One folder per video:** `videos/<CODE>/` (brief, beat map, script, editor sheet, asset list, review, approval)
- **Studied Reels:** `knowledge/cards/` (lesson cards) and `knowledge/reference/` (transcripts)
- **Data and learning:** `data/` (video map, Mark's edits, skill history and changelog)
- **Tools:** `tools/` (study a video, check a script, Script Room sync, progress windows)

## Setup
Videos, frames and the speech-to-text model are not in the repo. To study new videos:

```bash
python3 -m venv tools/.venv && tools/.venv/bin/pip install yt-dlp
brew install ffmpeg whisper-cpp
mkdir -p tools/models && curl -L -o tools/models/ggml-large-v3-turbo-q5_0.bin https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-large-v3-turbo-q5_0.bin
```

Then open the folder in Claude Code and run `/make-script`.
