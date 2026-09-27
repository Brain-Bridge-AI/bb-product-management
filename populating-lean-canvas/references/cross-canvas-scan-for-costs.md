# Cost Structure: Cross-Canvas Scan + ROI Check

Cost Structure isn't a standalone box — it's a synthesis of the other boxes viewed through a spend lens. This reference covers how to fill it and how to run the ROI check that closes out initial fill.

## Method: scan across the canvas

To fill Cost Structure, look at these already-filled boxes in order and extract the costs each implies:

### From Solution

What does it cost to build and deliver the Solution?

- Development time and engineering headcount (or contractor equivalents)
- Customization / implementation time per customer (for services-heavy products)
- Third-party API / service dependencies (LLMs, data providers, etc.)
- Infrastructure to host and scale (cloud, database, storage)
- Ongoing maintenance and support

### From Channels

What does it cost to reach the customer?

- Outbound sales tools (LinkedIn Sales Navigator, Apollo, etc.)
- Sales team compensation (reps + SDRs if applicable)
- Marketing / content / community investment
- Event sponsorships or presence in targeted peer groups
- Onboarding and customer success time per new customer

### From ongoing operations

What does it cost to keep running, regardless of customer count?

- Core team compensation (founders, shared-services)
- Company-level infrastructure (accounting, legal, HR)
- Subscription software the company runs on

## Numbers are required, not optional

Categories alone don't tell you whether the business is viable. **Prompt the user for dollar estimates** on each cost line. Ranges are fine — rough ballparks are fine — but "TBD" is not fine if you want to run the ROI check.

If the user balks, explain why: "The ROI check (comparing cost to revenue at plausible scale) is a completion criterion for initial fill. Even rough estimates let us run that check. If the numbers come out obviously wrong, we know to reframe something on the canvas before going further."

## The ROI check

Once Cost Structure and Revenue Streams both have numbers (even as ranges), compare them at a realistic scale.

Three outcomes:

1. **ROI plausible.** Sum(Revenue) at some achievable customer volume > sum(Cost) at the same scale. Note "ROI plausible" in the canvas footer with the rough breakeven point.
2. **ROI unclear.** The math is too noisy to tell, usually because the customer-volume assumptions are wide-open. Note "ROI unclear — requires better volume assumptions" and list what needs to be pinned down.
3. **ROI implausible.** Costs clearly exceed realistic revenue. Note "ROI implausible at current model — canvas needs to be reframed." Flag it prominently. **Do not ship the canvas as-is.**

The ROI check is a sanity gate, not a detailed financial model. It catches canvases where the business doesn't work before they get treated as validated.

## What belongs in Cost Structure

Only costs required to **validate the UVP** at the stage the canvas describes. For an early-stage / MVP canvas:

- Cost lines needed to deliver the Solution to the early adopter
- Cost lines needed to reach the early adopter via the listed Channels
- Core ops costs that will exist regardless of customer count
- LLM / cloud spend if the product uses them meaningfully

## What does NOT belong

- Hypothetical future hires for a team you don't have yet
- Marketing channels you've never run
- Expansion costs for customer segments beyond the early adopter
- Full enterprise-grade compliance costs if the early adopter doesn't require them

If the user tries to add costs that don't tie to Solution / Channels / ongoing ops for the current scope, ask: "Does this cost exist in the current stage of the business, or is this future-state?" Move future-state costs to the Go-learn-this list, not Cost Structure.

## Common failure modes

- **Categories only, no numbers.** Incomplete. Prompt for estimates.
- **Including hypothetical future costs.** Dilutes the current-state picture.
- **Missing customer-acquisition cost.** People forget Channels produces cost lines. Always scan Channels.
- **Missing per-customer delivery cost.** For services-heavy products, customization/implementation is a real per-customer cost — not a one-time investment.
- **No ROI check.** Canvas complete without it is incomplete.

## Example scan

Given a canvas where:
- Solution = customized SaaS + mobile app + speech-to-text
- Channels = direct LinkedIn outreach + mastermind groups
- Revenue = implementation fees + usage-based token markup

The Cost Structure scan produces:
- LinkedIn Sales Navigator + similar outbound tools (from Channels)
- Sales team time for outreach (from Channels)
- Technical implementer time per customer (from Solution)
- Token/LLM usage cost (from Solution, ongoing)
- Cloud infrastructure (from Solution, ongoing)
- Founder/core team compensation (ongoing ops)

Each gets a dollar estimate (range). Sum(Cost) at 5-customer scale gets compared to Sum(Revenue) at 5-customer scale. ROI verdict goes in the canvas footer.
