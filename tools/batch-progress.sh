#!/bin/zsh
# batch-progress: live view of several scripts moving through the pipeline.
# Usage: tools/batch-progress.sh "Title" J024 J025 J026 J027
TITLE="$1"; shift
cd "$(dirname "$0")/.."
spin=('|' '/' '-' '\'); i=0; start=$(date +%s)
mark() { [[ -s "$1" ]] && echo "done " || echo " ... "; }
while true; do
  clear
  el=$(( $(date +%s) - start ))
  echo "$TITLE  ${spin[$(( i % 4 + 1 ))]}   (running $(( el / 60 ))m $(( el % 60 ))s)"; echo
  printf "%-6s %-7s %-8s %-8s %-8s %-8s\n" CODE Brief "Beat map" Script Review Approved
  all=1
  for c in "$@"; do
    d=videos/$c
    a=$(mark $d/brief.md); b=$(mark $d/beatmap.md); s=$(mark $d/$c-1-SCRIPT.md); r=$(mark $d/review.md); p=$(mark $d/approval.md)
    printf "%-6s %-7s %-8s %-8s %-8s %-8s\n" $c "$a" "$b" "$s" "$r" "$p"
    [[ "$p" == "done " ]] || all=0
  done
  echo; echo "Director → Scriptwriter → Script critic → Director. Ctrl+C to close."
  (( all )) && { echo; echo "All approved."; break; }
  i=$(( i + 1 )); sleep 3
done
