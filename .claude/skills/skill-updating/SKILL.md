---
name: skill-updating
description: The rules for changing any TQX skill - when a repeated correction or a data pattern earns a change, how to write it as a before/after proposal, who approves it (the Director, with the limits that stay with Mark), how to apply, log and roll it back, and the weekly summary for Mark. Use whenever the Skill updater, or anyone else, wants to add, change or remove a rule, example or fact in a TQX skill.
---

# Skill updating

Skills only change through this process. Nobody edits a skill file directly, including an agent in the middle of writing a script.

## What can trigger a change

| Trigger | Threshold | Evidence |
|---|---|---|
| A correction from Mark | The same kind of fix seen **2 times** | `fix-log` rows (the "Seen" column) |
| An analytics pattern | The same pattern across at least **5 videos** of the same kind, on the same account, compared at the same age (48h or 7d) | `metrics-definitions`, `content-machine/data/snapshots/` |
| A drop-off cause | The same cause found on at least **5 videos** | `retention-diagnosis` |
| A lesson from the link database | A rule `kb-curation` scores firm (3+ creators), or a new tip or contest | Teaching cards, `kb-curation` rule ledger |
| A product change | Mark or an official TQX page says so (1 time is enough) | `product-truth-gatc`, `product-truth-qube` |
| A broken fact | A source no longer says what the row claims (1 time is enough) | `claims-and-proof` |

Under the threshold, log it and change nothing. A fix-log row with "Seen 1" stays a row until it happens again.

| Bad | Fixed |
|---|---|
| One video with a number hook does well → "Always open with a number" added to the hook rules. | Logged as one data point. After 5 number-hook videos beat the account's average 3-second view rate at 48h, propose the rule with all 5 codes listed. |

## Who approves

**The Director approves by default.** Mark gets the weekly summary (below).

**These always go to Mark.** The Director can't approve them:
- Removing, weakening or rewording anything Mark set or wrote himself: his edits, his decisions, and every row under "Decisions", "Working with Mark" and "Mark's own edits" in `fix-log`. Mark's edits are final.
- Locked facts in `product-truth-gatc` and `product-truth-qube`, and any new product fact.
- Loosening `finance-compliance`. Making it stricter is fine for the Director.
- Creating a new skill or deleting one.

**Never allowed, whoever approves:**
- Rules about what to make or how often to post: posting quotas, topic lists, "half the videos must mention X". Skills cover how to write, what's true and what's allowed. (Mark, Oct 21: "I don't want restraints on this type of creativity.")
- Changing a number so it matches a recording. Stop and tell Mark instead.
- Anything that mentions TQX OS.

## The proposal (one per change)

```
CHANGE: [skill] · [section]
Type: add rule / change rule / remove rule / add example / fix fact
Trigger: [fix-log rows, video codes or lesson cards] · count [n] of [threshold]
Before:
> [the exact current text, or "none"]
After:
> [the exact new text]
Why: [one or two lines; Mark's own words when it comes from fix-log]
Clashes: [any other skill that says the opposite, or "none"]
Approver: Director / Mark (and why it's Mark)
```

Rules for writing a proposal:
- One change per proposal. Make the smallest edit that fixes it.
- Every writing rule comes with a bad line and a fixed line, taken from a real script.
- Search every other skill for a rule that says the opposite. If there is one, the proposal changes both, or goes to Mark.
- The rule goes in the skill the fix-log row names. Never copy one rule into two skills; point to the skill that owns it.
- Keep each SKILL.md under about 500 lines. When a skill gets longer, move long example lists into a `references/` file inside that skill's folder and link to it.

## The Director's check

- [ ] The threshold is met and every piece of evidence is listed.
- [ ] It isn't on the "always Mark" or "never allowed" lists.
- [ ] No other skill contradicts it after the change.
- [ ] The "Before" text matches the file exactly.
- [ ] Any script line in it passes `spoken-sentence-rules` and `anti-ai-patterns`.

Rejected proposals get logged with the reason. They can come back once there's new evidence.

## Applying a change

1. Save the current file to `content-machine/data/skill-history/{skill}/{YYYY-MM-DD}-{n}.md`.
2. Make the exact edit. Nothing else in the file changes.
3. Mark the fix-log rows it came from: add "→ rule in `{skill}`, {date}" to the Rule / skill cell.
4. Add a line to `content-machine/data/skill-changelog.md`: date · skill · type · one-line summary · trigger · approved by.
5. If the folder is in git, commit it: `skill({skill}): {summary}`.

## Rolling back

- If Mark disagrees, or results get worse after the change, restore the saved copy from `skill-history` and log "rolled back" with the reason.
- Every rule that came from data gets rechecked after the next 5 videos of that kind. If the pattern no longer holds, propose removing it.

## Weekly summary for Mark

Short, in table form. Items waiting on Mark go first.

```
SKILL CHANGES · week of [date]
Waiting on you: [list, or "nothing"]

| Skill | What changed | Why | Approved by |
|---|---|---|---|

Rejected: [n] · Rolled back: [n]
```

## Not a change (no proposal needed)

- Adding a new row to `fix-log`.
- Updating codes, status or views in `slop`.
- Adding a newly sourced claim to `claims-and-proof`, with its primary-source link. Log it in the changelog.
- Saving a new lesson card or teaching card.
