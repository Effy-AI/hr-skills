# Build the HR context for AI

**HR context files setup** (`hr_context`)  
Build the folder structure, context files, and logs that future AI sessions run on — assembled from what can be verified about your company, not a generic template.

Build a small set of documents that lets any future AI session — a chat, a project, an agent,
another skill in this plugin — start with the company's HR already understood: how it's
organised, when things happen, what's already decided, where the real documents live, and how
each HR process actually runs.

**Why it's built this way.** An AI's attention is limited, so the goal is the *smallest set of
high-signal information* that does the job, not everything you can find. Structure is part of the
instruction: document names, an index that says what lives where, and short documents with one
purpose each let the AI find the right thing without reading everything. And context is not
records — so explain this to the user in two or three lines at the start, in your own words,
because the natural assumption is that you're about to copy their HRIS:

- It holds **patterns, cadences, decisions and pointers** — how the company works, not who works
  there. Employee data stays in the HR system.
- Policies and templates are **linked, never copied**. There's one master of each document, and
  it isn't here.
- It's what lets every later AI session skip the "let me explain our company" part.

The document set, templates and review prompt are in the **Document set** section at the end — use it in Step 3.

## Step 0 — Where it will live

Check what's connected, then recommend one home (the two can be combined):

- **Effy AI knowledge** — if the Effy AI connector is available, recommend this. Each document
  becomes a knowledge document that Effy's agents and the other skills in this plugin read
  automatically, so the context works in every session without anyone attaching files.
- **A shared folder** — a connected local folder (suggest the name `HR-CONTEXT-FOR-AI`), a drive
  folder, or a wiki space. Use this when there's no Effy, or as well as Effy if the user wants
  files they can open.

Ask once which they want. If neither is available, say the documents will exist only in this chat
and they'll need to copy them out — then continue. Don't block on it.

## Step 1 — Read everything already reachable

Say in one sentence what you're about to search, then read before asking anything. Sources, in
rough order of yield:

- **What already exists as context.** Effy AI's knowledge documents (search for context, process,
  policy, handbook, onboarding, review), and any existing context folder or wiki space. Update
  what's there rather than duplicating it.
- **Claude's memory and past chats**, if this session has them — what the user has already said
  about the company, its processes, decisions and preferences. Treat it as the user's own account
  (good evidence), but confirm anything that may be stale.
- **Effy AI records**, if connected — the employee directory (size, teams, locations — counts and
  structure only), career tracks, growth-plan periods, 1-on-1 activity cadence, review reports.
- **Email and calendar** — recurring HR events (review cycles, surveys, comp reviews, all-hands),
  announcements, the last few hires and exits (for the process, not the people).
- **Drives and wikis** — handbook, policies, process docs, templates, offer letters, review forms.
- **HR, ATS, payroll and task tools** — which tools are used for what, and the processes visible in
  them (hiring stages, onboarding checklists).

Collect facts with their source. Weigh them: a document or a recurring calendar event beats a
one-off email; what the user said beats what you inferred; nothing beats nothing — never fill a
gap with what "companies like this usually do".

## Step 2 — Interview, then show the plan

Start with four or five lines on what you found and where. Then ask **only what the evidence
couldn't answer**, one question at a time, up to ten. Focus on:

- What the user owns versus delegates, and who owns each HR process.
- Decisions already made that AI should never reopen (e.g. contractors excluded from review cycles).
- Which processes cause the most work — those get a process document first.
- Anything you found that contradicts something else. Quote both, ask which is right.

Then **show the plan before building**: the list of documents, one line each on what it will say
and what it rests on, and which ones are new versus updates. Wait for a yes.

## Step 3 — Build the documents

Use the set and templates in the **Document set** section below: the workspace map, the AI usage rules
pointer, `company/` facts, one `processes/` document per process actually run, and the two logs.
Build only what the evidence and interview support — a process the company doesn't run gets no
document, and a section with nothing real in it is left out, not padded.

Rules for every document:

- **Short and high-signal.** Under 2,000 words; most well under. Patterns, not raw notes.
- **Pointers, not copies** for policies, templates and anything with a master elsewhere.
- **No employee names**, ever — roles only. No salaries, ID numbers, health or personal details.
- **Mark every inferred line** `[CONFIRMED]` or `[GUESS: verify]`. Anything the user stated or a
  document shows is confirmed; anything you deduced is a guess until they check it.
- **Route content by type.** Company facts go in `company/`; how a process runs goes in
  `processes/`; methods and playbooks are skills, not context; reference documents stay where they
  are and get indexed; current-cycle evidence (exports, candidate files) belongs in a project for
  that job, not here.

Where a dedicated skill does a process better, say so and offer it rather than writing a thinner
version here: `onboarding-process` for onboarding, `hr-ai-usage-policy` for the AI rules,
`employee-handbook` for the handbook.

## Step 4 — Save

Show the final list of documents to be created or updated, then save after an explicit yes.

- **To Effy AI knowledge** — one knowledge document per document in the set, titled with its path
  so they sort and read as a workspace: `HR context — README`, `HR context — company/org-basics`,
  `HR context — processes/review-cycle`, and so on. Search first and update a matching document
  rather than creating a second. Logs are documents too, so corrections stay with the context.
- **To a folder** — the same set as markdown files in the structure from the **Document set** section, with a
  `README.md` in every folder.

Then add the first line to the context log: today's date, what was created.

## Step 5 — Optional extras

Offer each in one line; build only on a yes.

- **Project packs** — for each HR job the user runs (review cycle, handbook and policy, pay,
  hiring, onboarding, surveys, HR helpdesk), a pack to set up a dedicated AI project: its name, the
  instructions to paste, what to upload each cycle, and 3–5 facts for the project's memory. One
  room per job, never one giant "HR" project — mixed context degrades every task it touches.
- **Weekly context review** — a scheduled task that reads the logs and recent outputs and proposes
  fixes. The prompt is in the **Document set** section below. It proposes; it never edits on its own.

## Finish

Two or three lines: what was created or updated and where, how many `[GUESS: verify]` lines are
waiting for the user, and the one process document most worth writing properly next. Remind them
of the habit that keeps this alive: when they correct the AI on something non-trivial, add a dated
line to the feedback log.

## Document set


### 1. The set

```
HR-CONTEXT-FOR-AI/
├── README.md               Map of the workspace: what lives where, how to work here
├── ai-usage-policy.md      Rules, read before every task (pointer to the policy if it lives elsewhere)
├── company/
│   ├── README.md
│   ├── org-basics.md       Size, locations, teams, ownership, how decisions get made
│   ├── hr-calendar.md      Review cycles, survey cadence, comp review dates, planning
│   ├── decision-log.md     HR decisions with dates and reasons
│   └── policies-index.md   Pointers to policies where they live — never copies
├── processes/
│   ├── README.md
│   └── <one per process actually run>.md   e.g. review-cycle, hiring, onboarding
├── OUTPUTS/
│   └── README.md           Deliverables, one subfolder per project
└── logs/
    ├── README.md
    ├── context-log.md      What changed in the workspace, and when
    ├── feedback-log.md     What the AI got wrong, and what's true
    └── context-reviews/    Weekly review output, one file per review (YYYY-MM-DD.md)
```

Why each part exists:

- **READMEs** answer three questions: what lives here, when to read it, when to write here. An AI
  reads the top README first, then the folder README, then the file it needs.
- **`company/` vs `processes/`** — facts change rarely and are looked up often; processes are what
  the AI follows when working. Separating them keeps both short.
- **`policies-index`** keeps one source of truth for each policy.
- **`decision-log`** stops the AI reopening settled questions.
- **`logs/`** record changes and corrections, which feed the weekly review.

In Effy AI knowledge, each file becomes one knowledge document titled `HR context — <path>`
(e.g. `HR context — company/decision-log`). `OUTPUTS/` and `context-reviews/` stay in a folder if
the user has one; otherwise skip them.

### 2. Templates

Fill only what the evidence supports. Mark inferred lines `[CONFIRMED]` / `[GUESS: verify]`.

### README.md (top level)

```markdown
# HR context — <Company>

Context for AI sessions and agents working on <Company>'s HR. Read this first.

## What lives where
- `ai-usage-policy` — the rules. Read before every task.
- `company/` — facts that rarely change: org, calendar, decisions, where policies live.
- `processes/` — how each HR process actually runs. Follow these when doing the work.
- `logs/` — what changed and what the AI got wrong. Check `feedback-log` before repeating a task.

## How to work here
- Never put employee names, salaries or personal details in these documents.
- Link to policies and templates; never copy them.
- If something here contradicts what you find elsewhere, say so — don't silently pick one.

Owner: <role>. Last updated: <date>.
```

### Folder README (company/, processes/, logs/)

```markdown
# <folder>

What lives here: <one line>.
Read it when: <one line>.
Write here when: <one line>.
```

### company/org-basics.md

```markdown
# Org basics

- Headcount: <n, as of date> [CONFIRMED]
- Locations / countries with employees: <…>
- Entities or employer-of-record: <…>
- Teams and reporting lines: <functions, heads by role>
- Ownership and stage: <bootstrapped / VC-backed / …>
- How decisions get made and communicated: <…>
- Tools — source of truth for what: <HRIS, payroll, ATS, reviews, chat, docs>
- HR team: <roles; who owns which process>
```

### company/hr-calendar.md

```markdown
# HR calendar

| When | What | Owner | Notes |
| --- | --- | --- | --- |
| <Jan–Feb> | <Annual review cycle> | <HR lead> | <self → manager → calibration> |
| <Quarterly> | <Engagement pulse> | … | … |
```

### company/decision-log.md

```markdown
# Decision log

Settled decisions. Don't reopen these without the owner.

- <YYYY-MM-DD> — <decision>. Why: <reason>. Owner: <role>.
```

Example: `2026-03-02 — Contractors are excluded from review cycles. Why: no line manager and
fixed-scope contracts. Owner: Head of People.`

### company/policies-index.md

```markdown
# Policies index

| Policy | Where it lives (link) | Owner | Last reviewed |
| --- | --- | --- | --- |
| Employee handbook | <link> | <role> | <date> |
```

### processes/<process>.md

```markdown
# <Process> — how it actually runs

Trigger: <what starts it>. Owner: <role>. Cadence: <…>. Tools: <…>.

## Steps
1. <timing> — <owner> — <action> [CONFIRMED]
2. …

## Inputs and templates
- <name> — <link>

## Where it usually goes wrong
- <evidence-backed point>

## Decisions that apply
- See decision-log: <entry>
```

### logs/context-log.md

```markdown
# Context log

- <YYYY-MM-DD> — <what changed in the workspace>.
```

### logs/feedback-log.md

```markdown
# Feedback log

One dated line per non-trivial correction: what the AI got wrong, and what's true.

- <YYYY-MM-DD> — Said the review cycle runs in January. True: it runs in July. Fix: hr-calendar.
```

### 3. Project pack

```markdown
# Project pack — <job, e.g. Review Cycle>

Project name: <…>
Instructions to paste: <job-specific rules, e.g. "Remove names before analysis", "Answer only from the named policies">
Upload each cycle: <current evidence: exports, forms, candidate files>
Facts for project memory (3–5): <rating scale; cycle timing; who calibrates; …>
```

Rooms to offer, only for jobs the user actually runs: Review Cycle, Handbook & Policy, Pay,
Hiring, Onboarding, Surveys, HR Helpdesk.

### 4. Weekly review prompt

For a scheduled weekly task (in the Claude desktop app: Settings → Scheduled tasks → New):

```
Review the HR context workspace.
1. Read the READMEs and work from the actual structure.
2. Find the last review in logs/context-reviews/ and cover the period since then — or the last
   7 days if there is none.
3. Read the feedback log, the context log, new deliverables in OUTPUTS/, the context documents,
   and relevant email and calendar for the period.
4. Answer four questions in under 400 words:
   - Corrections: what was corrected, and which document should have prevented it.
   - Gaps: up to 5, ranked by what they cost.
   - Drift: where a document no longer matches reality — quote both sides.
   - Bloat: documents over 2,000 words, or never referenced.
Propose edits with exact wording; don't make them. "Nothing this week" is a valid answer.
No employee names. Save as logs/context-reviews/YYYY-MM-DD.md.
```

The review can't see past conversations unless the session has memory or chat search, so
corrections only count once they're in the feedback log.
