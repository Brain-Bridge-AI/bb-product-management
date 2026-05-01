---
name: running-rapid-experiments
description: Guide a team or individual through the Brain Bridge Rapid Experiment Loop — starting from a Lean Canvas, brainstorm and prioritize business-model assumptions, pick the single Leap of Faith Assumption (LOFA) to test, design a fast-and-frugal experiment with a clean If-X-then-Y%-will-Z hypothesis, run it with 3–5 real customers, and land on an evidence-driven Iterate / Persevere / Pivot decision. Use this skill whenever the user wants to "design an experiment", "test an assumption", "validate a hypothesis", "run a rapid experiment", "figure out if customers really want this", "prove out a pricing model", "de-risk a product bet", or "decide whether to pivot or persevere". Also triggers when the user is stuck on a Lean Canvas box because they don't have evidence yet — the right next move is an experiment, not another guess. Do NOT trigger for pilots, production A/B tests, or statistical studies — rapid experiments are small-n (3–5 customers) learning cycles aimed at evidence collection, not scientific validation. And surveys are explicitly off-limits here: this skill is about what customers DO, not what they say.
---

# Running Rapid Experiments

## What this skill is for

Rapid experiments are **evidence-gathering cycles coupled to a Lean Canvas**. The point is learning, not proving. You pick the single riskiest assumption the business model is making (the **Leap of Faith Assumption**, LOFA), design a small fast-and-frugal test that puts real behavior (not opinions) in front of you, run it with 3–5 real customers, and let the evidence move you forward.

The Brain Bridge **Rapid Experiment Loop** is the canvas that structures one cycle. Reference poster: `/Volumes/Trebleet/Downloads/BrainBridge_Experiment_Loop_FINAL_46x36.pdf`. The loop has five stages:

1. **START** — Header: Team, Vision, Customer, Problem, Solution (carried over from the Lean Canvas)
2. **Prioritize Assumptions** — Brainstorm all assumptions, place on Crucial × Known 2×2, pick the LOFA
3. **Hypothesis** — Customer Behavior, Target Metric, Experiment (the "If X, then Y% will Z" trio)
4. **Run** — Observations, Results
5. **Learn** — Insights, Decision (Iterate / Persevere / Pivot), Update

The key distinction this skill enforces: **what customers DO vs. what customers SAY.** Surveys, interest polls, "would you buy this" questions all capture words, which are weak evidence. Rapid experiments capture actions. When the user suggests a survey, route them to `references/experiment-types-say-vs-do.md`.

## Read before running

Before executing a cycle, read the references relevant to what the user needs:

- `references/rapid-experiment-loop-methodology.md` — canvas walkthrough, vocabulary (LOFA, lead domino, leap of faith, iterate/persevere/pivot), why the loop is coupled to the Lean Canvas.
- `references/experiment-types-say-vs-do.md` — **read this whenever the user is scoping the Experiment box.** Organizes experiment types by signal strength and shows how to convert a "we'll ask them" design into a "we'll watch them do something" design.
- `references/hypothesis-template.md` — the If-X-then-Y%-will-Z template with worked examples across pricing, channel, segment, problem, and solution LOFAs.
- `references/assumption-grid-placement.md` — decision rules for Known/Unknown and Crucial/Not-Crucial axes with worked cascading-risk examples.
- `references/decision-iterate-persevere-pivot.md` — full decision guidance including the whiplash / rebooting warnings and the "first-cycle pivot is suspicious" rule.

## Inputs to ask for

1. **A paired Lean Canvas.** If none exists, stop and route the user to the `populating-lean-canvas` skill. The Experiment Loop is useless without a canvas — the canvas *is* the thing being tested.
2. **Mode:** workshop / solo / cross-functional team. Header fill effort and run timebox scale with audience. Workshop → 1–2 hour run, polished header. Solo → paste the canvas over the header, move fast.
3. **Cycle number.** First cycle? Third? Tenth? First-cycle defaults differ from mature-cycle defaults (bigger n, known baselines, higher pivot bar).
4. **Out-dir.** Default `~/.openclaw/workspace/running-rapid-experiments/<experiment-slug>/`.

## Workflow

### 1. Load the paired Lean Canvas

If no canvas exists, stop and suggest `populating-lean-canvas`. Do not try to run an experiment against a non-existent business model.

### 2. Fill the header

Team, Vision, Customer, Problem, Solution. These boxes are **administrative** — they let anyone landing on the poster know what's being tested without asking. Effort scales with audience. For solo work, paste the Lean Canvas over the top — the five boxes are direct references.

### 3. Brainstorm all assumptions

Walk the Lean Canvas box-by-box in its normal fill order (Customer → Problem → Solution first). For each box, ask: **"what must be true for this to work?"** Premortem framing — easier to surface hidden assumptions by imagining failure than by listing beliefs.

Format every assumption as **"customers will [behavior]."** Behavioral, not belief. The grammar matches what the Hypothesis template will demand — don't make yourself rewrite later.

Expect at least three categories:
- **Customer / behavioral** ("customers will adopt the token-based pricing model")
- **Technical / feasibility** ("the token metering will measure usage accurately")
- **Market / risk** ("mid-size-org CFOs will be open to custom AI software vendors")

Team brainstorm beats solo. If no team is available, use the LLM itself as a team-proxy — feed the canvas and ask for assumption candidates.

### 4. Place assumptions on the 2×2 grid

- **Horizontal (Known ↔ Unknown):** how much real evidence you have. Rich experience / existing data / market evidence → Known. No evidence → Unknown.
- **Vertical (Crucial ↔ Not Crucial):** lead-domino framing. What would crush the business if false? Some assumptions are upstream of others — if the upstream fails, downstream doesn't matter.

**Placement is relative, not absolute.** You're ranking post-its against each other, not assigning scores. Comparative ranking is honest; absolute scoring pretends to precision you don't have.

See `references/assumption-grid-placement.md` for worked cascading-risk examples.

### 5. Pick the LOFA

**Top-top-right of the grid = Leap of Faith Assumption.** The single assumption whose answer collapses the most downstream risk across the business. If answering this doesn't cascade, it's not the LOFA even if it's unknown and crucial on its face.

Validate: does answering this change what we'd do about Channels, Revenue, Key Metrics, or other canvas boxes? If no, re-rank.

**Terminology note:** the canvas box is labeled "Riskiest Assumption." What you fill in is the LOFA you selected from the grid. The grid produces a ranking of riskiness; the LOFA is the single one you commit to testing this cycle.

### 6. Draft the Hypothesis

The three boxes — Customer Behavior, Target Metric, Experiment — **fit together and iterate, not sequentially.** The forcing function is the sentence:

**"If we [X = experiment], then [Y% = target metric] of customers will [Z = customer behavior]."**

Writing this sentence locks values for all three boxes at once. See `references/hypothesis-template.md` for worked examples.

**Customer Behavior.** Brainstorm a handful of candidate observable actions first. Don't commit to the first one that sounds fine. The depth ladder (choose among options < recall prior use < explain in own words) is only visible when you generate the set. Narrow to the candidate that writes cleanly into the template *and* produces the strongest signal on the LOFA. **No surveys.** Read `references/experiment-types-say-vs-do.md` to see why and to generate stronger candidates.

**Target Metric.** Pick a number. This is a **pre-commitment, not a prediction.** Without a pre-committed line, the team will rationalize any result as success after the data lands. On first-cycle experiments it's **art, not science** — use the team-poll heuristic: ask each teammate how likely they think the experiment is to hit positive. Mostly optimistic → pick a larger percentage. Mixed → pick a smaller one. In solo mode, check (a) your confidence, (b) prior evidence, (c) strength of signal from the proposed behavior, and land on a number. Don't debate 45% vs 47% — customers will teach you the real number over iterations; baselines emerge by cycle 3 or 4.

**Experiment.** Scope as **lightweight project planning** — who does what by when. Live channels (in-person, Google Meet) beat async channels when the LOFA is the thing you know least — richer interaction surfaces signal you don't know to ask for. Narrate the experiment end-to-end so the team can internalize what running it looks like. Build in **surprise-capture** via follow-up questions after the measurement — right/wrong is the metric, the *why* is where insights live. Frame the ask as "feedback on our system," not as a test — reduces subject pressure and gets honest "I don't actually know" answers.

**Hard constraint: the customer must always leave happy.** Rapid experiments routinely put incomplete artifacts in front of real customers — that's fine. You cannot leave the customer upset. This constraint wins over speed and frugality when they conflict. If the design risks an unhappy customer, redesign before running.

### 7. Run the experiment

- **Timebox:** 1–2 hours on the first workshop cycle. If it doesn't fit, the design isn't minimum-viable.
- **Sample size:** 3–5 customers early, scale up as confidence grows. Rapid experiment ≠ pilot ≠ statistical study. Don't chase significance; chase learning.
- **Parallelize** execution across team members.
- **No assistance during the session.** Helping the subject contaminates the signal — you'd be measuring their understanding-plus-your-hints.
- **Take copious notes — verbal AND physical.** Body language often carries signal that the verbal response hides (confident-sounding guessing vs. uncertain-sounding understanding).
- **Stay focused on the LOFA, but capture bleed-over.** Experiments routinely teach things about other assumptions and other canvas boxes. Capture the bleed — don't discard it.

### 8. Capture post-session

Three distinct boxes, each with a different purpose:

- **Observations** — what happened and why. Detailed notes, photos, body-language-level detail. This is where the qualitative surround lives for later re-interpretation.
- **Results** — the measurement. Did the target behavior occur, at what rate. Clean separation of the metric from the qualitative surround.
- **Insights** — the **artistic** box. Prompts: "what surprised me?", "what didn't I expect to see?", "what pattern am I starting to see across multiple interactions?" Less scientific on purpose. Trying to make insights rigorous kills them. Single-session insights are thin; 3–5 sessions start to show shape.

All three are evidence inputs to the Decision — **none is the Decision itself.** The Decision is judgment on the combined evidence; data-only decisions miss the why, qualitative-only decisions miss the signal.

### 9. Decide: Iterate / Persevere / Pivot

Read `references/decision-iterate-persevere-pivot.md` before making the call. Quick reference:

- **Iterate** (default on early cycles). Signal unclear or denominator too small. Same LOFA, maybe tweaked experiment, bigger sample.
- **Persevere.** LOFA proven true. Reprioritize the assumption grid, pick the next LOFA, run again.
- **Pivot.** Evidence says something on the Lean Canvas must change. **High bar.** First-cycle pivots are suspicious — dig deep before approving. Be surgical, not a reboot: change the box the evidence supports changing, not the whole canvas.

**No single experiment holds the answer.** Decisions are trend reads across multiple experiments, not single-data-point calls.

### 10. Update

- **Edit the whole Lean Canvas, not just the LOFA's box.** Bleed-over teaches across boxes; scanning the whole canvas is where compound updating happens.
- **Clean-slate the Experiment Loop poster.** Move completed-cycle post-its to an archive flip chart. The poster is a working surface; the archive is history.
- **Append to the evidence repository.** Minimum: markdown evidence log in the out-dir (template in `assets/evidence-log-template.md`). Richer: AI knowledge repo or Airtable for cross-cycle search. **Compound learning depends on searchable memory — paper doesn't survive the second cycle.**
- Loop back: Iterate → step 6 (redraft Hypothesis with same LOFA, bigger n). Persevere → step 4 (reprioritize grid, pick next LOFA). Pivot → step 2 (update header from canvas edits, restart).

After the cycle closes, consider invoking `capturing-customer-insights` on the experiment debrief. It'll suggest candidate insights (supported/contradicted assumptions, customer quotes gathered during the experiment, surprises) to file into the segment folder for compounding across cycles. Optional — but the evidence log is project-local; the insights repo is how findings survive across experiments and teammates.

## Outputs

Produce:

1. **Experiment Loop markdown** at `<out-dir>/experiment-loop.md` — filled-out template including header, ranked assumption grid with LOFA highlighted, Hypothesis (X, Y%, Z), Experiment plan, and after running: Observations, Results, Insights, Decision, Update notes. Template: `assets/experiment-loop-template.md`.
2. **Evidence log entry** — append-only markdown block in `<out-dir>/evidence-log.md` so compound learning survives between cycles. Schema in `assets/evidence-log-template.md`.
3. **Lean Canvas update pointer** — if Pivot or Persevere, concrete notes on what changes on the canvas or which LOFA is next.

## Edge cases to watch for

- **Survey drift.** When the user suggests "let's send them a survey," redirect to `references/experiment-types-say-vs-do.md` and work with them on a do-based alternative. Surveys capture words; words are weak evidence.
- **Conflation with pilot / A-B test.** Early-stage experiments are n=3–5 learning cycles, not significance tests. If the user is debating sample-size math, remind them: the customers will teach the target over iterations.
- **Target-metric precision debates.** If the team is debating 45% vs 50% for more than a few minutes, intervene. Precision is fake when the underlying estimate is a team-poll heuristic.
- **First-cycle pivot.** Push back: "This is your first experiment. Before pivoting, iterate with a bigger sample and see if the signal holds." User can override with explicit evidence; default to iterate.
- **Unhappy customers.** Non-negotiable. If the design risks it, redesign.
- **Bleed-over lost.** If post-session capture only covers the LOFA, explicitly prompt: "what else did you learn about other assumptions or other parts of the canvas?"
- **No evidence repo.** If the user skips logging between cycles, they lose compound learning. Verify the evidence log was written before closing the cycle.
- **Single candidate behavior.** If the user commits to the first behavior that sounds fine, push them to generate at least two more before narrowing. The depth ladder only shows up when you see the set.

## Not for

- Pilots (production rollouts with real commercial commitments)
- A/B tests on shipped features (those are production statistical tests)
- Scientific studies (different methodology, different sample sizes, different goal)
- Surveys (forbidden — see `references/experiment-types-say-vs-do.md`)
- Research projects without a paired Lean Canvas (route to `populating-lean-canvas` first)
