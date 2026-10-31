#!/bin/zsh
# progress: live view of a batch of study-video jobs.
# Usage: tools/progress.sh <folder-with-one-subfolder-per-video> <total-count>
DIR="$1"; TOTAL="$2"
spin=('|' '/' '-' '\')
i=0
while true; do
  clear
  done_n=$(ls -d "$DIR"/*/ 2>/dev/null | while read d; do [[ -f "$d/contact.jpg" || -f "$d/FAILED.txt" ]] && echo x; done | wc -l | tr -d ' ')
  pct=$(( done_n * 100 / TOTAL ))
  bar=$(printf '%*s' $(( pct / 4 )) '' | tr ' ' '#')
  gap=$(printf '%*s' $(( 25 - pct / 4 )) '' | tr ' ' '.')
  echo "Studying Reels  ${spin[$(( i % 4 + 1 ))]}"
  echo
  echo "[$bar$gap] $done_n / $TOTAL  ($pct%)"
  echo
  for d in $(ls -td "$DIR"/*/ 2>/dev/null | head -20); do
    name=$(basename "$d")
    if [[ -f "$d/FAILED.txt" ]]; then
      echo "  FAILED   $name"
    elif [[ -f "$d/contact.jpg" ]]; then
      secs=$(grep duration_s "$d/meta.txt" 2>/dev/null | awk '{printf "%.0fs", $2}')
      who=$(grep '^channel:' "$d/meta.txt" 2>/dev/null | cut -d' ' -f2)
      echo "  done     $name  @$who  $secs"
    elif [[ -f "$d/transcript.txt" ]]; then
      echo "  frames   $name"
    elif [[ -f "$d/video.mp4" ]]; then
      echo "  transcribing  $name"
    else
      echo "  downloading   $name"
    fi
  done
  if (( done_n >= TOTAL )); then echo; echo "All done. Claude is writing the cards next."; break; fi
  i=$(( i + 1 ))
  sleep 2
done
