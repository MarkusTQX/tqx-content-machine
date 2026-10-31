# TQX Content Machine: Agents & Skills Plan

**Products:** GATC (Global AI Trading Championship) and QUBE
**Editor:** done by a human for now; the Editor agent gets added later.

## Why the skill set has to be this detailed

Most line-by-line fixing comes from four places, and each needs its own skill:

1. **Wrong words.** Claude drifts between synonyms, invents terms, and explains things the audience already knows.
2. **Written, not spoken.** Essay rhythm, AI tells ("it's not X, it's Y", lists of three, em dashes), sentences nobody would actually say.
3. **Broken logic.** Every line sounds fine, but the hook's promise is never paid off, steps get skipped, or conclusions aren't earned.
4. **Wrong facts.** Invented features, outdated numbers, trading concepts explained slightly wrong, which costs credibility with traders immediately.

---

## Part 1: The skill library

### A. Who we're talking to

| Skill | What goes in it | What Claude gets wrong without it |
|---|---|---|
| `audience-profile` | Each persona: trading experience, what they already know, what they believe, pains, goals, objections, what they've been burned by (signal groups, bots, courses), awareness stage (never heard of AI trading → ready to join GATC) | Pitches at the wrong level: explains what they know, skips what they don't, writes for a generic "trader" |
| `audience-language` | The exact phrases the audience uses, taken from comments, DMs, Reddit and competitors' comment sections, grouped by pain point | Writes in marketer language instead of the words the audience uses |

### B. What we're talking about

| Skill | What goes in it | What Claude gets wrong without it |
|---|---|---|
| `product-truth-gatc` | What GATC is, how it works step by step, what's live today vs on the roadmap, real numbers with a source and date, what it is **not** | Invents features, describes the mechanics wrong, uses outdated numbers |
| `product-truth-qube` | Same structure for QUBE | Same |
| `terminology` | Glossary table with these columns:<br>• **term**: the approved one<br>• **definition**<br>• **never say**: banned synonyms<br>• **capitalisation**<br>• **explain or assume?**: per audience<br>• **internal-only?**: terms never said on camera<br><br>Include a "correct in a sentence" example for each. | The weeks-of-fixing problem: synonyms drifting ("bot" / "algo" / "model" / "agent"), wrong definitions, internal jargon leaking into scripts |
| `trading-fundamentals` | Correct meanings at the right depth (drawdown, win rate, sim vs live, backtest vs forward test, leverage, etc.), plus common misconceptions and how *we* explain each | Statements that are slightly wrong, which experienced traders spot instantly |
| `claims-and-proof` | Every approved claim, paired with its proof (screenshot, leaderboard, result) and its allowed wording | Unproven "trust me" claims, which kill trust in a sceptical finance audience |
| `positioning` | How we differ from signal groups, copy-trading, other AI bots and courses; the "enemy" we push against; comparisons we never make | Sounds like every other trading account |

### C. How we sound

| Skill | What goes in it | What Claude gets wrong without it |
|---|---|---|
| `tqx-voice` (Mark's rewrite) | Who's speaking, point of view (I / we / you), attitude, energy, humour level, stance on hype. **Built from transcripts of Mark talking naturally**: voice notes, lives, best videos. | Falls back to Claude's default polite, explainer voice |
| `spoken-sentence-rules` | Sentence length range, one idea per sentence, contractions, how sentences may start, rhythm, punctuation for delivery, a read-aloud test. Every rule gets a bad line and a fixed line. | Essay sentences that read fine on paper but sound wrong when spoken |
| `anti-ai-patterns` | Banned patterns, each with its fix:<br>• "It's not X, it's Y"<br>• lists of three<br>• em dashes<br>• "Here's the thing", "Let's dive in"<br>• "game-changer"<br>• rhetorical-question chains<br>• colon reveals<br>• hedging<br>• summary endings<br>• motivational filler | The giveaways that make a script sound AI-written |

### D. How a script is built

| Skill | What goes in it | What Claude gets wrong without it |
|---|---|---|
| `hook-writing` | From the link database: hook types, formulas, rules for the first 1–3 seconds, how spoken and on-screen text work together | Generic, slow, or clickbait hooks that don't fit TQX |
| `story-structures` | From the link database: named structures with their beats, which goal each fits, seconds per beat at 30/45/60s | Shapeless middles; payoff in the wrong place |
| `retention-writing` | From the link database: open loops, a re-hook every few seconds, pattern breaks, payoff placement | Viewers leave in the middle |
| `script-logic` | The reasoning chain:<br>• the hook's promise must be paid off<br>• every line answers "so what?" or "how?"<br>• no skipped steps<br>• cause and effect must be correct<br>• one main idea per video<br>• the "explain it to a friend" test | **Scripts that sound fine line by line but don't make sense as a whole** |
| `content-formats` | Our recurring formats (e.g. GATC leaderboard update, AI-vs-AI, behind the build, myth-bust): template, length, when to use each | Reinvents the format every time; inconsistent series |
| `cta-and-offer` | What we ask for at each goal (follow, comment a keyword, join GATC, try QUBE), exact wording, where it goes | Missing, random, or wrong-offer CTAs |
| `on-screen-text` | What goes on screen vs what's spoken, caption length, never duplicating the voiceover | Scripts with nothing for the screen, or text that fights the voiceover |

### E. Guardrails

| Skill | What goes in it | What Claude gets wrong without it |
|---|---|---|
| `finance-compliance` | No return promises, required disclaimers, sim-vs-live wording, banned phrases ("guaranteed", "passive income", etc.) | Claims that are legally risky or look like a scam |

### F. Quality: how fixes stop repeating

| Skill | What goes in it | What Claude gets wrong without it |
|---|---|---|
| `gold-standard-scripts` | 10–20 approved scripts, annotated line by line with why each line works. Plus rejected scripts with why they failed. | Misreads the rules; good examples teach more than rules do |
| `fix-log` | **Every correction Mark makes:** original line → fix → reason → which rule it breaks. When a fix repeats, the Skill updater turns it into a rule. | The same mistake gets fixed for weeks. With this, each kind of mistake gets fixed once. |
| `script-qa-checklist` | The line-by-line review that runs before any script reaches Mark | Problems reach Mark instead of being caught first |

### Two process rules

1. **Write in passes, not all at once.** Logic outline (beats, promise, payoff, the one idea) → draft → voice pass → QA. Most logic failures happen when everything is written in one go.
2. **Use code for the checks code can do.** Banned phrases, em dashes, terms that aren't in the glossary, overlong sentences: a small checker script catches these every time, and it runs automatically so it can't be skipped.

---

## Part 2: The agents

### Production loop

#### 1. Director
Sets the weekly content plan and the angle for each video; approves the outline, script and final cut.

| Skill | Why this agent needs it |
|---|---|
| `content-strategy` | Content pillars, posting mix, what this week should push (GATC vs QUBE) |
| `audience-profile` | Checks each angle matters to a real persona |
| `positioning` | Keeps every video on-message against competitors |
| `content-formats` | Picks the right format for the goal |
| `content-scorecard` | Defines "good" with metrics, not gut feel |
| `script-logic` | Approves the outline's promise and payoff before drafting starts |
| `hook-writing` | Judges hooks by the same rules the writer uses |
| `finance-compliance` | Final compliance sign-off |
| `gold-standard-scripts` | Measures every script against the standard Mark set |

#### 2. Scriptwriter
Writes in passes: outline → draft → voice pass, with estimated timestamps per line.

| Skill | Why this agent needs it |
|---|---|
| `audience-profile` | Who it's writing for and at what level |
| `audience-language` | Uses the audience's own words |
| `product-truth-gatc` / `product-truth-qube` | Only states facts that are true and current |
| `terminology` | The exact approved term, every time |
| `trading-fundamentals` | Explains concepts correctly |
| `claims-and-proof` | Only uses claims that have proof on screen |
| `positioning` | Frames the product against the right enemy |
| `tqx-voice` | Sounds like Mark |
| `spoken-sentence-rules` | Writes for speaking, not reading |
| `anti-ai-patterns` | Avoids the AI giveaways while drafting |
| `hook-writing` | The opening 1–3 seconds |
| `story-structures` | The shape of the whole video |
| `retention-writing` | Keeps viewers through the middle |
| `script-logic` | Makes the argument hold together |
| `content-formats` | Follows the format the Director picked |
| `cta-and-offer` | The right ask, worded correctly |
| `on-screen-text` | Writes the text layer alongside the spoken lines |
| `finance-compliance` | Stays compliant while drafting |
| `gold-standard-scripts` | Matches the quality bar |
| `fix-log` | Doesn't repeat past mistakes |

#### 3. Script critic
Reviews every script line by line before the Director sees it, and sends it back with specific fixes. It's a separate agent because a writer reviewing its own work misses its own habits.

| Skill | Why this agent needs it |
|---|---|
| `script-qa-checklist` | The review procedure |
| `terminology` | Flags every wrong or drifting term |
| `product-truth-gatc` / `product-truth-qube` | Fact-checks every product statement |
| `trading-fundamentals` | Catches technically wrong explanations |
| `spoken-sentence-rules` | Flags lines that won't sound natural spoken |
| `anti-ai-patterns` | Flags AI giveaways (plus the automatic checker) |
| `script-logic` | Checks the promise is paid off, no steps are skipped, conclusions are earned |
| `tqx-voice` | Flags lines that don't sound like Mark |
| `finance-compliance` | Flags risky claims |
| `fix-log` | Checks none of Mark's past corrections have come back |

#### 4. Production
Turns the locked script into a storyboard and shot list.

| Skill | Why this agent needs it |
|---|---|
| `storyboarding` | Turns lines into shots: framing, angle, movement, duration |
| `filming-setup` | Only plans shots Mark can film with his gear and locations |
| `on-screen-text` | Places the text layer in each shot |
| `product-truth-gatc` / `product-truth-qube` | Knows which product screens exist |

#### 5. B-roll
Lists every screen recording and screenshot needed, with a capture checklist.

| Skill | Why this agent needs it |
|---|---|
| `broll-sourcing` | Matches script lines to visuals; how to capture each one |
| `claims-and-proof` | Every claim gets its proof visual |
| `product-truth-gatc` / `product-truth-qube` | Knows which screens and accounts exist |
| `terminology` | Labels on screen match the script's terms |

### Research loop

#### 6. Video analyst
Downloads, transcribes and grabs frames, then writes one lesson card per video.

| Skill | Why this agent needs it |
|---|---|
| `video-breakdown` | Fixed lesson-card format, so every video is analysed the same way |

#### 7. Librarian
Combines lesson cards into skills and ranks rules (strong / contested / single-source).

| Skill | Why this agent needs it |
|---|---|
| `kb-curation` | Dedupes, tags and scores knowledge |
| `skill-creator` ✅ | Writes skills in Anthropic's format |

#### 8. Competitor scout
Finds top-performing Reels in the niche and writes "remix for GATC/QUBE" briefs.

| Skill | Why this agent needs it |
|---|---|
| `video-breakdown` | Analyses competitors the same way as the study videos |
| `remix-for-product` | Keeps the structure but rebuilds it around our product, without copying footage |
| `audience-profile` | Only picks videos that fit our audience |
| `positioning` | Remixes from our angle, not theirs |

### Feedback loop

#### 9. Analytics
Pulls metrics for each post and matches them to the video ID and its script.

| Skill | Why this agent needs it |
|---|---|
| `metrics-definitions` | Which numbers to pull and how to compare videos fairly |
| `content-scorecard` | Scores each post against the targets |

#### 10. Retention analyst
Maps each drop-off to a script line and gives the cause.

| Skill | Why this agent needs it |
|---|---|
| `retention-diagnosis` | Turns a drop at a timestamp into a script cause |
| `hook-writing` | Diagnoses drops in the first 3 seconds |
| `story-structures` / `retention-writing` | Diagnoses mid-video drops |
| `script-logic` | Spots drops caused by confusing or unearned lines |

#### 11. Skill updater
Turns patterns in the data and in Mark's fixes into proposed skill changes; Mark approves each one.

| Skill | Why this agent needs it |
|---|---|
| `skill-updating` | Rules for changes: minimum sample size, show a diff, log it |
| `fix-log` | Mark's repeated corrections become new rules |
| `skill-creator` ✅ | Keeps skills in the correct format |

✅ = already exists

---

## Part 3: Who writes what

### Mark writes (only Mark knows this)
- [ ] `terminology` ← start here
- [ ] `gold-standard-scripts` ← start here
- [ ] `tqx-voice` (rewrite)
- [ ] `audience-profile`
- [ ] `product-truth-gatc` (seed from the existing `tqx-gatc-workflow` skill)
- [ ] `product-truth-qube`
- [ ] `claims-and-proof`
- [ ] `positioning`
- [ ] `finance-compliance`
- [ ] `content-strategy`
- [ ] `content-formats`
- [ ] `cta-and-offer`
- [ ] `content-scorecard`
- [ ] `filming-setup`
- [ ] `broll-sourcing`

### The pipeline builds (from links and recordings)
- [ ] `hook-writing` (from the link database)
- [ ] `story-structures` (from the link database)
- [ ] `retention-writing` (from the link database)
- [ ] `storyboarding` (from the link database)
- [ ] `audience-language` (from comments)
- [ ] raw material for `tqx-voice` (from Mark's own transcripts)

### Claude drafts, Mark corrects
- [ ] `anti-ai-patterns`
- [ ] `spoken-sentence-rules`
- [ ] `script-logic`
- [ ] `on-screen-text`
- [ ] `script-qa-checklist`
- [ ] `trading-fundamentals`
- [ ] `fix-log`
- [ ] `video-breakdown`
- [ ] `kb-curation`
- [ ] `remix-for-product`
- [ ] `metrics-definitions`
- [ ] `retention-diagnosis`
- [ ] `skill-updating`
- [ ] the automatic script checker (code)

**What makes skills hold up:** for every rule, include a **bad line and a fixed line**. Claude follows examples far more reliably than it follows rules. `terminology` and `gold-standard-scripts` save the most fixing time, so start there.
