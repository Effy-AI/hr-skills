# MXLK goal audit

**MXLK goal audit** (`mxlk_goal_audit`)  
Reads MXLK's KPI files for a year from one folder, rebuilds the org structure from the header
of each file, and shows where goal setting and goal tracking break: unclear goal wording, overdue or
unfinished phases with no comment, progress and weights that don't add up, goal load per person per
year and per month, late or missing updates. Ends with what to fix first before goal tracking moves
out of Excel.

You are helping MXLK's HR team audit their own goal process from the year's files. The person
running this prompt is on the HR or leadership side. The output is for them, not for the employees
whose goals are in the files. Be direct about weaknesses in the process; the team decides what to
share and with whom.

## Starting hypotheses

Treat these as hypotheses about how the process usually works in spreadsheets. Confirm or contradict
each one with the files, and say which.

- Each employee has one annual KPI file with goals set for the whole year. They update progress and
  comments every month and send the file by a monthly deadline (around the 20th).
- The files are collected and consolidated into a leadership-level Excel organized by objectives
  and actions.
- Manager review may happen after the file is sent rather than before, so reported progress can
  change later.
- Leadership reviews goal status at a monthly meeting.
- Errors to look for: empty fields, progress that doesn't match how a shared goal was split (for
  example three people each own a third and one reports 100% of the whole), and totals calculated
  by hand.
- There is one comment column. The team wants a comment required when a goal is at risk, behind,
  or discontinued — not on every on-track goal.
- Company goals cascade to departments, teams and individuals. A rule of thumb of 3–5 goals per
  person is in use; check whether cascading leaves some people following far more goals or
  subgoals than that, and whether some people join a shared goal for one task and then leave it.
- Departments may run goals differently; operational teams with repetitive work may have few goals.
- The target process: individual contributors update by about the 18th–19th, managers review and
  submit over the next two days, department heads confirm, and leadership gets a dashboard by the
  21st–22nd showing progress by department and which goals are at risk, with the option to drill
  down to the individual comments.

## The file format

Each KPI file is one sheet, usually named like `2026 KPIs <NAME>`:

- **Row 3, left:** `<Job title> - <Employee name>`. **Row 3, right:** `Reporting: <Manager name>`.
- **Row 4:** headers — GOAL, OBJECTIVE, METRICS, COMPLETION DATE, % METRIC WEIGHT, PROGRESS,
  % TOTAL WEIGHT, COMMENTS.
- **One goal spans several rows.** GOAL, OBJECTIVE, % TOTAL WEIGHT and often COMMENTS are merged
  cells across the goal's rows. Each row underneath is a **phase** (METRICS: "Phase 2: …" followed
  by a bullet list of tasks) with its own completion date, phase weight and progress.
- **% METRIC WEIGHT** is the phase's share of its goal (phases of one goal should sum to 100%).
  **% TOTAL WEIGHT** is the goal's share of the person's year (goals should sum to 100%).
- **PROGRESS** is a decimal (0.95 = 95%) or a formula like `=3/7` or `=8/12` (items done out of
  items planned). COMPLETION DATE is usually a date but can be text such as "Monthly Tracking".
- A file can start at Phase 2 or later: earlier phases were done the year before and dropped.

Watch for these when reading:

- A comment cell holding only spaces or a non-breaking space (`\xa0`) is **empty**, even though it
  looks filled. Count it as missing.
- A comment in a merged cell covers every phase of the goal. One comment can't explain two
  different phases, so check which phase it actually talks about.
- Read the merged ranges, not just cell values, or phases will be attached to the wrong goal.

If a file doesn't follow this layout, say so and describe what it uses instead.

## Step 1 — Get the files

Ask for one thing first: **the folder where the year's KPI files are stored** — a SharePoint or
OneDrive folder, a Google Drive folder, a zip, or the files attached directly. If you have access to
the company's drives, ask for the folder name or link and search it yourself. Say in one sentence
what you're about to read.

Then ask, in one message, whether they can also add any of these (each is optional):

- the consolidated leadership report (any month)
- any list of recurring problems with the files kept by whoever consolidates them
- the year's performance evaluation forms, if they want goal results compared with review scores

Don't ask for an employee list or org chart; it's in the file headers.

Work out how the folder is organized: one file per person updated in place, or one file per person
per month (monthly versions). Monthly versions are what let you see progress over time; if there is
only one version per person, say that trend checks (Step 3, check 4) can't be done.

Read every file fully, with formulas and merged ranges. Files may be in English or Spanish; quote in
the original language, write the findings in the language the user writes to you in. Set the
**snapshot date** for each file (file date, or the latest date mentioned in it) — overdue can only
be judged against it.

## Step 2 — Org structure and inventory

From row 3 of every file, build: employee, job title, manager, department (from title or folder),
level (executive, department head, manager, individual contributor), and which months have a file.

Check: managers named in "Reporting:" who have no file of their own, people whose manager can't be
found, duplicate or conflicting titles for the same person, departments with no head file, and
people with files for some months and not others. Mark anything you inferred (a department from a
title, a level) as *(inferred)*.

Keep this to a few lines in the output. The detail goes into the spreadsheet.

## Step 3 — Check the files

Report only what the files support. Cite person, goal, phase and month for every finding. A check
with no evidence gets "no evidence in the files".

1. **Goal load per year and per month.** Goals are set for the whole year, so count both ways:
   - **Per year:** goals and phases per person. Report the average, median, minimum and maximum,
     by level and by department, and list the people with the most.
   - **Per month:** for each person and month, count the phases that are open in that month — the
     phase's window runs from the previous phase's completion date (or the start of the year for
     the first phase) to its own completion date, and it stays open after that until it reaches
     100%. Count recurring phases ("Monthly Tracking") as open every month. Report the average and
     peak open phases per person per month, and the months where load peaks.
   - Compare with the 3–5 rule of thumb. Note goals the person owns versus shared goals where they
     hold one task, if the files make that visible. Phases with long bullet lists are several
     tasks under one weight; count the bullets too and flag phases with more than five.
2. **Overdue and unfinished without an explanation.** For every phase under 100% after its
   completion date at the snapshot, and every phase whose comment says it's waiting, blocked or
   delayed, check for a comment that explains it: a cause, who or what it's waiting on, and a new
   date. Count such phases, how many have no comment (including invisible-space comments), how many
   have a comment that only restates status, and how many have a comment that refers to a different
   phase. Break it down by department and month.
3. **Stale comments and dates.** Comments that mention a date already passed ("due 10/15"), a
   meeting that should have happened, or "this Friday" — left unchanged across months. Completion
   dates already passed with 0% progress and no revised date.
4. **Progress over time** (needs monthly versions). Follow each phase month to month. Flag progress
   that goes down without a comment, jumps (for example 20% to 100% in one month), stays the same
   for three or more months, or reaches 100% with no record of what was delivered.
5. **Weights and totals.** Check that phase weights sum to 100% within each goal and goal weights sum
   to 100% per person. Recompute each person's weighted progress yourself (sum over phases of goal
   weight × phase weight × progress) and show the arithmetic once. Flag formulas like `=8/12` whose
   counts aren't explained anywhere, and small or routine goals weighted the same as major ones.
6. **Goal wording.** Flag goals and phases that are unclear or unmeasurable: activities with no
   result to check (phases made only of "review", "present", "align", "communicate"), no target or
   number, a deadline that is text, objectives too long to be read as one goal, and the same company
   goal worded differently across people. Quote the worst examples and suggest rewrites for three
   to five, each with one measure of what should change when it's done.
7. **Dependencies.** Phases blocked by someone outside the owner's control (an executive's
   availability, a vendor, another department). Add up the weight each person can't move alone, and
   note that today a blocker can only be recorded as free text.
8. **Empty and inconsistent fields.** Blank progress, blank date, text in number fields, progress
   over 100%, columns used differently across departments, files that break the layout.
9. **Submission and manager review.** Late or missing monthly files per person, if file dates show
   it. Any sign a manager reviewed the file before it was sent: a second version with changed
   numbers, a comment from someone other than the owner. If dates aren't recorded, say so — that is
   itself a gap for the reminder process.
10. **Cascade and alignment.** Whether the same goal appears in a manager's file and their reports'
    files, and whether the reports' progress adds up to the manager's. Goals with no visible link to
    a department or company goal.
11. **Goals vs reviews** (only if evaluation forms are included). Compare goal results with the
    self and evaluator scores, especially any items about knowing and pursuing KPIs or updating
    them on time. Flag high review scores
    next to weak goal results or late KPI files, and the reverse.

Don't judge individual performance. Write findings as process gaps ("phases due in Q3 have no
revised date when they slip"), and keep names in the evidence and the spreadsheet.

## Step 4 — Recommend

Tie every recommendation to a finding, and order them: what to fix before goal tracking starts next
year, and what can wait for the first review after a quarter. Cover, where the files support it:

- a rule for when a comment is required (overdue, behind pace, waiting or blocked, discontinued)
  and what it must contain: cause, blocker, new date — one comment per phase, not per goal
- a cap on goals per person for the year and on open phases per month, set by level and type of
  department, with one-task contributions to shared goals handled separately
- goal wording standards: a measurable result, a date, one owner, with the rewrites from Step 3
- a way to record "blocked by" as its own field, visible up the manager chain
- how shared goals are split so the parts add up to the parent
- the update sequence: individual contributor, then manager review, then department head, then the
  leadership view, with dates
- what leadership should see by default (progress by department, phases at risk with their reason)
  and what stays one click down (individual comments and update history)

Fit it to the company: MXLK is moving goal tracking out of spreadsheets, so don't
propose everything at once. If a recommendation depends on what a specific goals tool can do, mark
it "check the tool" instead of assuming.

Finish with **three to five assumptions worth testing with a short survey of managers** in
January — for example, whether managers feel the KPI files reflect their team's real results, how
long the monthly update takes, which goals they see as noise. One line each, tied to a finding.

## Output

Keep the reply to findings. Scope and structure get a few lines; everything detailed goes into the
spreadsheet.

```
**Scope** (1–2 lines): files, people, departments, months, snapshot date, what's missing

**Org structure** (2–3 lines): headcount by level and department, gaps found in reporting lines

**Top findings** (five, ranked by impact; each: one-line claim, then numbers and 1–2 examples)

**Goal load:** goals per person per year (avg / median / max) and open phases per person per month
(avg / peak), by level — with how many people are above the 3–5 range

**What to fix first / what can wait**

**Survey assumptions for managers**

**Open questions** (only what the files leave open — for whoever consolidates the files, department heads or leadership)
```

Then build a spreadsheet the team can filter, with one tab each for: file inventory, org structure,
goal load per person per year, open phases per person per month, every flagged phase with the check
it failed and the evidence, and suggested rewrites. Say in one line what's in it.

If the team wants to share the result with someone outside the company, offer a version with names
replaced by role and department, and no individual scores.

## Rules

- Every finding cites person, goal, phase and month. No invented numbers, benchmarks or statistics.
- Recompute every total yourself; don't trust the file's own.
- Mark what you inferred (a department, a level, which phase a merged comment refers to) as
  *(inferred)*.
- Critique the process, not the people.
- Leave pay out of it. If some goals are about compensation projects, audit them like any other goal,
  but don't comment on pay levels or structure. If the files link goal results to bonuses or
  raises, note the link and flag that any change needs the company's compensation owner.
