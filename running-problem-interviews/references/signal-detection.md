# Signal Detection Rules

In-interview and post-interview rules for separating real signal from noise. Pull this up during the call if you can; review it after.

## The three bad data types — discount these

From *The Mom Test* (Rob Fitzpatrick). These three response types feel like validation and aren't. Treat them as low-signal, redirect if possible, or tag and discount in the debrief.

### 1. Compliments

Any variation of "great idea!", "I love it!", "that's brilliant!", "you should totally build that!"

Compliments are what polite people say when they don't know what else to say. They are not evidence of anything.

**What to do:**
- Don't celebrate. Do NOT write "customer loved it" in the debrief.
- Redirect: "Thanks — but I want to understand your own situation. Tell me about a specific time when [analogous thing] came up for you."
- Tag in the debrief as `[compliment - discount]`.

### 2. Fluff and hypotheticals

"I would probably...", "I might...", "Maybe I'd use it if...", "In theory we could...", "It depends..."

Hypothetical future-self answers are fiction. People are bad at predicting their own future behavior, and worse at predicting it under social pressure from an interview.

**What to do:**
- Redirect to past behavior: "Tell me about the last time something similar came up — what did you actually do?"
- If they can't produce a past example, that's itself a signal: the problem may not be real enough to have produced any past behavior.
- Tag in the debrief as `[fluff - discount]`.

### 3. Future promises

"I'd totally buy that!", "Send me the link when it's ready!", "I want to be a beta customer!"

Words are cheap. Until the customer has done something that costs them (money, time, reputation, commitment), the promise is noise.

**What to do:**
- If the experiment includes a commitment test, deploy it here (see `running-rapid-experiments`).
- Otherwise tag and move on. Do not count future-promises as validation.
- Tag in the debrief as `[future-promise - discount]`.

## The one good data type — unprompted mentions

**Unprompted mentions are the highest-signal data in any interview.**

When the customer brings up a pain, a frustration, a workaround, a past purchase, or a concern that you did NOT prompt them for, they're revealing something that's *already active in their mind*. That's worth ten prompted answers.

**What to do:**
- Listen for it actively. Every time the customer volunteers something off-question, note it.
- Tag in the debrief as `[UNPROMPTED]` — these entries should stand out.
- Unprompted pains that align with the LoFA are strong support. Unprompted workarounds that make the LoFA irrelevant are strong contradictions.

## Silence is a tool

After you ask a question, wait. Do not fill the pause.

Customers fill silence with the richest material — second thoughts, caveats, specific examples they were editing out, doubts they didn't want to voice first. If you fill the pause with a clarifying question, you cut all of that off.

**Rule of thumb:** count to five after the customer seems to stop. If they don't continue, then you can follow up. But most of the time they *will* continue, and what they say next will be better than the first answer.

## Advanced: deliberate-incorrect-paraphrase

Once or twice per interview, paraphrase the customer's position back in a directionally-wrong way. They will correct you with more richness than a direct question would elicit.

**Why it works:** people correct errors with more specificity and emotion than they answer questions. A direct question like "what's your fixed-cost base?" gets a list. A confidently-wrong paraphrase gets the list + the ratios + the nuance + the "let me explain, listen" posture.

**Example from practice:**
- Interviewer: "So you actually have almost all of your costs as variable costs."
- Customer (Dutch-direct, pushed back hard): "No, not at all, not at all. Listen, there's plenty of fixed cost too. The office lease, phones, insurance, bonded work — that's all fixed. AccuLynx I told you about, HailTrace, payroll — those are fixed monthly. The owner takes a salary, the bookkeeper is on salary... There's a fixed base that runs probably thirty, thirty-five thousand a month no matter what. Probably sixty-forty, maybe seventy-thirty variable to fixed, depending on the month..."

Much richer than "what's your fixed vs. variable split?" would have produced.

### Rules for use

- Use sparingly — once, twice at most per interview. Overuse destroys credibility.
- Requires prior signal to be plausible. Don't fabricate — paraphrase in a directionally-wrong way that still respects what they said.
- Best with interviewees who've shown willingness to be direct (Dutch-direct Jay, for example).
- Risky with polite/agreeable personality types — they may just agree to avoid conflict, giving you no correction signal.
- If the paraphrase is too off, they'll think you weren't listening. Stay close enough to their actual position that the error is plausible.

## Contamination flags

Watch for moments where YOUR language may have anchored the customer's answer:

- You explained your product mechanism, then asked about an analogous past behavior.
- You used an industry-specific framing the customer then echoed back.
- You summarized their position (not as a deliberate incorrect paraphrase) and they agreed rather than corrected.
- You asked a leading question.

Tag these moments in the debrief as `[contaminated - discount]` or `[interviewer-anchored]`. The data point may still be usable, but its signal is degraded.

## Quick reference card

During the call, hold in mind:

| You hear | You do |
|---|---|
| A compliment | Redirect to past-behavior story |
| A hypothetical | "Tell me about the last time that actually came up" |
| A future promise | Tag and move on — don't celebrate |
| An unprompted pain | Tag UNPROMPTED, dig deeper |
| Silence after your question | Wait. Do not fill it. |
| Urge to explain your product | Deploy the deflection phrase instead |
