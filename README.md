# Brain Bridge Product Management Skills

A set of seven Claude Code skills used in the Brain Bridge Lean Canvas / Rapid Experiment workshop, including the WP Engine workshop (April 2026). Each skill is a self-contained folder you can drop into your Claude Code installation.

## What is a "skill"?

A skill is a directory with a `SKILL.md` file (plus optional scripts and references) that Claude Code loads as part of its working context. When you describe a task that matches a skill's trigger conditions, Claude uses the skill's instructions to do the work.

## The skills in this bundle

1. **populating-lean-canvas** — Fill a Lean Canvas for a product or business idea through a customer-anchored interview, with provenance tracking (heard-from-customer vs. assumption vs. best-guess).
2. **crafting-vision-statements** — Craft a short, motivating 3+ year vision statement that anchors strategy and survives experiment pivots.
3. **researching-customer-segments** — Use public data to pressure-test whether a chosen customer segment is the right size and shape: big enough to matter, narrow enough to dominate, reachable for interviews.
4. **running-problem-interviews** — Prep, conduct, and debrief a customer problem interview tied to an active Leap of Faith Assumption.
5. **running-rapid-experiments** — Guide a team through the Brain Bridge Rapid Experiment Loop: pick the LoFA, design the experiment, run it with 3 to 5 real customers, land on Iterate / Persevere / Pivot.
6. **leading-experiment-reviews** — How a leader should run the team share-out after a rapid experiment: poke holes in the experiment (not the business model), bring wider-lens evidence, clear the path for the next cycle.
7. **capturing-customer-insights** — Capture insights from interviews, experiments, and research into a segment-organized repository that compounds over time.

## How they fit together

```
crafting-vision-statements
        |
        v
populating-lean-canvas  <----  capturing-customer-insights
        |                              ^
        v                              |
researching-customer-segments          |
        |                              |
        v                              |
running-problem-interviews  ----------->
        |                              |
        v                              |
running-rapid-experiments   ----------->
        |
        v
leading-experiment-reviews
```

Vision anchors the canvas. The canvas surfaces assumptions. Segment research and problem interviews test the riskiest assumptions. Rapid experiments turn assumptions into evidence. Leaders review the results. Insights compound back into the canvas.

## Installing

### Option A: Drop into Claude Code

Copy any skill folder into `~/.claude/skills/`:

```bash
cp -R populating-lean-canvas ~/.claude/skills/
```

Restart Claude Code. The skill is now available.

### Option B: Read the SKILL.md files directly

Every skill folder has a `SKILL.md` at its root. You can read it as a methodology guide even without Claude Code, the prompts and frameworks stand on their own.

## License and attribution

Provided for participants of Brain Bridge workshops. Brain Bridge Inc. retains authorship; you are welcome to use, adapt, and share within your organization.

Questions: aaron@brainbridge.app
