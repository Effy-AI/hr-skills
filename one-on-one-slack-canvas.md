# 1-on-1 Slack canvases

**1-on-1 Slack canvases** (`one_on_one_slack_canvas`)  
Set up a daily scheduled task that keeps one shared Slack canvas per direct report — short dated notes from every 1-on-1 plus prep for the next one — built from Slack, notetaker meetings and the calendar.

Keep one shared Slack canvas per direct report. Each holds two things: short dated notes from
every 1-on-1 that happened, and prep for the next one. A daily scheduled task maintains them, so
neither person has to write the meeting up or remember what was open.

The canvas belongs to both people. That fact drives every rule below: the employee reads
everything written there, so it must be built only from things they already saw, and it holds
topics and commitments, never verdicts about them.

This prompt works in two modes. Pick by context:

- **Setup** — a person is present and asked to start, change or extend the routine. This is the
  first run.
- **Daily run** — a scheduled task fired with a config block (see Setup step 6). Nobody is
  watching: ask nothing, decide, and report at the end.

## The two privacy rules

These hold in both modes and outrank everything else here.

1. **Slack: use only conversations this employee is a member of.** That means channels where a
   membership check shows their user ID, group DMs that include them, and the direct message
   between them and the manager. Verify membership with the connector for every channel you draw
   from; a message that mentions them is not proof they can see the channel. Never use the
   manager's DMs with other people, or any channel the employee is not in, even a public one.
2. **Meetings: use only meetings this employee attended.** Confirm from the notetaker's
   participant or speaker list. An invite alone is not attendance. If you cannot confirm it,
   skip the meeting.

The test for any line: could this employee already have read or heard the source? If not, the
line does not exist for their canvas — not reworded, not hinted at. Each report is processed
separately; what you learned while working on one person never informs another person's canvas.

The calendar is used for scheduling facts only — when a 1-on-1 is, was, or was cancelled — and
only from events this employee is invited to. The rest of the manager's calendar is not a
source. Email, performance reviews, compensation, and other people's canvases are out of scope.

## Setup

### 1. Check connections

Three things are needed. Look at the tools actually present, including deferred ones.

- **Slack**, with canvas create, read and update tools — required.
- **At least one notetaker** (Granola, Fathom, Zoom, Notion meeting notes, Fireflies, Otter, or
  similar) — required.
- **A calendar** (Google Calendar, Outlook, or similar) — it is how the routine knows each
  person's 1-on-1 schedule: when the next one is, and whether one was cancelled or moved.

If Slack or a notetaker is missing, stop and ask the user to connect it. Do not continue with
half the inputs: without a notetaker there are no 1-on-1 notes, and without Slack there is
nowhere to put them. If the calendar is missing, ask the user to connect it too; if they choose
not to, continue, infer cadence from past notetaker meetings, and say the next-meeting dates
will be estimates. If the environment has a connector search or suggest tool, use it so they get
a one-click option. Slack canvases are not available on free Slack plans; if canvas creation
fails for that reason, say so.

Note which notetakers are connected. If there are several, use all of them and deduplicate
meetings by time and participants.

### 2. Establish the direct reports and their 1-on-1 schedule

Find the reports before asking: an HR system or directory if one is connected (manager field),
what is already known about the user, Slack profiles, recurring two-person events on the
calendar, recurring two-person meetings in the notetaker. Then show the list and get a yes — one
question. Getting the roster wrong means a canvas about the wrong person, so this confirmation
is the one that is not optional.

For each report resolve and record: full name, Slack user ID, email, and their 1-on-1 schedule
from the calendar — the recurring event, its day, time and frequency, and the next occurrence.
Schedules differ per person; do not assume one cadence for the team. If someone has no recurring
1-on-1 on the calendar, say so in the confirmation — a missing slot is worth the manager knowing.

**Match the person, not the name** — a customer or colleague with a similar name is the classic
error.

### 3. Agree how updates are applied

Ask once which mode they want:

- **Auto** — the daily run writes to the canvases directly. The employee sees changes as soon as
  they land.
- **Review** — the daily run writes nothing. It reports the proposed changes and applies them
  only when the manager says so in that run's session.

If the user has a standing rule about not sending or publishing without approval, default to
Review and say why.

### 4. Create the canvases

One canvas per report, titled `1:1 - {Manager first name} / {Report first name}`. Seed it using
the daily-run method below with a longer lookback: the last five 1-on-1s for prep, and a dated
note entry for only the most recent one. If there is no history, create it with empty prep and
say so in one line on the canvas.

If a canvas for this pair already exists (search Slack by title first), adopt it instead of
creating a second one.

### 5. Share them

Read the Slack tools' descriptions. If the create tool can place a canvas in a DM or share it
with a user, create it in the DM with that report, with edit access.

If it cannot (common — many connectors only create a standalone canvas owned by the manager):

- Draft, do not send, a DM to each report containing the canvas link and one line on what it is
  and that they should add their own topics. Use the draft tool if there is one; otherwise give
  the user the text to paste.
- Tell the user how to finish, once: send the draft; when Slack asks whether to give the
  recipient access, choose edit access. Or open the canvas, use Share, add the person with
  "can edit". Optionally add the canvas as a tab in the DM so it is one click away. Slack's
  labels vary by version; describe the action, not exact button names.

Until a canvas is shared it is private to the manager. Report which ones are still unshared.

### 6. Create the scheduled task

Check existing scheduled tasks first; update the existing one rather than creating a duplicate.
Use the session's scheduled-task tool (search for it if tools are deferred). A session-local
timer that dies with the conversation does not count; if no real scheduling tool exists, say
that and give the user the task prompt to schedule themselves.

**Runs every day.** Choose the time from what you know about the user: their time zone, working
hours, and when their 1-on-1s fall on the calendar. Aim for shortly after their working day
ends — the day's meetings have finished processing in the notetaker, and prep is waiting the
next morning. With no evidence, use early evening local time. Avoid exact hours and half hours.
Tell the user the chosen time in one line; do not ask.

The task starts a fresh session with no memory of setup and no copy of this file, so **the task
prompt must carry everything it needs**. Build it from two parts:

1. The config block below, filled in.
2. The full text of three sections of this file, copied verbatim: *The two privacy rules*,
   *Daily run*, and *Things that go wrong*. Do not summarise them — a shortened copy is where
   the privacy rules get lost.

```
Daily run of the 1-on-1 Slack canvases routine. Unattended — do not ask questions.
Follow the instructions below the config exactly.

Manager: {name} | Slack {U...} | {email} | time zone {IANA zone}
Mode: {auto | review}
Notetakers: {list}
Calendar: {connector, or "not connected"}
Direct reports:
- {name} | Slack {U...} | {email} | canvas {F...} | usual 1:1: {day, time, frequency, or unknown}
- ...
```

The schedule line is a fallback only; the daily run reads the live calendar. When the roster or
mode changes later, update the config in the existing task.

### 7. Confirm

One short message: reports covered with each next 1-on-1 date, canvas links, which still need
sharing, run time, mode.

## Daily run

### 0. Check connections, every run

Connections drop between runs, so confirm each one answers before relying on it: Slack, each
notetaker, and the calendar. A failed source is not an empty source — "no meetings found" from a
notetaker that did not respond would silently skip a 1-on-1.

- Slack down: nothing can be written. Stop and report.
- A notetaker down: do not write notes or clear prep items for the affected window; report it.
  The next run's lookback will catch up.
- Calendar down or not connected: continue, use the schedule in the config, mark next-meeting
  dates as estimated, and report it.

Then, for each report in the config, independently:

### 1. Read the canvas

Read it fresh to get current content and section IDs (IDs change after every update). The
footer line gives the last update date. Look back from that date, at least 48 hours and at most
14 days. The overlap is deliberate — notetakers process late — so deduplicate against what the
canvas already says. If the canvas is missing or unreadable, skip this report and say so.

### 2. Read the calendar for this person's 1-on-1 schedule

Find the 1-on-1 events between the manager and this report: those in the lookback window, and
the next upcoming one. From them establish:

- **Which 1-on-1s were scheduled in the window**, and whether each ran, moved or was cancelled.
- **When the next one is.** This dates the prep heading and decides urgency: if it is today or
  tomorrow, the report to the manager includes what they should close before the meeting.
- **Changes since the config was written** — a new recurring slot, a different day, no slot at
  all. Report these so the manager can update the routine.
- **Cancellation pattern.** One cancelled 1-on-1 is noise. Two or more in a row is a signal for
  the manager's private report, never for the canvas.

### 3. Collect meetings

From the notetakers, list meetings in the window that both the manager and this report attended
(privacy rule 2). Sort each into:

- **1-on-1** — exactly these two people, and the conversation is a check-in. A matching calendar
  1-on-1 event is the strongest evidence; otherwise a title like "1:1" or the two names, or
  content ranging over the person's work, blockers and growth. Two people working through one
  task together is not a 1-on-1.
- **Other** — anything else the report attended.

If the calendar shows a 1-on-1 that was not cancelled but no notetaker has a record of it, do
not write a note entry and do not clear prep items. Report it: it may have run unrecorded, and
the manager can add a line themselves.

### 4. Debrief each new 1-on-1

Skip any 1-on-1 whose date already has an entry. For the rest, follow the debrief method
([one-on-one-debrief.md](https://github.com/Effy-AI/hr-skills/blob/main/one-on-one-debrief.md)),
compressed:

- Separate **discussed** (a topic came up), **decided** (a choice both would agree was made) and
  **committed** (someone will do a specific thing by a specific time). A conditional agreement
  recorded as a decision is the costliest error.
- Every line traces to the record. Do not infer a decision from a discussion or a commitment
  from an intention. Where owner or date is unclear, write it as stated and mark it.
- Action items need an owner and a due date; with none set, use the date of the next 1-on-1
  from the calendar and mark it assumed. Phrase each so it is obvious next time whether it
  happened.
- Close or carry the previous open items based on what was said.

### 5. Scan for discussion points

Sources: the other meetings from step 3, and Slack messages in the window that the report wrote,
was mentioned in, or took part in a thread of — each checked against privacy rule 1 before use.

Most days this adds nothing, and that is correct. The bar: **would this deserve three minutes of
a thirty-minute 1-on-1?** Worth adding:

- a blocker they raised that nobody resolved
- a commitment either of them made, with a date
- a decision that is waiting on the manager
- specific good work worth naming out loud
- a theme surfacing for the second or third time
- an interest or stretch they showed — something volunteered for, a question about direction

Not worth adding: routine status, FYIs, anything already resolved, anything about a third
person's performance.

### 6. Refresh the prep

Follow the prep method
([one-on-one-prep.md](https://github.com/Effy-AI/hr-skills/blob/main/one-on-one-prep.md)),
compressed for a shared page:

- Read the pattern across the recent notes, not just the last meeting. Something raised three
  times that has not moved is the real topic.
- Questions use GROW (Goal, Reality, Options, Will) and are about this person's actual
  situation. A question that would work for any employee is not worth writing.
- If a growth plan the employee can see is available, tie development points to goals they set.
  Never present a general impression as progress against a goal nobody agreed.

### 7. Write the canvas

Use exactly this structure. Leave out any prep section with nothing in it, except the
employee's own section, which always stays.

```
# Next 1:1 - {date from calendar, or "not scheduled"}
## Open action items
- [ ] {item} - {owner}, due {date}
## Worth discussing
- {point} ({source: meeting or channel, date})
## Questions
- {question}
## Topics from {report first name}
(theirs to fill in)
## One thing to try
{one sentence}

# Notes
## {date}
{summary, 1-2 sentences}
**Decided:** {...}
**Actions:** {item - owner, due}; {...}

---
Updated {date} from {sources}.
```

Rules for writing:

- **Short.** Prep fits on one screen: at most 5 points under Worth discussing, 2–3 questions.
  A note entry is at most 6 lines. If you are over, cut the weakest item.
- New note entries go at the top of Notes, newest first. Never rewrite an older entry.
- **Do not delete or reword anything a person wrote.** "Topics from ..." is theirs entirely.
  In the other prep lists, add your items and remove only your own items that a later 1-on-1
  covered or that were ticked off. When a 1-on-1 has happened, clear the covered points and move
  open actions forward.
- Topics, not verdicts. Write "the migration estimate slipped twice — what is in the way?",
  never an assessment of the person. Nothing about wellbeing, health or personal matters goes on
  the canvas unless it is an action both agreed to.
- **One thing to try** is a single sentence on meeting practice for both people, drawn from how
  their recent 1-on-1s actually went — for example, "the last two ended without owners on
  actions: close with who, what, when". It is about the meeting, never about either person.
  Omit it when there is nothing specific; change it when it stops being true.
- Follow the Slack tool's canvas markdown rules, including its date format for date headings.
- In Review mode, write nothing: put the exact proposed changes in the report instead.

### 8. Report to the manager

The final message is private to the manager and is the only place for what must not be on a
shared page. Per report, in a few lines:

- what changed on the canvas, or "no changes", and when the next 1-on-1 is
- **a careful-read flag first, if any** — a wellbeing, retention or disengagement signal, stated
  as a read from evidence, not a conclusion
- when the next 1-on-1 is today or tomorrow: what the manager should close beforehand — their
  own open commitments to this person
- how they seemed in the latest 1-on-1, in a sentence, tied to something said
- feedback worth giving, as Situation → Behavior → Impact, only when the record holds a real
  observation; positive feedback counts and is underused
- one coaching note for the manager on their own 1-on-1 practice when the evidence supports it:
  who did most of the talking, whether the employee's agenda came first, development topics
  skipped several meetings running, 1-on-1s cancelled or repeatedly moved, no recurring slot at
  all

Also list connection problems from step 0, schedule changes, and anything skipped and why
(unconfirmed attendance, unreadable canvas, a 1-on-1 with no recording). A day with nothing new
is one line.

## Things that go wrong

- **Wrong person.** A prospect call read as a 1-on-1 produces fluent notes about the wrong
  conversation. When a match is uncertain in an unattended run, skip and report it.
- **Invented history.** A thin record gives a thin canvas. Never fill a section because the
  template has a slot.
- **Leaking across reports.** A comment the manager made about one report in a meeting another
  report attended does not go on anyone's canvas.
- **A dead connector read as a quiet day.** Check connections first, every run.
- **A report leaves or is added.** Do not guess from Slack activity; the config is the roster.
  Changes come from the manager through Setup.
