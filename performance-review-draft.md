# Draft a performance review

**Performance review draft** (`performance_review_draft`)  
Draft any review in the cycle — your self-review, a review of a direct report, an upward review of
your manager, or a peer review — from your own meeting history and tools. Every claim tied to a
citation, gaps flagged instead of filled. Run once per review.

> **HR: adjust this before sending it out.** Paste the exact questions from each of your review
> forms into SECTION 2 — word for word, in the same order they appear — one block per review
> type you run. Then replace the frameworks block with your own values or competency model, or
> delete it. Takes about ten minutes and it's the difference between "neat demo" and "done in 15
> minutes": if the questions match the form, people paste answers straight across. Any block you
> fill in, the AI uses as-is and won't ask about. Any block you leave empty, the AI asks the
> person for their form.
>
> **Everyone else: don't edit SECTION 1.** Paste the whole thing in and answer the questions it
> asks. Run it in your own environment, on your own account. If your HR team left SECTION 2
> empty, you can paste your form's questions there yourself and the AI won't ask for them.
>
> If your AI only searches recent notes by default, tell it first: *"Search all my meetings from
> [start of the review period] to now."*

---

## SECTION 1 — INSTRUCTIONS

Your task is to draft one performance review for me — a structured answer to every question on
the review form, grounded in evidence from my own meetings and tools, written in my voice. It
may be my self-review, or a review I'm writing about someone else. I'll edit the draft and submit
it in our review system.

### Step 1 — Work out who I am. Do this before asking me anything.

1. **Check every connection you have** — HR system or employee directory, org chart, calendar,
   meeting notes and transcripts, chat, email, docs. Tell me which sources you can see and
   roughly how much from the last six months is in them. If you can't see anything, say so
   plainly and ask me to attach what I have, rather than drafting from nothing.

2. **Work out my role from what you find:** my name, job title, team, who I report to, and
   whether anyone reports to me. Use the directory or org chart first; fall back to calendar
   patterns (recurring 1:1s), email signatures and chat profiles. Say how you know each fact.

3. **If I'm a manager, map both directions:** list my direct reports, and identify my own manager.
   Also note the three to five people I work with most outside my reporting line — they're the
   likely peer-review candidates.

4. **Show me the result in two or three lines** — "You're [title] on [team], reporting to [name].
   You have [n] direct reports: …" — and ask me to correct anything wrong. Don't build on a
   guessed org chart.

Use my job title (or the reviewee's) to calibrate what "expectations" and "impact" mean for the
role and level. A Senior Engineer and a first-year analyst aren't judged on the same scale. Assume
the review period is the last six months unless SECTION 2 or I say otherwise, and state that
assumption.

### Step 2 — Ask me up to three questions. One at a time.

**Question 1 — Which review?** Offer only the options that fit my role:

- **Self-review** — always.
- **Manager review** of a direct report — only if I have direct reports.
- **Upward review** of my manager — if I have a manager.
- **Peer review** of a colleague — always.

**Question 2 — Who is it about?** Skip this for a self-review. Otherwise offer the names you
found in Step 1 that fit the review type — my direct reports, my manager, or my most frequent
collaborators — and let me name someone else. Then find their job title and confirm it with me.

**Question 3 — What's on the form?** Look at SECTION 2 first. If the block for the chosen review
type has questions in it, use them verbatim and **don't ask this question.** If it's empty, ask me
to paste the questions from my review form, or attach the form. If I don't have one, offer the
standard questions in SECTION 3 and use them only if I agree.

### Step 3 — Read, learn my voice, then draft.

- **Ask me to attach anything missing** before you write: 1:1 notes, goal or OKR docs, project
  updates, previous reviews, peer feedback.

- **Read everything from the review period** where the reviewee appears or is discussed — 1:1s,
  team meetings, project syncs, planning sessions, retros, customer and stakeholder calls, any
  thread where their work came up. For a self-review, that's everything I worked on.

- **Learn my voice** from what you can see — how I actually phrase things in meetings, messages
  and email. Typical wording, sentence length, how direct I am. Write it the way I'd write it:
  direct, specific, short paragraphs, no corporate filler. Not generic AI prose.

- **Respect the frameworks in SECTION 2** if there are any. Assess against them and word
  achievements and development areas in their language, naming the specific principle or
  dimension demonstrated.

- **Ground every claim in evidence.** No generic praise, no unsupported criticism, no invented
  achievements. For every outcome, behaviour, win, miss or quote, add a citation like
  `[Meeting name — date, ~timestamp]`, or `[Meeting name — date]` if there's no timestamp.
  **Never state a fact without a source.**

- **Focus on outcomes, behaviours and impact** — not effort, not personality. Balance strengths
  with honest development areas. If the evidence is thin or one-sided, say so instead of
  overstating.

- **Ask me questions whenever it would produce a better draft** — work that left no trace,
  ambiguities, conflicting evidence. Up to five focused questions per round. Use my answers as
  evidence but mark those parts `[from my input]` rather than dressing them up as a citation.
  Don't guess.

- **Keep sensitive detail out** — salary, health, personal matters, anything from a private
  conversation that doesn't belong in a review. Refer to third parties by role or initials.

### Adjust for the review type

- **Self-review.** First person, about me. Don't inflate: if something didn't go well, a
  self-review that says so with evidence is worth more than one that doesn't — it's the part my
  manager will trust.

- **Manager review.** About my direct report, in my voice as their manager. Fair and specific. If
  the form has a rating, recommend one and justify it in two or three sentences from the
  evidence. If they manage people themselves, also assess their leadership: how they develop
  people, set vision and context, drive execution, and build team health.

- **Upward review.** About my manager, from where I sit. Focus on what I experienced directly:
  clarity of goals and priorities, quality of support and feedback, how reliably 1:1s and
  commitments happened, how they handle disagreement, whether I'm growing. Respectful and
  concrete — specific enough to act on. If upward reviews here are anonymous, flag any detail
  that would identify me so I can decide whether to keep it.

- **Peer review.** About a colleague, from my side of the work. Stick to what I saw directly in
  shared projects — collaboration, reliability, quality of their work as it reached me. Say what
  I can't see; a peer review isn't a full performance assessment.

### Output format

Start with one line: review type, who it's about, their title, the review period.

Then, for every question on the form, in order:

```
Q: [the question from the review form, repeated verbatim]
A: [your draft answer]
```

Keep each answer tight. After the last one, add:

- **Evidence gaps** — anything I should verify or fill in from memory before submitting,
  especially work that left no trace in any tool.
- **Two or three things worth raising** in the review conversation that don't fit neatly into the
  form, each with its citation.

---

## SECTION 2 — REVIEW QUESTIONS & COMPANY FRAMEWORKS

*(HR, or anyone running this: paste your form's questions into the block for each review type,
word for word. A filled block means the AI won't ask for the form. Leave a block empty and the
AI will ask.)*

### Review period

*(optional — e.g. "1 January to 30 June 2026". If empty, the last six months.)*

### Self-review questions

*(empty)*

### Manager review questions

*(empty)*

### Upward review questions

*(empty)*

### Peer review questions

*(empty)*

### Company frameworks — sample, replace with yours or delete

Map achievements and development areas to our values and name the specific behaviour
demonstrated:

- **Ownership** — follows through on commitments, owns outcomes and mistakes, steps up
  beyond the role.
- **Collaboration** — shares knowledge, aligns early, disagrees constructively, supports
  teammates.
- **Excellence** — holds high standards, seeks feedback, pays attention to detail, keeps
  learning.
- **Customer focus** — grounds decisions in customer impact and empathy for users.

---

## SECTION 3 — STANDARD QUESTIONS (fallback only)

Use these only if SECTION 2 is empty for the chosen review type, I have no form, and I've agreed
to use them.

**Self-review**

- **Q1:** To what extent did you deliver against the expectations set for this period? What
  outcomes, achievements or behaviours had the greatest positive impact? Where did you fall
  short?
- **Q2:** What are your key strengths? What is the one area, skill or behaviour that would most
  increase your impact or growth over the next six months?
- **Q3:** What support do you need from your manager or the company to do that?

**Manager review**

- **Q1:** To what extent did this team member deliver against the expectations set for this
  period? What outcomes, achievements or behaviours had the greatest positive impact? Where did
  their performance fall short?
- **Q2:** What are this team member's key strengths? What is the one area, skill or behaviour
  that would most increase their impact or growth over the next six months?
- **Q3:** Overall performance summary — choose one: Below Expectations | Meets Expectations |
  Exceeds Expectations. Explain your choice in two or three sentences.

**Upward review**

- **Q1:** What does your manager do that most helps you do your best work?
- **Q2:** What is the one thing they could do differently that would make the biggest
  difference to you or the team?
- **Q3:** How clear are you on your priorities and on what good performance looks like in your
  role? What would make it clearer?

**Peer review**

- **Q1:** Where did this colleague have the most positive impact on work you shared this
  period?
- **Q2:** What is the one thing they could do differently to be more effective in working with
  you or the team?

---

**I own the final text.** You draft, I edit and submit. I won't send anything I haven't read.

**Nothing here is shared.** I'm running this in my own environment on my own context. My notes
never leave my tools — only the final text I choose to paste into the review form.
