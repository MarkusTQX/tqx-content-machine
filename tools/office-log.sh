#!/bin/zsh
# office-log: post an event to the studio view.
# Usage: tools/office-log.sh <agent> <state: working|done|waiting|idle> <code> "<message>"
HERE="${0:A:h}"; LOG="$HERE/../data/office-log.jsonl"
python3 -I -c 'import json,sys,time; print(json.dumps({"t":time.time(),"agent":sys.argv[1],"state":sys.argv[2],"code":sys.argv[3],"msg":sys.argv[4]}))' "$1" "$2" "$3" "$4" >> "$LOG"
