---
name: populating-lean-canvas
description: Fill a Lean Canvas for a product, feature, or business idea through a customer-anchored interview, not a form-fill. The skill sustains a real-customer focus throughout, qualifies the early adopter using the "rip it out of my hands" test, brainstorms each box broadly before winnowing, enforces provenance (heard-from-customer vs. assumption vs. best-guess), and visibly distinguishes all three. Most boxes are elicited from the user's direct customer knowledge; UVP and Unfair Advantage are seeded by the skill because users commonly lack instincts there. Output is a Markdown 9-box canvas with full provenance, a distilled "go learn this" list of gaps, and a rough ROI check. Use this skill whenever the user says "do a lean canvas for X", "fill out a canvas for this product idea", "populate the canvas for <company/feature>", "help me think through <product> with a canvas", "what does the canvas say about <idea>", "stress-test this with a canvas", "give me the 9-box view of this product", or when any strategy/product/sales conversation surfaces a new offering that doesn't have a canvas yet. Do NOT trigger for Business Model Canvas (different tool — 9 different boxes), CPS Zooms (use product-management), pitch-deck generation (use using-gamma or generating-pitch-decks), post-fill validation work, or iteration on an already-filled canvas.
---

# Populating a Lean Canvas

## The meta-principle (read this first)

A Lean Canvas is a **customer-world-alignment exercise**, not a strategy document. Every box — segments, problem, pricing, channels, metrics, UVP, everything — is a different facet of the same discipline: **align with how the customer sees the world.**

If you forget this in the middle of filling a box and start writing what you think the world is like, stop and come back to what the customer would say, do, spend, and feel.

## Hard halt: no customer, no canvas

Before anything else, check for a specific real anchor customer — named, concrete, a real person or organization the user has actually talked to or observed.

If the user doesn't have one, halt and say something like:

> "Without at least one real customer conversation, a Lean Canvas is guessing on paper. The value of the canvas comes from the friction between your assumptions and what a real person actually said or did. Have at least one conversation first — it doesn't have to be a formal interview, just a real exchange about the problem — then come back and we'll fill the canvas together."

Do not proceed with a fictional or aggregate customer. The entire workflow depends on a real anchor.

## Phase boundary

This skill covers **initial fill only.** What happens to red or starred items afterwards — customer empathy work, behavioral experiments to convert assumptions into facts — is a separate phase the user handles elsewhere.

Inside initial fill, however, back-edits to earlier boxes as later boxes reveal new understanding are **expected and welcome.** Working Channels might reveal a missing Segments attribute; that's the dance working correctly during first-pass authoring, not a phase violation.

If the user drifts into post-fill activities mid-session (validation plans, experiment design, customer outreach planning), flag it: "That's a post-fill activity — let's park it for after the canvas is done." Capture the parked thought in the sticky-notes register and continue.

## Inputs to ask for

1. **Product / feature / idea name** — what are we canvassing?
2. **Anchor customer** — name + one sentence of context. Non-negotiable. If missing, halt per above.
3. **What you know about this customer** — notes, transcripts, memories of conversations, things they said verbatim.
4. **Known competitors or existing vendors** the customer uses or has considered. Seeds the Existing Alternatives sub-field.
5. **Pricing model** for comparable offerings the customer currently pays for. Seeds Revenue alignment.
6. **Output location.** Default: `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/2nd Brain (I)/1-Projects/<project>/lean-canvas.md` (Obsidian). Override if user prefers.

If the user only gives you the product name, start asking for the others one at a time. Don't batch the questions.

## Shoe-stepping prep (explicit, before any box)

Before touching boxes, prompt the user to actively step into the customer's perspective. This isn't metaphorical — it's the active, sustained mode that makes the canvas a real customer-world document instead of a strategy fiction.

> "Before we start filling boxes, take a minute and put yourself in [anchor customer]'s shoes. What do they look like? What did they actually say? What's the situation their organization is in? In a perfect world, try to feel what they're feeling right now — frustration, fear, ambition, whatever it is. Tell me what comes to mind."

Explicit emotional simulation matters. "In a perfect world you want to try to feel some of the emotions that customer is feeling." A canvas built from cognitive speculation about a customer's state is weaker than one built from a real attempt to inhabit their frame.

Capture whatever the user says into a buffer — verbatim quotes especially — and use them when relevant boxes come up.

**Shoe-stepping is a mode, not a step.** It's sustained across every box. Whenever the user starts writing abstract strategy instead of customer-anchored content, bring them back to the shoe-stepping stance.

## The provenance tag system (applies to every item in every box)

Every item written anywhere on the canvas gets one of three tags:

- `[heard]` — The customer said or did this directly. Verbatim quotes are strongly preferred. This is the gold standard.
- `[assumed]` — You inferred it. It's an educated guess based on context but the customer did not confirm. Render these in italics or with a visible `[ASSUMED]` prefix.
- `[★ best-guess]` — Multiple candidates exist and you believe this one is the top priority, but you have not confirmed it. Needs customer validation.

A canvas covered in `[assumed]` tags is an **honest signal**, not a failure. It's a map of what you need to learn. Padding with confident-sounding content that's actually assumption is the real failure mode.

The skill must enforce this rigorously. If the user writes an item and doesn't tag it, ask: "Did [anchor customer] actually say/do that, or are you inferring?" Never silently accept untagged items.

## The nine boxes (fill order + load-bearing rule per box)

Canonical sequence + the single most important rule per box. Load the named reference when you work that box for the full method.

1. **Customer Segments (always first).** Brainstorm **unique attributes and observable behaviors** — never demographics. Qualify the early adopter with the **"who's gonna rip this out of my hands" test**: would they take an MVP right now because the situation is too painful to wait? Requires articulating pain, which links Segments to Problem. *Load `segments-behaviors-not-demographics.md` when working this box.*
2. **Problem** (linked pair with Segments). Three named sub-fields — not one:
   - **Pains / what's getting in the way**
   - **Desired outcomes**
   - **Existing alternatives**
   Verbatim customer quotes preferred. Brainstorm widely, star the probable top pain. *Load `problem-sub-fields.md`.*
3. **Solution** (glance-back to Problem). Minimum features that address the top pains — NOT the roadmap. For every solution item, verify it ties to a specific Problem-box pain. Solution creep is the failure mode.
4. **UVP (seed-mode — you supply principles + candidates).** Two sub-fields, both required:
   - **Primary UVP sentence** — customer-world / vision-statement shape
   - **High-level concept** — `X for Y` analogy
   *Load `uvp-seed-principles.md` when you hit this box.*
5. **Channels.** Depth calibrated to data. 2-3 channels the user genuinely has in mind > 5+ padded options. Distinguish validated (actually used to reach this customer) from assumed. Produce a specific channel-learning probe for the Go-learn-this list.
6. **Revenue Streams.** Name pricing model(s) + dollar ranges. **Match to how the customer already pays for similar things** — pricing that clashes with the customer's existing spend model creates education cost; flag it explicitly.
7. **Cost Structure.** Cross-canvas scan — pull costs from Solution (build+implement) + Channels (reach+onboard) + ongoing ops. **Numbers required, not just categories.** The ROI check is a completion criterion. *Load `cross-canvas-scan-for-costs.md`.*
8. **Key Metrics.** Product-specific success metrics only — NOT revenue/expenses/MRR/active users (those are baseline business metrics elsewhere). Each metric traces to a Problem-box pain. 1-2 metrics — never a dashboard.
9. **Unfair Advantage (seed-mode — last on purpose).** Jason Cohen's rule: "can't be easily copied or bought." User-facing test: **"Does your candidate describe a category with lots of people in it? If yes, it's not unfair."** Common padding to reject: "great team", "passion", "first mover", "better product", generic tech adjectives, "30 years of experience". **"None yet" is a valid and often correct answer** — padding hides the real question. *Load `unfair-advantage-seed-principles.md`.*

**After the Customer-Problem-Solution triangle, order is a matter of taste.** The triangle is the load-bearing unit. What matters most after that: **connections between boxes + specificity within each.** If the user wants a different order after the triangle, honor it. Don't gatekeep on sequence.

## Box-modality split

Two different ways of filling a box:

**Elicit-mode (7 boxes):** Segments, Problem, Solution, Channels, Revenue Streams, Cost Structure, Key Metrics. You interview the user. They contribute content from their knowledge of the anchor customer. You ask, they answer, you tag for provenance.

**Seed-mode (2 boxes):** UVP, Unfair Advantage. The user commonly lacks strong instincts here. Instead of interviewing, the skill supplies canonical principles and drafts 2-4 session-specific candidates. The user reacts.

The pattern behind the split: **evidence-grounded** boxes (where direct customer knowledge lives) are elicit-mode. **Principle-governed** boxes (where the rule is "don't pad" and most people need external scaffolding) are seed-mode.

When switching into seed-mode, tell the user explicitly: "Most people don't have strong instincts for [UVP/Unfair Advantage] — let me supply the principles and draft some candidates for you to react to."

## Interviewer discipline (applies across all elicit-mode boxes)

- **Open-ended questions only.** Never offer multiple-choice ("is it X or Y?"). Ask open and let the answer come in the user's frame.
- **One question per turn.** Don't stack questions hoping to save time — stacked questions get partial answers.
- **Follow the user's language.** If they use a specific word, pick it up and use it in follow-ups. Don't translate into your vocabulary.
- **Ask what they actually did, not what a textbook says.** Real practice > framework-speak.
- **Verbatim quotes preferred.** Whenever the user produces a phrase the customer actually said, capture it exactly. Don't summarize.
- **Brainstorm broadly, then winnow.** Every box is fill-widely-then-select, never fill-in-the-right-answer. Encourage the user to dump everything they have before they prioritize.
- **Cross-box bleed is normal.** When the user surfaces something that belongs to a different box, capture it in the sticky-notes register (see below) and keep working the current box.
- **Back-edits during initial fill are welcome.** If later-box work reveals a gap in an earlier box, edit the earlier box in place. This is the dance, not iteration.

## The "sticky notes" register

Create a register at the start of the session: a scratch buffer where cross-box insights go. When the user surfaces something that belongs to a different box while working the current one, capture it there tagged with the target box. At close-out, sweep the register and place items in their correct boxes.

This matches how the expert actually fills a canvas — with sticky notes pinned near the target boxes — translated to a Markdown workflow.

## Full methodology reference

For the complete methodology (customer-anchored approach, full rip-test discussion, provenance discipline, brainstorm-winnow, and all 9 boxes in depth), load `references/lean-canvas-methodology.md`. Worth reading end-to-end on the first use of this skill so the full frame is in context before you start interviewing.

## The ROI check (completion criterion, not post-fill work)

Cost Structure and Revenue Streams must have numbers, not just categories. Once both are filled with estimates (ranges are fine), the skill computes a rough ROI comparison at canvas level:

- If sum(Revenue) plausibly > sum(Cost) at some realistic scale: note "ROI plausible" in the canvas footer.
- If not: flag "ROI unclear" or "ROI implausible." **This is signal to reframe the canvas, not to ship it.**

The ROI check is part of initial fill completion. If the user resists giving numbers, prompt: "Even rough ranges work — we need this to know if the business math is plausible. What's your ballpark?"

## The "Go learn this" list (canvas footer)

At close-out, distill every `[assumed]` item, every `[★]` item, and every thin-box probe into a list of **specific questions the user should ask real customers next.** Not "validate assumptions" — literally the questions.

For example, if the Problem box has `[★ commission-to-value gap]`, the go-learn-this list might read:

> - Ask [anchor customer]: "Of the money you spend on salespeople, what percentage feels like it's generating value you can point to?"

This list is the actionable bridge from canvas to next phase.

## Close-out sequence

1. **Sticky-notes sweep.** Place every parked insight in its correct target box.
2. **Back-edit sweep.** Review whether later-box work revealed any gaps in earlier boxes. Apply pending back-edits.
3. **Generate "Go learn this" list.** Every `[assumed]` / `[★]` / thin-box item becomes a specific customer question.
4. **ROI check.** Compare Cost vs. Revenue; flag at canvas level.
5. **One-paragraph canvas summary.** What the canvas says about this product, and where the weak spots are.
6. **Write the Markdown file** using `assets/lean-canvas-template.md` as the layout.
7. **Tell the user:** "Initial fill complete. The next phase — validating red and starred items through customer conversations or behavioral experiments — is outside this skill. The Go-learn-this list is your starting point for that phase."

## Edge cases and known failure modes

- **No real customer.** Hard halt (above). Do not accept "a persona we made up."
- **Demographics in Segments.** Reframe to behaviors: "What behavior is that shorthand for?" Never silently accept.
- **Solution creep.** Solution items that don't tie to a specific Problem pain. Push back and require a trace.
- **Premature Problem closure.** User names one pain and wants to move on. Force brainstorm-broadly — the hidden gaps are where unmet needs live.
- **User writes UVP blind.** Switch to seed-mode. Don't accept a blank-slate UVP from a user who flagged they don't have strong instincts.
- **User pads Unfair Advantage with "great team" / "passion" / similar.** Push back using the "lots of people like that" test: "Does that describe a category with many people in it? If yes, it's not unfair." Offer "none yet" as a defensible answer.
- **Cost Structure with categories only, no numbers.** Prompt for dollar estimates. Don't run ROI check without them.
- **Key Metrics listed as revenue/profit/active users.** Those are baseline business metrics, not the Key Metrics box. Redirect to product-specific success metrics that trace to the Problem box.
- **Padded Channels (5+ items with no evidence).** Shallow-but-honest > padded. Push back, keep only what the user can support.
- **User drifts into post-fill work mid-session.** Flag it, park it in the sticky-notes register, resume the current box.

## Interviewer anti-patterns to avoid

- **Don't batch questions.** One at a time.
- **Don't offer multiple-choice.** Open-ended always.
- **Don't seed unsolicited.** Only switch to seed-mode when the user flags they're weak on the box, OR when the box is UVP or Unfair Advantage by default.
- **Don't summarize the user's verbatim language.** Capture literally.
- **Don't accept untagged items.** Every item gets a provenance tag.
- **Don't rush past "not sure".** Uncertainty is an answer — star it and move on.

## What success looks like

A completed canvas in Markdown with:
- All 9 boxes filled or explicitly flagged as thin with specific learn-about probes
- Every item tagged `[heard]` / `[assumed]` / `[★]`
- UVP with both sub-fields (primary vision-statement sentence + X-for-Y concept)
- Cost/Revenue with numbers and a ROI check verdict
- A Go-learn-this list at the bottom translating red/star items into customer questions
- A sticky-notes section showing any cross-box captures
- A one-paragraph canvas summary

The canvas is honest (mostly-red is OK if that's where the user really is), specific (verbatim quotes preferred), and customer-aligned (every box connects back to how the real anchor customer sees the world).
