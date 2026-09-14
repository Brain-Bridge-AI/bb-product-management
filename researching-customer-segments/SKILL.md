---
name: researching-customer-segments
description: Research a customer segment using public data to help the user decide whether the segment they picked on their Lean Canvas is the right size and shape to pursue — big enough to matter, narrow enough to dominate, reachable for interviews. Input is a Lean Canvas or at minimum the Customer, Problem, and Solution from the canvas. Output is a segment research report delivered either inline in chat or as a Google Doc, the user picks. Use whenever the user says "research this segment", "is this segment big enough", "how big is the market for [segment]", "help me size the [X] opportunity", "pull public data on [segment]", "where do I find [segment] for interviews", "I need to validate my segment before interviews", or "pressure-test my segment". Do NOT use this to replace customer interviews or experiments — the skill is explicitly a pre-interview desk research step, not a substitute for hearing from real customers. Do NOT trigger for prospect-company research on a single target (use bb-prospect-research), for filling out the Lean Canvas itself (use populating-lean-canvas), or for post-interview customer analysis. Pairs with populating-lean-canvas upstream (where the segment was picked) and running-problem-interviews downstream (where the segment gets tested with real humans).
---

# Researching Customer Segments

## What this skill is for

You've picked a customer segment on your Lean Canvas and you want to know, before you go talk to anyone, whether it's the right size and shape to bet on.

This skill uses public data to answer three questions:

1. **Is the segment big enough to matter?** How many companies or people fit the definition? What's the rough revenue pool?
2. **Is it narrow enough to dominate?** (Moore's bowling pin test — can you be the clear best choice for this specific group?)
3. **Can you reach them for interviews?** Where do they gather, who do they trust, what filters identify them in Apollo / LinkedIn Sales Nav / industry rosters?

It is NOT a replacement for customer interviews or experiments. Desk research produces a defensible *hypothesis* about segment fit; real customers produce the evidence. If the user tries to use this skill to skip interviews, stop and route them to `running-problem-interviews`.

## What the skill needs as input

At minimum, the Customer + Problem + Solution from a Lean Canvas. Ideally the full canvas.

If the user only has a segment hypothesis without a canvas ("fractional CFOs at small businesses"), ask them for at least the problem they believe this segment has and the solution they're considering. Without those, the sizing exercise is just market research with no anchor to their bet.

If the user wants to pick a segment from scratch, route them to `populating-lean-canvas` first.

## Output

Ask the user: "Do you want this in chat or as a Google Doc?"

- **Chat**: deliver the report inline. Good for quick sanity checks, morning briefings, or when you're iterating fast.
- **Google Doc**: create via `gog docs create` to the appropriate project folder in Drive. Good for sharing with teammates or when the research is going to be referenced over weeks.

In either case, the report has the same four sections below.

## The report structure

Use this exact template:

```markdown
# Segment Research: [segment name]

- Date: YYYY-MM-DD
- Source canvas: [link to Lean Canvas doc, or "CPS only"]

## 1. Segment hypothesis (from the canvas)

- **Customer:** [verbatim from canvas]
- **Problem:** [verbatim from canvas]
- **Solution:** [verbatim from canvas]
- **Our bet:** [one-sentence restatement of why this segment, in plain words]

## 2. Size — is it big enough?

- **Estimated count:** [N companies or people matching the definition, with source]
- **Revenue pool (if B2B):** [rough revenue of the segment — $X billion in aggregate, with source]
- **Growth:** [shrinking / flat / growing, with source]
- **Geographic concentration:** [e.g., "60% of these companies are in TX, FL, CA" with source]
- **Filters that narrow from "anyone who might have the problem" to "this specific segment":** [explicit list — e.g., NAICS 238160 + 10-50 employees + uses AccuLynx + storm-chase business model]

Conclusion: [Big enough / Borderline / Too small] — one sentence on why.

## 3. Shape — is it narrow enough to dominate?

- **The "bowling pin" test** (from Moore): could you realistically be the #1 choice for this specific group in 18 months? If not, the pin is too fat — narrow further.
- **Compelling reason to buy NOW:** [regulatory shift, competitive pressure, funding event, seasonal trigger — anything that makes THIS the moment]
- **Observable behaviors that identify the segment:** [what they DO that signals they're in the segment — e.g., "posted a job for an ops manager in the last 90 days" or "switched from QuickBooks in the last year"]
- **Adjacent segments you might expand to later:** [the next bowling pins, per Moore's attack sequence]

Conclusion: [Narrow enough / Still too broad] — one sentence on why.

## 4. Reachability — can you find them to interview?

- **Where they gather:** [specific communities, events, Slacks, subreddits, associations, podcasts, LinkedIn groups]
- **Who they trust:** [analysts, publications, associations, specific thought leaders]
- **Filters for Apollo / LinkedIn Sales Nav / ZoomInfo:** [concrete filter stack you'd save as a list]
- **Candidate interview targets (5-10 named):** [real companies or people fitting the definition — from LinkedIn, industry rosters, 10-Ks, etc.]

## 5. What this desk research CANNOT tell you

A short list of questions that only real customer interviews can answer. Copy from `references/what-desk-research-cannot-tell-you.md`. Customize to the segment.

## Next step

Based on size + shape + reachability, the skill's recommendation:
- [Segment is viable — go run problem interviews with the candidates above. Route to `running-problem-interviews`.]
- [Segment needs narrowing — here's the next pin to try.]
- [Segment is too small or too hard to reach — reconsider the canvas. Route to `populating-lean-canvas`.]
```

## The research process

### Step 1 — Restate the segment hypothesis

Pull Customer + Problem + Solution from the canvas verbatim. Write your own one-sentence restatement of the bet. If you can't restate it in one sentence without hand-waving, the canvas itself is fuzzy — surface that back to the user before researching.

### Step 2 — Find the size

Use `references/data-sources-for-segment-research.md` for the specific public sources and what each produces. Don't invent numbers. Every claim in the Size section should cite a source (NAICS code, IBISWorld report, LinkedIn Sales Nav filter result, industry association roster, etc.).

If you can't defend the count within an order of magnitude, say so — "I estimate 5,000-50,000 businesses fit this definition; the uncertainty comes from [X]."

### Step 3 — Apply the bowling pin test

Moore's question: *Could you realistically be the #1 choice for this specific group within 18 months?*

If the segment is "small businesses" or "SMBs" or "CFOs" — too fat, narrow. If it's "fractional CFOs helping roofing contractors with storm-chase billing in TX/FL in the 10-50-employee range" — getting closer to a pin.

Narrow until narrowing further would either (a) eliminate real candidates you can reach or (b) make the segment too small to matter.

### Step 4 — Find observable behaviors

Desk research can surface these without interviews:
- Recent hiring (job boards) — "hired an ops manager in the last 90 days"
- Recent tool adoption (technographic data, G2 reviews, case studies)
- Recent triggering events (funding rounds, new leadership, regulatory shifts)
- Community participation (posting in specific subreddits, attending specific conferences)

Observable behaviors are the segment's identifiers. They also become the recruiting filters for interviews.

### Step 5 — Build a candidate interview list

Produce 5-10 named companies or people who demonstrably fit the segment definition. Use LinkedIn, industry association rosters, G2 reviews, 10-Ks, podcast guest lists. These are the first interview targets for `running-problem-interviews`.

### Step 6 — List what you still don't know

This is the most important section of the report. Pull from `references/what-desk-research-cannot-tell-you.md` and customize to the segment. This is what forces the user to go talk to real humans.

### Step 7 — Deliver

Ask the user: chat or Google Doc? Then deliver.

After delivery, consider invoking `capturing-customer-insights` on the report. The size claims, observable behaviors, and filter stack are candidate insights worth filing into the segment folder so the next researcher (or the interviewer after Phase 1 calls) starts from what we already know. Optional — especially valuable if this is the first pass on a segment.

## Hard rule — this skill does not replace interviews

If the user's prompt or follow-up suggests they're using this research to *decide* whether the segment is the right bet, redirect:

"Desk research tells you whether the segment is the right size and shape to bet on — not whether the bet itself is sound. The only way to know if the customers actually have this problem, will pay to solve it, and will change their behavior for your solution is to talk to real customers. I can produce the research now; you still need to run interviews and experiments before committing. Want to continue?"

Never produce a report that lets the user skip the interview phase. See `references/what-desk-research-cannot-tell-you.md` for the explicit list of questions this skill can't answer.

## Integration with other skills

- **`populating-lean-canvas`** — upstream. The segment hypothesis comes from here. If there's no canvas and no CPS, route back before researching.
- **`running-problem-interviews`** — downstream. The candidate list and recruiting filters from this skill feed directly into interview prep.
- **`running-rapid-experiments`** — downstream. If the segment passes desk research and initial interviews, the segment definition becomes the recruit screener for experiments.
- **`bb-prospect-research`** — different job. That skill researches ONE target company for sales. This skill researches a SEGMENT of many companies for canvas validation.
- **`using-gog`** — used to create the Google Doc output if the user picks that format.

## References

- `references/data-sources-for-segment-research.md` — what each public data source produces, with example queries.
- `references/what-desk-research-cannot-tell-you.md` — the hard list of questions only real customers can answer; copy into every report's Section 5.
- `references/bowling-pin-sizing.md` — Moore's narrowing approach with worked examples of "too fat" vs. "right-sized" segments.
