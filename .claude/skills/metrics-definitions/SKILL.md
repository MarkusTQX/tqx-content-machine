---
name: metrics-definitions
description: Which Instagram numbers to pull from Metricool for each TQX Reel and account, what each one means, which fields are deprecated, and how to compare videos fairly (same age, per reach, organic vs paid). Use when the Analytics agent pulls metrics, when matching a post to its video code, or whenever anyone compares how TQX videos performed.
---

# Metrics definitions

Source of data: **Metricool** (connected Oct 21 2026). No Meta developer app is needed; Metricool pulls Instagram insights itself. Pull with the Metricool tools `getAnalyticsDataByMetrics` and `getAnalyticsAvailableMetrics`.

Connected so far: one brand, Instagram **markus_ai_quant** (brand timezone Asia/Bangkok). Any other account (@tqx.ai, Joshua's) must be added in Metricool before it can be measured.

This file defines the numbers. It does not set targets; targets live in `content-scorecard` once Mark sets them.

## Per-Reel metrics (network `instagram`, connector `reels`)

| Field ID | Metric | What it means | Use it for |
|---|---|---|---|
| IGRE02 | Date with time | When the Reel was posted | Age of the post |
| IGRE03 | Content | The caption text | Matching to the video code |
| IGRE06 | Reel url | Link to the Reel | Matching to the video code |
| IGRE04 | Reel Id | Instagram's ID | Joining tables |
| IGRE23 | Views | Times the video was watched (organic) | Headline number |
| IGRE11 | Reach | Unique people who saw it (organic) | The base for every rate |
| IGRE28 | Reel view rate | % of views from people who watched more than 3 seconds | **Hook strength** |
| IGRE27 | Retention | Average % of the video watched | **Holding attention** |
| IGRE24 | Average watch time | Average seconds watched | Compare with video length |
| IGRE26 | Video duration | Length in seconds | Needed to read watch time |
| IGRE25 | Video view total time | Total time watched | Overall attention |
| IGRE10 | Likes | Organic likes | Engagement |
| IGRE07 | Comments | Organic comments | Engagement; keyword CTA response (QUBE, GATC) |
| IGRE12 | Saved | Organic saves | "Worth keeping" signal |
| IGRE21 | Shares | Organic shares | "Worth sending" signal; strongest reach driver |
| IGRE29 | Reposts | Reposts | Sharing signal |
| IGRE09 | Interactions | Likes + comments + saves + shares (organic) | Total engagement |
| IGRE08 | Engagement | Interactions per 1,000 people reached (organic) | Engagement rate |
| IGRE14 / IGRE16 / IGRE17 / IGRE18 / IGRE20 | Paid views / paid reach / paid interactions / paid clicks / spend | Boosted-post numbers | Only for boosted Reels; keep separate |
| IGRE22 | Interactions total | Paid + organic | Only when you mean both |

**Never use (deprecated):** IGRE13 "Video Views" and IGRE15 "Video Views total". Use IGRE23 Views.

## Account metrics (network `instagram`, connector `evolution`)

| Field ID | Metric | Use it for |
|---|---|---|
| IGEV01 | Followers (current) | Account size |
| IGEV43 / IGEV44 | Followers gained / lost | Net growth per period |
| IGEV22 | Reels published | Output volume |
| IGEV23 | Reels views | Total Reel views in the period |
| IGEV26 | Reels reach | People reached by Reels |
| IGEV30 | Avg reach per Reel | Typical Reel reach |
| IGEV39 | Reels shares | Shares across all Reels |
| IGEV42 | Accounts engaged | Unique accounts that interacted |
| IGEV06 | Account reach | All formats, organic + paid |

**Never use (deprecated):** IGEV03 Follows, IGEV07 Profile views, IGEV10 Website clicks, IGEV32–IGEV36 click fields.

Note: "Feed Posts" fields (IGEV04, IGEV09, IGEV11–IGEV15, IGEV40) exclude Reels. Don't use them for Reels.

## Derived numbers (calculate these)

| Name | Formula | Why |
|---|---|---|
| Shares per 1k reach | Shares ÷ Reach × 1,000 | Compares how shareable videos are, regardless of size |
| Saves per 1k reach | Saved ÷ Reach × 1,000 | Compares "worth keeping" |
| Comments per 1k reach | Comments ÷ Reach × 1,000 | Compares conversation and CTA response |
| Watch-through | Average watch time ÷ Video duration | Checks the Retention field; flags long videos |

## Comparing videos fairly

1. **Same age.** Compare videos at the same age: 48 hours and 7 days after posting. A 2-day-old Reel and a 3-week-old Reel can't be compared on totals. Snapshot each Reel's numbers at 48h and 7d.
2. **Rates over totals.** Use view rate, retention and the per-1k numbers to compare. Totals depend on reach, which depends on luck and timing.
3. **Organic and paid apart.** Never mix boosted numbers into organic comparisons.
4. **Same account.** Compare Mark's videos with Mark's, Joshua's with Joshua's. Different accounts have different audiences and sizes.
5. **Small samples.** Under 5 videos of a kind is anecdote, not a pattern. Say so.
6. **One thesis per video.** Tag each video with its type (from the brief) so results can be grouped.

## Matching a Reel to its video code

Metricool doesn't know our codes (J001, M05). Keep a mapping table: video code → Reel URL (IGRE06) → post date. It lives in `content-machine/data/video-map.csv` (columns: code, presenter, title, reel_url, reel_id, posted_at). The 48h and 7d snapshots go in `content-machine/data/snapshots/{code}_48h.json` and `{code}_7d.json`. Fill it in on the day each video is posted. If a caption includes the title, match on that as a fallback, then confirm with Mark.

## What Metricool doesn't give

- **The second-by-second retention curve.** Metricool gives average retention (IGRE27) and the 3-second view rate (IGRE28), not where people dropped off. For drop-off points, Mark screenshots the retention graph in the Instagram app for each post.
- Comment text for keyword counts: check ManyChat or Instagram directly.
