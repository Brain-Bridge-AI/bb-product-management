---
name: capturing-customer-insights
description: Capture customer insights into a segment-organized Google Drive repository that compounds over time. The skill proactively drafts candidate insights from interview debriefs, experiment results, desk research, or ad-hoc observations; presents them to the user one at a time for approve / edit / reject; and writes only approved insights as Google Docs in the appropriate segment folder. Use whenever the user says "capture insights from [debrief]", "log what we learned", "add insights for [segment]", "what do we know about [segment]", "pull insights from this interview", "compound what we just learned", or any time a customer-facing artifact (interview, experiment, research report, transcript) has just been produced and the findings should outlive the artifact. Also triggers as the downstream step after running-problem-interviews, running-rapid-experiments, and researching-customer-segments. Do NOT trigger for capturing internal team lessons-learned (different scope), for personal journal entries (belongs in Obsidian daily notes), or for sales-deal-specific notes (use planning-outreach or deal records in Airtable). Pairs upstream with running-problem-interviews, running-rapid-experiments, researching-customer-segments, and populating-lean-canvas (provides evidence to ground canvas entries).
---

# Capturing Customer Insights

## What this skill is for

A customer insight repository that accumulates what Brain Bridge and AI Trailblazers learn about specific customer segments over time. Each insight is a small Google Doc with structured front matter, stored in a segment folder. Existing skills invoke this one during their debrief step to surface candidate insights, prompt for approval, and write only approved ones.

**The job is narrow:** suggest insights → prompt user → write approved insights. It does NOT do interview prep, experiment design, or segment research — those belong to their own skills. This skill owns one step: turning a raw debrief into durable, searchable findings.

## Where it lives

Two parallel repositories, one per organization:

- **Brain Bridge:** [Customer Insights root folder](https://drive.google.com/drive/folders/1NtO0j9Y85VlYBfJHu7vCzOZDFVdIth0g) — folder ID `1NtO0j9Y85VlYBfJHu7vCzOZDFVdIth0g`, account `aaron@brainbridge.app`.
- **AI Trailblazers:** [Customer Insights root folder](https://drive.google.com/drive/folders/1HZ71XysToA6WY4YIi7ubNfn_K3c9jenI) — folder ID `1HZ71XysToA6WY4YIi7ubNfn_K3c9jenI`, account `aaron@aitrailblazers.org`, on the AITB shared drive so the team can access.

Ask the user which organization if it's ambiguous. BB and AITB insights stay separate — they're different customer worlds with different segments.

## Folder and file layout

Under each root:

```
Customer Insights/
├── [segment-slug]/
│   ├── Segment Definition — [Segment Name]   ← live canvas-level definition
│   ├── YYYY-MM-DD — [short insight title]     ← one Google Doc per insight
│   ├── YYYY-MM-DD — [short insight title]
│   └── ...
├── [another-segment]/
└── ...
```

Segment slugs are kebab-case, descriptive. Examples: `fractional-cfos-small-b2b`, `roofing-contractors-tx-storm-chase`, `aitb-event-sponsors-midsize-tech`.

## Insight Google Doc structure

Every insight Doc opens with a front-matter block (plain text at the top, human-readable), then the insight content. Use this exact structure:

```
---
Segment: [segment-slug]
Date: YYYY-MM-DD
Source: problem-interview | experiment | desk-research | observation | transcript
Source Ref: [link to source doc — debrief, experiment report, transcript, etc.]
Confidence: high | medium | low
Supports: [comma-separated list of canvas assumptions or LoFAs this supports]
Contradicts: [comma-separated list of canvas assumptions or LoFAs this contradicts]
Tags: [comma-separated: pricing, buying-behavior, workarounds, etc.]
---

# [One-line headline of the insight]

One paragraph of the insight in plain language. What did we learn?

## Source quote (if available)

"Verbatim customer quote, exact words."

## Implications

What this changes about the canvas, experiment, strategy, or pitch. Specific, not abstract.
```

## The suggest-and-prompt workflow

This is the core of the skill. Run this flow whenever a debrief, experiment, or research artifact lands.

### Step 1 — Gather the raw material

Ask the user which artifact you're pulling insights from. Accept:
- A Google Doc URL (interview debrief, experiment debrief, research report, meeting transcript)
- A file path (Obsidian debrief note)
- Text pasted inline
- Or "from our conversation" — pull from the current session's recent work

Read the source. Identify which organization (BB or AITB) and which segment. If segment is ambiguous, ask the user.

### Step 2 — Draft candidate insights

Scan the source for:
- **Unprompted customer mentions** — tagged `[UNPROMPTED]` in debriefs, or surfaced in raw transcripts as things the customer raised without being asked. These are always candidate insights.
- **Verbatim customer quotes** that carry weight. The quote is the evidence.
- **Behavioral observations** — what customers did, not what they said.
- **Surprises** — anything the interviewer flagged as unexpected.
- **Experiment findings** — what supported or contradicted the hypothesis.
- **Desk research findings** — size, shape, reachability claims with sources.

For each candidate, draft the full insight Doc structure (front matter + headline + paragraph + quote + implications). Assign a proposed Confidence level:
- **High** — direct behavior observed from 3+ customers, OR experiment data from 3+ customers, OR cited public data.
- **Medium** — one customer's direct behavior, OR a strong unprompted mention, OR a vivid past-behavior story from one person.
- **Low** — single compliment, hypothetical, future promise, or conjecture. Usually these shouldn't be captured at all — only capture if the source/context makes them worth revisiting.

Typical yield: 3-7 candidate insights per problem-interview debrief; 2-5 per experiment; 4-8 per desk research report.

### Step 3 — Prompt the user, one insight at a time

Present candidates one at a time, not all at once. For each:

1. Show the drafted Doc content (front matter + body, rendered as a preview block).
2. Ask: **"Approve / edit / reject?"**
3. If **approve** — write the Doc to the appropriate segment folder (see step 4).
4. If **edit** — let the user dictate changes, redraft, re-show, re-ask.
5. If **reject** — drop it, move on.

Never batch-approve. Each insight gets individual judgment because confidence and framing vary case-by-case.

### Step 4 — Write approved insights to Drive

For each approved insight:

1. Confirm (or create) the segment folder. If the segment folder doesn't exist yet, create it with `gog drive mkdir "[segment-slug]" --parent [root-folder-id] --account [account]`.
2. Create the Google Doc: `gog docs create "YYYY-MM-DD — [short title]" --parent [segment-folder-id] --account [account]`.
3. Populate the Doc: clear it, write a PLACEHOLDER marker, then use `gog docs find-replace [docId] "PLACEHOLDER" --content-file [path] --format=markdown` to render the markdown.
4. Confirm the Doc link with the user.

If the segment definition Doc (`Segment Definition — [Segment Name]`) doesn't exist in the folder yet, offer to create one. It captures the canvas-level segment info (see `references/segment-definition-template.md`).

### Step 5 — Return a summary

After all approved insights are written, give the user:
- A count (N insights approved, M edited, K rejected).
- Links to each new Doc.
- A note on whether the segment folder is new or existing.
- Any flags — e.g., "3 of 5 insights had `Confidence: low` and I flagged them for reject, you approved anyway — consider if these belong."

## Reading insights — the other half

The skill also supports **reading** existing insights when the user or another skill asks "what do we know about [segment]?"

### Step R1 — Find the segment folder

List folders in the appropriate Customer Insights root. Fuzzy-match against user's segment reference if needed.

### Step R2 — List insight Docs

Return titles + dates. If the user wants to filter, accept:
- By source type (problem-interview / experiment / desk-research / observation)
- By confidence (high / medium / low)
- By tag
- By supports or contradicts (give me insights that support LoFA X)

### Step R3 — Summarize

When the user asks for a summary (or another skill is reading for prep), return:
- The segment definition (from `Segment Definition — ...` doc if it exists).
- Top 5-10 insights by confidence, with headline + one-line paragraph.
- Any contradictions between insights — call these out explicitly.
- Last-updated date.

Keep the summary tight. Tens of insights should collapse to a ~300-word brief.

## Integration with other skills

Other skills invoke this one via these hooks:

| Skill | When | What it passes |
|---|---|---|
| `running-problem-interviews` | End of debrief (Phase C) | The debrief Google Doc URL + segment reference |
| `running-rapid-experiments` | End of cycle (Persevere/Pivot/Stop decision) | Experiment debrief + supported/contradicted assumptions |
| `researching-customer-segments` | End of desk research report | The research Doc + segment |
| `leading-experiment-reviews` | Read-only, during leader's prep | Segment name |
| `populating-lean-canvas` | Read-only, during canvas drafting | Segment name |

The invoking skill doesn't duplicate the suggest-and-prompt logic. It just says "now invoke `capturing-customer-insights` on this artifact" and passes the source.

## Organization routing

When in doubt about whether an insight goes to BB or AITB:

- BB: any insight about a prospective or current Brain Bridge consulting customer, their problems, their buying behavior, or their industry.
- AITB: any insight about AITB event participants, sponsors, mentors, community members, or the nonprofit/community space.
- Some insights could serve both (e.g., general observations about how CFOs evaluate AI tools). Default to the primary source's org, note in the insight body that it may also apply to the other org.

## Hard rules

- **Never write an insight without user approval.** Auto-capture is tempting but produces noise that buries signal. The prompt step is the quality gate.
- **Always capture verbatim quotes when they exist.** Paraphrases rot; quotes travel.
- **Capture unprompted mentions even if they're outside the current scope.** They're gold. A roofing-contractor insight that surfaces during a fractional-CFO interview still goes in the roofing folder.
- **Never auto-mark an insight `high` confidence.** Default to `medium`; let the user upgrade to `high` if the evidence warrants.
- **Do not summarize multiple customer interactions into one insight.** One insight = one source. If three interviews support the same pattern, write three insights and link them via `Supports: [same-assumption-id]`, not one rolled-up insight.

## References

- `references/segment-definition-template.md` — the structure for the live `Segment Definition — ...` doc at the top of each segment folder.
- `references/suggest-insights-prompts.md` — the specific prompts for scanning interview debriefs, experiment reports, and desk research for candidate insights.
- `references/gog-commands.md` — the exact `gog` commands for creating folders, creating Docs, and writing markdown-formatted content.
