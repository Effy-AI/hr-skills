---
name: review-form-optimizer
description: Audit and rewrite performance or 360 review forms (peer, upward, self, manager) from the current form plus a CSV of last cycle's answers: answer-quality stats, clearer wording, max 15 questions per form, past vs new question tables. Use when anyone wants to improve, redesign or benchmark review questions, even if they only say 'our reviews are useless'.
---

# Review Form Optimizer

Turns a company's current review form(s) and last cycle's answers into a short report. The report shows how useful the answers were and gives a rewritten form: **Past question | New question**, one table per distinct form. It was built from a real engagement: a 300-person company, 16,500 360 answers, compared against four other companies' review exports.

The reader is usually an HR or People lead. Write for them in plain language: short sentences, numbers instead of adjectives, no jargon ("halo effect" becomes "the five scores measure one overall impression").

## 1. Collect inputs

Ask once, in one message, for:

1. **The current form(s).** Any format: pasted text, doc, PDF, screenshot, or an export from the review tool. Ask for the full question text, including the descriptions under each competency and the rating scale labels. Descriptions matter: long, multi-part descriptions are a main cause of weak answers.
2. **Last cycle's answers as a CSV**, bulk export, all review types in one file or one file per type. Typical columns are Cycle, Review type, Reviewer, Reviewee, Topic, Question, Answer, Score. Anonymised reviewer names are fine.
3. **Context:** headcount, which review types they run (peer, upward, self, manager), the main language people answer in, and whether managers and individual contributors get different forms.

If no CSV arrives, say that without answers you can only review the wording, then continue: skip steps 3–4 and say so in the report. If only the CSV arrives, rebuild the form from the Question/Topic columns and the Score↔Answer label pairs, and say the descriptions may be incomplete.

Self and manager forms are often pasted as filled-in examples. Extract the questions from them, and use the answers as qualitative evidence: repetition, "see above", "as I mentioned before", topics squeezed into the wrong question. Never quote a named person's answer in the report.

## 2. Inventory the question sets

- One question set per distinct form: review type × cycle, and IC vs manager variants. If two forms have identical questions, treat them as one and say which forms it covers.
- For each set, list every question in order with its full original text, its type (rating / open / choice), and its scale labels. In a CSV, labels come from the Answer value on rows that have a Score.
- Flag template issues while you're there: an "explain your rating" box with no rating above it, the same generic text repeated under N topics, or one question appearing in two sections.
- Count questions per form. Over 15 is a finding by itself.

## 3. Analyse the answers

Write the script at the end of this file to the scratchpad and run it on each CSV: `python3 -I analyze_reviews.py <file.csv> > stats.json`. It maps common header names automatically. If a column is missing, check `columns_used` in the output and fix the alias list.

It reports, per review type:

| Signal | What it tells you |
| --- | --- |
| forms, reviewers per reviewee, % reviewees with fewer than 3 reviewers | coverage and anonymity risk |
| rating distribution and labels | whether the scale is used or compressed (e.g. 94% at 3+) |
| `same_score_everywhere_pct` | forms giving one score to every competency: competencies aren't distinguished |
| `all_top_score_pct`, and the same split by reviewer count | blanket top scores; whether they rise when the group is small (anonymity) |
| `mean_inter_item_correlation` | over ~0.5 means the competencies measure one overall impression (halo) |
| spread of `mean_by_question` | a spread under ~0.3 points means the ratings barely differ |
| per open question: median words, % under 10, % 30+, non-answer %, example % | depth and evidence of each question |
| low-visibility mentions, dash-only answers | reviewers rating people they barely know; form fatigue |

Then read the answers yourself. Numbers say how long answers are, not whether they help. For each open question, read 15–20 answers at random plus the `rich` and `weak` samples, and judge:

- **Specific:** does it name a situation, project, result or behaviour?
- **Actionable:** could the person act on it next month?
- **Fatigue:** "same as above", answers copied between boxes, quality falling in later questions.
- **Answering the wrong question:** strengths written under improvements, or a motivation concern written under "skills".

The "example %" signal is a keyword heuristic (numbers, months, "project", "for example"). Use it to compare questions, not as a precise rate.

### Reference ranges

From five companies' review exports (anonymised, about 37,000 answers, 2025–2026). Use them as a guide and say so in the report; roles, languages and company size differ.

| Signal | Weak | Typical | Strong |
| --- | --- | --- | --- |
| Peer/upward open answers, median words | ≤15 | 20–35 | 60+ (with an example-based question) |
| Peer/upward non-answers | 30–40% | 10–25% | under 5% |
| Self-review open answers, median words | ~20 | 50–100 | 130+ |
| Forms with one score for all competencies | 25–35% | 10–25% | under 10% |
| Forms with top score on everything (peer) | 7%+ | 3–6% | under 3% |
| Same, upward | 25%+ | 10–12% | under 8% |

The question wording drives most of the difference:

- "How did this person impact your own or your team's performance? Give 1–2 examples." → median 70 words, 96% substantive.
- "What's an area you'd like to see this person improve?" → median 9 words.
- "What challenges did you face, and how did you address them?" (self) → median ~150.
- "Looking back at the expectations set last review: to what extent were they delivered?" (manager) → ~175.

### Interpretation rules (learned the hard way)

- **Test the anonymity explanation before you write it.** Compare all-top rates by reviewer-count band. In the source case, upward all-top forms were twice the peer rate, which fits anonymity. But peer all-top barely moved between 2 and 10 reviewers, so there the scale label was the cause, not anonymity. Write each cause only where the data supports it.
- **Get the denominators right.** Forms each person *received* is not forms each reviewer *wrote*. Usually each reviewer writes about 1 form; fatigue then comes from boxes per form, not forms per reviewer.
- **Recompute every benchmark you quote** from the files. Do not use a remembered number, and do not average away the weakest company without saying so.
- **Language affects word counts.** Lithuanian, Finnish and other agglutinative languages use fewer words for the same content. If 30%+ of answers are in another language, mention it, and suggest showing questions in both languages.
- **A low non-answer rate with short answers** is a depth problem, not an engagement problem. Say which one it is.
- If the user says a number ("80 forms are all top performer"), check it against the data, confirm or correct it, and give the exact figure.

## 4. Show the statistics to the user

Before rewriting anything, share a compact summary in chat so they can react:

- per form: question | median words | 30+ words | non-answers;
- rating signals: scale use, same-score forms, all-top forms (and the split by group size);
- 3–5 "what this means" lines in plain words.

Ask nothing unless a choice is genuinely theirs. If they're unattended, continue.

## 5. Diagnose the wording

Check every current question against these patterns. Each one is a reason to rewrite.

| Pattern | Why it hurts | Fix |
| --- | --- | --- |
| One rating covers 4–6 behaviours in a 60–80 word description | reviewers can't tell what they're rating, so they give one score to everything | one observable behaviour per item, one sentence |
| Peers rate on performance labels (Meets / Exceeds / Top Performer) | only the manager knows the role's expectations; peers pick the middle or the top | frequency scale: Rarely · Sometimes · Consistently · Almost always · Role model · Can't assess |
| No "Can't assess" | people rate colleagues they barely know ("we rarely work together") | add it to every peer/upward rating |
| "Explain your rating" after every rating | the most boxes for the least content; "see above", dashes | one example box: "Pick the rating you feel strongest about and describe a situation that shows it" |
| "What are their strengths? / Where could they improve?" | gets general praise and "nothing" | ask for a real situation (Impact) and one change (start / stop / do differently) |
| Self form: does well / improve / skills / growth goals all overlap | people repeat themselves | merge into distinct questions: results, what went wrong, next year, direction |
| No anchor to the period's goals | ratings float free of what was agreed | "How would you rate your performance against the goals set for this period? What drove that result?" |
| No place for misses, motivation or workload | managers bury concerns in the wrong box | explicit "what went wrong"; manager-only motivation/support question |
| Engagement items in a performance review ("How well does the company value me?", fixed choice) | one click, no reason, nobody follows up | move to the engagement survey, or replace with an open blockers question |
| Overall rating defined differently on self and manager forms, or calculated by hand | inconsistent and circular | one formula written on the form (e.g. 50% competencies / 30% goals / 20% 360), set by the company; no self overall rating |
| Goal/OKR % turned into bucket ratings | cliffs (68% = 3, 70% = 4) | rate performance against goals on the expectations scale and comment on what was missed |
| One form for every role | the manager has to average strong and weak areas into one score | per-area rating ("main areas of the role"), or IC vs manager variants |
| Upward results shown with 1–2 reviewers | not anonymous, so scores inflate | minimum 3 reviewers before results show |

## 6. Rewrite

Principles:

- **Max 15 questions per form.** Aim for 8–10 per peer/upward form (about 10 minutes). If you offer a bank for self/manager, give up to 20 to choose from and say "pick 8–10".
- **Keep the competency names where you can** so results compare year over year. Say so when a change breaks the trend (e.g. replacing Interpersonal with Trust on the upward form).
- **Scales:** frequency scale + Can't assess for peer and upward. Expectations scale (Below / Meets / Exceeds expectations) for ratings that exist only in self and manager reviews. Note that a 3-point scale pushes everyone to "Meets"; offer "Far exceeds" if they need to separate strong performers.
- **Align wording across forms.** IC self-review items 1–5 use the exact peer-form wording in first person; manager self-review items 1–5 use the upward-form wording. That lets the person compare their view with how others see them. The manager review asks the same questions about the employee as the self-review, in the same order.
- **Every rating asks for one example. Every open question asks for a real situation.**
- **Put sensitive items in manager-only fields** (attrition risk, motivation concerns), so they aren't written where the employee reads them.
- Suggest platform features (AI follow-up questions, reviewer minimums) only as "if your tool supports it".

Proven question library (adapt the wording to the company's terms):

**Peer (IC):** Analytical thinking: breaks down complex problems and reaches a clear conclusion without unnecessary delay · Communication: tells me about delays and changes that affect my work before I have to ask · Working relationships: when we disagree, the conversation stays respectful and useful · Reliability: delivers what they promise on time, or warns early when that will change · Expertise: I would go to them for advice in their area · Example (one box) · Impact: describe one time this year this person made a real difference to your work or team; what did they do? · One change: the one thing they could start, stop or do differently that would help you most.

**Upward:** Decisions: makes sound decisions on complex problems and explains why · Priorities: makes priorities clear, especially when they change · Feedback: gives me feedback specific enough to act on · Planning: plans the team's work so deadlines are realistic and met · Trust: I can disagree or raise a concern without worrying about consequences · Keep (with an example) · Change: one thing that would help you do your best work · Learning (optional): what have you learned from your manager this year?

**Self/manager (IC | manager variant):** Performance against goals · Main areas of the role | People leadership · Results (2–3, what you did, what changed) | Team results and your part · What went wrong and what you'd do differently · Impact on others | Growing people · One change you expect colleagues to ask for | Change you expect your team to ask for · Feedback taken from last cycle | Keep · Ownership: a problem solved unasked | Hard conversations · Ways of working (process, tool, AI) | Hiring and onboarding · Collaboration with other teams · Next year: 1–2 skills and support needed · Direction in 1–2 years · Blockers · Manager-only: Motivation | People risks.

## 7. Output

Default to a shareable document (a Docs-type artifact if available, otherwise a well-formatted .md or .docx), exportable to PDF. Structure:

1. **Summary:** 3–4 lines on what's wrong and the 3 changes.
2. **What the last cycle's data shows:** numbered findings, each with its number and plain meaning (blanket top scores, same-score forms, answer length vs reference ranges, the question-level table), then "What this means" bullets. Skip this section if no CSV was provided.
3. **Peer and upward: new questions.** Why the scale changes (short), other changes as bullets, then one table per form.
4. **Self and manager: new questions.** What to fix (bullets with evidence), then the table(s).
5. **Next steps:** 3–4 numbered actions, including how to check next cycle (longer answers, fewer non-answers, fewer same-score forms).
6. One-line note that comparisons use anonymised data from other companies.

**The core table, one per distinct form:**

| Past question (cycle) | New question |
| --- | --- |
| **Rating scale:** the old labels | **Rating scale:** the new labels |
| **Analytical thinking (rating):** the full original description, verbatim | **Analytical thinking:** one-sentence behaviour |
| **Rating explanation (asked 5 times):** full original text | **Example (one box):** … |
| — | **New item:** … (a dash means newly added) |
| **Old item:** full text | Removed. Reason, and where its content went. |

Rules for the table: keep the past text verbatim with its descriptions, so the reader sees the contrast. Account for every past question (rewritten, merged or removed). Put the scale row first. Bold the label at the start of each new question.

For self and manager banks with IC and manager variants, a two-column **Individual contributors | People managers** table with numbered rows works better. Put the shared (peer/upward-aligned) items first, add a "Scales" row at the top, and tag manager-only items.

If forms differ by review type, IC vs manager, or cycle, produce one table per distinct question set. Don't make one for duplicates.

## 8. Before you hand it over

- Re-run or spot-check every number in the report against `stats.json`.
- Count questions in each new form (≤15) and check every past question is accounted for.
- No names of individual employees, reviewers or quoted people. Other companies appear only as anonymised references, never by name.
- Plain language: the summary is under 80 words and nothing needs an HR-research vocabulary to read.
- In the chat reply, list anything the user should decide or verify: trend-breaking changes, the 3-point-scale trade-off, features their tool may not have, benchmark caveats.

## Analysis script

```python
import sys, re, json
import warnings
import pandas as pd
warnings.filterwarnings("ignore")

# Map common export headers to canonical names (Effy export headers are the defaults).
ALIASES = {
    "cycle": ["Cycle", "Review cycle", "Campaign"],
    "type": ["Review type", "Relationship", "Reviewer type", "Form"],
    "reviewer": ["Reviewer", "Reviewer email", "Author"],
    "reviewee": ["Reviewee", "Reviewee email", "Employee", "Subject"],
    "topic": ["Topic", "Competency", "Section"],
    "question": ["Question", "Question text", "Prompt"],
    "answer": ["Answer", "Response", "Text answer", "Comment"],
    "score": ["Score", "Rating", "Numeric answer"],
}
NON_ANSWER = (r"^(-+|\.+|/|n/?a|no|none|nothing|not really|not sure|all good|nėra|neturiu|nieko|"
              r"viskas gerai|нічого|немає|ничего|нет)\b|nothing to add|no comments?|can'?t think|"
              r"see above|said above|as above|as mentioned|jau anksčiau|sunku pasakyti")
EXAMPLE = (r"for example|e\.g\.|for instance|such as|when (s?he|they|we|i)\b|project|client|customer|"
           r"meeting|launch|deadline|last (month|quarter|year)|\b(q[1-4]|jan|feb|mar|apr|may|jun|jul|aug|"
           r"sep|oct|nov|dec)\w*\b|\d")
LOW_VIS = (r"don'?t work (closely|much|together)|rarely work|limited interaction|haven'?t worked|"
           r"not enough (context|interaction|information)|hard to (say|evaluate|judge)|can'?t (evaluate|assess)")


def pick(df, key):
    for c in ALIASES[key]:
        if c in df.columns:
            return c
    return None


def words(s):
    return len(str(s).split()) if isinstance(s, str) else 0


def main(path):
    raw = pd.read_csv(path)
    cols = {k: pick(raw, k) for k in ALIASES}
    d = pd.DataFrame({k: raw[c] if c else None for k, c in cols.items()})
    d["type"] = d["type"].fillna("All") if cols["type"] else "All"
    d["cycle"] = d["cycle"].fillna("") if cols["cycle"] else ""
    d["answer"] = d["answer"].fillna("").astype(str).str.strip()
    d["score"] = pd.to_numeric(d["score"], errors="coerce") if cols["score"] else float("nan")
    d["w"] = d["answer"].map(words)
    qtext = d["question"].astype(str).str.replace(r"\s+", " ", regex=True).str.strip()
    # Same generic text (e.g. "explain your rating") can repeat under several topics: keep them apart.
    d["q"] = (d["topic"].astype(str) + " :: " + qtext) if cols["topic"] else qtext
    d["q"] = d["q"].str.slice(0, 160)
    d["form"] = d["reviewer"].astype(str) + "|" + d["reviewee"].astype(str) + "|" + d["type"].astype(str) + "|" + d["cycle"].astype(str)
    rated = d["score"].notna()
    out = {"file": path, "columns_used": cols, "rows": len(d), "by_type": {}}

    for rt, g in d.groupby("type"):
        r = g[rated.loc[g.index]]
        o = g[~rated.loc[g.index]].copy()
        o["non"] = o["answer"].str.lower().str.contains(NON_ANSWER, regex=True) | (o["w"] < 4)
        o["ex"] = o["answer"].str.contains(EXAMPLE, case=False, regex=True)
        o["lowvis"] = o["answer"].str.contains(LOW_VIS, case=False, regex=True)
        t = {
            "forms": g["form"].nunique(),
            "reviewees": g["reviewee"].nunique(),
            "reviewers": g["reviewer"].nunique(),
            "reviewers_per_reviewee_median": float(g.groupby("reviewee")["reviewer"].nunique().median()),
            "reviewees_with_lt3_reviewers_pct": round(float((g.groupby("reviewee")["reviewer"].nunique() < 3).mean() * 100), 1),
        }
        if len(r):
            top = r["score"].max()
            pf = r.groupby("form")["score"].agg(["min", "max", "count", "std"])
            pf = pf[pf["count"] >= 3]
            t["ratings"] = {
                "scale_max": float(top),
                "distribution_pct": (r["score"].value_counts(normalize=True).sort_index() * 100).round(1).to_dict(),
                "labels": r.groupby("score")["answer"].agg(lambda s: s.value_counts().index[0]).to_dict(),
                "forms_rated": len(pf),
                "same_score_everywhere_pct": round(float((pf["min"] == pf["max"]).mean() * 100), 1) if len(pf) else None,
                "all_top_score_forms": int(((pf["min"] == top)).sum()),
                "all_top_score_pct": round(float((pf["min"] == top).mean() * 100), 1) if len(pf) else None,
            }
            means = r.groupby("q")["score"].agg(["mean", "size"]).round(2)
            t["ratings"]["mean_by_question"] = means.sort_values("size", ascending=False).head(15)["mean"].to_dict()
            wide = r.pivot_table(index="form", columns="q", values="score", aggfunc="first")
            if wide.shape[1] >= 3:
                c = wide.corr().values
                n = c.shape[0]
                vals = [c[i, j] for i in range(n) for j in range(i + 1, n) if pd.notna(c[i, j])]
                t["ratings"]["mean_inter_item_correlation"] = round(sum(vals) / len(vals), 2) if vals else None
            # all-top rate by number of reviewers the reviewee had (anonymity check)
            nrev = g.groupby("reviewee")["reviewer"].nunique()
            pf2 = pf.copy()
            pf2["n"] = [nrev.get(f.split("|")[1], 0) for f in pf2.index]
            pf2["band"] = pd.cut(pf2["n"], [0, 2, 4, 1000], labels=["1-2", "3-4", "5+"])
            t["ratings"]["all_top_pct_by_reviewer_count"] = (
                pf2.groupby("band", observed=True).apply(lambda x: round(float((x["min"] == top).mean() * 100), 1)).to_dict())
        if len(o):
            q = o.groupby("q").agg(
                answers=("w", "size"), median_words=("w", "median"), mean_words=("w", "mean"),
                under10_pct=("w", lambda s: (s < 10).mean() * 100), over30_pct=("w", lambda s: (s >= 30).mean() * 100),
                non_answer_pct=("non", lambda s: s.mean() * 100), example_pct=("ex", lambda s: s.mean() * 100),
            ).round(1).reset_index()
            t["open_questions"] = q.sort_values("answers", ascending=False).to_dict("records")
            t["open_overall"] = {
                "answers": len(o), "median_words": float(o["w"].median()),
                "over30_pct": round(float((o["w"] >= 30).mean() * 100), 1),
                "non_answer_pct": round(float(o["non"].mean() * 100), 1),
                "example_pct": round(float(o["ex"].mean() * 100), 1),
                "low_visibility_mentions": int(o["lowvis"].sum()),
                "dash_only_answers": int(o["answer"].str.fullmatch(r"[-./]+").sum()),
            }
            t["open_examples"] = {
                "rich": o[(o["w"] >= 50) & o["ex"]]["answer"].str[:300].head(3).tolist(),
                "weak": o[o["non"] & (o["w"] > 0)]["answer"].value_counts().head(10).to_dict(),
                "low_visibility": o[o["lowvis"]]["answer"].str[:200].head(3).tolist(),
            }
        out["by_type"][str(rt)] = t
    print(json.dumps(out, indent=1, ensure_ascii=False, default=str))


if __name__ == "__main__":
    for p in sys.argv[1:]:
        main(p)
```

The `weak` and `low_visibility` samples can contain employee names. Use them to understand patterns; don't paste them into the report.
