# Document our onboarding process

**Onboarding process documentation** (`onboarding_process_docs`)  
Work out how onboarding actually runs here — from your email history and a short interview — then write it up as a checklist per owner: HR, hiring manager, buddy, IT, new hire.

I want you to write my company's onboarding process into one document. Before writing anything,
learn how onboarding actually works here. Three passes. Do not skip ahead, and do not write the
document until Pass 3.

## Ground rules

Follow these for the whole conversation.

- **Document the current state only.** Write what we actually do, not what a good process would
  look like. Never improve, reorder, or "clean up" a step while documenting it. If you see an
  obvious problem, save it for the *Known failure points* section — do not fold the fix into
  the process as if it already existed.
- Refer to people by **role and initials**, never full names. `Hiring manager (J.K.)`, not
  `Jamie Kowalski`.
- **Never write sensitive personal data** into the document, even if you find it: ID or passport
  numbers, bank details, home addresses, salary figures, immigration status, health information.
  Describe the *step* that handles the data, never the data itself.
- **Never invent** a tool, step, person, or date. If you don't know, it becomes a question — in
  Pass 2, or in the clarification round before the document is written.
- Plain language. Two pages maximum.
- **In chat, be brief.** This is separate from the document itself — it's about how you talk to
  me while building it. One direct question at a time, no preamble. When you report what you
  found (Pass 1 recap, timeline notes, anything conversational), compress it to 1-2 sentences —
  I can ask for the detail if I want it.

  Don't write: "No recent-hire trail exists. The HRIS has only 3 records (you, Sergey Karlo —
  status 'Invited,' no hire date, Chloe J — a Kimmeridge contact, not an employee). Calendar
  shows Sergey Karlo, Alexey Postulha, and Andrii Hromovyi on a recurring 'Team Sync' going back
  to March 2025 — over a year of history, not a new hire. Slack DMs with Sergey are all
  product/eng work..." and so on.

  Write instead: "No onboarding trail anywhere — HRIS, calendar, Slack, email. Either the team
  hasn't grown in a year, or hiring happens somewhere I can't see. Which is it?"

### How to weigh evidence

Not everything you learn counts the same. From strongest to weakest:

1. A calendar event, sent email, or completed task that actually happened
2. An existing onboarding document, checklist, or template
3. An HRIS or system record
4. The same step observed across two or more hires
5. What I or a manager *say* happens
6. My recollection of a one-off
7. Common HR practice — **this is worth nothing here; never use it to fill a gap**

When strong evidence contradicts what I tell you, do not merge the two into something vague.
Quote the evidence, name the conflict, and ask which is right.

**Absence is evidence too.** A step everyone says exists but no email, calendar event, or task
ever shows; an account created two days late; someone asking twice for the same thing; HR
chasing a manager — each of these tells you something the happy-path story does not. Record
what you *expected to find and didn't*, not only what you found.

**One hire is not a process.** For every step, note how many of the recent hires it appears
for. Seen for all of them: standard. Seen once: possibly a one-off — ask before treating it as
standard. Never generalize a single welcome email into "we send welcome emails."

## Step 0 — Where this gets saved

Before anything else, ask me to click **'add folder'** and attach the folder where my HR context
files live (or should live). The document you write at the end belongs in that folder, alongside
the rest of my HR context — not in a scratch directory I'll never find again.

Mention the name: **if I've already run Effy's `hr-context-files` prompt, that folder is called
HR-CONTEXT-FOR-AI**. Say so when you ask — it turns a vague question into one I can answer in two
seconds. Don't insist on the name, though; a differently-named folder with the right contents is
fine, and the check below is on contents, not on the label.

Once I've attached it, look at what's in it:

- **Folder has an HR context structure already** (company/, processes/, logs/ or similar) — good.
  Read what's there before Pass 1; existing process files, decision logs, and policy indexes are
  Pass 1 evidence, and often the strongest kind. Then carry on.
- **Folder is empty or has no HR structure** — build it first, following the `hr-context-files`
  skill (https://github.com/Effy-AI/hr-skills/blob/main/hr_context_files.md): the company/,
  processes/, OUTPUTS/, and logs/ folders, each with a README.md explaining what lives there and
  when to read or write it. If `hr-context-files` is installed as a skill here, invoke it rather
  than reimplementing it from memory. Say in one line that you're doing this and why. Then start
  Pass 1 — the onboarding document you produce becomes the first real file in processes/.

If I don't pick a folder, say once that the document will only exist in this chat, and continue.
Don't block on it.

## Pass 1 — Find out what actually happens

Gather evidence from every source you can reach before you ask me anything.

### Task and project tools

**If I have a task tracker connected — Asana, Monday, Jira, Wrike, Todoist, ClickUp, Linear or
similar — search it now.** Onboarding usually lives there as a template project, a recurring
checklist, or a set of tasks named after the new hire. Look for:

- onboarding templates, project templates, task templates
- projects or task lists named after recent hires
- tasks assigned to HR, IT, or a hiring manager around a start date
- **overdue and repeatedly rescheduled tasks** — these mark the steps that keep slipping
- comments arguing about who owns a step

Record the task name, owner, due date relative to the start date, and whether it was completed
on time.

### Knowledge bases and documents

**If I have Confluence, Notion, Google Drive, SharePoint, Slack or similar connected, search
those too**, plus any local files you can read. Look for onboarding checklists, first-week
schedules, welcome decks, start-here pages, IT setup runbooks, and 30/60/90 templates.

### Email and calendar

**If you can search my email or calendar, do it now.** Find the last 2 or 3 people we hired.
Search around their start dates for:

- offer confirmations and signed contracts
- welcome emails and first-week schedules
- IT and equipment requests, account setup
- intro announcements to the company or team
- **reminders and chase-ups** — "did this get done?", "still waiting on", "can you send"

The reminders matter most. Every reminder marks a step that does not happen on its own. Note who
had to chase whom, and for what.

For each step you find, record: what happened, who did it, how many days before or after the
start date, what evidence backs it (per the hierarchy above), how many hires it appears for,
and whether it slipped.

### Ask me for the plans themselves

Whatever you found, **ask me to paste or attach the onboarding plans we already use** — links to
a Notion page, an Asana or Monday template, a Google Doc, or files (PDF, DOCX, PPTX, XLSX).
Tell me exactly what would help most, based on the gaps in what you found. Wait for my reply
before continuing.

If I give you **more than one plan**, work out which role each one covers — engineering, sales,
support, manager, generic — from its content. Say what you concluded, one line per plan. **If a
plan's role is unclear, or two plans look like they cover the same role, ask me** rather than
guessing.

**If you have no access to any of these sources**, say so plainly and tell me exactly what to
paste in: email threads around the last 2 or 3 hires, and any onboarding notes, checklists, or
templates we already have.

Build a picture of what we actually do, not what we'd say we do. Beyond asking for the plans, do
not ask me anything else yet.

## Pass 2 — Interview me

Ask me questions **one at a time**. Wait for each answer before asking the next.

**Ask only what the evidence could not answer, and stop when further answers would no longer
change the document.** Ten questions is the ceiling, not the target — three good questions beat
ten dutiful ones. A question you could have answered yourself from Pass 1 is a wasted question.

Start by telling me, in three or four lines, what you found in Pass 1. Then ask in this order
of importance:

1. **Ownership ambiguity** — a step happened but nobody clearly owns it, or two people each
   think the other does it.
2. **Missing critical steps** — something onboarding cannot work without, with no evidence it
   happens: contract signature, payroll setup, account creation, equipment.
3. **Contradictions** — the evidence says one thing, a document or my earlier answer says
   another. Quote what you found and ask which is right. Never silently pick one version.
4. **One-offs vs standard** — steps seen for only one hire that you need classified.
5. **Employee-experience gaps** — the new hire waited, asked twice, or had nothing to do.
6. **Minor details** — only if questions remain in the budget.

Topics worth covering where gaps exist: the owners (me, hiring manager, buddy, IT); offer to
day 1; day 1 and week 1; check-ins at 30/60/90; tool names (HRIS, payroll, e-signature,
tracker, chat — names, not categories); documents every new hire gets and where each master
lives; variants by role or country; where the process most often falls over.

## Pass 3 — Reconstruct, close the gaps, then write

### Timeline first

Before asking anything else, show me the process as a compact timeline relative to the start
date, so I can validate it at a glance. One line per step: timing, owner, action, and — only
where the backing is weak — a short evidence note.

```
T-14  HR            contract sent for signature
T-7   IT            accounts created            (1 of 3 hires — on time; other 2 late)
T-1   Manager       welcome message             (seen once — one-off?)
D1    HR            orientation
D30   Manager       check-in                    (your recollection only)
```

Mark every line you cannot back with strong evidence. This timeline is the skeleton of the
document — errors are cheapest to catch here.

### Clarification round

Check your material against the checklist below. Anything you cannot state as fact — because no
evidence covers it, or my answers left it open — becomes a question.

**Ask me those questions now, as one grouped list**, organized by owner. Say what you already
have and what is missing. Wait for my answers.

Use this checklist to find the gaps. It is the standard shape of an onboarding process, not a
description of ours — treat every line as something to *ask about*, never something to assume.

**HR** — contract out for signature; HRIS profile and payroll set up; hire announced to the
company; manager and buddy notified; hardware ordered; welcome email with the first-day
schedule; new-hire document copies made; day-1 welcome conversation; benefits enrollment; the
30/60/90 check-in cycle.

**Hiring manager** — recurring 1:1 and week-1 intro meetings booked; buddy picked; the 30/60/90
adapted for this hire; day-1 personal welcome; a first real task assigned; check-ins at 30, 60
and 90.

**Buddy** — hello message before day 1; day-1 tour or tools walkthrough; touchpoints through
week 1; when the duty ends.

**IT** — laptop prepared; accounts created from a role template; day-1 handover; two-factor
login verified.

**New hire** — contract signed; ID and bank details submitted (where, and by which route);
day-1 setup checklist; the start-here page read; intro meetings booked; benefits enrolled; first
task finished; any reflection or self-review before the day-30 check-in.

If I say a step doesn't exist here, leave it out of the document. Do not fill it with a
plausible default.

### Write the document

**Write only what I confirmed or what the evidence shows.** No inferences, no placeholders, no
suggested-but-unverified steps. If something is still unknown after the clarification round,
leave it out and say, in one line at the end, what you left out and why.

Do not clutter the document with evidence citations. Mark only the weak spots: append
`*(unverified)*` to any step backed by nothing stronger than recollection, so a reader knows
exactly which lines to double-check. Everything unmarked is evidence-backed or confirmed.

Sections, exactly these:

1. **Overview** — the phases from offer accepted to day 90. Three sentences.
2. **One section per owner** — HR, hiring manager, buddy, IT, new hire. Each a checklist ordered
   by timing, with the timing on every line (`10 days before start`, `day 1`, `week 1`) and,
   where one exists, the trigger that starts it (`after contract signed`, `when HRIS record
   created`).
3. **Variants** — per role, per country. Only real differences. Skip the section if there are
   none.
4. **Tools and documents** — what we use, links to where the masters live, and which documents
   get duplicated for each new hire. **Links, never copied content.**
5. **Check-in and feedback cadence.**
6. **Known failure points** — the steps the evidence shows slipping: reminders sent, deadlines
   missed, duplicated work. One line each, stating what the evidence was. Facts only — no
   recommendations unless I ask for them.
7. **Data note** — which steps touch sensitive personal data (ID documents, bank details, home
   addresses), and how we handle them.

### Finish by writing the file

The job is not done when the document is written — it is done when the file exists on disk in my
folder. A document that only ever appeared in chat scrolls away and was never worth building.

To close out:

1. **Write the file** to `processes/onboarding.md` inside the folder I picked in Step 0. Use your
   file-writing tools — don't paste the document into chat and call it delivered.
2. **Append to `logs/context-log.md`**: today's date and one line saying the onboarding process
   was documented. That log is how future sessions know this already exists and shouldn't be
   redone from scratch.
3. **Show me the file.** Give me a way to open it — a file card or the full path. Then tell me,
   in one or two sentences, where it landed and anything you left out and why.

If Step 0 produced no folder — I declined, or none was available — say so plainly and output the
whole document in chat as markdown in a single code block so I can copy it out. That is the
fallback, not the default; if a folder exists, the file gets written.
