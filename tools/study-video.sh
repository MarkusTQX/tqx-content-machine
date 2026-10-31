#!/bin/zsh
# study-video: turn one video (link or file) into what Claude can read.
# Usage: tools/study-video.sh <instagram-url-or-video-file> <output-folder>
# Makes: video.mp4, info.json (if from a link), transcript.srt/.txt (timestamped),
#        frames/every_2s_*.jpg, frames/cut_*.jpg (scene changes), cuts.txt, contact.jpg, meta.txt
set -euo pipefail

SRC="$1"
OUT="$2"
HERE="${0:A:h}"
MODEL="$HERE/models/ggml-large-v3-turbo-q5_0.bin"

mkdir -p "$OUT/frames"

# 1. Get the video
if [[ -f "$SRC" ]]; then
  ffmpeg -loglevel error -y -i "$SRC" -c copy "$OUT/video.mp4" 2>/dev/null || cp "$SRC" "$OUT/video.mp4"
else
  "$HERE/.venv/bin/yt-dlp" --quiet --no-warnings --no-playlist --write-info-json \
    --remux-video mp4 -o "$OUT/video.%(ext)s" "$SRC"
  [[ -f "$OUT/video.info.json" ]] && mv "$OUT/video.info.json" "$OUT/info.json"
fi
VIDEO="$OUT/video.mp4"
[[ -f "$VIDEO" ]] || { echo "No video downloaded" >&2; exit 1; }

# 2. Basic facts
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$VIDEO")
{
  echo "source: $SRC"
  echo "duration_s: $DUR"
  if [[ -f "$OUT/info.json" ]]; then
    python3 -I -c 'import json,sys; d=json.load(open(sys.argv[1]))
for k in ("uploader","channel","upload_date","view_count","like_count","comment_count","title","description"):
    v=d.get(k)
    if v is not None: print(f"{k}: {v}")' "$OUT/info.json"
  fi
} > "$OUT/meta.txt"

# 3. Transcript with timestamps
ffmpeg -loglevel error -y -i "$VIDEO" -ar 16000 -ac 1 -c:a pcm_s16le "$OUT/audio.wav"
whisper-cli -m "$MODEL" -f "$OUT/audio.wav" -l auto -osrt -otxt -of "$OUT/transcript" >/dev/null 2>&1
rm -f "$OUT/audio.wav"

# 4. Frames: one every 2 seconds, plus every scene cut
ffmpeg -loglevel error -y -i "$VIDEO" -vf "fps=0.5,scale=540:-2" "$OUT/frames/every_2s_%03d.jpg"
# Cuts: watch the top third too, since most TQX-style edits only change the insert above the presenter
ffmpeg -hide_banner -i "$VIDEO" -vf "select='gt(scene,0.3)',showinfo" -an -f null - 2>&1 \
  | grep -o 'pts_time:[0-9.]*' | cut -d: -f2 > "$OUT/cuts_full.txt" || true
ffmpeg -hide_banner -i "$VIDEO" -vf "crop=iw:ih/3:0:0,select='gt(scene,0.12)',showinfo" -an -f null - 2>&1 \
  | grep -o 'pts_time:[0-9.]*' | cut -d: -f2 > "$OUT/cuts_top.txt" || true
sort -n -u "$OUT/cuts_full.txt" "$OUT/cuts_top.txt" > "$OUT/cuts.txt"; rm -f "$OUT/cuts_full.txt" "$OUT/cuts_top.txt"
i=0; while read -r ts; do i=$((i+1)); ffmpeg -loglevel error -y -ss "$ts" -i "$VIDEO" -frames:v 1 -vf "scale=540:-2" "$OUT/frames/cut_$(printf %03d $i).jpg"; done < "$OUT/cuts.txt"

# 5. Contact sheet (every 2s, 6 across)
ffmpeg -loglevel error -y -i "$VIDEO" -vf "fps=0.5,scale=270:-2,tile=6x5" -frames:v 1 "$OUT/contact.jpg"

echo "done: $OUT ($(printf '%.0f' "$DUR")s, $(wc -l < "$OUT/cuts.txt" | tr -d ' ') cuts)"
