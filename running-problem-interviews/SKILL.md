---
name: running-problem-interviews
description: Prep, conduct, and debrief a customer problem interview tied to an active Leap of Faith Assumption in a Brain Bridge Rapid Experiment. Use whenever the user says "prep a problem interview with [person]", "draft the interview script for [prospect]", "I'm interviewing [name] about [LoFA]", "build the script for the [deal] customer interview", "help me run a problem interview", or when a task in an experiment loop calls for customer interviews to test a specific assumption. Also triggers when the user is scoping an experiment that needs real customer conversations and has a candidate interviewee in mind. Do NOT trigger for: sales discovery calls (those are selling-adjacent — use managing-finances-bb), solution demos, generic meeting prep (use preparing-for-meetings), relationship-building conversations, or pulling action items from a completed call (use searching-meeting-transcripts). Pairs with running-rapid-experiments upstream — the experiment defines what the interview is testing.
---

# Running Problem Interviews

## What this skill is for

A **problem interview** is a 30-45 minute structured conversation with a prospective customer that tests a single Leap of Faith Assumption (LoFA) from an active Rapid Experiment. It is NOT a sales discovery call, a demo, or a general relationship chat.

The interview has one job: elicit past-behavior stories that either support or contradict the specific LoFA being tested. Done well, the customer does almost all the talking and leaves feeling like they were listened to deeply. Done poorly, the interviewer leaks product-framing, anchors the customer's answers, and contaminates the data the experiment depends on.

This skill owns the end-to-end workflow: prep (including LLM-assisted script drafting with a mandatory human edit pass), in-interview discipline, and debrief capture. It pairs with `running-rapid-experiments` upstream — if there is no active experiment and no LoFA, stop and route there first.

## Before you start: confirm the preconditions

Refuse to draft a script unless both are true:

1. There is a **named active experiment** with a specific LoFA the interview is testing.
2. There is a **Lean Canvas** for the product.

If either is missing, route the user to `running-rapid-experiments`. Drafting an interview without a concrete LoFA produces a pleasant conversation with no pass/fail criteria — a waste of the customer's time and yours.

## Inputs you'll need

- **Active experiment / LoFA** — what single assumption this interview tests.
- **Lean Canvas** — product context; drives the opener.
- **Experiment plan document** — goes into the LLM draft input.
- **Interviewee identity** — full name, role, company, relationship to any existing deal. **Fact-check this**, see step 2 below. Do not trust the user's memory of the person.
- **Whether this is part of an active experiment with a prior stimulus.** If yes, the customer has already seen material (pricing sheet, prototype, pitch) and the interview debriefs their reaction. If no, the interview is cold. This changes question order — see `references/interview-structure.md`.

## Workflow

### Step 1 — Confirm the experiment and LoFA

Restate the LoFA to the user in one sentence. If fuzzy, refuse and route to `running-rapid-experiments`.

### Step 2 — Fact-check the interviewee

Before any drafting, verify the interviewee's identity:

- Look up their Airtable contact record (use `looking-up-contacts`).
- Search for prior meeting transcripts with them (use `searching-meeting-transcripts`).
- Check related deal notes (use `looking-up-deals`).

Verify role, company, posture toward the project, and sensitivities. This step is non-optional — in the session that produced this skill, the user misremembered an interviewee as a "fractional CFO" when the person was actually a fractional sales leader, which would have produced a badly-targeted opener and wasted an interview.

Produce a short interviewee brief: name, role, company, recent interactions, voice/style cues from transcripts, known preferences.

### Step 3 — Draft the script via LLM

Paste into an LLM turn:
- The Lean Canvas
- The experiment plan document
- The interviewee brief from step 2
- Whether this is cold or part of an active experiment with prior stimulus
- The instruction: "Use the `running-problem-interviews` skill as the frame for drafting this script."

Expect the LLM to produce something 75-80% of the way there. Do not use it as-is.

### Step 4 — Run the mandatory human edit pass

LLM drafts reliably miss on these points. Edit each before you consider the script ready:

- **Strip casual slang** that doesn't fit the user's voice ("went down", "vibes", etc.). The user's register is direct and neutral.
- **Remove multiple-choice enumerations** inside questions. "Utilities, payment processing, cloud, or anything" is a survey prompt that anchors the customer on your categories. Ask the question bare.
- **Delete time-per-question estimates.** LLMs are reliably wrong about these.
- **Check question ordering.** If the interview is part of an active experiment with prior stimulus, the stimulus debrief goes FIRST, not buried at the end — the customer has fresh reactions, lead with them. If cold, order broad-to-specific. See `references/interview-structure.md`.
- **Verify every question** against `references/question-design-checklist.md`. Open-ended only. Past behavior only. No yes/no. No hypotheticals. No asking the customer to predict their future behavior.
- **Add "how do you solve this today?"** as a standard probe whenever a pain surfaces. This uncovers existing alternatives and switching costs, and often reveals that what sounds like a painful problem has an acceptable workaround — which changes the LoFA verdict.
- **Qualifying questions upfront, if needed.** If the interviewee's fit to the target customer segment isn't already confirmed from prior interactions, add 2-3 demographic/role/authority questions at the top. If fit is confirmed (returning contact, known prospect), skip.

### Step 5 — Write the opener (vision statement)

Format: "I believe I can help [specific customer segment] [specific outcome]." Segment-specific, outcome-focused, no product noun, no features. See `references/vision-statement.md` for template and examples.

For a follow-up interview with someone the user has already met, the full vision statement can be replaced with a warm restatement of purpose ("I'm working on something new, today I just want to learn from you").

### Step 6 — Write the pre-drafted deflection phrase

When the interviewee asks "what are you working on?" or "what is your product?", the interviewer needs a verbatim line to deploy. Ad-libbing in the moment leads to solution-talk which contaminates every subsequent answer.

Default template: "I'm so early I have nothing to show yet. Happy to share more on our next call. Today I really just want to learn from you."

Tune to context. See `references/deflection-phrase.md`.

### Step 7 — Confirm logistics

- Recording consent (ask explicitly at call start).
- Pairing: one interviewer + one observer is the default. Solo is acceptable **only if recording is confirmed working**.
- No questions in the script whose answer is available publicly — that wastes the customer's time.

### Step 8 — Write the final script

Target structure:
- 30 minutes (45 max).
- 3-5 core questions. Depth per question, not breadth across many.
- Anchor the customer early on a specific past story, then drill with "why" and follow-ups.
- Close with "is there anything I should have asked about?" and "who else would have strong opinions on this?"

See `references/interview-structure.md` for full templates (cold and experiment-paired variants).

Save the script to `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/2nd Brain (I)/1-Projects/[Project]/problem-interviews/YYYY-MM-DD-[interviewee]-script.md` alongside a short interview brief (LoFA being tested, interviewee background, sensitivities, logistics).

## In-interview discipline

During the call, hold these disciplines. They are the difference between real signal and contaminated data.

### No solution-talk

Do not pitch. Do not explain the product. Do not describe features. The moment you talk about your solution, you anchor every subsequent answer on your framing.

If the customer asks "what are you working on?", deploy the pre-drafted deflection phrase verbatim (step 6). Don't ad-lib.

### Visible checklist

Keep the 3-5 core questions visible. Rich follow-up threads can eat the full 30 minutes and leave the LoFA-critical question unasked. Move on from a thread when it's done, even if it's interesting.

### Signal-detection rules

Three things to watch for in real time and in the debrief. Full detail in `references/signal-detection.md`.

- **Three bad data types to discount** (from The Mom Test): compliments ("great idea!"), fluff/hypotheticals ("I would probably"), and future promises ("I'd totally buy that"). Redirect to past-behavior stories, or discount in the debrief. Do not treat any of these as validation.
- **Unprompted mentions are the highest-signal data.** When the customer brings up a pain you did NOT ask about, tag it as `unprompted` — it carries more weight than anything you prompted.
- **Silence is a tool.** After asking a question, wait. Do not fill pauses. Customers fill silence with the richest material — second thoughts, caveats, specific examples.

### Advanced: deliberate-incorrect-paraphrase

Once or twice per interview, paraphrase the customer's position back in a directionally-wrong way to provoke a correction. People correct errors with more richness than they answer direct questions.

**Example from the elicitation session**: user asserted "so you actually have almost all of your costs as variable costs" — knowing it was wrong. The Dutch-direct interviewee corrected him with a much richer fixed-vs-variable breakdown than a direct question would have elicited.

Use sparingly. Requires prior signal to be plausible. Don't fabricate — paraphrase in a directionally-wrong way that still respects what they said. Risks: if too off, the customer thinks you weren't listening; with a non-direct personality, they may just agree to be polite.

### Problem ranking (conditional)

If the interview explores multiple pain points, or the customer volunteers multiple unprompted, add a ranking turn near the end: "Of everything we talked about today, which one causes you the most trouble? Which one do you think about most often?" Must-solve / nice-to-solve / don't-care. Skip this turn when the interview targets a single LoFA with one pain.

## Close-out

Two questions at the end:

1. "Is there anything I should have asked about?" — surfaces the interviewee's own priorities rather than confirming yours.
2. "Who else at [their company] would have strong opinions on this?" — opens referrals.

## Debrief (after the call)

Capture within 24 hours while memory is fresh. See `references/debrief-template.md` for the full structure. The non-negotiables:

- **Verbatim customer quotes** on key pain points and decision moments. Pull from the recording/transcript. Quotes travel across time and teammates; paraphrases rot.
- **Unprompted mentions flagged.** These carry more weight than prompted answers.
- **LoFA signal summary** — does the evidence support, contradict, or leave ambiguous the assumption being tested?
- **Contamination flags** — moments where the interviewer's language may have anchored the customer's answers.
- **Three-bad-data-types flags** — compliments, fluff, future-promises recorded but tagged as low-signal.
- **Next steps** — any commitments made, follow-ups scheduled, referrals to chase.

Once the debrief is written, consider invoking `capturing-customer-insights` on it. That skill will suggest candidate insights (unprompted mentions, verbatim quotes, behaviors) for you to approve/edit/reject and file into the segment folder. Optional — skip if the interview was thin or nothing surprised you. But compounding only happens if you capture.

## Decision rule — never decide from interviews alone

A single interview is one data point, rich but partial. **Decisions on whether a LoFA is validated or invalidated require experiment evidence + interview context + hard data** (usage metrics, conversion rates, commitment signals, actual payments).

The interview's job is to inform the experiment's interpretation, not to substitute for it. Sample-size and stopping-criteria discipline live upstream in `running-rapid-experiments`.

## Related skills

- **`running-rapid-experiments`** — owns experiment design, LoFA selection, sample size, commitment-and-currency tests if required. Upstream of this skill.
- **`populating-lean-canvas`** — uses broader discovery interviews early in canvas construction. Different job: mapping the territory vs. testing a specific assumption.
- **`searching-meeting-transcripts`** — pulls prior transcripts for the fact-check step, and post-interview analysis.
- **`looking-up-contacts` / `looking-up-deals` / `looking-up-organizations`** — fact-check inputs.
- **`preparing-for-meetings`** — generic meeting prep; do not use for problem interviews.

## References

- `references/question-design-checklist.md` — the open-ended / past-behavior / no-multiple-choice rules with examples of each violation.
- `references/interview-structure.md` — full script templates for cold and experiment-paired variants, with opener through close.
- `references/vision-statement.md` — opener format, worked examples, when to skip.
- `references/deflection-phrase.md` — "what are you working on?" deflection template and tuning guidance.
- `references/signal-detection.md` — three bad data types, unprompted vs prompted, silence, deliberate-incorrect-paraphrase with examples.
- `references/debrief-template.md` — post-interview capture structure.
