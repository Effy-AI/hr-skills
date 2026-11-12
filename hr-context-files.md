# Set up the HR context

**HR context files setup** (`hr_context_files`)  
Build the folder structure, context files, and logs that future AI sessions run on — assembled from what can be verified about your company, not a generic template.

Build the context that makes future AI sessions useful without re-explaining the company every
time: how HR works here, on what cadence, which decisions are already made, and where the real
documents live. Built from what you can verify, not from a generic template.

**Explain in two or three lines what this is**, because the natural assumption is that you're
about to duplicate the HRIS — and the user should resist that. In your own words:

- It holds *context*, not records. Patterns, cadences, decisions and pointers — how the company
  works, not who works there. Employee data stays in the HRIS.
- It's what lets AI sessions and agents start with the company already understood.
- Policies and templates are **linked**, never copied. There is one master of each document, and
  it isn't here.

## Step 0 — Where it will live

Two options, and they can be combined:

- **Effy AI's knowledge**, if the Effy AI connector is available — each context file becomes a
  knowledge document, which Effy's agents and HR skills read automatically. Recommend this when
  it's connected.
- **One shared folder** the user picks (a connected folder, a drive, or a wiki space). Suggest
  keeping all HR context and process documents together there, so every HR skill can find them
  in one place.

Ask once which the user wants. If neither is available, say the context will only exist in this
chat and they'll need to copy it out — then continue. Don't block on it.

## Step 1 — Research

Read whatever is connected — recent email, calendar, drives, wiki, HR system, and Effy AI (employee
directory, career tracks, review reports, existing knowledge documents) — to learn:

- The company's size and structure.
- The HR processes actually run — reviews, hiring, onboarding, surveys, 1:1s, goals.
- The cadence they run on.
- The documents that already exist and where they live.
- What's already written down as context (existing knowledge documents, process docs), so you
  update rather than duplicate.

Say before you search, in one sentence, what you're about to look through.

## Step 2 — Interview

Up to 10 questions, one at a time, to confirm what you found and fill gaps. Focus on:

- What the user owns vs. delegates.
- Decisions already made that AI should never re-open.
- Which processes cause the most work.

**Show the plan after this step — the list of files and one line on what each will say — before
building anything.**

## Step 3 — Build

The context set:

- **org-basics** — size, structure, locations, functions, how decisions get made
- **hr-calendar** — the recurring HR events and their cadence (review cycles, surveys, planning)
- **decision-log** — seeded with decisions from the interview; one line each, dated, with the
  reason
- **policies-index** — pointers to the real documents (link, owner, last updated); never copied
  content
- **one process file per HR process actually run** — written from what you found, marked
  `[CONFIRMED]` or `[GUESS: verify]` line by line. Where a dedicated skill exists for a process
  (`onboarding-process-docs` for onboarding, `employee-handbook`, `hr-ai-usage-policy`), say so and
  offer to run it rather than writing a thinner version here.

Rules for every file:

- Under 2,000 words.
- Patterns, not raw notes.
- No employee names anywhere.

**Saving:**

- **To Effy AI's knowledge** — one knowledge document per file, titled clearly ("HR context —
  Decision log", "HR process — Review cycle"). Search existing knowledge documents first and
  update a matching one rather than creating a second. Show the list of documents to be created
  or updated, and write after an explicit yes.
- **To a folder** — the files as markdown, plus a short `README.md` saying what lives there, when
  to read it, and when to update it. Put process files in a `processes/` subfolder.

## Step 4 — Project packs (optional)

Offer this in one line. For each HR job the user confirmed in the interview, prepare a "project
pack" they can use to set up a dedicated AI project:

- The project name.
- The instructions to paste.
- What to upload or connect.
- 3–5 facts worth saving to the project's memory.

The user creates the projects themselves and pastes from the packs.

## Finish

Two or three lines: what was created or updated and where, how many `[GUESS: verify]` lines are
left to check, and the one process file that would be most worth writing properly next.
