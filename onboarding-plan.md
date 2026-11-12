# Build the onboarding plan for a new hire

**New hire onboarding plan** (`onboarding_plan`)  
Apply your documented onboarding process to one person — an owned and dated task list, welcome email, first-week schedule, draft 30/60/90, and a push to your tools once you approve.

The user has a new hire and wants the onboarding plan.

Collect whatever the user has already said about the hire — role, department, manager, start
date, country — and look the hire up where they may already exist: Effy AI's employee directory if
connected, the HRIS, or the ATS offer record. Don't stop to ask for the rest yet; Step 2 works out
which details the process actually needs.

Also look for **the plans used for recent hires in the same role** — onboarding projects or
checklists in the task tracker (Asana, Monday, Jira, Wrike, ClickUp), first-week schedules in
calendars, onboarding docs in drives. They show how the documented process is applied in
practice and are a source for Steps 3–7. They don't override the process document: where they
disagree, flag it.

## What this is, and what it isn't

This plan is the company's documented onboarding process applied to one person. **Nothing
invented, nothing skipped.** You are not designing an onboarding process here — you are
instantiating the one that exists.

A plan with invented steps in it is worse than no plan, because someone will follow it and do the
wrong thing.

## Step 1 — Get the onboarding process document

Ask the user for their onboarding process documentation, or where to find how onboarding should
work: a file, a folder, a link to a wiki or Drive page, or a knowledge base in a connected tool.
Ask once, in one line.

While waiting, or if the user points you somewhere, search what you can reach: Effy AI's
knowledge documents if the Effy AI connector is available (that is where `onboarding-process-docs`
offers to store it), connected folders, and connected drives and wikis (Google Drive, Notion,
Confluence, SharePoint). Identify the document by content, not by name:
it describes the onboarding process end to end, split by owner, and names the tools the process
runs in. A file called `onboarding.md` that turns out to be a checklist template or a policy
summary is not it.

- **Exactly one document qualifies** — read it, tell the user which one you're using and when it
  was last updated, and move on.
- **Several could be it** — list them and ask which is current. Don't merge them.
- **Promising names, but none describes both the process and the tools** — say so, name what you
  looked at, and ask the user to point you to the right one. Don't fall back to the closest
  match.
- **You can't read the location the user named** — ask them to paste the document or attach the
  file, and wait.

Do not build a plan from general knowledge of how onboarding usually works.

### No onboarding documentation exists

If the user says there is no documented process, or nothing qualifies after they've pointed you
to where it should be, stop and get it written first — don't build the plan on top of a gap.

- Tell the user in one line that the plan needs a documented process, and offer to create it now
  with the `onboarding-process-docs` skill (about 15–20 minutes: it reconstructs how onboarding
  actually runs from email, calendar and task tools plus a short interview).
- On a yes, invoke `onboarding-process-docs` and run it to the end. When the process document
  exists, come back to Step 1, read it, and continue to Step 2.
- If the skill isn't available in this environment, tell the user to install or run
  `onboarding-process-docs` themselves, then re-run this skill.

Don't try to do that skill's job inline — a per-hire plan derived from nothing is guesswork with
a due date attached.

## Step 2 — Work out which hire details matter, then collect the missing ones

From the process document, list the details of a hire that change the plan. A detail matters if
the process branches on it — country variants, per-department documents, role-specific steps — or
if dates are counted from it, like the start date. Typically that's role, department, manager,
start date, and country, but the document decides, not this list.

Then compare against what the user has already said:

- **Matters and given** — use it. Don't re-ask to confirm.
- **Matters and missing** — ask for all of these in one message, saying for each why the process
  needs it ("country decides which variant applies"). Wait for the answers.
- **The process never branches on it** — don't ask for it.

If the user has said something about this hire the process has no branch for — a contractor, a
part-time start, a second office — flag it now as a process gap rather than silently treating
them as the default case.

## Step 3 — Look for role- or department-specific material

Check whether the process document, or a companion document next to it, covers this role or
department: a meeting list, a 30/60/90 outline, a list of documents to copy per hire. Find it by
content, the same way as Step 1, in the same places.

If nothing role-specific exists, say so in one line and continue with the general process only.
Don't substitute another department's material. The sections that would have come from it
(first-week meetings, 30/60/90 outline, documents to copy) stay visibly thin and go on the gaps
list in Step 8.

## Step 4 — The task list

Every task from the source documents, as one list. For each:

- **The task**, in the words the source document uses.
- **Exactly one owner** — HR, the manager, the buddy, IT, or the new hire. One. A task owned by
  two people is a task nobody does.
- **A due date counted from the start date** — an actual date, plus the relative offset in
  brackets so it can be sanity-checked. `12 March [10 days before start]`.
- **Which document it came from.**

Order by due date, earliest first, including everything that happens before day one.

**If a document leaves a task without a clear owner, flag it — don't guess.** Put it in a
separate "needs an owner" list at the end with the task, where it came from, and who it plausibly
belongs to as a question for the user. A task assigned by guesswork fails silently, because the
person named never knew about it.

Same for a task with no timing: flag it rather than inventing an offset.

Apply the country variant from the documents. If they describe no variant for the hire's country,
say so explicitly — that's a gap in the process, not something for you to fill.

## Step 5 — The welcome email and first-week schedule

**Welcome email**, in the user's voice. If you can see how they write — their emails, their
messages — learn from that. If you can't, ask for two or three emails they've sent, or ask how
formal the company is. Don't default to corporate HR register.

It should cover what the documents say a welcome email covers: start time, where to go or which
link to join, who'll meet them, what to bring or set up beforehand, and what the first day looks
like. Nothing that isn't in the documents.

**First-week schedule**, built from the documented meeting list. Each entry: what the meeting is,
who's in it, how long, and roughly when in the week. Flag any meeting the list names without
saying who runs it.

## Step 6 — The manager's 30/60/90

Draft it from the documented outline. The shape is:

- **First 30 days — learning.** Getting up to speed on the domain, the tools, the people.
- **Days 30–60 — contributing.** Doing real work with support.
- **Days 60–90 — owning.** Carrying something end to end.

Mark the whole thing **DRAFT**. The manager owns this, not HR and not you. It's raw material for
them to adapt to the person they've actually hired — say that at the top of the section so nobody
mistakes it for settled.

Where the outline is thin or missing, leave the gap visible rather than padding it with generic
milestones. If the hire is on a career track in Effy AI, use their level's expectations
(`hr_get_employee_career_framework`) to make the 30/60/90 concrete.

## Step 7 — Documents to duplicate

From the documented copy list: which documents get a per-hire copy, with a link to each master.

**Links, never copied content.** If a master has no link in the source document, list the
document and flag that the link is missing.

## Step 8 — Show one review pack

Everything above, in one place, in this order: hire details · task list · needs an owner ·
welcome email · first-week schedule · 30/60/90 draft · documents to duplicate.

**Don't create anything in other tools yet.** No calendar invites, no tickets, no emails sent, no
documents duplicated, no messages to the manager or the new hire. Step 10 is the push, and it only
runs on the user's say-so.

Finish with two short lists:

- **Gaps** — every task with no owner, no date, or no link, and every place the documents were
  silent. This is what the user needs to close before the push.
- **What the documents don't cover for this hire** — anything specific to this role, country, or
  person that the process doesn't address. That's a note for improving the process document, not
  something to solve now.

## Step 9 — Sign the pack

End the review pack with this block, filled in. It travels with the plan wherever it's pasted, so
anyone reading it later can see what produced it and regenerate it.

```
Generated from: onboarding-plan
Date: [today]
Sources: [process doc name] [last updated] · [role/department doc name, if any] [last updated]
Open gaps at generation: [number]
```

If the user pasted the source documents rather than you reading them, say so on the Sources line
instead of naming a location.

## Step 10 — Push it, once approved

**Wait for an explicit instruction to push.** Not "looks good" in passing. Until then Step 8
stands and nothing gets created anywhere.

### Where it goes

Wherever the process document says — Slack lists, Wrike, Monday.com, Asana, Notion, a shared
sheet. **Don't pick a tool.** If the document doesn't say where the task list lives, ask once and
use the answer. Never default to whichever tool you happen to be connected to.

Before starting, tell the user which tools you can reach right now and which you can't. For
anything you can't reach, produce the output in a format they can paste straight into it — a CSV
with the right column headers for that tool, or the tool's own import format — rather than
skipping it silently.

### The task list

Create every task from the approved pack. For each one, set:

- **The assignee** — the owner from the pack, resolved to that person's actual account in the
  tool. If you can't match a name to an account, leave it unassigned and say so. An unassigned
  task the user knows about beats a task assigned to the wrong person.
- **The due date** — the calculated date from the pack, not the relative offset.
- **A description** naming which source document the task came from.

**Anything still in the "needs an owner" or "gaps" list does not get pushed.** Pushing a task
with a guessed owner is the exact failure Step 4 exists to prevent, and it's worse here because
now it looks official.

### Calendars

Find the calendars of everyone named in the first-week schedule — the manager, the buddy, IT, and
anyone running an intro meeting.

For each meeting: check attendee availability in the relevant week, pick a time that works for
all of them, and create the invite with the meeting name, attendees, and duration from the
documents. Keep the first-week meetings in the order the schedule sets, not wherever there's a
free slot — a tools walkthrough after the first standup is the wrong way round.

Also create the manager's recurring 1:1 with the new hire, starting in week one.

Two things to get right:

- **Don't invite the new hire before their account exists.** Their work address usually isn't
  live until IT provisions it. Create the invites without them, list which ones need them added,
  and say when to do it — or add them only if you can confirm the account is active. An invite
  sent to a personal address on day zero is a bad first impression and a small data leak.
- **Respect the country.** Check public holidays and the normal working week for the hire's
  country before placing anything. A first day scheduled on a public holiday is the kind of error
  that reaches the new hire.

If you can't reach calendars, output the schedule as a list of proposed times with attendees so
the user can create them, and say which conflicts you couldn't check.

### Documents

Duplicate the documents from the copy list, name each copy for this hire the way the process
document says, and put them where it says. If the naming convention isn't specified, ask rather
than inventing one.

### Don't create anything twice

Before creating anything, check whether it already exists — a task list for this hire, calendar
invites, duplicated documents. If it does, update it rather than making a second copy, and say
what you found. The user will re-run this after fixing a gap, and a re-run that doubles
everything is worse than one that does nothing.

### Report back

One short summary: what was created, where, with links. Then what wasn't, and why — tools you
couldn't reach, people you couldn't match to accounts, meetings you couldn't schedule, gaps that
stayed gaps.

**Nothing goes to the new hire or the manager in this step** unless the user asked for it
specifically. Creating the plan and announcing it are two different decisions.

### Offer: keep the 30/60/90 in Effy AI

If Effy AI is connected and the hire is in its employee directory, offer once to save the
approved 30/60/90 as a growth plan for the hire — type Personal development, the quarter they
start in as the period, status **Draft** (not visible to the employee until someone moves it on).
That way the manager can check it off in 1:1s and it carries into the first review. Read the
plan type's structure with `metadata_get_object_schema` (`growthplan`, variant
`personal-development`), fit the 30/60/90 into it, show the result, and create it with
`hr_create_growth_plan` only on an explicit yes. If the hire isn't in the directory yet, say so
and offer it again once they are.
