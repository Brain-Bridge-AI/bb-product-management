# Rapid Experiment Loop — Methodology Reference

## What the loop is

The Brain Bridge Rapid Experiment Loop is a one-page canvas for running a single evidence-gathering cycle on a business model. It lives downstream of a Lean Canvas — the canvas describes the model, the loop tests a specific claim the model is making.

Reference poster: `/Volumes/Trebleet/Downloads/BrainBridge_Experiment_Loop_FINAL_46x36.pdf`

The loop's job is **learning under uncertainty, fast.** Not validation. Not scientific proof. Evidence collection on a single assumption at a time, with enough rigor to move the team forward without the overhead that would slow them down.

## Why it's coupled to a Lean Canvas

The loop header (Team, Vision, Customer, Problem, Solution) carries over directly from the Lean Canvas. This coupling is load-bearing, not decorative:

- Every experiment is anchored to a specific model. Decoupled experiments drift into "learning activities" that don't update anything.
- The assumption-brainstorm in step 2 walks the Lean Canvas box-by-box. Without a canvas, the brainstorm is ungrounded.
- The Update step (step 5) feeds evidence back into the canvas. Without a canvas, nothing to update.

If no Lean Canvas exists, stop and populate one first (skill: `populating-lean-canvas`). Do not invent a stub canvas so you can run the loop — the experiment will anchor to fiction.

## Vocabulary

### LOFA — Leap of Faith Assumption

The single assumption the team commits to testing this cycle. Selected from the top-top-right of the Crucial × Known 2×2. Its defining property is **cascading risk**: answering the LOFA collapses uncertainty across many downstream canvas boxes, not just the one the LOFA came from.

The canvas box is labeled "Riskiest Assumption." What you fill in is the LOFA — the grid produces a *ranking* of riskiness; the LOFA is the single one you commit to.

### Lead domino

The metaphor for the Crucial axis. Some assumptions are upstream of others — if the upstream one is false, the downstream ones don't matter. The lead domino is the one whose failure would crash the business. Place those higher on the Crucial axis.

### Leap of faith

Ash Maurya's term for the single assumption a business is most dependent on. Synonymous with LOFA in this workflow.

### Iterate / Persevere / Pivot

The three Decision options after running:

- **Iterate.** Signal unclear or denominator too small. Run again with same LOFA, maybe tweaked experiment, bigger sample. Default on early cycles.
- **Persevere.** LOFA proven true. Reprioritize the grid, pick the next LOFA.
- **Pivot.** Evidence says the Lean Canvas must change. High bar.

### Say vs. Do

The central distinction for experiment design. What customers **say** (survey responses, stated intent, interest expressions) is weak evidence — people report inaccurately about their own future behavior. What customers **do** (click, sign up, pay, articulate, use) is strong evidence. The loop explicitly excludes surveys. See `experiment-types-say-vs-do.md` for the full taxonomy.

## Why rapid experiments are different from pilots / A-B tests / studies

| | Rapid experiment | Pilot | A-B test | Scientific study |
|---|---|---|---|---|
| n (sample) | 3–5 early, scale with confidence | 10s to 100s of real customers | 1000s | Predetermined by power analysis |
| Goal | Learning, evidence collection | Commercial rollout at small scale | Optimize a known funnel | Statistical significance |
| Time | 1–2 hours first cycle | Weeks to months | Days to weeks | Weeks to months |
| Commercial commitment | None — customers are happy but not buying | Real — actual product delivered | Real — production feature | None — research |
| Decision output | Iterate / Persevere / Pivot | Scale or kill | Variant A or B | Accept or reject hypothesis |

If the user is debating sample-size math or p-values, they're probably not running a rapid experiment. That's OK — but route them to the right methodology, not this one.

## The rhythm across cycles

A single cycle yields thin learning. The power of the loop is compounding across cycles:

1. **Cycle 1** — crude target metric (team-poll guess), n=3–5, result is usually "iterate." First real contact with customers on this LOFA.
2. **Cycle 2** — bigger n, maybe tweaked experiment. Starting to see real behavior.
3. **Cycle 3** — baseline emerging. Target metric is informed by actual customer data, not guesses.
4. **Cycle 4+** — confident Persevere or Pivot decision possible. Move to the next LOFA or change the canvas.

Expect 3–5 cycles per LOFA in serious use. Teams that pivot after one cycle give themselves whiplash and don't learn.

## The evidence repository

The Experiment Loop poster is a working surface — one cycle at a time. Compound learning across cycles requires a separate, searchable store:

- **Minimum:** markdown evidence log in the out-dir. Per-cycle row with LOFA, hypothesis, n, target vs. actual, top observations, top insights, decision.
- **Richer:** AI knowledge repo (Claude-indexed markdown, or similar).
- **Enterprise:** existing product-management tools for customer-interaction capture.

The canvas is the thinking surface; the repo is the memory. Both are needed. Teams that only have the canvas forget what they already learned and re-run experiments they've already answered.

## Integration with other skills

- **`populating-lean-canvas`** — upstream dependency. Run that first if no canvas exists.
- **`eliciting-knowledge`** — sibling skill. If a LOFA is about tacit expert knowledge, eliciting-knowledge may be the right test design.
- **`bb-prospect-research`** — helpful when the customer-recruitment step of the Experiment plan needs real targets.
