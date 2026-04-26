# Interview Structure Templates

Two variants. Pick based on whether the interview is part of an active experiment (customer has seen prior stimulus) or cold (no prior stimulus).

## Variant A: Part of an active experiment (stimulus-paired)

The customer has already reacted to material — a pricing sheet, prototype, pitch deck, mockup. Lead with their fresh reaction before it stales.

### Structure (30 min target)

1. **Opener (1-2 min)** — vision statement + recording consent. See `vision-statement.md`.
2. **Qualifying questions (2-3 min, conditional)** — skip if fit is already confirmed.
3. **Q1 — Stimulus debrief (5-8 min)**
   "You just went through [the material]. In your own words, what did you take away?"
   Follow-ups: What was clear? Where did you get stuck? How would you explain it to [their boss / their team]? What would you push back on?
4. **Q2 — Anchor story (8-10 min)**
   "Tell me about the last time you [did the analogous past thing]. Walk me through how that went."
   Follow-ups: Who was involved? How did it get decided? What surprised you? How do you handle this today?
5. **Q3 — Adjacent past behavior (5-8 min)**
   "Tell me about [analogous domain]. What's your experience there?"
   Follow-ups: Why that approach? What went wrong? What would you do differently?
6. **Q4 — Problem ranking (3-5 min, conditional)** — if multiple pain points surfaced, have the customer rank them.
7. **Close (2 min)** — "Anything I should have asked about?" + "Who else at [their company] would have strong opinions on this?"

## Variant B: Cold interview (no prior stimulus)

No material has been shown. Work broad to specific, build from concrete past behavior to the LoFA-adjacent territory.

### Structure (30 min target)

1. **Opener (1-2 min)** — vision statement + recording consent.
2. **Qualifying questions (2-3 min, conditional)** — skip if fit is already confirmed.
3. **Q1 — Anchor story (8-10 min)**
   "Tell me about the last [relevant past action — purchase, decision, problem]. Walk me through it."
   Follow-ups: Who was involved? How did it get decided? What surprised you?
4. **Q2 — LoFA-adjacent pain (8-10 min)**
   "Tell me about [the specific domain the LoFA is about]."
   Follow-ups: When does that come up? How often? How do you solve it today? What have you tried that didn't work?
5. **Q3 — Alternatives / workarounds (5-8 min)**
   "What's your workaround today? What else have you looked at?"
   Follow-ups: Why didn't [alternative] work? What's stopped you from [obvious fix]?
6. **Q4 — Problem ranking (3-5 min, conditional)** — if multiple pain points surfaced.
7. **Close (2 min)** — "Anything I should have asked?" + "Who else would have strong opinions?"

## Timing notes

The LLM that drafts the first pass will guess at minutes-per-question. Those guesses are reliably wrong — ignore them. In practice:

- Anchor stories take 8-12 minutes when done well (the customer needs room to remember and narrate).
- Follow-up "why" chains eat time fast. Budget.
- The close always takes longer than you expect because referrals and "oh, and also..." happen here.

If you're running long on Q1-2, cut Q3 rather than rushing. Three deep questions beat five shallow ones.

## Follow-up prompt library

Pull from these during any question when the answer is too abstract:

- "Tell me about a specific time when..."
- "Walk me through what actually happened."
- "What did you do next?"
- "Who was involved?"
- "Why did you pick that?"
- "What were you worried about?"
- "What surprised you?"
- "How do you handle it today?"
- "What's your workaround?"
- "What have you tried that didn't work?"
- "Say more about that."
- (silence — let them fill it)

## Platform formatting

When writing the script to Obsidian:
- Use standard markdown headers for each section.
- Include the LoFA being tested as a front-matter banner at the top of the script so the interviewer sees it during prep.
- List follow-ups as indented bullets under each core question so they're visible at a glance during the call.
