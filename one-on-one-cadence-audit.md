# Audit my 1:1 cadence

**1-on-1 cadence audit** (`one_on_one_cadence_audit`)  
Reads a manager's calendar and reports back, per direct report, how many 1:1s actually got
scheduled, when the last one was, and where the longest gap is. Read-only — it never touches
the calendar.

I think I'm running regular 1:1s with everyone. I want to know whether that's true, or whether
one or two people have quietly gone months without one.

Work from my calendar, not from my memory. Count what's there and tell me the numbers.

## Step 1 — Establish who and when

Ask me for:

- **The manager** — name and email. Usually me; sometimes I'm auditing someone else's cadence.
- **The direct reports** — name and email for each.
- **The window** — default to the last three months if I don't say.

Use the timezone of the manager's calendar for every date you report, and say which timezone
that is.

Don't start pulling until you have all three. If I've given you a team list in some other form —
an org chart, a Slack group, an email thread — read it and confirm the list back to me before
you use it.

## Step 2 — Check access

List the calendars you can see. Confirm you can read the manager's calendar. **If you can't,
stop and say so** — everything below depends on it, and a partial answer here is worse than no
answer.

Note which of the reports' calendars you can also read. Use those only to cross-check the
manager's calendar, never as the primary source. If you can see both and they disagree, flag
the discrepancy rather than picking one.

**If you have no calendar access at all**, say that plainly and stop. Ask me to export the
manager's calendar for the window and paste it in, or run this somewhere with calendar access.
Don't estimate.

## Step 3 — Pull the events

List every event on the manager's calendar in the window.

- Include recurring instances **individually**, not the series. A weekly series that was
  cancelled six times is not six meetings.
- Exclude: cancelled instances, all-day events, events the manager declined, and events with
  zero duration.

## Step 4 — Classify

For each report, a candidate 1:1 has to satisfy **both** of these:

**(a) Pairing.** The report is an attendee alongside the manager and nobody else — or the
attendee list is empty or incomplete, but the report's name is in the title.

**(b) Intent.** The title indicates a recurring individual check-in. Titles like: `1:1`, `1-1`,
`one-on-one`, `sync`, `catch-up`, `check-in`, `weekly`, or a `Manager / Report` name pair.

Do **not** count: standups, demos, sprint planning, retros, interviews, candidate calls, or any
meeting whose title names a customer, prospect, or third party.

Sort every candidate into one of three buckets:

| Bucket | Meaning |
| --- | --- |
| **Confirmed** | (a) and (b) both clearly met |
| **Ambiguous** | Meets one condition; or the title is generic or empty; or attendees are missing and the name isn't in the title |
| **Excluded** | Fails (b) |

**Never move an event from ambiguous to confirmed to make the numbers look better.** List the
ambiguous ones separately with the reason each is unclear. A clean-looking number I can't
trust is worth nothing to me.

## Step 5 — Report

For each report:

- Count of confirmed 1:1s.
- Every date, ascending (dd MMM), with the event title.
- Date of the most recent one, and days since.
- Longest gap between consecutive 1:1s, in days.
- Implied cadence: weekly, biweekly, monthly, or irregular.
- Ambiguous events: date, title, why it's unclear.

Then two lines across the whole team: who gets the most contact time, and who has the largest
gap.

## Rules

- **Read-only.** Never create, update, or delete an event. This is an audit, not a scheduling
  session.
- **Report only what the calendar shows.** No inferred meetings, no estimates, no filling gaps
  with what probably happened.
- **A calendar entry proves a meeting was scheduled, not that it happened.** Say this once in
  the output, so I read the numbers as a ceiling rather than a fact.
- **If a report has zero confirmed 1:1s, say zero.** Don't soften it and don't pad it with
  ambiguous events. That finding is the reason I ran this.
- **Don't interpret the pattern as a judgment about anyone.** Give me the counts and the gaps.
  The reason someone has a nine-week gap is a conversation, not a calculation.
