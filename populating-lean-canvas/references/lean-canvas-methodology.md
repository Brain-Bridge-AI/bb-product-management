# Lean Canvas Methodology

The customer-world-alignment approach to filling a Lean Canvas, grounded in how practitioners actually work (not how textbooks describe the boxes).

## The meta-principle that makes everything work

**Every box is a different view of the same customer's world.** Segments names who they are. Problem names what hurts. Solution names what relieves the hurt. Channels names how they get found. Revenue names how they pay. Cost names what it takes to deliver. Metrics names how to tell it's working. UVP names the post-solution world in a sentence. Unfair Advantage names why nobody else can deliver it.

If any box starts feeling like abstract strategy, come back to the anchor customer. Re-imagine them. Re-read what they said. Every decision on the canvas runs through that filter.

## The anchor

Pick a specific real customer. Named. Concrete. Someone the user has talked to, observed, or worked alongside. The entire canvas is filled in that person's frame. This is non-negotiable.

If the user doesn't have one, halt the session. A Lean Canvas without a real anchor is guessing on paper — the friction between assumptions and what a real person said is the only thing that makes the canvas useful.

## Shoe-stepping

Before touching boxes, actively step into the customer's perspective. The user should be able to:

- Visualize what the customer looks like
- Recall what they said, especially verbatim
- Imagine the situation their organization is in
- Feel what they're feeling — frustration, curiosity, ambition, fear

This isn't a pre-step — it's a mode sustained across the whole session. Whenever the user loses the thread on a box, bring them back here.

## The nine boxes

### 1. Customer Segments (always first)

The anchor box. Everything else in the canvas derives from and must connect back to this.

- Fill by brainstorming **unique attributes and observable behaviors** of the anchor customer.
- Reject demographics. Demographics are shorthand for behaviors. Unpack them. See `segments-behaviors-not-demographics.md`.
- Name the **early adopter** explicitly (as distinct from the broader future market). The canvas is filled for the early adopter.
- Qualify the early adopter via the **rip-it-out-of-my-hands test**: would they take an MVP right now because their situation is too painful to wait? Running this test requires articulating the pain, which is why Segments and Problem are a linked pair.

### 2. Problem (linked to Segments)

Three named sub-fields — not one. See `problem-sub-fields.md` for how to fill each:

- **Pains / what's getting in the way**
- **Desired outcomes**
- **Existing alternatives**

Brainstorm widely, then winnow. Use verbatim customer language wherever possible.

### 3. Solution (glance-back to Problem)

The minimum features that address the top pains. Not the roadmap. Not the vision.

**Glance-back discipline:** for every solution item you write, immediately look at the Problem box and verify it ties directly to a specific pain. If it doesn't, cut it or mark it speculation. Solution creep is the failure mode here.

### 4. UVP (seed-mode)

See `uvp-seed-principles.md` for the full seed protocol. In short: the skill supplies principles + drafts 2-4 candidate UVPs grounded in this session's Problem + Solution content, and the user reacts. Two sub-fields:

- Primary UVP sentence (customer-world / vision-statement shape)
- High-level concept (X for Y analogy)

### 5. Channels

How the early adopter gets found / reached / onboarded.

- Depth is calibrated to data. If the user knows little about how this customer makes buying decisions, write the 2-3 channels they genuinely have and flag it as a learn-about-this area. **Shallow-but-honest > padded-and-confident.**
- Distinguish **validated** channels (actually used to reach this customer) from **assumed** channels.
- Staged GTM is valid: "sales-led now, self-serve later as onboarding streamlines."
- Generate a specific **channel-learning probe** for the Go-learn-this list (e.g., "how did your organization decide on your current software purchases?").

### 6. Revenue Streams

How value is captured.

- Name the pricing model(s): upfront services, usage-based, subscription, etc.
- **Match to how the customer already pays for similar things.** Pricing that clashes with the customer's existing spend model creates education cost — flag it explicitly.
- Capture ranges where possible.

### 7. Cost Structure (cross-canvas scan)

See `cross-canvas-scan-for-costs.md` for method. In short: Cost isn't a standalone box — it's a synthesis across Solution (build + implement) + Channels (reach + onboard) + ongoing ops (infra, platform fees, team time).

**Numbers are required, not optional.** The ROI check (Cost vs. Revenue) is a completion criterion of the initial fill. If the user balks at numbers, prompt for ranges — even rough ballparks work.

### 8. Key Metrics

**Product-specific success metrics only.** Not revenue, expenses, MRR, or active users — those are baseline business metrics that live elsewhere.

Key Metrics in this box answer one question: **what numbers tell us this specific product is solving this specific customer's pain?** Every metric traces back to a Problem-box pain (glance-back discipline again).

1-2 metrics. A dashboard doesn't belong here.

### 9. Unfair Advantage (seed-mode, last)

See `unfair-advantage-seed-principles.md` for the full seed protocol. In short: Jason Cohen's rule ("can't be easily copied or bought") plus the "lots of people like that" disqualifier, plus the padding list, plus the durable-advantage list. **"None yet" is a valid and often correct answer** — padding hides the real question.

This box is last because running the other boxes first usually reveals what's actually defensible, or clarifies that nothing is yet.

## Provenance is everything

Every item in every box gets one of three tags:

- `[heard]` — direct from the anchor customer, verbatim preferred
- `[assumed]` — inferred, not yet validated
- `[★ best-guess]` — probable top priority among multiple candidates, needs confirmation

A canvas mostly covered in `[assumed]` is an honest signal, not a failure. The honest canvas shows you where to focus the next phase of customer conversations. A canvas where everything looks confident but is actually assumption is the real failure.

## Brainstorm-broadly-then-winnow

Every box, every time. Dump everything the user has before selecting what lands in the box. This isn't a test with a right answer — it's exploration with a structured output.

Corollary: boxes bleed. Working one box often surfaces insights that belong to another. Capture them in the sticky-notes register and keep working the current box.

## Back-edits during initial fill

As later boxes reveal new understanding, **back-edit the earlier boxes in place**. This is the dance working correctly during first-pass authoring, not a phase violation.

Distinct from post-fill iteration, which is out of scope for this skill — that's what happens after the initial fill is done and the user returns with validated learnings from customer conversations or experiments.

## Close-out

1. Sticky-notes sweep — place parked items in correct boxes.
2. Back-edit sweep — apply any pending back-edits surfaced late.
3. Go-learn-this list — translate every `[assumed]` / `[★]` / thin-box item into a specific customer question.
4. ROI check — Cost vs. Revenue; flag canvas-level verdict.
5. Canvas summary — one paragraph on what the canvas says and where the weak spots are.
6. Write the file. Remind the user the next phase (validation) is out of scope for this skill.
