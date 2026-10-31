---
name: product-truth-gatc
description: What GATC (Global AI Trading Championship) is, how someone joins and builds an agent step by step, how it connects to Claude and Codex, and the locked facts (prize, scoring, season). Use whenever a TQX script, caption, DM, storyboard or B-roll list mentions GATC, so nothing about the competition is invented or described wrong.
---

# GATC: product truth

Only state what is in this file. If a script needs a GATC fact that isn't here, stop and ask Mark. Never guess a feature, a number or a date.

## What GATC is, in one line

An AI-only trading competition: people build an AI trading agent and the agent trades on its own. No manual orders.

Agents can trade on a simulation account (fake money) or live (Mark, Oct 22). The workshop setup below uses a simulation account; that's the one to show viewers first.

An entry can be a team of agents, each with one job. Call it "a team of agents" (see `terminology`).

## Locked facts (from the TQX brief; do not question or "fix" them)

| Fact | Exact wording to use |
|---|---|
| Name | GATC, the Global AI Trading Championship |
| Who trades | Only AI agents. No humans placing orders. |
| Scoring | 55% on return, 45% on risk |
| Season 1 | July 2026 to June 2027 |
| Regions | Hong Kong, Singapore and the US |
| Prize pool | HK$14 million (about US$1.8 million). Prizes paid monthly, quarterly and annually. |
| Where | Inside the TQX workspace at tqx.ai (Q logo → Competition) |

How to say the scoring out loud for beginners: "How much it makes counts for a bit more than half the score. How much risk it took counts for the rest." Put "55% return · 45% risk" on screen. For Marcus-level viewers, say the split directly.

## How someone joins and builds an agent (from the Singapore workshop deck, Oct 2026)

1. Go to tqx.ai. Log in, or sign up. Google sign-up is fastest; a manual password needs at least 8 characters.
2. In the workspace, click the Q logo (top left) → Competition → Join. Confirm the entry.
3. Create a simulation account. This is where the agent trades with no live money. In this setup, don't connect a live brokerage account. Going live is a separate step, after the agent has been tested.
4. Create the agent. TQX shows two API keys. Copy both. Treat them like passwords: never on screen, never in a shared chat. If one leaks, rotate it immediately.
5. Open c.tqx.ai/set and copy the full setup prompt. Use the version on that page, not an older prompt shown inside TQX.
6. Open a coding agent (Claude or Codex), paste the full prompt, and enter both keys when it asks. Do this in a trusted private session.
7. Choose the strategy. The setup proposes several directions; pick one and answer its follow-up questions:
   - Market: where should it trade?
   - Signal: what should trigger a trade?
   - Risk: how much can it risk?
   - Cadence: how often should it act?
8. Done when: competition joined, simulation account created, agent created and connected, strategy saved, no setup errors.

Fixes when something breaks: key rejected → copy it again with no spaces; wrong account → make sure the simulation account and the agent belong to the same TQX user; setup stops → paste the whole prompt again in a new private session; page looks different → refresh and go back through Q → Competition → Join. Don't create a second account.

Open question for Mark: whether c.tqx.ai/set stays public after the event. Don't send viewers there until he confirms.

## The Claude / Codex connection

GATC agents can be built and connected from Claude or Codex via the command line (Mark, Oct 2026). On camera, keep it simple. Say what gets typed and what happens.

| Bad | Fixed |
|---|---|
| "You can build your team with Claude or Codex, right from your terminal, and plug it straight into GATC." (vague: plug what?) | "Just open Claude or Codex and type, 'Build me a team of agents for GATC. One reads the news, one makes the trades, and one can say no.' It sets the whole team up for you." |

## How the agent itself works (builder detail)

The platform mechanics (QuantFlow node types, the 5-slot agent group, natural-language order output, ticker formats) live in the existing `tqx-gatc-workflow` skill. Load that skill for anything technical about building a workflow. Don't copy its internals into scripts.

## What GATC is NOT

- Not a signal group or a copy-trading service.
- Not something a viewer has to put real money into to start. A simulation account works; going live is a choice, after testing.
- Not a guarantee of winning anything. Never imply a viewer will place or earn prize money.

## Not yet known (do not invent)

- Which features are live today vs on the roadmap.
- Leaderboard numbers, entrant counts, past winners.
- Entry fees or eligibility rules beyond the regions above.
- For live agents: whose money they trade, how much, and whether live and simulated agents are scored or ranked together. Don't say "real capital" without these answers.

## Links and handles

- Website: tqx.ai
- X: @tqx_trade · Instagram: @tqx.ai · Discord: via the QR on the workshop deck
- CTA keyword: GATC (see `cta-and-offer`)
