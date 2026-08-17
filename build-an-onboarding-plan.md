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
documents duplicated, no messages to the manager or the new hire. We push after I've reviewed.

Finish with two short lists:

- **Gaps** — every task with no owner, no date, or no link, and every place the documents were
  silent. This is what I need to close before we push.
- **What the documents don't cover for this hire** — anything specific to this role, country, or
  person that our process doesn't address. That's a note for improving
  `processes/onboarding.md`, not something for you to solve now.
