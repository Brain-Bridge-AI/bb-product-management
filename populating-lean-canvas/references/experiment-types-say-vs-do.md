# Experiment Types — Say vs. Do

This reference exists because rapid experiments live or die on one distinction: **what customers say vs. what customers do.** The canvas itself prints "no surveys!" for a reason. Read this any time you're scoping the Experiment box or when the user proposes "let's ask them."

## The core problem with what customers SAY

Stated intent is a notoriously weak predictor of actual behavior. People:

- **Are polite.** They say yes because disagreeing feels rude.
- **Guess at their own future selves.** They can't accurately forecast how they'll behave in a future context.
- **Want to be interesting.** They describe aspirational versions of themselves.
- **Pattern-match to what the interviewer seems to want.** Demand characteristics.
- **Forget their constraints.** In the abstract, a feature sounds great; in their actual workflow, they don't adopt it.

Every one of these failure modes is absent when you observe actual behavior. That's the whole reason the loop exists.

## Red flags — designs that drift into SAY

If any of these show up in the experiment design, it's a SAY experiment regardless of the label:

- "Survey them about…"
- "Send a poll…"
- "Interest form / waitlist sign-up" *without a subsequent real commitment step*
- "Would you buy this?" / "Would you use this?" / "How interested are you in…"
- "Rank these features"
- "Focus group"
- "Net promoter score"
- Any question framed as "would/could/might"

These have a place in discovery research, but they're not rapid-experiment evidence. If the user proposes one, convert it — see the patterns below.

## DO experiments — the full taxonomy

Organized roughly from weakest signal to strongest. Pick based on what the LOFA actually demands.

### 1. Fake door / landing page test

**What it is.** Publish a landing page describing the product as if it exists. Customers who want it click "sign up" or "get early access" and give you an email. You see the conversion rate.

**Signal.** Real interest under real friction (giving an email, committing attention).

**When to use.** LOFA is about *whether people want this enough to take a step*. Classic for testing new product concepts or new segments.

**Failure modes.**
- Traffic from a generic source (Google Ads to a cold audience) is noise — interest is about the *qualified* visitor. Control the traffic source or be explicit about it.
- A pretty landing page with no commitment step tests design, not interest. Always include the commitment step.
- Measuring impressions instead of conversions. Impressions are SAY (they looked); conversions are DO (they acted).

### 2. Concierge MVP

**What it is.** Deliver the product outcome *manually* to a handful of real customers. No product, just humans doing the work. The customer pays (or at least commits real currency — time, reputation, introductions) for the outcome.

**Signal.** Willingness to pay for the outcome itself, independent of the product. Very strong — proves the problem is worth solving.

**When to use.** LOFA is about *whether the problem is worth paying to solve* or *whether this outcome is valuable enough that the delivery mechanism doesn't matter yet*.

**Failure modes.**
- Giving it away free defeats the test — if they won't pay, you haven't learned willingness-to-pay.
- Scaling it before the signal is clear. The point of concierge is that it doesn't scale; that's the feature, not the bug.

### 3. Wizard of Oz

**What it is.** Customer uses what looks like a product. Behind the interface, humans are doing the work. They don't know.

**Signal.** Does the workflow work? Would customers use a real version? Strong signal on product-market fit of the workflow, independent of engineering cost.

**When to use.** LOFA is about *whether the product shape is right* — before investing in building it for real.

**Failure modes.**
- The humans can't keep up, users notice, test contaminated.
- Ethical concerns about deception — be transparent afterward and never have the humans harm the user.

### 4. Pre-sales / smoke test

**What it is.** Real money down before the product exists. Kickstarter-style, or direct invoiced commitment with a refund clause. LOIs from B2B customers.

**Signal.** The strongest. Willingness to pay cash for a future product is the hardest signal to fake.

**When to use.** LOFA is about *commercial viability at a price*. When the LOFA hinges on whether someone will *actually buy*.

**Failure modes.**
- Low friction "reserve your spot" without actual payment drifts into SAY territory (interest, not purchase).
- Heavy legal overhead can kill the speed of the experiment. Use LOIs or non-binding commitments with real signatures when full payment is too slow.

### 5. Definitions / knowledge probe

**What it is.** Ask the customer to articulate the model / concept / term in their own words, unaided. If they can define it, they understood it.

**Signal.** Understanding. The opposite of nodding-along.

**When to use.** LOFA is about *whether customers understand something* — a pricing model, a technical concept, a value prop. (This is the type used in the elicited example: token-based pricing model.)

**Failure modes.**
- Helping them during the probe contaminates everything. No assistance.
- Measuring right/wrong on multiple choice is weaker — they can pattern-match. Free-form articulation is the test.

### 6. Observational study

**What it is.** Watch customers in their real environment without intervention. Shadow them. Record screen-time or session-time if digital.

**Signal.** Actual behavior, not reported behavior.

**When to use.** LOFA is about *what customers actually do in their workflow* — and self-report is unlikely to be accurate. Common for LOFAs about current behavior ("do salespeople actually update the CRM?") or problem discovery ("where does the real friction live?").

**Failure modes.**
- Observer effect — they behave differently when watched. Multi-session studies or unobtrusive methods reduce it.
- Watching without a hypothesis gives you anecdotes, not evidence. Know what you're looking for.

### 7. Behavioral choice

**What it is.** Put multiple real options in front of the customer with real consequences. Watch which one they pick. Not a survey — the choice has a follow-on (they commit to it, pay for it, schedule it).

**Signal.** Revealed preference under consequence. Stronger than stated preference.

**When to use.** LOFA is about *which thing customers prefer* when they have to live with the choice. Channel selection, feature prioritization, pricing tier selection.

**Failure modes.**
- If the options are presented as hypothetical, it reverts to SAY. Real consequences are load-bearing.
- Choice-set biases (order effects, decoy options). Know the cognitive-bias literature or accept that you're capturing relative signal, not absolute.

### 8. Prototype task

**What it is.** Give the customer a working or wizard-of-oz prototype. Assign them a real task from their workflow. Measure completion, time, friction points. Record the session.

**Signal.** Does the product actually work for the task? Where does it break down?

**When to use.** LOFA is about *whether the product shape solves the problem at all.* Usability and fit testing.

**Failure modes.**
- Assigning an artificial task ("imagine you wanted to…") drifts toward SAY. Real tasks from their real workflow only.
- Measuring completion without capturing friction misses the learning. Always capture where they hesitated, backed up, or asked for help.

## Conversion patterns — turning a SAY experiment into a DO experiment

When the user proposes a SAY experiment, here's how to transform it.

**"Let's survey CFOs about whether they'd adopt token pricing."**
→ *Put several pricing models in front of them and ask which one they'd sign an LOI on.* (Behavioral choice with real consequence.)
→ *Give them a quiz to define the terms unaided.* (Definitions/knowledge probe.)

**"Let's do a focus group to understand the problem."**
→ *Observe 3 customers in their real workflow doing the task we think is broken.* (Observational study.)
→ *Concierge the outcome for 3 customers manually and see whether they keep paying for it.* (Concierge MVP.)

**"Let's build an interest form."**
→ *Make a landing page with a paid pre-order or LOI commitment step.* (Pre-sales.)
→ *Make a landing page with a sign-up that immediately books a real session.* (Fake door with commitment.)

**"Let's ask them to rank these features."**
→ *Show them the features as real buttons in a prototype and see which they click for a real task.* (Prototype task + behavioral choice.)

**"Let's do a net promoter score."**
→ *Wait a week after use and see who comes back, or who brings a colleague.* (Observational.)

## Signal strength cheat sheet

From weakest to strongest on "is this what customers actually do":

1. Survey / poll (don't)
2. Interest form without commitment
3. Fake door / landing page with sign-up
4. Behavioral choice with consequence
5. Observational study in real environment
6. Prototype task with real workflow
7. Definitions / knowledge probe unaided
8. Wizard of Oz with real use
9. Concierge MVP with real commitment (time, money, reputation)
10. Pre-sales / real money down

Pick the highest-on-this-list design that's still feasible for your cycle. "Feasible" factors in: speed to build, customer-recruitment cost, and the hard constraint that the customer must leave happy.
