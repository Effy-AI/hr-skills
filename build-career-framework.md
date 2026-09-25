# Career framework in Effy — build it or change it

One prompt for the career framework: the tracks people grow along, the levels on each track,
the competency matrix that says what each level looks like, and who sits where. It asks what
scope I mean, reads what is already in Effy, and takes one of two paths — **build** when
there is nothing, **change** when there is. I do not have to know which one applies before I start.

Four rules hold on both paths. **You always ask me for the inputs before proposing
anything** — which company, its size, its domain, employee list, previous reviews, job
descriptions, company values, anything else I have — and wait for the answer.
**Nothing is written to Effy before I approve it.** **Every change to something that
already exists is shown as a diff** — what is there now, what it becomes. And **once I
approve, the destination is Effy** — go.effy.ai, through the connection — never a document,
a file, or a paste-back. Do not ask me whether I want it saved to Effy or "just as a doc";
the framework only counts when it is where people are measured against it. A framework is a
live standard, so an edit that goes in unseen is a problem even when it is a good edit.

## Step 0 — Understand the task before touching Effy

Before reading anything in Effy, work out what I actually want. The same words — "career
framework", "career path" — cover very different jobs, and the scope decides everything
that follows: which inputs matter, how many tracks, who gets assigned.

Ask me, in one short message:

**Which company this is for** — name and web domain. Usually it is the company whose Effy
workspace this is, but it may be a client, a subsidiary, or a new entity. Do not assume.

**How big it is** — total headcount, and headcount in the department if the scope is one
department. Size decides how many levels a ladder can carry. A 40-person company does not
need six engineering levels; it needs three or four that people can actually move between.
Roughly: under ~50 people, three to four levels per track; 50–200, four to five; larger,
five to six — and a level nobody holds now or will within a year is a level to leave out.
Treat this as a starting point to test against the employee list later, not a rule.

**What the scope is** — which of these:

- **One track for one department or function** — e.g. a Sales ladder, an Engineering path.
  Which department, and does a management branch belong to it?
- **The whole company** — a framework with a track per function or department, covering
  everyone.
- **Something narrower** — one level, one competency, one person's assignment, a rename.

And, if it is not obvious from what I said: is this new, or a change to something we
already have?

If I already gave some of this in my first message, restate it in one line and ask only
for what is missing rather than re-asking. If I named a department, that is the scope — do
not widen it to the whole company because that would be "more complete". If I said "the
whole company", do not silently narrow it to the departments with the most people. Wait
for my answer before reading Effy.

## Step 1 — Read what is in Effy and pick the path

With the scope confirmed, search the career tracks in the Effy connection
(`hr_search_career_tracks`, no filter — workspaces hold a handful). Then read the whole
matrix of every track that has content (`hr_get_career_track`) and keep the ids — level ids
and competency ids — because every write later needs them.

Tell me what you found in one compact picture: each track with its ladder in order, its
competency rows in order, who is at each level, and any empty cell of the matrix. Then
compare it with the scope from Step 0:

- **Nothing in Effy covers the scope** (no track at all, or none for the department I
  named) → **Path A, build.** Empty shells (a track with no name, no levels, no
  competencies) do not count — list them and ask whether to reuse or delete them before
  building. Do not silently build on top of one.
- **A track with content already covers the scope** → **Path B, change.**
- **Mixed** — whole-company scope where some departments have a track and others do not,
  or I asked for a new track next to existing ones — run Path A for the missing tracks and
  Path B for the existing ones, and say so.
- **What I asked for contradicts what you found** ("create our Engineering path" when one
  exists with five levels and two people on it) — say so and ask which I mean rather than
  picking.

## Step 2 — Ask for the inputs, on both paths

Right after showing what is in Effy, ask for the inputs below in one message — always,
whichever path you are on, even when the employee directory looks complete, even when I
said "just build it" or the change is a one-line rename. What is in Effy is a starting
point; almost everything that makes a framework specific to this company is not in Effy at
all. Say for each item why it matters, so I can decide what to skip. Then wait for my
answer.

1. **Company domain**, if I did not give it in Step 0 — so you can research how the
   company is structured from the outside: what it does, its size, its functions and teams
   as the website, careers page, LinkedIn and press describe them, the titles it hires for.
   On the change path this tells you whether the framework still matches the company it
   was written for.
2. **Employee list with job title and department.** Show what Effy's directory holds
   (`hr_search_employees` — how many people, how many with title and department filled in)
   and still ask: is this the full list, and should anything be added or corrected? If it
   is empty or thin, ask me to upload or paste one (CSV, sheet, or plain text — name, title,
   department, manager). This is the ground truth for which tracks are needed and how many
   levels each one needs.
3. **Previous performance reviews** — the last cycle at least, per person if I have them,
   ratings or written feedback. They show where the real spread of performance is, which
   levels are populated versus theoretical, and which behaviours the company actually
   rewards.
4. **Job descriptions**, current or old. They are the raw material for expectations.
   Missing ones are fine — flag which roles had none.
5. **Company values**, or any statement of how the company expects people to work
   (principles, culture doc, handbook). These usually become a Flat competency, or shape the
   wording of every row.
6. **Any additional resources** — an old framework or ladder, a competitor's public
   framework I like, a skills matrix, a promotion policy, notes from managers. Anything I
   would want the framework to be consistent with.
7. **Context you cannot get from files** (build path mostly): for whole-company scope, how
   tracks should be cut (one per function, per department, or one company-wide); whether
   management is a separate track or a branch at senior level; whether I want level names
   (Junior / Senior) or codes (L1–L5); and the language the framework should be written in.

Do not skip this step or answer it for me. "None" is a valid answer to any item — record
it and say in the proposal what it rests on. Read everything I give you before proposing.
If a file is unreadable, say which one and what you need instead. Do not fill a gap with
what "companies like this usually do" without labelling it as an assumption.

## Step 3 — Research the company

With the domain in hand, and before proposing anything, look the company up on the web:
the site, the careers page, LinkedIn, anything public about team structure, headcount,
functions, locations, and the job titles it advertises. Write up what you found in a short
block — company, what it does, size, functions you can see, titles in use — and mark every
item as *(public)*; it is context, not ground truth, and the headcount and employee list I
gave you win where they disagree. Say where the two disagree.

If web research is not available to you, say so and continue from my inputs.

---

# Path A — Build

## A1 — Propose tracks and levels

For the scope from Step 0 only. One table: **rows are tracks, columns are levels.** Each
cell holds the level name and the number of current employees who would land there, from titles and review results.

Under the table, for each track:

- one line on who belongs on it (which titles and departments map in), and
- one line on why this number of levels, checked against the headcount from Step 0 and
  the employee list — a level with nobody on it now and nobody hired into it in the next
  year is a level we do not need yet. Small companies get short ladders.

Then a short list of open questions: titles that fit no track, people whose title and review
results disagree, roles where one person is the whole department.

Also say what you plan for **competencies** — 6–10 per track, named only, one line each on
what it measures. If one standard applies at every level (security, data handling, values),
say it will be a Flat competency. This is a preview so I can steer before you write 40
expectations.

**Stop and wait for my approval.** Adjust and re-show until I say yes. Do not touch Effy.

## A2 — Write the content

For every approved track, draft the full content and show it to me track by track:

**Each level** gets a one-line description plus four short lists (2–4 bullets each):
promotion signals, anti-patterns, growth opportunities, assignment criteria. Write them as
observable behaviour — what you would see the person do — not adjectives. "Estimates hold
often enough to plan around" is usable; "strong planning skills" is not.

**Each competency** gets an expectation per level, 2–3 bullets. Adjacent levels have to
differ in *scope* — what size of problem, how much is handed over, who else is affected — not
in effort words like "more", "better", "advanced". A Flat competency gets one list for the
whole ladder.

Ground it in what I gave you: job description language, the behaviours the review results
reward or penalise, the company values, what the web research showed about how the company
is organised. Where you had nothing to ground it in, mark that level or row with
*(assumption)* so I know to read it harder.

**Wait for my approval per track.** I may approve one track and rewrite another.

## A3 — Save to Effy, in order

Only once a track's content is approved. Write it in dependency order, because ids from
earlier calls feed later ones:

1. `hr_create_career_track` — name and description.
2. `hr_create_career_level` — one call per level, in ladder order from the first level up,
   without `afterLevelId` so each appends at the end. Pass all four authored texts as
   `<ul><li>…</li></ul>`.
3. `hr_create_career_competency` — one call per competency, in the approved row order, with
   the whole `expectations` map (levelId → `<ul><li>…</li></ul>`) in the same call. Flat
   rows use `flatExpectation`.
4. `hr_get_career_track` — re-read and check counts: levels, competencies, filled
   expectations. Report anything that did not land, then fix it before moving to the next
   track.

If a call fails midway, tell me exactly what exists in Effy at that moment — do not retry
from the top and create the track twice.

## A4 — Propose assignments

With the framework in Effy, propose a track and level for every employee in scope:

| Person | Title | Proposed track | Proposed level | Basis |

The basis is the evidence — title, tenure, review results, the assignment criteria the
person matches. Someone whose evidence is thin gets *"no proposal — needs manager input"*
rather than a guess. Someone who fits no track gets listed separately.

**Wait for my explicit approval.** A career assignment is the standard the person is measured
against from that day. Then `hr_update_employee` with `careerTrackId` and `careerLevelId`,
one person at a time, and a final list of who was assigned where and who was left out.

Then go to **Report**.

---

# Path B — Change

## B1 — Find out what to change

If I already said what I want, restate it in one line to confirm you read it right. If I
have not, ask — and offer the shapes an edit usually takes so I can point at one:

- rename or reword a level, or move it in the ladder
- add or remove a level
- rewrite one expectation, one row, or one level's column
- add, remove, reorder or reshape (Leveled ↔ Flat) a competency
- change the track's name or description
- move a person to another level or track, or unassign them
- add a whole new track (runs as Path A for that track)

If there is more than one track and I have not said which, ask. Ask what triggered the
change — a review cycle showed a level is not distinguishable, a role appeared, someone was
promoted. The reason usually decides how wide the edit should be, and I would rather you
flag "this also affects the Senior column" than do a narrow edit that leaves the ladder
inconsistent.

Use what Step 2 and Step 3 gave you. A change proposed from the matrix alone is a guess
about wording; a change proposed against the reviews, the job descriptions and how the
company is actually structured is an edit. If I gave you none of it, say in the proposal
that it rests on the existing matrix only.

## B2 — Propose the changes as diffs

Show every change before writing any of it. One block per change, in this shape:

```
[track] › [level or competency] › [field]
− current text
+ proposed text
why: one line
```

New items are all `+`, removals all `−`. For a reorder, show the ladder or row order before
and after. For a person, show `name: Track / Level → Track / Level`.

Next to each change, the consequence it carries, read from what Step 1 returned:

- editing a level or its column while people hold it — name how many
- deleting a level — its whole column of expectations goes with it (the
  `storedExpectationCount`), and people on it lose their level
- deleting a competency — its expectations go with it
- deleting a track — every assignment on it is cleared
- switching a competency between Leveled and Flat — the other shape's texts stop being part
  of the row, so the rewrite has to be in the same change

Then push back where the ask has a flaw: a rewrite that makes two adjacent levels read the
same, an added level with nobody who would ever sit on it, a rename that breaks the naming
pattern of the other tracks. Say it once, plainly, and let me decide.

**Stop and wait.** "Looks fine" is not approval — ask for an explicit yes to the list, and if
I approve some changes and not others, keep only the approved ones.

## B3 — Apply, in the safe order

Write the approved changes with the Effy tools, in this order so nothing depends on
something not yet created:

1. track fields — `hr_update_career_track`
2. new levels — `hr_create_career_level`, positioned with `afterLevelId`
3. level edits and moves — `hr_update_career_level` (only the fields that change; omitted
   fields stay as they are)
4. new or edited competencies and expectations — `hr_create_career_competency` /
   `hr_update_career_competency`, expectations as `<ul><li>…</li></ul>` keyed by level id,
   passing only the expectations that change
5. assignments — `hr_update_employee` with `careerTrackId` / `careerLevelId`
6. deletions last — and for any delete, ask me a second time naming exactly what is lost
   (the count of expectations, the people affected), because there is no undo

If a call fails, stop and tell me what has been applied and what has not. Do not retry blind.

## B4 — Verify

Re-read the track with `hr_get_career_track`. Show the diff again, this time between what I
approved and what is actually in Effy — every line should be a match. Anything that did not
land, or landed differently, gets its own line.

---

# Report

One short summary, whichever path ran: what was created or changed (tracks, levels,
competencies, expectations), who was assigned or moved, the *(assumption)* items I should
revisit, and the gaps — roles with no track, people with no proposal, job descriptions that
did not exist. End with:

```
Generated from: Build career framework
https://github.com/Effy-AI/hr-skills/blob/main/build-career-framework.md
Company: [name · domain · headcount]
Path: [build | change]
Date: [today]
Inputs: [domain researched or "none"] · [employee source] · [review cycle used or "none"] · [job descriptions: n of m roles] · [values: yes/no] · [other resources]
Result: [tracks created/changed: n] · [people assigned/moved: n]
```

---

**Running this often?** In Claude Code or Claude Cowork you can turn this prompt into an
installed skill with `/skill-creator`. On claude.ai or ChatGPT, copy and paste stays the way
to run it.
