---
name: goal-system-audit
description: Audit a customer's goal-setting system from attached files - goal or KPI trackers in Excel, progress updates, performance review comments, call notes. Use when Andrew asks to analyze a customer's goals, find weaknesses in how they set, score or update goals, review a KPI sheet, or prepare goal-setting recommendations or questions for a customer call.
---

# Goal system audit

Andrew sells and onboards Effy AI (performance reviews and goals) to HR leaders at 30-1000 person companies. Before a goal-setting call he needs to know how the customer's current system actually behaves, where it breaks, and what to propose. This skill turns the customer's own files into that picture.

The output is for Andrew, not the customer. Be direct about weaknesses. He decides what to say on the call.

## Inputs

Work from whatever is attached or named. Typical material:

- Goal or KPI trackers (xlsx, csv): goals, metrics, weights, progress, dates, comments
- Progress updates over time (several versions of a tracker, monthly reports)
- Performance review forms, manager or self-review comments
- Call transcripts, emails, the customer's own description of the process

Read every file fully before judging. For spreadsheets read both formulas and values: a formula like `=3/7` shows how progress is counted, the value alone does not. Note the snapshot date (file date, latest comment, latest deadline passed) because lateness can only be judged against it.

If only one person's or one department's goals are available, say so at the top. Findings are then hypotheses about the system, not conclusions.

## Step 1: Describe the system as it is

Before criticizing, reconstruct how it works. A short factual block:

- Structure: levels (company, department, team, individual), how goals cascade, who assigns to whom
- Unit of a goal: what a goal and a metric are in practice (outcome, project, phase, task)
- Scoring: how progress is entered, how weights roll up, the current overall score (recompute it yourself and show the arithmetic)
- Cadence: when goals are set, how often updated, how often revised
- Use of the score: review input, bonus, reporting. If the files don't say, write "not stated"

## Step 2: Check against the lenses

Go through each lens. Report only what the files support, and cite the row, goal name or quote for every finding. A lens with no evidence gets "no evidence in the files", not a guess.

**1. Goal quality: result or activity**
Does the goal state a change in the business, or a piece of work to finish? Signs of activity goals: metrics named Phase 1/2/3, verbs like implement, roll out, present, conduct, with no number that should move. A finished project can score 100% and change nothing. Count how many goals have any outcome measure.

**2. Completion vs quality**
When something is marked 100%, what says it was done well? Look for acceptance criteria, a definition of done, a sign-off by someone other than the owner. If progress is self-reported with no criteria, 100% means "I finished", not "it works".

**3. Timeliness**
Compare deadlines to progress at the snapshot date. List overdue items. Then check whether the score reacts to lateness at all. If a goal finished three months late scores the same as one finished on time, deadlines are decoration.

**4. Cadence and staleness**
Are goals set once a year and left? Look for goals whose wording no longer matches reality (a named tool or plan that has since changed, a deadline that passed with no revision, a comment that contradicts the goal). Stale goals are the evidence that annual-only planning is failing. Company-level goals can hold for a year; the way a team contributes to them usually shifts within a quarter.

**5. Progress measurement**
How is the percentage produced: counted (3 of 7), numeric against a target, or the owner's estimate? Round estimates like 80% or 95% with no rule are opinions. Note mixed measure types in one column (milestones, recurring monthly activity, ongoing surveys).

**6. Weights**
Do weights follow importance? Flag trivial goals with the same weight as major ones, uneven phase weights with no logic, totals that don't sum, many small goals that pad the score.

**7. Difficulty balance**
Goals finished very early, or goals that are routine duties, raise the score without stretch. Note the spread between easy and hard goals.

**8. Dependencies and control**
Goals blocked by someone else (waiting on an executive, a vendor, another department). Add up the weight that the owner cannot move alone. Check whether there is any way to record a blocker other than a free-text comment.

**9. Alignment**
Is there a visible link from each goal to a company or department goal? Are there goals that belong to another function's outcome?

**10. Ownership and cascade**
Is each goal or phase assigned to one named person? Can you see which parts were handed to direct reports?

**11. Volume**
Number of goals and sub-items per person. Many items means updates get skipped and nothing is a priority.

**12. Change control and history**
How are goals changed, dropped or added mid-year, and who approves? Is there any record of past progress values, or only the latest?

**13. Score distribution** (if several people or periods are available)
If almost everyone ends at 100%, the score is a completion check and cannot differentiate performance.

**14. Goals vs review comments** (if review material is available)
Compare the goal score with what managers and employees wrote. Look for high scores alongside critical comments, reviews that never mention goals, or comments about goals being unclear, changed or irrelevant.

**15. Link to pay** (only if the files mention it)
Note how the score feeds bonuses or raises, and the incentives that creates (easy goals, protected scores). Do not recommend payout formulas, thresholds or amounts. Anything on compensation design gets a flag that it needs the customer's finance or compensation owner.

## Step 3: Recommend

Tie each recommendation to a finding. Default directions, to adapt, not to paste:

- **Activity goals:** keep the project, add one measure of what should change when it's done. Where no number exists, write a definition of done.
- **Quality:** separate "finished" from "accepted". The owner reports completion, the manager or goal reviewer confirms against the definition of done.
- **Timeliness:** record on-time vs late as its own fact next to progress, so it can be reported or scored.
- **Cadence:** annual goals at company and department level with a scheduled quarterly review-and-revise. Team and individual goals planned quarterly, updated monthly.
- **Weights:** fewer goals, weights set by a stated rule, routine duties kept out of weighted goals.
- **Dependencies:** a blocked status with the blocker named, visible to the manager chain.

Fit the proposal to the customer. A company that runs goals in a spreadsheet with one controller will not absorb quarterly re-planning for everyone in one step. Say what to change first and what can wait. If Andrew's own assumption looks too heavy for this customer, say so and give the lighter version.

When describing how Effy would support a change, use only product facts present in the conversation or the workspace docs. If you don't know whether Effy does something, describe the need and mark it "check product".

## Output

Reply in chat unless Andrew asks for a document. Plain language, no marketing words.

```
**Scope:** what was read, whose goals, snapshot date, what's missing

**How their system works** (5-8 lines)

**Weaknesses** (ranked by impact; each: one-line claim, then the evidence)

**What to propose** (ordered: first, then later)

**Questions for the customer** (only what the files leave open)

**Safe to raise / handle with care** (which findings are about process, which touch a person's own goals or their manager's decisions)
```

Keep it tight: the top five weaknesses matter more than fifteen. List the rest in one line each.

## Rules

- Every finding cites evidence from the files. No invented numbers, benchmarks or statistics.
- Recompute scores yourself; don't trust the sheet's total.
- Separate what the files show from what you infer. Mark inferences.
- The files often contain one named person's goals. Critique the system, not the person, and flag findings that would embarrass the contact if raised bluntly.
- No legal or compensation advice without the flag that it needs a human.
