# Scanning Sources for Candidate Insights

Specific patterns to look for when pulling candidate insights from each source type. The better the scan, the better the suggestions, the less work for the user.

## From a problem-interview debrief

The `running-problem-interviews` skill produces debriefs with tagged sections. Look for:

### Always captured

- **`[UNPROMPTED]` tags** — every unprompted mention is a candidate insight. These are the highest-signal findings in any debrief. Don't skip.
- **Key behaviors observed** — the "what did the customer DO" section. Each distinct behavior is a candidate.
- **Existing alternatives / workarounds** — each workaround tells you about switching costs.
- **Surprises** — the debrief's "what did not you expect" section. Surprises beat confirmations.

### Captured with care

- **Verbatim quotes** — pull any quote marked `(no tag)` (i.e., regular past-behavior data). Skip quotes tagged `[compliment - discount]`, `[fluff - discount]`, or `[future-promise - discount]` unless the interviewer flagged them as "worth revisiting."
- **Problem ranking results** — if the interview had a ranking turn, the ranked list itself is an insight. One insight: "In this interview, customer ranked X > Y > Z for must-solve."

### Usually skipped

- The interview prep notes, the opener, the questions themselves — these are process artifacts, not findings.
- Generic "the call went well" observations — not learning about the customer.
- Interviewer self-critique (except as useful meta-lessons elsewhere, not in customer insights).

### Typical yield

3-7 candidates per 30-minute interview debrief. A Mom Test-compliant interview yields more than a rambly one.

---

## From a rapid-experiment debrief

The `running-rapid-experiments` skill produces Persevere / Pivot / Stop reports. Look for:

### Always captured

- **Supported assumptions** — for each assumption the experiment supported, write one insight tagged `Supports: [assumption-id]` with confidence = high (experiments produce behavioral data by design).
- **Contradicted assumptions** — same but `Contradicts: [assumption-id]`. These are often more valuable than supported ones because they force the canvas to update.
- **Unexpected findings** — things that surprised the experiment team. Usually the richest insights.

### Captured with care

- **Customer quotes collected during the experiment** — pull them individually as insights, each with their own Doc. Quotes > summaries.
- **The evidence metric itself** — "3 of 5 customers committed a calendar slot" is an insight. Confidence = high because it's behavioral.

### Usually skipped

- The experiment design itself — belongs in the experiment Doc, not in customer insights.
- Internal team logistics about running the experiment.

### Typical yield

2-5 candidates per experiment cycle.

---

## From a desk research report (researching-customer-segments)

The research skill produces a 5-section report: Segment Hypothesis / Size / Shape / Reachability / What We Can't Know. Look for:

### Always captured

- **Size claims with sources** — one insight per claim. Confidence = medium (public data, not customer behavior), unless the source is census-level, in which case high.
- **Observable behaviors identified** — each "behavior that identifies the segment" is an insight. Confidence = medium (based on hypothesis, not yet confirmed).
- **Named candidate interview targets** — not insights themselves, but update the segment definition's "reachability" section.

### Captured with care

- **Bowling-pin test outcome** — if the research concludes the segment is too fat/too thin/right-sized, that conclusion is an insight tagged with confidence = medium.
- **Filter stack** — the specific NAICS + headcount + geography + behavioral combo. One insight, tagged `Tags: recruitment-filter`.

### Usually skipped

- The "what we cannot know" list — that's an explicit reminder that desk research didn't answer those questions. Don't capture it as an insight; instead, ensure the listed questions get asked in the next interview.

### Typical yield

4-8 candidates per desk research report.

---

## From a meeting transcript (not a debrief)

Sometimes the user wants to pull insights from a raw Google Meet transcript — a sales call, a customer success check-in, a user research session — without running the full problem-interview debrief flow. Look for:

### Always captured

- **Unprompted customer complaints or praise about existing tools** — high-signal statements about workarounds and pain.
- **Specific past-behavior stories** — "last quarter we did X and it failed because Y."
- **Named numbers, counts, thresholds** — "we spend $40K/month on tools we barely use." Concrete numbers travel well.

### Captured with care

- **The salesperson's summary of what the customer said** — be careful; salespeople round up. Prefer to go back to the transcript and pull the customer's actual words.

### Usually skipped

- Small talk, scheduling chatter, product demo logistics.
- The salesperson's pitch.

### Typical yield

2-6 candidates per hour of transcript.

---

## From an ad-hoc observation

Sometimes the user just says "Capture this: I noticed that fractional CFOs keep mentioning they can't get their team to use the forecasting tool." No source document. Just a verbal observation.

Accept the observation, draft it as a single-insight candidate with:
- `Source: observation`
- `Source Ref: [session context — e.g., "Pablo conversation 2026-04-24"]`
- `Confidence: low` by default (observations are weak evidence unless backed by specifics)

Ask the user if there's a specific conversation, source, or behavior they're thinking of — often there is one, and upgrading to `Source: problem-interview` with a source ref raises confidence immediately.

---

## The universal test

Before proposing a candidate insight to the user, ask yourself: **"If someone six months from now reads just this insight, will they be able to use it?"**

- If the answer is yes — propose it.
- If it requires context from the source doc to make sense — write the context into the insight body so it stands alone.
- If it's fundamentally too thin to stand alone — drop it. Noise buries signal.
