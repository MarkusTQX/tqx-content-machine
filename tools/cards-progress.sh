#!/bin/zsh
# cards-progress: live view of cards being written by helpers.
# Usage: tools/cards-progress.sh <cards-folder> <total> [title]
DIR="$1"; TOTAL="$2"; TITLE="${3:-Writing cards}"
spin=('|' '/' '-' '\'); i=0; start=$(date +%s)
while true; do
  clear
  n=$(ls "$DIR"/*.md 2>/dev/null | grep -v '/_' | wc -l | tr -d ' ')
  pct=$(( n * 100 / TOTAL )); bar=$(printf '%*s' $(( pct / 4 )) '' | tr ' ' '#'); gap=$(printf '%*s' $(( 25 - pct / 4 )) '' | tr ' ' '.')
  el=$(( $(date +%s) - start )); mm=$(( el / 60 )); ss=$(( el % 60 ))
  echo "$TITLE  ${spin[$(( i % 4 + 1 ))]}   (running ${mm}m ${ss}s)"; echo
  echo "[$bar$gap] $n / $TOTAL  ($pct%)"; echo
  if (( n == 0 )); then
    echo "  Helpers are reading the instructions and the first videos."
    echo "  The first cards usually appear after 2 to 4 minutes."
  fi
  ls -t "$DIR"/*.md 2>/dev/null | grep -v '/_' | head -25 | while read f; do echo "  done  $(basename "$f" .md)"; done
  (( n >= TOTAL )) && { echo; echo "All cards written. Claude is putting the summary together next."; break; }
  i=$(( i + 1 )); sleep 1
done
