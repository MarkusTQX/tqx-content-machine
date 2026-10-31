---
name: kb-curation
description: How the Librarian turns a pile of teaching cards (from educational videos about hooks, storytelling, retention, editing) into clean, scored rules - merging duplicates, counting how many different creators teach each rule (3 or more = firm rule, 1–2 = tip), flagging rules creators disagree on, rejecting anything that clashes with TQX's own skills, and handing firm rules to skill-updating. Use whenever new teaching cards arrive, or when building or refreshing hook-writing, story-structures, retention-writing or storyboarding.
---

# Knowledge-base curation

Mark sends videos of creators teaching how to make content. `video-breakdown` turns each one into a teaching card listing the rules it teaches. This skill sorts all those cards into one list of rules per topic, scored by how many creators agree. Firm rules then go into the skill for that topic (`hook-writing`, `story-structures`, `retention-writing`, `storyboarding`).

## Where things live

| What | Where |
|---|---|
| Teaching cards | `content-machine/knowledge/cards/{topic}/{date}_{account}_{short-title}.md` |
| The rule ledger, one per topic | `content-machine/knowledge/rules/{topic}.md` |
| Topics | hooks · storytelling · retention · editing · storyboarding · other |

## Scoring (Mark, Oct 22)

| Status | When | What happens to it |
|---|---|---|
| **Firm rule** | Taught by **3 or more different creators**, and nobody teaches the opposite | Proposed for the skill's main rules (through `skill-updating`) |
| **Tip** | Taught by 1 or 2 creators | Goes in the skill's "Tips to try" section. The writer may use it; it isn't required |
| **Contested** | Some creators teach it and others teach the opposite | Both sides go in the skill's "Contested" section with their counts. Only our own data or Mark settles it |
| **Rejected** | Clashes with a TQX skill (see below) | Logged in the ledger with the reason; never goes in a skill |

Counting rules:
- **Every creator counts once.** Proof doesn't add weight (Mark, Oct 22). Record the evidence a creator gave anyway, so Mark can see it.
- **One creator, many videos = 1.** Count accounts, not videos. Two accounts run by the same person count once.
- **Reposts and copies don't count.** If an account is clearly repeating another creator's video, count only the original.

## Our own results beat any creator count

Once a rule has been tested on our videos (5 videos of the same kind, per `skill-updating`), write the result in the ledger: helped, hurt, or no difference, with the video codes.
- **Helped:** it stays or becomes firm, whatever the creator count.
- **Hurt:** it gets proposed for removal, even if 10 creators teach it.
- **No difference:** keep its current status, and note the test.

## Step by step, each time new cards come in

1. **Read every new card.** Take each row from "Rules taught".
2. **Match it to the ledger.** Two rules are the same rule if following one means you're following the other. Wording doesn't matter.

   | Same rule | Different rules |
   |---|---|
   | "Show the result in the first second" / "Lead with the end result" | "Show the result first" / "Ask a question first" |

   If one rule is a narrower version of another ("put a number in the first 3 words" vs "use numbers in hooks"), count it toward the broader rule *and* track the narrow one as its own row. The narrow one needs its own 3 creators to become firm.
3. **Add or update the row.** Add the creator handle and the card. Recount.
4. **Look for opposites.** If any creator teaches the opposite of a rule, mark both as contested and link them.
5. **Check it against the TQX skills.** If following the rule would break a TQX skill, mark it rejected. Common ones:

   | Creator rule | Clashes with | Status |
   |---|---|---|
   | "Promise a result in the hook: 'This made me $10K'" | `finance-compliance` (no promised returns) | Rejected |
   | "Use 'It's not X, it's Y' for contrast" | `anti-ai-patterns` #1 | Rejected |
   | "Tease something you never pay off" | `script-logic` #1 (the hook's promise gets paid off) | Rejected |
   | "Say 'link in bio'" | `cta-and-offer` (comment-keyword CTA) | Rejected |

   A rejected rule can still teach something. If there's a version that doesn't break the skill, write it as its own row.
6. **Write the change report** (format below) and send firm-rule changes to `skill-updating` as proposals.

## The rule ledger

```
# Rule ledger: [topic]
Last updated: [date] · Cards: [n] · Creators: [n]

| ID | Rule (one plain line) | Creators (handles) | Count | Status | Opposite of / clashes with | Cards | Tested on our videos |
|---|---|---|---|---|---|---|---|
| H01 | Show the end result in the first second | @a, @b, @c, @d | 4 | Firm | | [card files] | Not yet |
| H02 | Put a number in the first 3 words | @a, @e | 2 | Tip | narrower version of H07 | ... | Not yet |
| H03 | Start facing the camera | @b, @f | 2 | Contested | opposite of H04 | ... | Not yet |
| H04 | Start on the screen, not your face | @c | 1 | Contested | opposite of H03 | ... | Not yet |
| H05 | "This made me $10K" result hooks | @g, @h, @i | 3 | Rejected | finance-compliance | ... | n/a |
```

Keep each row's quote trail: every count must be traceable to a card and a timestamp.

## How rules go into the skill

When a rule turns firm (or a tip or contest is added), the proposal to `skill-updating` includes:
- The rule in one plain line.
- The creator count and handles.
- **A TQX bad line → fixed line**, written for a real GATC or Qube video and checked against `spoken-sentence-rules`, `terminology` and `finance-compliance`.

Each topic skill is laid out in this order:
1. **Firm rules**, each with its count and a TQX example
2. **Tips to try**
3. **Contested**, with both sides and their counts
4. **Tested on our videos**, with the results and video codes

## Change report (after every batch)

```
KB UPDATE · [topic] · [date]
New cards: [n] · New creators: [n]

Now firm: [IDs + one line each] → sent to skill-updating
New tips: [IDs]
New contests: [ID vs ID]
Rejected: [IDs + which skill they clash with]
Needs Mark: [anything only he can decide, or "nothing"]
```

## Don'ts

- Don't count a rule from a reference video (lesson card). Only teaching cards count. A viral video *doing* something isn't a creator *teaching* it.
- Don't upgrade a tip to firm because it "sounds right". Only the count, or our own results, can do that.
- Don't drop a contested rule because you prefer one side. Keep both until data or Mark settles it.
- Don't write TQX-specific topics or posting rules into the ledger. It records how to make content, not what to make.
