# Build a growth plan

**Build a growth plan** (`growth_plan_builder`)  
Draft a growth plan for one person — career development, personal development, leadership development, or a performance improvement plan — grounded in their career level and what the next level asks, their latest reviews, their 1:1s and goals, then save it to Effy AI as a draft after approval.

Draft one growth plan for one person: where they're heading, the gap between where they are and
what that asks, the steps and actions that close it, and how progress gets checked. Grounded in
the person's actual record — not a generic list of courses.

A growth plan is worth having when it names a specific gap, a specific action that closes it, and
a date someone will look at it again. Most plans fail by being a wish list: "improve
communication", "take a leadership course", no owner, no date, never reopened. Every line in this
plan has to be something the manager could check at the next quarterly review.

## Rules

- **Ground every gap in evidence** — the person's career framework, a review, a 1:1, a goal, or
  what the user told you. Mark anything that comes only from the user's recollection
  `[from your input]`, and anything you inferred `(assumption)`.
- **Never invent** a level expectation, a review comment, a commitment, or a resource the company
  offers (a budget, a mentoring programme, a course). If you don't know whether it exists, ask or
  leave it as a question.
- **Nothing is written to Effy before the user approves the draft.** Plans are created as
  **Draft**, which keeps them hidden from the employee until someone moves them on. Never change a
  plan's status, access, or send notifications unless the user asks for that specifically.
- **No sensitive detail** in the plan — health, personal circumstances, pay. If something like
  that affects the plan, the plan says what changes (scope, timing), not why.
- **No compensation advice.** If the plan touches a raise or promotion outcome, it says what the
  promotion case would need, never what pay follows.

## Step 1 — Who, which type, which period

Get, in one short message, what the user hasn't already said:

- **Who the plan is for.** With Effy AI connected, resolve the person in the employee directory
  and confirm role, team and manager in one line. Match the person, not the name — check it's the
  right employee before reading anything else.
- **Which type of plan:**
  - **Career development** — growing toward a next level or a different role, 12–36 months.
  - **Personal development** — building specific skills in the current role.
  - **Leadership development** — growing as a manager or toward people leadership.
  - **Performance improvement** — closing a gap against the current level's expectations, with a
    defined timeline. See the note in Step 4.
  If the user doesn't know, suggest one from what they've said, in one line.
- **Which period** — a year, half or quarter ("H1 2027", "Q2 2027"). With Effy, resolve it with
  `hr_search_growth_plan_periods`.

Check for an existing plan for this person and period (`hr_search_growth_plans`). If one exists,
say so and ask whether to update it or start a new one. Don't create a second plan silently.

## Step 2 — Gather the record before asking for it

Read what you can reach in Effy AI **and** in the user's other connected tools — a review tool
(Lattice, Culture Amp, Leapsome, 15Five), the HRIS, notetakers and meeting notes (Fathom, Granola,
Zoom, Notion), drives with old development plans, a goals or OKR tool. Effy may hold only part of
the record. Rough order of yield; say in one sentence what you're about to read.

- **Career framework** — `hr_get_employee_career_framework`: their track and level, the current
  level's expectations per competency, and the next level's expectations, promotion signals,
  anti-patterns and growth opportunities. This is the spine of a career development plan. If the
  person isn't on a track, say so: the plan can still be built from reviews and the user's input,
  but the gap analysis will be weaker — and suggest `build-career-framework` for later.
- **Performance reviews** — the latest review reports for this person, as far as the user's access
  allows: ratings, manager comments, self-review, peer feedback. Look for the development areas
  that more than one source names.
- **1:1s** — 1-on-1 activities logged in Effy, meeting notes, transcripts. Look for aspirations the
  person has stated, blockers that keep recurring, and feedback given more than once.
- **Previous growth plans** — what was planned last time, and what happened to it. A gap that was
  on the last plan and hasn't moved is the most important line in this one.
- **Goals** — current goals or OKRs, so the plan's actions don't compete with the day job.

Without Effy, the same sources apply minus the Effy records; ask the user to paste or attach
whatever isn't reachable.

Then summarise in three or four lines what you found and what's missing, and ask only what the
record can't answer — once, in one message, at most four questions. Usually:

- What does the person want? (The plan fails if it's only what the company wants.)
- What can the company actually offer — stretch projects, a mentor, budget, time?
- Anything the manager knows that isn't written down?

## Step 3 — Pick the gaps that matter

From the record, list every gap between the person's current evidence and the target (next level
for career development; current level for performance improvement; the named skills for personal
or leadership development). Then choose **two or three** to build the plan around. More than three
and nothing gets done.

Choose by: what the next level most depends on, what more than one source names, what the person
said they want, and what's been on a previous plan without moving. Say in one line why these and
not the others; list the rest as "parked for the next plan".

For each chosen gap: the expectation (in the framework's own words), the current evidence (cited),
and what "met" would look like — observable, so two people could agree whether it happened.

## Step 4 — Draft the plan

**Read the plan type's structure from Effy** before writing: `metadata_get_object_schema` for
`growthplan` with the plan type's variant (`career-development`, `personal-development`,
`leadership-development`, `performance-improvement`). The `description` field's instruction is the
company's document structure for that type — follow it section by section, using its headings. If
Effy isn't connected, use this default:

1. **Direction** — the target and the horizon, and why it fits the person and the company.
2. **Gap analysis** — one entry per chosen gap: expectation, current evidence, what "met" looks
   like.
3. **Milestones** — two to four intermediate checkpoints, each with a date.
4. **Development actions** — one per line, each linked to a gap, with an owner and a due date.
   Prefer experience (a stretch project, owning an area, leading a meeting) over courses;
   roughly most growth comes from doing the work, some from people, least from training — use
   courses only where a specific skill needs teaching.
5. **Support** — what the manager commits to, a mentor or sponsor if one exists, resources
   actually available.
6. **Check-ins and sign-off** — monthly progress in 1:1s, a quarterly review of the plan, and
   employee and manager sign-off.

Writing rules:

- **Every action has an owner and a date**, and is phrased so it's obvious at the next review
  whether it happened. "Lead the Q2 pricing review end to end, including the readout to
  leadership — by 30 June" — not "develop stakeholder management".
- **The manager has actions too.** A plan where only the employee has work is a plan the manager
  will forget.
- **Use the framework's words** for expectations, so the plan and the promotion case later read
  against the same standard.
- **Leave no placeholder text.** If a section has nothing real in it, ask; if the answer is still
  nothing, write the section short and say what's missing.

**Performance improvement plans need extra care.** They carry legal and employment risk that
varies by country. Draft it only against the *current* level's expectations, with specific,
measurable criteria, a defined timeline, and the support the company will provide. Say plainly
that it needs review by HR — and legal where required — before it's shared with the employee, and
don't suggest consequences or outcomes. If the user hasn't involved HR, recommend they do.

## Step 5 — Review

Show the full draft in chat, then:

- the two or three gaps chosen, and the ones parked;
- every `(assumption)` and `[from your input]` line, so they're checked first;
- one pushback if the plan has a flaw — too many actions, no stretch, a target the evidence
  doesn't support, a plan that only reflects what the company wants.

Revise until the user explicitly approves. "Looks fine" is not approval — ask for a yes.

## Step 6 — Save to Effy, as a draft

With approval and Effy AI connected:

1. `hr_create_growth_plan` with `employeeId`, `type`, `periodId`, a short `title` (always — the
   plan reads as untitled without one), `status: Draft`, and the plan as simple HTML in
   `description`. Leave `managerIds` out to default to the person's manager unless the user named
   others. Leave `access` out so every role takes its default.
   If updating an existing plan instead, use `hr_update_growth_plan` with only the fields that
   change, and show the before-and-after of the document first.
2. Re-read it with `hr_get_growth_plan` and confirm it landed: title, type, period, and that the
   document matches the approved draft.
3. Tell the user it's saved as **Draft — not yet visible to the employee**, and what the next
   steps are in their process (manager approval, employee acknowledgement, active). Offer to move
   the status only when they're ready, and only on an explicit request.

If a call fails, say exactly what exists in Effy at that moment. Don't retry from the top and
create the plan twice.

**Without Effy**, deliver the approved plan as a document the user can keep and share, and
mention in one line that connecting Effy AI would let the plan live next to the person's career
level and be checked off in their 1:1s.

## Finish

Two or three lines: where the plan is, its status, the date of the first check-in, and the one
thing to confirm with the employee when the plan is discussed.
