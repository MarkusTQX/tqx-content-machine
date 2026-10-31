#!/bin/zsh
# study-batch: run study-video on every "name url" line of a links file, into one folder.
# Usage: tools/study-batch.sh <links-file> <out-folder>
HERE="${0:A:h}"; LINKS="$1"; OUT="$2"
while read -r name url; do
  [[ -z "$name" || -f "$OUT/$name/contact.jpg" ]] && continue
  "$HERE/study-video.sh" "$url" "$OUT/$name" </dev/null >/dev/null 2>&1 || { mkdir -p "$OUT/$name"; echo "failed: $url" > "$OUT/$name/FAILED.txt"; }
done < "$LINKS"
