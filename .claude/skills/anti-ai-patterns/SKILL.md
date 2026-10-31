---
name: anti-ai-patterns
description: Banned patterns that make a TQX script sound AI-written - "it's not X, it's Y", decorative lists of three, em dashes, stock openers, buzzwords, rhetorical-question chains, colon reveals, hedging, summary endings and motivational filler - each with a fix, plus patterns a code checker can catch. Use when drafting or reviewing any TQX script, caption or DM.
---

# Anti-AI patterns

Viewers clock these in a second, and Frank (the skeptic) will say so in the comments. Each pattern below has a bad line and a fixed line. The last section lists what the automatic script checker should flag.

## Banned patterns

### 1. "It's not X, it's Y"
| Bad | Fixed |
|---|---|
| "It's not about the tool. It's about the rules." | "The tool doesn't matter much. Your rules do." |
| "This isn't trading. It's gambling." | "That's gambling. You just called it trading." |

### 2. Decorative lists of three
Three adjectives or three parallel phrases added for rhythm. A real list of three things is fine; three words for one thing isn't.
| Bad | Fixed |
|---|---|
| "It's fast, simple and powerful." | "It took me 40 seconds." |
| "No emotions. No guessing. No mistakes." | "It doesn't panic when the price drops." |

### 3. Em dashes
Never in spoken lines or on-screen text. Use a period or a comma.
| Bad | Fixed |
|---|---|
| "The backtest looked perfect — then it went live." | "The backtest looked perfect. Then it went live." |

### 4. Stock openers and transitions
"Here's the thing", "Let's dive in", "Let's break it down", "In today's world", "Buckle up", "Picture this:" as a crutch, "Here's why that matters".
| Bad | Fixed |
|---|---|
| "Here's the thing: most traders lose." | "In India, 93% of people trading futures and options lost money over three years." |
| "Let's break it down." | Cut it. Go straight to the first point. |
| "Usually, turning a research paper into something tradable means hours of reading..." (also "Instead, I connect...", "Claude actually reads...") | "Turning a research paper into something tradable means hours of reading, decoding equations, and manually implementing the strategy. Or does it?" (Mark, J031: lead-in words cut) |

"Picture this:" as an opener is banned. Using "picture" to set up a made-up number is fine, and `finance-compliance` requires it (or "say", or "for example"): "Picture you had $10,000."

### 5. Buzzwords
"game-changer", "revolutionary", "unlock", "supercharge", "seamless", "cutting-edge", "next level", "leverage" as a verb, "delve", "harness", "empower", "elevate".
| Bad | Fixed |
|---|---|
| "AI is a game-changer for traders." | "AI can test an idea on ten years of prices in a minute." |

### 6. Rhetorical-question chains
One question can hook. Two or three in a row is a tell.
| Bad | Fixed |
|---|---|
| "Want to trade smarter? Tired of losing? Ready to try AI?" | "Be honest: are you actually making money day trading after fees?" |

### 7. Colon reveals
| Bad | Fixed |
|---|---|
| "The secret to beating the market: patience." | "In 2024 the S&P 500 went up 25%. The average fund investor made 16.5%." |

### 8. Hedging
"might potentially", "arguably", "it could be said", "in some cases", "generally speaking".
| Bad | Fixed |
|---|---|
| "This could potentially help some traders." | "This is how you find out if your idea works before it costs you money." |

When a fact needs a limit, state the limit exactly instead of hedging: "In one study of Taiwanese day traders..."

### 9. Summary endings
"So, to sum up", "In short", "At the end of the day", "The bottom line is".
| Bad | Fixed |
|---|---|
| "So, to sum up: test before you trade." | End on the payoff or the CTA. "Comment QUBE and I'll send you the free link and a step-by-step on building your first strategy." |

### 10. Motivational filler
"You've got this", "Your future self will thank you", "The journey starts today", "Let's get it".
| Bad | Fixed |
|---|---|
| "Start your trading journey today." | Cut it. |

### 11. Over-tidy symmetry
Every line the same length and shape, every point getting a matching one-liner. Vary it the way people talk.

## For the automatic checker (code)

Flag every match for a human to review. Case-insensitive.

| Check | Pattern |
|---|---|
| Em dash | `—` |
| Not X, it's Y | `\b(it'?s not|it isn'?t|it wasn'?t|this is not|this isn'?t|this wasn'?t|that'?s not|that isn'?t|that wasn'?t|they'?re not|they aren'?t|you'?re not|you aren'?t)\b.{0,60}?[.,;]\s*(it'?s|it was|this is|that'?s|they'?re|you'?re)\b` |
| Stock openers | `here'?s the thing|let'?s dive in|let'?s break it down|buckle up|in today'?s|picture this` |
| Buzzwords | `game[- ]changer|revolutioni[sz]e|unlock|supercharge|seamless|cutting[- ]edge|next level|delve|harness|empower|elevate` |
| Hedging | `might potentially|could potentially|arguably|it could be said|generally speaking` |
| Summary endings | `to sum up|in short,|at the end of the day|the bottom line is` |
| Motivational filler | `you'?ve got this|future self|your journey` |
| Question chains | two or more lines in a row ending in `?` |
| Banned finance phrases | see `finance-compliance` (guaranteed, risk-free, passive income, can't lose) |
| Off-glossary terms | any word in the "Never say" column of `terminology` |
| Long sentences | more than 20 words between sentence ends |
