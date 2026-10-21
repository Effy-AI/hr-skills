# Analyze our performance review cycle

**Review cycle analysis** (`review_cycle_analysis`)  
Turn a pile of review files into one calibration-ready report. Every calibration angle is
calculated on the file, not guessed — managers who rate everyone at the top, managers who give
every report the same score, top and bottom ratings with no evidence behind them, and where
employees and managers disagree. Top five findings first, then the managers to talk to before
calibration and why. Plus cohort scores, themes, bias flags, and a promotion-ready shortlist
capped at 15% of headcount.

I'm going to give you our performance review data. Turn it into one report our leadership team
can actually use before and during calibration: where our ratings are inconsistent, which
managers to talk to first, how each cohort is doing, and who's promotion-ready.

Work through four intake steps first. Don't skip ahead, and don't start analysing until you have
what each step asks for.

## Ground rules

- **Calculate, don't estimate.** Every number in the calibration sections — counts, averages,
  spreads, percentages, gaps — comes from a calculation on the data I gave you. If you can run
  code, load the file and compute it there. If you can't, compute it step by step and show the
  counts so I can check them. Never write "most managers" or "around a third" without the
  number behind it.
- **Numbers first, then plain words.** Under every table or figure, write one or two sentences
  saying what it means, in language a CEO would use. "Manager C rated all 6 reports 5 out of 5.
  No other manager rated more than half their team at the top." Not "elevated leniency
  observed".
- **Keep calculation and judgement apart.** The calibration angles below are calculations on
  ratings that are already in the file. Your own 1–5 competency scoring is a judgement on the
  written comments. Label which is which in the report, and never let your scoring stand in
  for a rating someone actually gave.
- **Anonymize by default.** Unless I tell you otherwise, replace every employee's real name
  with `Employee 1`, `Employee 2` and so on before you analyse anything. Build the map once and
  apply it everywhere — including names that appear *inside* written comments. People write
  things like "I worked closely with Sarah on Q3", and Sarah may never appear as a reviewee or
  a reviewer. Replace longer names before shorter ones so "Sarah Smith" doesn't leave a
  stray "Smith". Managers follow whatever I choose in Step 4. Don't show me the name map
  unless I ask.
- **Never invent a quote or an example.** Quote verbatim. If there's nothing in the data, write
  "no evidence in the data" and move on.
- **Anonymize peer quotes** — strip names, job titles, and identifying details from anything a
  peer wrote, so a quote can't be traced back to the person who wrote it.
- **No demographic guessing.** If there's no demographic column in my data, skip anything
  that would need one. Never infer gender, ethnicity, or age from a name.
- **Every flag is "flag for human review."** You surface the pattern; we decide what it means.
  A manager who rated everyone at the top may have a genuinely exceptional team. Say what the
  numbers show and what question it raises — never a verdict about a person's character or
  competence.
- **Small teams get numbers, not flags.** A manager with fewer than three rated reports can't
  show a pattern. Show their numbers, mark them "too few to flag", and leave them out of the
  top findings.

## Step 1 — The review data

Ask me to upload or paste the reviews. Any mix of self-reviews, manager reviews, peer/360
feedback, and upward feedback. Any format — spreadsheet, doc, PDF, or pasted text.

Work out the structure yourself: who's being reviewed, who wrote each response, which type of
rater they are, which fields are numeric ratings versus written comments, and which comment
goes with which rating. Work out the rating scale — 1–5, 1–10, or labels like "Meets /
Exceeds". If it's labels, map them to an ordered scale and show me the mapping. If it's
genuinely ambiguous after a real attempt, ask me **one** targeted question. Don't interrogate
me.

Then tell me in two lines what you found: how many people, how many reviews of each type,
which scale, and which rating you'll treat as "the overall rating" for calibration.

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
themselves — the manager review's author is usually the reporting manager — and **say clearly
in the report that you inferred it**.

Then show me the breakdown before you go further: *"I've sorted 51 people into 4 Leadership,
12 Managers, 35 ICs. 11 people write manager reviews; 2 of them have fewer than three reports.
Confirm or correct before I run the analysis."* Fixing this now is cheap. Fixing it after the
report is built is not.

## Step 3 — Our values and competencies (optional)

Ask for our company values and role expectations. If I only have one of the two, take it and
carry on. If I have neither, use these six and say in the report that defaults were used:

**Craft** (quality of their actual discipline) · **Delivery** (turning work into shipped outcomes) ·
**Collaboration** (how they work with people around them) · **Influence** (how far their effect
reaches beyond their own work) · **Ownership** (following through, owning mistakes) ·
**Judgement** (decision quality under uncertainty)

Weight them equally unless I say otherwise.

## Step 4 — The format, and manager names

Ask me two things in one message:

1. **Who is this for?**
   - **A document** — if it's going to leadership. Something they read top to bottom and can
     forward.
   - **An interactive page** — if I want to filter by team or manager during the calibration
     meeting. In Claude this is called an artifact, and it opens next to the chat.
2. **Named or labelled managers?** The manager list is meant to be acted on, so it's usually
   more useful with real manager names. Default is `Manager A`, `Manager B` unless I say to keep
   names. Employees stay anonymized either way unless I say otherwise.

If you can produce neither a document nor a page, say so and output markdown here.

## The analysis

### Part A — Calibration angles (calculated on the file)

Run each of these as a calculation on the overall ratings in the file. For each one, show the
table, then the plain-words finding underneath. Print the threshold you used next to each
angle so we can argue with it.

1. **Distribution.** Company-wide count and percentage at each point on the scale. Then the
   same per manager and per cohort. Plain words: is the scale being used, and where does it
   bunch?

2. **Everyone at the top.** Per manager: number of rated reports, and the share rated at the
   highest point on the scale. Flag a manager when **every** report got the top rating. Mark
   "watch" when three quarters or more did. Compare with the company-wide share at the top, so
   the finding reads "6 of 6, against 14% company-wide".

3. **No differentiation.** Per manager: how many distinct rating values they used, and the
   spread (standard deviation). Flag a manager who gave **every** report the same rating,
   whatever that rating is. Mark "watch" when one value covers four in five reports or more.
   A manager with eight reports who used one number hasn't made a distinction between any of
   them — that's the question for calibration.

4. **Lenient and severe managers.** Per manager: their average rating minus the average of
   everyone else's ratings. Flag a gap of half a point or more on a 5-point scale (scale it for
   others — a full point on 1–10). Put the numbers side by side and remember small teams are
   noisy: say how many reports each average rests on.

5. **Compression.** The share of all ratings that land on the two middle values of the scale,
   company-wide and per manager. Flag when it's above 80%. That means the scale isn't
   separating anyone.

6. **Extreme ratings without evidence.** Take every rating at the **top** and **bottom** of the
   scale. For each, find the written justification attached to it and record:
   - its word count (calculated);
   - whether it contains at least one specific example — a named project, deliverable,
     event, date, number or observed behaviour (a judgement — quote the example you found, or
     write "none").
   Classify each as **Evidenced** (has a specific example), **Thin** (comment exists, no
   specific example) or **None** (no comment at all). Report the counts for top ratings and
   bottom ratings separately, per manager and company-wide, and list every Thin and None case.
   A top or bottom rating is the one most likely to be challenged in calibration, and the one
   that most needs a reason on paper.

7. **Employee–manager alignment.** For everyone with both a self-rating and a manager rating:
   gap = self minus manager. Flag a gap of one point or more on a 5-point scale (scaled for
   others), in either direction. Report:
   - the count and list of people over the threshold, split into "rated themselves higher"
     and "rated themselves lower";
   - per manager: average gap, and how many of their reports are over the threshold.
   A manager whose reports all rate themselves well above the manager's rating usually points
   to expectations that were never made clear. That's a conversation with the manager, not
   with each employee.
   If peer or upward ratings exist, run the same check for manager vs peer average, and flag
   where the manager is the outlier.

8. **Completeness.** Per manager: reports with no manager review, and reviews with a rating
   but no comment. Missing reviews skew every other number for that team, so say so.

### Part B — Reading the written feedback (judgement, labelled as such)

1. **Score each person on each competency, 1–5**, and quote the specific evidence you scored
   it on. A score with no quote behind it isn't a score.
2. **Weighted overall score** per person. Average per cohort, and per leader's team. Where your
   score and the rating in the file disagree by a point or more, list it — it often marks a
   rating the comments don't support.
3. **Cluster the written feedback into themes** — Start / Stop / Continue. A theme needs at
   least two different raters saying it, or it's an opinion, not a theme.
4. **Bias pass on the language.** Flag these types, and print the definition next to each flag so
   we can learn to spot them ourselves:
   - *Halo / horn* — one strong impression colouring every other rating for that person.
   - *Vague positive* — praise with no specifics. Often hides an unwillingness to say anything real.
   - *Recency* — the whole review is about the last few weeks.
   - *Coded language* — words applied to some people and not others: "abrasive", "emotional",
     "not a culture fit", "needs polish".
   - *Rater variance* — one person's ratings scattered far wider than everyone else's.
5. **Promotion readiness** — Yes / Not yet / No, with the evidence. Two hard rules:
   - If you have evidence covering less than 60% of a person's competencies, the answer is
     **"Not yet"**. Never "Yes" on thin data.
   - The promotion-ready shortlist is capped at **15% of total headcount**. No exceptions. If
     more people qualify mechanically, rank by strength of evidence and cut. Say in the report
     how many qualified versus how many made the list.
   - Anyone whose top rating was classified Thin or None in Part A can't be on the shortlist
     on that rating alone. Say so next to their name.
6. **Development plan** — two to four concrete actions per person. Things they'd actually do,
   not "improve communication".

### Part C — Pick the top five findings

From everything in Parts A and B, pick the five findings that matter most for calibration.
Rank by how many people the finding affects and how far it moves ratings — a manager rating
eight people at the top beats one odd comment. Each finding gets: a one-line headline, the
numbers behind it, one or two sentences in plain words, and who to talk to about it.

### Part D — The manager list

One entry per manager who has at least one flag or "watch" from Part A, ordered by how much
needs discussing. For each:

- the flags, each with its numbers ("all 6 reports rated 5/5; company-wide 14%");
- the top or bottom ratings they gave with Thin or None evidence;
- their reports' self vs manager gaps, if over the threshold;
- **the question to ask them before calibration** — one or two, specific and neutral. "What
  separates your strongest and weakest report this cycle?" — not "why are you so lenient?"

Then list the managers with no flags in one line, so nobody wonders whether they were checked.

## The report

Build it in the format I chose in Step 4.

- **Document:** structured top to bottom as below, with tables and short paragraphs. Readable
  printed or forwarded.
- **Interactive page:** one self-contained page with every number embedded. Filters for team,
  manager, cohort and flag type that update every table at once. Sortable tables. The top five
  findings and manager list stay visible at the top. Works offline, no external data.

Structure, top to bottom:

1. **Header** — company, review cycle, date generated, number of people and reviews.
2. **Top five findings** — from Part C. This is what gets read, so it comes first.
3. **The manager list** — from Part D. Who to talk to before calibration, and why.
4. **Executive summary**, 300–500 words: two paragraphs on the whole company (rating
   distribution, how well the scale is used, top three strengths, top three risks, the single
   most important recommendation). Then one short paragraph per Leadership person on their
   area — average rating, biggest calibration concern, biggest risk.
5. **Calibration detail** — one subsection per angle in Part A, in order: threshold, table,
   plain-words finding. Per-manager table with every manager as a row: reports, average, gap to
   company, spread, distinct values used, % at top, % at bottom, top/bottom ratings without
   evidence, average self vs manager gap, missing reviews, flags.
6. **Cohort overview** — for each of the three cohorts: headcount, mean rating, spread, the top
   10% and bottom 10% by name and rating, and one sentence on what the cohort looks like.
7. **Promotion-ready shortlist** — max 15% of headcount. Per row: name, cohort, role, the single
   strongest piece of evidence (a verbatim quote where possible), the most-cited development
   area, overall score, and how much of their competency set you actually had evidence for.
8. **Language and bias flags** — from Part B, one table grouped by flag type, with the
   definition printed once at the top of each group. Columns: type, what it means, who it
   concerns, the comment.
9. **Person by person** — grouped by cohort, Leadership first, then Managers, then ICs. Sort by
   rating within each cohort. Inside the IC group, sub-group by their manager. For each person:
   rating in the file, your overall score, promotion verdict and rationale, development plan,
   competency scores with evidence, themes, self-vs-manager-vs-peer gaps, flags. Leave out any
   section you have no data for — never print "no data" placeholders.
10. **Methodology footer** — the scale and any label mapping, every threshold used, the weights,
    where the data came from, which numbers are calculated and which are your judgement,
    whether default competencies were used, whether the org structure was given or inferred,
    which managers were too small to flag, and what to be careful about when reading this.

## Finish with

Three sentences: the headline finding, the biggest calibration risk, and one thing that's going
well. Then tell me which parts of the analysis were thin on evidence, so I know what not to lean
on in a calibration or promotion conversation.
