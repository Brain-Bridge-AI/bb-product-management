# Assumption Scoring — Numeric Alternative to the 2×2 Grid

The 2×2 grid (`assumption-grid-placement.md`) is the default. It's fast, visual, and honest about being a relative ranking — ideal for a live team workshop with post-its.

But the grid doesn't travel well. When the work is **async, solo, or client-facing** — a Google Doc handed to a client, an LLM working from a Lean Canvas with no room to gather around a whiteboard — a numeric scoring table communicates the same prioritization in a form you can paste, sort, and revisit. Use this variant in those cases.

The axes map 1:1 to the grid:

| Grid axis | Scoring axis |
|---|---|
| Crucial ↔ Not Crucial (vertical) | **Criticality** (1–5: how damaging if this is false?) |
| Known ↔ Unknown (horizontal) | **Uncertainty** (1–5: how confident are we it's true? higher score = less confident) |

## Workflow

### 1. Enumerate assumptions in validation dependency order

Walk the canvas and list every assumption that must be true for the business to work, grouped by where it sits in the validation chain:

**Market → Problem → Value → Channel → Conversion → Retention → Economics → Defensibility → External**

Upstream categories gate downstream ones — same lead-domino logic as the grid's Crucial axis, just made explicit as a sequence. If a Market assumption fails, the Channel assumptions never get tested.

Each assumption must be:
- **Discrete** — one claim, not a compound sentence. Split "customers want X and will pay Y" into two.
- **Testable** — phrased so an experiment could prove it false.
- **Uniquely IDed** — e.g. `MKT-1`, `PROB-2`, `ECON-1`. The IDs let downstream artifacts (scoring table, experiment plans) reference assumptions without restating them.

### 2. Score each assumption

| Field | Scale | Question |
|---|---|---|
| Criticality | 1–5 | If this is false, how damaging? 5 = business doesn't work at all; 1 = minor operational tweak. |
| Uncertainty | 1–5 | How confident are we it's true? 5 = pure assumption, no evidence; 1 = rich direct evidence / existing data. |
| **Risk** | C × U | Calculated. Range 1–25. |

Bucket by Risk:

| Bucket | Risk | Meaning |
|---|---|---|
| **HIGH** | ≥ 20 | Test these first. This is the grid's upper-right quadrant — the LOFA shortlist. |
| **MED** | 10–19 | Watch. May become HIGH as you learn. |
| **LOW** | < 10 | Defer. Don't spend experiments here. |

### 3. Pick the LOFA — still a cascade test

The highest Risk score is the *starting* shortlist, not the automatic winner. Apply the same cascade test as the grid: among the HIGH-risk assumptions, the LOFA is the one whose answer **de-risks the most other assumptions** as a side effect. See the worked cascade examples in `assumption-grid-placement.md` — that logic is identical here. A 20 that cascades beats a 25 that doesn't.

## Honest caveat — scores are still judgments, not measurements

The grid deliberately avoids numbers because absolute scoring pretends to a precision you don't have. The scoring table reintroduces numbers for portability, so guard against the false confidence:

- Treat Criticality and Uncertainty as **relative rankings forced onto a 1–5 scale**, not objective measurements. Calibrate each score against the others in the set, exactly as you'd place post-its relative to each other on the grid.
- Don't agonize over a 3 vs a 4. The buckets (HIGH/MED/LOW), not the exact products, drive the decision.
- A tidy table of Risk scores can read as more rigorous than the underlying guesses warrant. When presenting to a client, say out loud that these are calibrated judgments to be revised as evidence comes in — that's the whole point of the loop.

## When to use which

| Situation | Use |
|---|---|
| Live team workshop, whiteboard or Miro | **2×2 grid** (`assumption-grid-placement.md`) |
| Async doc, solo founder, LLM-driven from a canvas, client deliverable | **Scoring table** (this file) |
| Need both | Score first for the artifact, then plot the HIGH bucket on a grid for the cascade discussion |
