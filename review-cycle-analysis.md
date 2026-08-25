# Analyze our performance review cycle

I'm going to give you our performance review data. Turn it into one report our leadership team
can actually use: how each cohort is doing, who's promotion-ready, and where our reviews are
being graded inconsistently.

Work through three intake steps first. Don't skip ahead, and don't start analysing until you have
what each step asks for.

## Ground rules

- **Anonymize by default.** Unless I tell you otherwise, replace every real name with
  `Employee 1`, `Employee 2` and so on before you analyse anything. Build the map once and
  apply it everywhere — including names that appear *inside* written comments. People write
  things like "I worked closely with Sarah on Q3", and Sarah may never appear as a reviewee or
  a reviewer. Replace longer names before shorter ones so "Sarah Smith" doesn't leave a
  stray "Smith". Do not show me the name map unless I ask.
- **Never invent a quote or an example.** Quote verbatim. If there's nothing in the data, write
  "no evidence in the data" and move on.
- **Anonymize peer quotes** — strip names, job titles, and identifying details from anything a
  peer wrote, so a quote can't be traced back to the person who wrote it.
- **No demographic guessing.** If there's no demographic column in my data, skip anything
  that would need one. Never infer gender, ethnicity, or age from a name.
- **Every bias flag is "flag for human review."** You surface the pattern; we decide what it
  means. Never render a verdict about a person's character.

## Step 1 — The review data

Ask me to upload or paste the reviews. Any mix of self-reviews, manager reviews, peer/360
feedback, and upward feedback. Any format — spreadsheet, doc, PDF, or pasted text.

Work out the structure yourself: who's being reviewed, who wrote each response, which type of
rater they are, and which fields are numeric ratings versus written comments. If it's genuinely
ambiguous after a real attempt, ask me **one** targeted question. Don't interrogate me.

## Step 2 — Who reports to whom

Ask me for a list of people with: name, job title, team, and who they report to.

Then sort everyone into three groups:

- **Leadership** — C-level, VPs, Heads of, Directors. Anyone with managers reporting to them.
- **Managers** — people managers who aren't Leadership. They have at least one direct report,
  and they report to someone who also has reports.
- **Individual contributors** — everyone else, including senior people with no direct reports.

If I give you my own groupings, use mine instead and note that in the report.

If I don't have a roster, work with what I've got and ask one focused question — usually "do you
have a list of who reports to whom?". If I have nothing, infer the structure from the reviews
themselves and **say clearly in the report that you inferred it**.

Then show me the breakdown before you go further: *"I've sorted 51 people into 4 Leadership,
12 Managers, 35 ICs — confirm or correct before I run the analysis."* Fixing this now is cheap.
Fixing it after the report is built is not.

## Step 3 — Our values and competencies (optional)

Ask for our company values and role expectations. If I only have one of the two, take it and
carry on. If I have neither, use these six and say in the report that defaults were used:

**Craft** (quality of their actual discipline) · **Delivery** (turning work into shipped outcomes) ·
**Collaboration** (how they work with people around them) · **Influence** (how far their effect
reaches beyond their own work) · **Ownership** (following through, owning mistakes) ·
**Judgement** (decision quality under uncertainty)

Weight them equally unless I say otherwise.

## The analysis

1. **Score each person on each competency, 1–5**, and quote the specific evidence you scored
   it on. A score with no quote behind it isn't a score.
2. **Weighted overall score** per person. Average per cohort, and per leader's team.
3. **Cluster the written feedback into themes** — Start / Stop / Continue. A theme needs at
   least two different raters saying it, or it's an opinion, not a theme.
4. **Bias and calibration pass.** Flag these types, and print the definition next to each flag so
   we can learn to spot them ourselves:
   - *Halo / horn* — one strong impression colouring every other rating for that person.
   - *Vague positive* — praise with no specifics. Often hides an unwillingness to say anything real.
   - *Recency* — the whole review is about the last few weeks.
   - *Coded language* — words applied to some people and not others: "abrasive", "emotional",
     "not a culture fit", "needs polish".
   - *Rater variance* — one person's ratings scattered far wider than everyone else's.
   - *Manager leniency drift* — one manager grading consistently higher or lower than the rest.
   - *Compression* — everyone landing on 3s and 4s, which means the scale isn't being used.
5. **Gap analysis** — where a person got both a self-review and a manager or peer review,
   show the difference. Big self-vs-manager gaps in either direction are worth a conversation.
6. **Promotion readiness** — Yes / Not yet / No, with the evidence. Two hard rules:
   - If you have evidence covering less than 60% of a person's competencies, the answer is
     **"Not yet"**. Never "Yes" on thin data.
   - The promotion-ready shortlist is capped at **15% of total headcount**. No exceptions. If
     more people qualify mechanically, rank by strength of evidence and cut. Say in the report
     how many qualified versus how many made the list.
7. **Development plan** — two to four concrete actions per person. Things they'd actually do,
   not "improve communication".

## The report

**If you can produce a file or an artifact**, build it as one self-contained HTML page I can open
in a browser and send on. **If you can't**, output it here as markdown.

Structure it top to bottom:

1. **Header** — company, review cycle, date generated.
2. **Executive summary**, 300–500 words: two paragraphs on the whole company (overall score,
   shape of the distribution, top three strengths, top three risks, the single most important
   recommendation). Then one short paragraph per Leadership person summarising their team —
   average score, top performer, biggest risk, one calibration concern. This is the part a CEO
   reads first, so make it skimmable leader by leader.
3. **Cohort overview** — for each of the three cohorts: headcount, mean score, spread, the top
   10% and bottom 10% by name and score, and one sentence on what the cohort looks like.
4. **Promotion-ready shortlist** — max 15% of headcount. Per row: name, cohort, role, the single
   strongest piece of evidence (a verbatim quote where possible), the most-cited development
   area, overall score, and how much of their competency set you actually had evidence for.
5. **Calibration flags** — one table grouped by flag type, with the definition of each type
   printed once at the top of its group. Columns: type, what it means, who it concerns, the
   comment.
6. **Person by person** — grouped by cohort, Leadership first, then Managers, then ICs. Sort by
   score within each cohort. Inside the IC group, sub-group by their manager. For each person:
   overall score, promotion verdict and rationale, development plan, competency scores with
   evidence, themes, self-vs-manager-vs-peer gaps, bias flags. Leave out any section you have
   no data for — never print "no data" placeholders.
7. **Methodology footer** — the scale, the weights, where the data came from, whether default
   competencies were used, whether the org structure was given or inferred, and what to be
   careful about when reading this.

## Finish with

Three sentences: the headline finding, the biggest calibration risk, and one thing that's going
well. Then tell me which parts of the analysis were thin on evidence, so I know what not to lean
on in a promotion conversation.
