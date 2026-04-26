# Decision — Iterate / Persevere / Pivot

After running and capturing Observations, Results, and Insights, the team lands on one of three decisions. Read this before making the call.

## Setup: what the decision is actually about

Canvas text: *"Was your riskiest assumption true? Look for a trend in your evidence over time. No single experiment holds all the answers."*

Two load-bearing ideas:

1. **Trend, not snapshot.** A single experiment is one data point. Decisions read trends across cycles.
2. **Evidence-driven.** The decision combines Results (the measurement), Observations (the why), and Insights (the patterns). Data-only decisions miss the why; qualitative-only decisions miss the signal.

## Iterate

**What it means.** Same LOFA next cycle. Possibly tweaked experiment. Bigger sample.

**When to pick it.**
- Signal unclear (ran into target, but n was small and variance is high).
- Missed target, but Observations suggest the experiment design itself had issues (not the LOFA).
- Hit target, but on n=3 — want n=10 before committing.

**This is the default on early cycles.** Small denominators + the riskiest-unknown assumption = unclear signal almost by definition. Iterating is not weakness; it's the core move.

**Tweaks to consider when iterating:**
- Bigger n (3 → 10 → 20).
- Same experiment on a different customer segment (if the LOFA is segment-specific).
- Same experiment with tighter framing (if follow-up questions revealed confusion).
- Different channel (if recruitment was the bottleneck).

## Persevere

**What it means.** LOFA is proven true enough. Reprioritize the assumption grid. Pick the next LOFA. Keep the business model.

**When to pick it.**
- Results hit target, with enough n that you trust the signal.
- Observations corroborate the Result (the why matches the what — customers behaved that way because they genuinely get it, not because of experimental artifacts).
- Insights don't contradict the Result (no pattern emerging that says "they passed the test but for the wrong reason").

**What happens next.** Go back to the assumption grid. The LOFA you just tested moves off the grid (or gets marked resolved). The next-ranked assumption in the upper-right becomes the new LOFA. Run the loop again.

## Pivot

**What it means.** Evidence says something on the Lean Canvas must change.

**When to pick it.**
- Results clearly missed target, and Observations explain why in a way that implicates the canvas, not the experiment.
- Insights surface a pattern that re-shapes how you think about a customer / problem / solution / pricing / channel box.
- Same-LOFA evidence from multiple cycles says "this won't work as designed."

**High bar.** A pivot changes the business model. Be sure.

### Pivot anti-patterns

**Whiplash.** Pivoting every cycle. Teams that do this never learn because they change the model faster than any single assumption can be tested.

- **First-cycle pivots are especially suspicious.** Before approving one, push back: "This is your first experiment on this LOFA. Can we iterate with a bigger sample before changing the canvas?" Default to iterate unless the user has compelling evidence.

**Rebooting.** Changing many canvas boxes when the evidence supports changing only one. Be surgical.

- If the experiment was on pricing, the pivot is on the Revenue box, not the whole canvas.
- Other boxes may update as a *consequence* of the primary pivot (new pricing changes implications for Channels) — but the primary change is where the evidence points.

**Evidence-driven test.** Before approving a pivot, answer: *does the evidence specifically support the change we're making?* If no, re-scope the change or iterate instead.

### Pivot types

When a pivot is warranted, name the type — it keeps the change surgical:

- **Segment pivot** — same problem/solution, different customer segment. (Evidence: pain-intensity difference across segments.)
- **Problem pivot** — same segment, different problem. (Evidence: the problem you picked isn't the most painful.)
- **Solution pivot** — same problem, different solution shape. (Evidence: proposed solution doesn't fit the workflow.)
- **Pricing pivot** — same everything, different revenue model. (Evidence: CFOs don't understand token pricing; switch to flat-fee.)
- **Channel pivot** — same everything, different go-to-market. (Evidence: LinkedIn direct doesn't work; Vistage groups convert.)
- **Value-prop pivot** — reposition the same product around a different pain or outcome. (Evidence: the message that resonates isn't the one you're leading with.)
- **Segment-size pivot** — zoom in (narrower, more specific segment) or zoom out (broader segment).

Name the type. Update only the affected boxes. Document the evidence that drove it.

## Pre-decision checklist

Before calling the decision, verify:

1. **n is visible.** How many customers did you actually see? Is it enough to trust the signal? (If n=1–2, almost always iterate.)
2. **Observations corroborate or contradict.** Walk through each session's Observations notes. Do the qualitative signals match the Results?
3. **Insights don't contradict.** Check the artistic box for patterns. Is there a "they passed but…" or "they failed but…" that complicates the call?
4. **Bleed-over captured.** Did the experiment teach about other assumptions? Note those for canvas update, even if the LOFA decision is straightforward.
5. **Evidence repo updated.** Before closing the cycle, write the entry to the multi-experiment log. This is where compound learning lives; skipping it breaks the system.

## The loop continues

- **Iterate** → re-draft the Hypothesis (Step 6 in SKILL.md) with the same LOFA and the adjustments you chose. Run again.
- **Persevere** → go back to the assumption grid (Step 4 in SKILL.md), reprioritize, pick the next LOFA. Run again.
- **Pivot** → update the affected Lean Canvas boxes first (Step 10 in SKILL.md, but applied surgically), then restart the brainstorm (Step 3) with the updated canvas.

In all three cases, update the canvas and update the evidence log before starting the next cycle.
