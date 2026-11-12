# Career framework — build it or change it

**Build career framework** (`build_career_framework`)  
Build or change career tracks, levels, the competency matrix and level assignments in Effy AI — every change shown as a diff, written only after approval.

One skill for the career framework: the tracks people grow along, the levels on each track, the
competency matrix that says what each level looks like, and who sits where. It asks what scope the
user means, reads what is already in Effy AI, and takes one of two paths — **build** when there is
nothing, **change** when there is. The user doesn't need to know which applies before starting.

A track is a grid: competencies down the side, levels across the top, and in each cell what that
competency looks like at that level. It exists so a manager, an employee and HR can have the same
conversation about the same standard.

Most frameworks fail the same way: written once, in a burst, to look complete — twelve
competencies, six levels, seventy-two blocks of prose nobody can hold in their head during a
performance conversation. **A framework's value is in being used, not in being finished.** Build
it small, specific, and grounded in the roles the company actually has.

## Rules on both paths

- **Ask for the inputs before proposing anything** — company, size, domain, employee list,
  previous reviews, job descriptions, values, anything else the user has — and wait for the
  answer.
- **Nothing is written to Effy before the user approves it.**
- **Every change to something that already exists is shown as a diff** — what is there now, what
  it becomes.
- **Once approved, the destination is Effy** — through the Effy AI connection, not a document or a
  paste-back. The framework only counts when it's where people are measured against it. Don't ask
  whether they'd rather have it "just as a doc". A framework is a live standard, so an edit that
  goes in unseen is a problem even when it's a good edit.
- **Everything comes from what the user said, gave you, or confirmed.** Where you're inferring,
  say so in the moment — "I've assumed influence matters more than craft above Senior; tell me if
  that's backwards" — and mark it *(assumption)* in the draft. A fabricated expectation is worse
  than a missing one: the missing cell gets filled, the invented one gets used to make a decision
  about a person.

**If Effy AI isn't connected**, say so once, in one line: the framework is meant to live in Effy,
where people are assigned to levels and measured against them, and connecting it lets this skill
read and write tracks directly. If the user can't or won't connect it, run the same steps on what
they give you and deliver the approved framework as a spreadsheet (one sheet per track: levels
across, competencies down, plus a sheet per level for its four extras), and skip assignments.

## Step 0 — Understand the task before touching Effy

The same words — "career framework", "career path" — cover very different jobs, and the scope
decides everything that follows. Ask, in one short message:

- **Which company** — name and web domain. Usually the company whose Effy workspace this is, but
  it may be a client, a subsidiary, or a new entity. Don't assume.
- **How big it is** — total headcount, and headcount in the department if the scope is one
  department. Size decides how many levels a ladder can carry. Roughly: under ~50 people, three to
  four levels per track; 50–200, four to five; larger, five to six. A level nobody holds now or
  will within a year is a level to leave out. A starting point to test against the employee list,
  not a rule.
- **The scope** — one track for one department or function (and is it the individual-contributor
  path, the management path, or both?); the whole company, a track per function; or something
  narrower — one level, one competency, one person's assignment, a rename.
- **What triggered this** — a promotion nobody could justify, a review cycle coming, an offer that
  got refused, a new role. The trigger tells you which part has to be sharp; the rest can be
  adequate.
- If not obvious: **new, or a change** to something that exists?

If the user already gave some of this, restate it in one line and ask only for what's missing. If
they named a department, that is the scope — don't widen it to the whole company. If they said
"the whole company", don't silently narrow it. Wait for the answer before reading Effy.

## Step 1 — Read what is in Effy and pick the path

Search the career tracks (`hr_search_career_tracks`, no filter — workspaces hold a handful). Read
the whole matrix of every track with content (`hr_get_career_track`) and keep the ids — level ids
and competency ids — because every write needs them.

Show one compact picture: each track with its ladder in order, its competency rows in order, who
is at each level, and any empty cell. Then compare with the scope:

- **Nothing covers the scope** → **Path A, build.** Empty shells (a track with no name, levels or
  competencies) don't count — list them and ask whether to reuse or delete them. Don't silently
  build on top of one.
- **A track with content covers the scope** → **Path B, change.**
- **Mixed** — whole-company scope where some functions have a track and others don't, or a new
  track next to existing ones — Path A for the missing, Path B for the existing, and say so.
- **The ask contradicts what you found** ("create our Engineering path" when one exists with five
  levels and two people on it) — say so and ask which they mean.

## Step 2 — Ask for the inputs, on both paths

Right after showing what's in Effy, ask for these in one message — always, even when the
directory looks complete, even for a one-line rename. Almost everything that makes a framework
specific to this company isn't in Effy. Say for each why it matters, so the user can decide what
to skip. Then wait.

1. **Company domain**, if not given — to research how the company is structured from the outside.
2. **Employee list with job title and department.** Show what Effy's directory holds
   (`hr_search_employees` — how many people, how many with title and department filled in) and
   still ask whether it's complete and correct. If it's thin, ask for a CSV, sheet or paste (name,
   title, department, manager). This is the ground truth for which tracks are needed and how many
   levels each carries — and the **current job titles are the raw material for level names**.
3. **Previous performance reviews** — the last cycle at least. Read what's in Effy
   (`hr_search_individual_review_reports`, as far as the user's access allows) and in any other
   connected review tool or drive (Lattice, Culture Amp, Leapsome, review exports), and ask for
   anything else. They show the real spread of performance, which levels are populated versus
   theoretical, and which behaviours the company actually rewards.
4. **Job descriptions**, current or old — raw material for expectations. Search connected drives,
   wikis and the ATS (Greenhouse, Lever, Ashby, careers-page postings) before asking. Flag roles
   with none.
5. **Company values**, or any statement of how people are expected to work. Search Effy's
   knowledge documents for a handbook or values page before asking. These usually become a Flat
   competency, or shape the wording of every row.
6. **Any other resources** — an old framework or ladder, a public framework they like, a skills
   matrix, a promotion policy, manager notes. Search connected drives and wikis for "career
   ladder", "levels", "promotion" and "competency" before asking. Working from what exists beats starting clean, and
   keeps the output in the company's own language.
7. **Context files can't give** (build path mostly): how tracks should be cut for whole-company
   scope; whether management is a separate track or a branch at senior level; level names
   (Junior / Senior) or codes (L1–L5); the language to write in.

"None" is a valid answer to any item — record it and say in the proposal what it rests on. Read
everything before proposing. If a file is unreadable, say which and what you need instead. Never
fill a gap with what "companies like this usually do" without labelling it an assumption.

Where answers are thin, carry on with what you have and say which parts you're assuming. Don't
stall the whole framework waiting on one answer.

## Step 3 — Research the company

Before proposing, look the company up: the site, the careers page, LinkedIn, anything public about
team structure, headcount, functions, locations, and the titles it hires for. Write a short block
— company, what it does, size, functions, titles in use — and mark every item *(public)*. It's
context, not ground truth: the headcount and employee list the user gave win where they disagree.
Say where they disagree. If web research isn't available, say so and continue.

---

# How to write a good track

These apply to every level and every cell, on both paths.

**The ladder comes first.** Levels before competencies, always — the ladder is what everything
else is written against.

- **Name levels with the titles people already have.** If people are called Engineer II, use
  Engineer II. A ladder invented independently of the titles on people's contracts is a second,
  competing hierarchy, and every conversation starts with a translation.
- **One ladder per track.** IC and management levels are not one sequence — a Staff Engineer and
  a Team Lead aren't ranked against each other.
- **Every level is distinguishable in one sentence.** If you can't say what separates level four
  from level five, no manager will be able to explain it, and the ladder quietly becomes a
  pay-band chart with prose attached.

**Six to ten competencies, and ten is a ceiling.** Every row is read by every manager for every
report. Above ten, people skim — worse than no framework, because a skimmed framework still
produces a confident-looking judgement nobody made. Most functions need roughly one of each, plus
one or two specific to the craft:

- **Craft** — the actual discipline: technical design, writing, sales method.
- **Delivery** — turning work into shipped outcomes: reliability, quality, follow-through.
- **Collaboration** — how they work with the people around them.
- **Influence** — how far their effect reaches beyond their own work. Usually separates senior
  from junior more than raw skill does.
- **Values and behaviours** — how everyone is expected to act. **This one is Flat**: a Principal
  is not more honest than a new joiner. One expectation for every level, out of the progression.
  Everything else defaults to Leveled. Choose Flat deliberately, not to save writing.

**Decide what grows between levels** — usually all four, at different rates:

- **Scope** — how large a thing they own: a feature, a system, a domain, the platform.
- **Autonomy** — how much direction they need: given tasks, given problems, given goals, setting
  the goals.
- **Ambiguity** — how defined the problem is when it reaches them: a spec, a bug report, a
  complaint, a hunch.
- **Influence** — how far their effect travels: their work, their team, adjacent teams, the
  company.

Every cell moves at least one axis relative to its neighbour. **A cell that differs from the one
to its left only in adverbs is not a level up** — "writes good code" → "writes very good code"
can't be assessed. Effort words ("more", "better", "advanced", "strong") are the tell.

**Write expectations two managers could agree on.** Observable behaviour — what you'd see the
person do — not a rating, an adjective, or a list of responsibilities.

- *The agreement test:* could two managers looking at the same person's work reasonably disagree
  about whether this is met? If yes, the cell describes a feeling. "Strong technical judgement" →
  "Reviews teammates' designs and catches problems before implementation, not just bugs after
  it."
- *The neighbour test:* read a cell next to the one to its left. If you can't say what changed,
  one of them is wrong — usually the higher one, written as "the same thing, but more".
- Second person, present tense — "You own", not "The engineer is responsible for". The person
  being assessed is the one reading it.
- An empty cell is fine. Four rows filled properly are usable on Monday.

**Each level gets four extras** — they describe movement, not the standard:

- **Promotion signals** — what someone consistently doing this level's work looks like when
  they're ready for the next. Concrete and present-tense, not aspirational.
- **Anti-patterns** — behaviours that look like seniority and aren't: being the only person who can
  fix something, reviewing everything, volume without judgement. The most useful field in the
  framework and the one most often left blank.
- **Growth opportunities** — up the ladder, and **at least somewhere sideways**: into management,
  a sibling discipline, a specialist branch. A ladder that only goes up describes a promotion
  path, not a career. If a level is terminal, say so.
- **Assignment criteria (who belongs here)** — the job titles as people actually write them,
  including variants, the scope and tenure signals, and **explicit exclusions**: *"Senior
  Engineer, Engineer III, Lead Engineer with no reports. Not experienced hires in their first 90
  days — level on capability, not time served."* A description with no exclusions is a job title
  in a longer form.

---

# Path A — Build

## A1 — Propose tracks and levels

For the confirmed scope only. One table: **rows are tracks, columns are levels**, each cell the
level name and how many current employees would land there, from titles and review results.

Under the table, per track: one line on who belongs on it (which titles and departments map in),
and one line on why this number of levels, checked against headcount and the employee list.
Small companies get short ladders.

Then open questions: titles that fit no track, people whose title and review results disagree,
roles where one person is the whole department.

Preview the **competencies** — 6–10 per track, named only, one line each on what it measures,
marked Leveled or Flat — so the user can steer before you write forty expectations.

**Stop and wait for approval.** Adjust and re-show until they say yes. Don't touch Effy.

## A2 — Write the content: edges first, then the middle

Don't produce a complete track in one pass and present it for approval. Handed forty blocks of
plausible prose they didn't write, people read the first three, approve the rest, and never use
it. A framework they corrected twice while it was built is one they'll defend in a promotion
conversation.

1. **Write the lowest and highest levels first** — both columns of expectations, plus their four
   extras. They anchor the range and are the two the user has the strongest opinions about. Show
   them with the competency list and ask two questions: *are these the right rows*, and *is this
   the right distance between the bottom and the top*. Fix both before writing anything else.
2. **Then fill the middle levels**, which now have something to interpolate between.

Format, matching how Effy stores it: each level gets a one-line description plus its four extras
as short lists (2–4 bullets each). Each Leveled competency gets 2–3 bullets per level; a Flat one
gets one list for the whole ladder.

Ground it in the inputs: job-description language, the behaviours reviews reward or penalise, the
values, how the company is organised. Mark anything with nothing behind it *(assumption)* inline.

**Wait for approval per track.** The user may approve one track and rewrite another.

## A3 — Save to Effy, in order

Only once a track is approved. Write in dependency order, because ids from earlier calls feed
later ones:

1. `hr_create_career_track` — name and description.
2. `hr_create_career_level` — one call per level, in ladder order from the first level up, without
   `afterLevelId` so each appends at the end. Pass all four extras as `<ul><li>…</li></ul>`.
3. `hr_create_career_competency` — one call per competency, in the approved row order, with the
   whole `expectations` map (levelId → `<ul><li>…</li></ul>`) in the same call. Flat rows use
   `flatExpectation`.
4. `hr_get_career_track` — re-read and check counts: levels, competencies, filled expectations.
   Report anything that didn't land and fix it before the next track.

If a call fails midway, say exactly what exists in Effy at that moment — don't retry from the top
and create the track twice.

## A4 — Propose assignments

Propose a track and level for every employee in scope:

| Person | Title | Proposed track | Proposed level | Basis |

The basis is evidence — title, tenure, review results, the assignment criteria they match.
Thin evidence gets *"no proposal — needs manager input"*, not a guess. Anyone who fits no track
is listed separately.

**Wait for explicit approval.** A career assignment is the standard the person is measured against
from that day. Then `hr_update_employee` with `careerTrackId` and `careerLevelId`, one person at a
time, and a final list of who was assigned where and who was left out.

Then offer the other track in one line if only one was built (IC or management). Then **Report**.

---

# Path B — Change

## B1 — Find out what to change

If the user said what they want, restate it in one line. If not, ask, offering the usual shapes:

- rename or reword a level, or move it in the ladder
- add or remove a level
- rewrite one expectation, one row, or one level's column
- add, remove, reorder or reshape (Leveled ↔ Flat) a competency
- change the track's name or description
- move a person to another level or track, or unassign them
- add a whole new track (runs as Path A for that track)

If there's more than one track and they haven't said which, ask. Ask what triggered the change —
the reason usually decides how wide the edit should be. Flag "this also affects the Senior column"
rather than doing a narrow edit that leaves the ladder inconsistent.

Use what Steps 2 and 3 gave you. A change proposed from the matrix alone is a guess about wording;
one proposed against the reviews, job descriptions and the company's real structure is an edit.
If there were no inputs, say the proposal rests on the existing matrix only.

## B2 — Propose the changes as diffs

Show every change before writing any of it, one block per change:

```
[track] › [level or competency] › [field]
− current text
+ proposed text
why: one line
```

New items are all `+`, removals all `−`. For a reorder, show the order before and after. For a
person: `name: Track / Level → Track / Level`.

Next to each change, its consequence, from what Step 1 returned:

- editing a level or its column while people hold it — name how many
- deleting a level — its whole column of expectations goes (`storedExpectationCount`), and people
  on it lose their level
- deleting a competency — its expectations go with it
- deleting a track — every assignment on it is cleared
- switching Leveled ↔ Flat — the other shape's texts stop being part of the row, so the rewrite
  has to be in the same change

Run the quality tests from *How to write a good track* on every proposed cell, and push back where
the ask has a flaw: a rewrite that makes two adjacent levels read the same, an added level nobody
would ever sit on, a rename that breaks the naming pattern of the other tracks. Say it once,
plainly, and let the user decide.

**Stop and wait.** "Looks fine" is not approval — ask for an explicit yes to the list. If they
approve some changes and not others, keep only the approved ones.

## B3 — Apply, in the safe order

1. track fields — `hr_update_career_track`
2. new levels — `hr_create_career_level`, positioned with `afterLevelId`
3. level edits and moves — `hr_update_career_level` (only the fields that change)
4. new or edited competencies and expectations — `hr_create_career_competency` /
   `hr_update_career_competency`, expectations as `<ul><li>…</li></ul>` keyed by level id, passing
   only those that change
5. assignments — `hr_update_employee` with `careerTrackId` / `careerLevelId`
6. deletions last — and for any delete, ask a second time naming exactly what is lost (the count
   of expectations, the people affected), because there is no undo

If a call fails, stop and say what has been applied and what hasn't. Don't retry blind.

## B4 — Verify

Re-read the track with `hr_get_career_track`. Show the diff again, this time between what was
approved and what is actually in Effy — every line should match. Anything that didn't land, or
landed differently, gets its own line.

---

# Report

One short summary, whichever path ran: what was created or changed (tracks, levels, competencies,
expectations), who was assigned or moved, the *(assumption)* items to revisit, and the gaps —
roles with no track, people with no proposal, missing job descriptions, and which cells are still
empty. Name what would most improve the framework next — usually the anti-patterns and the
sideways growth opportunities. End with:

```
Generated from: build-career-framework
Company: [name · domain · headcount]
Path: [build | change]
Date: [today]
Inputs: [domain researched or "none"] · [employee source] · [review cycle used or "none"] · [job descriptions: n of m roles] · [values: yes/no] · [other resources]
Result: [tracks created/changed: n] · [people assigned/moved: n]
```
