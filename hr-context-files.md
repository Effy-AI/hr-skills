# Create my HR context files

**HR context files setup** (`hr_context_files`)  
Build the folder structure, context files, and logs that future AI sessions run on — assembled from what can be verified about your company, not a generic template.

Help me create my HR context files — the folder structure, context files, and logs that future
AI sessions will run on. Built from what you can verify, not from a generic template.

## Step 0 — Get the folder connected first

Before any research, ask me to click **'add folder'** and connect the folder where my AI context
files should live. If I don't have one yet, ask me to create it and name it **HR-CONTEXT-FOR-AI**
— a fixed name so every other HR prompt in this set can point at the same place instead of asking
me to hunt for it each time.

Everything you build in Step 3 goes inside that folder. Without it, the structure lands in a
scratch directory I'll never open again, and the next session starts from zero — which defeats
the entire point of building context.

**Explain to me, in two or three lines, what this folder is** — because the natural assumption is
that you're asking me to duplicate my HRIS, and I'll resist that, correctly. Make these points in
your own words:

- It holds *context*, not records. Patterns, cadences, decisions, and pointers — how we work, not
  who works here. Employee data stays in the HRIS.
- It's what makes future AI sessions useful without re-explaining the company every time.
- Policies and templates are **linked**, never copied. There is one master of each document and it
  is not in this folder.

If I decline or no folder is available, say plainly that the structure will only exist in this
chat and that I'll need to copy it out myself — then continue. Don't block on it.

## Step 1 — Research

Read my recent email, calendar, Drive, and Effy (whatever is connected) to learn:

- My company's size and structure.
- The HR processes I actually run — reviews, hiring, onboarding, surveys.
- The cadence they run on.
- The documents that already exist and where they live.

## Step 2 — Interview

Ask me up to 10 questions, one at a time, to confirm what you found and fill gaps. Focus on:

- What I own vs. delegate.
- Decisions already made that you should never re-open.
- Which processes cause me the most work.

**Show me the plan after this step before you build anything.**

## Step 3 — Build

Create this structure, with a README.md in every folder explaining what lives there, when to
read it, and when to write to it:

- **company/**: org-basics.md, hr-calendar.md, decision-log.md (seed it with decisions from
  the interview), policies-index.md (pointers to the real documents in Drive — never copy
  content)
- **processes/**: one file per process I actually run, written from what you found, marked
  [CONFIRMED] or [GUESS: verify] line by line
- **OUTPUTS/**
- **logs/**: context-log.md (first entry: today, workspace created), feedback-log.md (empty,
  with a one-line header explaining what goes in it), and an empty context-reviews/ folder

Rules for every file:

- Under 2,000 words.
- Patterns, not raw notes.
- No employee names anywhere.

## Step 4 — Rooms

For each HR job I confirmed in the interview, prepare a "project pack" as a file in
OUTPUTS/project-packs/:

- The project name.
- The instructions to paste.
- What I should upload.
- 3–5 memory facts to save.

I will create the projects in the app myself and paste from your packs.
