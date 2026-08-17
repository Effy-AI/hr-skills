# Build the onboarding plan for a new hire

We have a new hire. Build the onboarding plan.

**Hire:** [role] in [department], manager [initials], starting [date], based in [country].

If I haven't filled those in, ask me for them before you start. All five matter — the country
decides which variant applies, and the start date is what every due date is counted from.

## What this is, and what it isn't

This plan is our documented onboarding process applied to one person. **Nothing invented,
nothing skipped.** You are not designing an onboarding process here — we already have one.
You're instantiating it.

That distinction is the whole point. A plan with invented steps in it is worse than no plan,
because someone will follow it and do the wrong thing.

## Step 1 — Read the two source documents

You need two things:

1. **`processes/onboarding.md`** — our general onboarding process, split by owner.
2. **The department document for this role** — the meeting list, the 30/60/90 outline, and the
   document copy list for this department.

**If you can read files**, read both from my Claude-HR folder now. Tell me which two documents
you used and when each was last updated. If the department document doesn't exist for this
department, say so and stop — don't substitute another department's.

**If you can't read files**, ask me to paste both in, and wait. Do not proceed on one of the two,
and do not build a plan from general knowledge of how onboarding usually works. If I only have
one document, say what the other one would have given you and let me decide whether to
continue.

If neither document exists, tell me to document the process first — a per-hire plan derived from
nothing is guesswork with a due date attached.

## Step 2 — The task list

Every task from both documents, as one list. For each:

- **The task**, in the words the source document uses.
- **Exactly one owner** — me, the manager, the buddy, IT, or the new hire. One. A task owned by
  two people is a task nobody does.
- **A due date counted from the start date** — an actual date, plus the relative offset in
  brackets so it can be sanity-checked. `12 March [10 days before start]`.
- **Which document it came from.**

Order by due date, earliest first, including everything that happens before day one.

**If a document leaves a task without a clear owner, flag it — don't guess.** Put it in a separate
"needs an owner" list at the end with the task, where it came from, and who it plausibly belongs
to as a question for me. An assigned-by-guesswork task fails silently, because the person named
never knew about it.

Same for a task with no timing: flag it rather than inventing an offset.

Apply the country variant from the documents. If the documents describe no variant for
[country], say so explicitly — that's a gap in our process, not something for you to fill.

## Step 3 — The welcome email and first-week schedule

**Welcome email**, in my voice. If you can see how I write — my emails, my messages — learn
from that. If you can't, ask me for two or three emails I've sent so you have something to work
from, or ask me to describe how formal we are. Don't default to corporate HR register.

It should cover what the documents say a welcome email covers: start time, where to go or which
link to join, who'll meet them, what to bring or set up beforehand, and what the first day looks
like. Nothing that isn't in the documents.

**First-week schedule**, built from the department document's meeting list. Each entry: what the
meeting is, who's in it, how long, and roughly when in the week. Flag any meeting the list names
without saying who runs it.

## Step 4 — The manager's 30/60/90

Draft it from the department document's outline. The shape is:

- **First 30 days — stretch learning.** Getting up to speed on the domain, the tools, the people.
- **Days 30–60 — contributing.** Doing real work with support.
- **Days 60–90 — owning.** Carrying something end to end.

Mark the whole thing **DRAFT**. The manager owns this, not me and not you. It's raw material for
them to adapt to the person they've actually hired — say that at the top of the section so nobody
mistakes it for settled.

Where the department outline is thin, leave the gap visible rather than padding it with generic
milestones.

## Step 5 — Documents to duplicate

From the department document's copy list: which documents get a per-hire copy, with a link to
each master.

**Links, never copied content.** If a master has no link in the source document, list the document
and flag that the link is missing.

## Step 6 — Show me one review pack

Everything above, in one place, in this order: hire details · task list · needs an owner · welcome
email · first-week schedule · 30/60/90 draft · documents to duplicate.

**Don't create anything in other tools yet.** No calendar invites, no tickets, no emails sent, no
documents duplicated, no messages to the manager or the new hire. Step 8 is the push, and it
only runs once I've said so.

Finish with two short lists:
- **Gaps** — every task with no owner, no date, or no link, and every place the documents were
  silent. This is what I need to close before we push.
- **What the documents don't cover for this hire** — anything specific to this role, country, or
  person that our process doesn't address. That's a note for improving
  `processes/onboarding.md`, not something for you to solve now.

## Step 7 — Sign the pack

End the review pack with this block, filled in. It travels with the plan wherever I paste it, so
anyone reading it six months from now can see what produced it and go regenerate it.

```
Generated from: Build the onboarding plan for a new hire
https://github.com/Effy-AI/hr-skills/blob/main/build-an-onboarding-plan.md
Date: [today]
Sources: processes/onboarding.md [last updated] · [department doc name] [last updated]
Open gaps at generation: [number]
```

If you couldn't read the source documents yourself and I pasted them in, say so on the Sources
line instead of naming a file path — the pack should be honest about where its inputs came from.

## Step 8 — Push it, once I've approved

**Wait for me to say go.** Not "looks good" in passing — an explicit instruction to push. Until
then Step 6 stands and nothing gets created anywhere.

### Where it goes

Whatever the process document names — Slack lists, Wrike, Monday.com, Asana, Notion, a
shared sheet. **Don't pick a tool.** If the document doesn't say where the task list lives, ask me
once and use my answer. Never default to whichever tool you happen to be connected to.

Before you start, tell me which tools you can actually reach right now and which you can't. For
anything you can't reach, produce the output in a format I can paste straight into it — a CSV
with the right column headers for that tool, or the tool's own import format — rather than
skipping it silently.

### The task list

Create every task from the approved pack. For each one, set:

- **The assignee** — the owner from the pack, resolved to that person's actual account in the
  tool. If you can't match a name to an account, leave it unassigned and tell me. An unassigned
  task I know about beats a task assigned to the wrong person.
- **The due date** — the calculated date from the pack, not the relative offset.
- **A description** naming which source document the task came from, so anyone opening it can
  see why it exists.

**Anything still in the "needs an owner" or "gaps" list does not get pushed.** It stays a gap.
Pushing a task with a guessed owner is the exact failure Step 2 exists to prevent, and it's worse
here because now it's in a system where it looks official.

### Calendars

Find the calendars of everyone named in the first-week schedule — the manager, the buddy, IT,
and anyone running an intro meeting.

For each meeting in the schedule: check attendee availability in the relevant week, pick a time
that works for all of them, and create the invite with the meeting name, attendees, and duration
from the department document. Put the first-week meetings in the order the schedule sets, not
just wherever there's a free slot — a tools walkthrough after the first standup is the wrong way
round.

Also create the manager's recurring 1:1 with the new hire, starting in week one.

Two things to get right:

- **Don't invite the new hire before their account exists.** Their address usually isn't live until
  IT provisions it. Create the invites without them, list which ones need them added, and tell me
  when to do it — or add them only if you can confirm the account is already active. An invite
  bouncing to a personal address on day zero is a bad first impression and a small data leak.
- **Respect the country.** Check public holidays and the normal working week for [country]
  before placing anything. A first day scheduled on a public holiday is the kind of error that
  reaches the new hire.

If you can't reach calendars, output the schedule as a list of proposed times with attendees so I
can create them myself, and say which conflicts you couldn't check.

### Documents

Duplicate the documents from the copy list, name each copy for this hire the way the process
document says to, and put them where it says. If the naming convention isn't specified, ask
rather than inventing one — inconsistent names are what make these impossible to find later.

### Don't create anything twice

Before creating anything, check whether it already exists — a task list for this hire, calendar
invites, duplicated documents. If it does, update it rather than making a second copy, and tell
me what you found. I will re-run this after fixing a gap, and a re-run that doubles everything is
worse than one that does nothing.

### Report back

One short summary: what was created, where, with links. Then what wasn't, and why — tools you
couldn't reach, people you couldn't match to accounts, meetings you couldn't schedule, gaps
that stayed gaps.

**Nothing goes to the new hire or the manager in this step** unless I've asked for it specifically.
Creating the plan and announcing it are two different decisions.

---

**Running this often?** In Claude Code or Claude Cowork you can turn this prompt into an
installed skill, so it triggers whenever you mention a new hire instead of being pasted each
time. Run `/skill-creator` and give it this file. Not available in ChatGPT or on claude.ai —
there, copy and paste stays the way to run it.
