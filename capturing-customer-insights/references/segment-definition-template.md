# Segment Definition Template

Each segment folder gets one live document titled `Segment Definition — [Segment Name]` at the top. It's the canvas-level snapshot of who this segment is, refreshed as the team learns.

This Doc is different from individual insights — it's the **distillation**, not a single finding. It gets rewritten (not appended to) as understanding deepens.

## Structure

Use this exact outline when creating a new segment definition:

```
---
Segment: [kebab-case slug]
Org: BB | AITB
Status: active | paused | graduated | abandoned
Last Updated: YYYY-MM-DD
Insight Count: [how many insight Docs back this definition up]
---

# [Human-readable segment name]

## One-sentence identity
[The segment in one sentence. Specific enough for Moore's bowling-pin test.]

## Who they are
- [Attributes — firmographics if B2B, or demographic + behavioral if B2C]
- [Observable behaviors that identify them]
- [Trigger events that make NOW the right time]

## Core problems we believe they have
1. [Problem 1 — link to insights that support this]
2. [Problem 2 — link to insights that support this]
3. [Problem 3 — link to insights that support this]

## What we know about how they buy
- [Buying committee shape, decision-maker identity]
- [Price sensitivity and format preference]
- [Switching costs and inertia]

## Where they gather / who they trust
- [Communities, events, publications, analysts]

## Active assumptions we're testing
- [LoFA 1 — link to experiment in progress]
- [LoFA 2 — link to experiment in progress]

## What contradicts our current picture
- [Insights that complicate the story — link them]

## Size & reachability (from researching-customer-segments)
- Estimated count: [N, with source]
- Revenue pool: [if B2B, with source]
- Filter stack for outreach: [NAICS + headcount + geography + behavioral]

## Current canvas / experiments
- Lean Canvas: [link]
- Active experiments: [links]

## Related segments
- Adjacent bowling pins: [links]
- Graduated from: [if this segment narrowed out of a broader one]
```

## When to update

The segment definition gets rewritten whenever:

- A new insight materially changes one of the sections (e.g., new evidence about buying committee shape, new trigger event discovered).
- An experiment produces a persevere or pivot decision that shifts the segment's shape.
- A desk research pass refines the size, reachability, or filter stack.
- The segment itself narrows or splits into multiple sub-segments.

Bump the `Last Updated` date and `Insight Count` every time.

## When NOT to update

Don't update when:

- A single new insight just adds nuance without changing the picture — let it live in its own Doc, not the definition.
- You're tempted to add everything you learned — the definition is the distillation, not the archive.

## Rule of thumb

If you can't read the segment definition in under 3 minutes, it's too long. Keep the ruthless summary bias — individual insight Docs carry the detail, the segment definition carries the shape.

## Who owns updating it

The person closing the loop on the triggering artifact (the interviewer after a debrief, the experiment driver after a cycle, the researcher after a desk pass). The `capturing-customer-insights` skill, invoked at the end of those workflows, should prompt: "This new insight seems to change [section of segment definition]. Should I update the segment definition Doc?"
