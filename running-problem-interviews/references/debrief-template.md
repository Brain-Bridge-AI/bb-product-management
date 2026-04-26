# Post-Interview Debrief Template

Capture within 24 hours, ideally within 2. Memory decays fast; quotes turn into paraphrases.

## File location

Save as:
`~/Library/Mobile Documents/iCloud~md~obsidian/Documents/2nd Brain (I)/1-Projects/[Project]/problem-interviews/YYYY-MM-DD-[interviewee]-debrief.md`

Next to the script file (same folder, same date-interviewee prefix, `-debrief.md` suffix).

## Template

```markdown
# Problem Interview Debrief: [Interviewee Name]

- **Date:** YYYY-MM-DD
- **Interviewer(s):** [name(s)]
- **Duration:** [actual minutes]
- **Recording:** [path to recording or transcript]
- **Experiment / LoFA tested:** [one-sentence LoFA]

---

## LoFA signal summary

One paragraph. Does this interview support, contradict, or leave ambiguous the LoFA? Be explicit — do not default to "mixed signal" to avoid committing.

Remember the decision rule: **this is one data point, not a decision.** Decisions require experiment evidence + interview context + hard data.

## Verbatim customer quotes

Pull 5-10 direct quotes from the recording/transcript. Preserve their words exactly. Tag each:

- `[UNPROMPTED]` — customer raised this without being asked. Highest signal.
- `[compliment - discount]` — "great idea!" style. Low signal.
- `[fluff - discount]` — "I would probably..." hypothetical. Low signal.
- `[future-promise - discount]` — "I'd totally buy that." Low signal until backed by action.
- `[contaminated - discount]` — interviewer's framing may have shaped the answer.
- (no tag) — regular past-behavior data point.

Example:

> **[UNPROMPTED]** "Honestly, the thing that kills us every storm season is we can't get fast enough quotes out the door. We lose deals to whoever shows up first."

> **[fluff - discount]** "I mean, I'd probably use something like that if it was priced right."

## Key behaviors observed

What did the customer *do* (in past situations they described)? Distinct from what they *said they'd do*.

- [past behavior 1]
- [past behavior 2]

## Existing alternatives / workarounds

What are they using today to solve this problem?

- [alternative 1 and how it works / fails]
- [workaround that reveals the pain is manageable]

## Unprompted mentions (the high-signal section)

Collected from the quotes above. List them separately here so they stand out:

- [unprompted mention 1]
- [unprompted mention 2]

## Contamination flags

Places where the interviewer's language may have anchored the customer's answers:

- [moment 1 — what was said, what was answered, how it may have biased things]
- [moment 2 — ...]

If none, write "None observed."

## Problem ranking (if applicable)

If a ranking turn happened, capture it:

- Must-solve: [...]
- Nice-to-solve: [...]
- Don't-care: [...]

## Surprises

What did you not expect to hear? Surprises are often the most important finding.

## Next steps

- [ ] Commitments customer made (follow-up call, intro, pilot slot, etc.)
- [ ] Commitments interviewer made (share something, schedule follow-up)
- [ ] Referrals to chase (from close-out question)
- [ ] Updates to the experiment / LoFA interpretation
- [ ] Notes for the next interview in this experiment

## Raw notes / transcript pointer

Link or path to full transcript, plus any raw notes taken during the call.

---
```

## When to write the debrief

- **Within 2 hours** of the call if at all possible. Memory for tone, emphasis, and unprompted mentions decays fast.
- **Pull from the recording**, not just memory, for verbatim quotes. Paraphrased quotes rot — they lose nuance and become the interviewer's interpretation over time.
- If the interview was done in pairs, both interviewers contribute to the debrief. The observer's notes on body language, tone, and hesitations belong here.

## Using the debrief

- The debrief is the durable artifact the experiment depends on. A raw transcript is too long to process; the debrief is the distilled version.
- When analyzing multiple interviews for a single experiment, compare debriefs side-by-side. Patterns across unprompted mentions are especially strong signal.
- The debrief feeds the experiment's Learn stage (see `running-rapid-experiments`) — specifically the Insights and Decision boxes.
