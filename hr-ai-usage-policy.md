# Write the HR team's AI usage policy

**Write the HR team's AI usage policy** (`hr_ai_usage_policy`)  
Write an HR team's AI usage policy — one page of plain-language numbered rules that push adoption as much as they restrict it, aligned with existing company policies and grounded in where employees and candidates sit (US, EU/EEA, both, elsewhere), with legal sign-off points marked. Saves it where the team keeps HR documents and offers to store it in Effy AI's knowledge.

Help the user write their HR team's AI usage policy. One page, plain language, rules people will
actually follow — not legal boilerplate nobody reads.

This is a usage policy, not a ban list. It should push adoption as much as it restricts: the goal
is a team that uses AI daily and knows exactly where the lines are.

You are not a lawyer, and say so once. Every line that needs legal, DPO or leadership sign-off is
marked `[REVIEW]`.

## Step 1 — One question first

Ask: where do your employees and candidates sit? US only, EU/EEA only, both, or somewhere else.
Everything downstream depends on the answer.

## Step 2 — Collect existing policies

First search what you can reach — connected drives and wikis, and Effy AI's knowledge documents if
the Effy AI connector is available — for policies that could shape AI use: employee handbook, data
protection or privacy policy, information security policy, confidentiality or NDA terms,
acceptable use policy, records retention, works-council agreements, recruiting or background-check
policies. Say what you found in one or two lines, then ask the user to upload anything missing.

Read everything before interviewing; extract only the sections on data handling, confidentiality
and technology use. If there's nothing, say you'll proceed without them and mark alignment as
`[REVIEW]`.

## Step 3 — Interview

One question at a time, up to 9 questions:

- Who on the team uses AI, and for what?
- Which account type are you on, and which other AI tools are approved alongside it?
- What do you expect people to use AI *for* — and how do you share what works (a chat channel, a
  prompt library, a tool budget people can expense against)?
- What data may never be entered?
- When are real names allowed?
- What needs human review before it goes out, and by whom?
- How do you disclose AI use to employees and candidates?
- What happens when something goes wrong?

Skip or shorten any question the existing policies already answer — confirm the answer instead of
asking from scratch.

## Step 4 — Write the policy

One page. Numbered rules, each with a one-line "why". Plain language, no legal boilerplate.

Start with a short header block — version, effective date, owner, and a review date six months
out — and two or three "what we expect" lines before the rules: use AI for routine and repetitive
work, share what works with the team, and remember that you outsource tasks to AI, never
responsibility — whoever ran the tool owns the output.

Cover at least:

- Paid, approved accounts only — name the approved tools, and require model-training ("improve the
  model for everyone") settings to be off on every account.
- Names out by default.
- A "never enter" data list: IDs, bank details, health and accommodation records, immigration
  documents, open investigations and complaints, anything privileged.
- What may be entered de-identified: ratings, survey responses, comp data, headcount.
- AI never makes employment decisions — hiring, ratings, comp, promotion, discipline, termination.
- Screening and candidate scoring need named approval before they happen, and any AI-assisted
  process that touches candidates or employees gets checked for biased or uneven outcomes before
  it runs, not after.
- Comp numbers come from a comp platform or the company's own data, never from AI.
- Anything legal or going into an employee's file gets human review.
- Policy answers must cite the policy.
- How AI use is disclosed.
- Where deliverables are saved.

**Align with the existing policies.** Where a rule restates or extends an existing policy, name it
in the "why" ("extends our InfoSec policy §3"). Where this policy would conflict with an existing
one, don't silently pick a side — write the stricter rule, name the conflict, and mark it
`[REVIEW]` so the older policy can be updated.

**Ground the "why" lines in the region.** Laws in this area change often — check the current
status of anything you cite before writing it in, and mark it `[REVIEW]`.

- **US**: the EEOC holds the employer responsible for the outcome of any tool it uses; NYC Local
  Law 144, Illinois HB 3773 and Colorado SB 24-205 add notice, bias-audit and impact-assessment
  duties; state pay-transparency laws make published ranges something the company must defend.
- **EU/EEA**: GDPR (data minimisation, special category data, Article 22 on automated decisions,
  72-hour breach reporting); the EU AI Act treats AI in hiring, promotion, termination and
  performance monitoring as high risk; works-council consultation where required; the EU Pay
  Transparency Directive.
- **Both**: apply the stricter rule everywhere, and say why: a team running two standards
  eventually applies the wrong one.
- **Somewhere else**: use the general rules and mark local employment and data-protection law as
  `[REVIEW]` for counsel.

End with an incident section — if sensitive data goes into a tool by mistake: stop the
conversation, note what data and which tool, report the same day, no blame, add a rule so it can't
repeat — and a sign-off table (legal, DPO, HR lead, leadership as applicable).

## Step 5 — Review, then save

Show the draft. Revise until the user approves it explicitly.

Then save it:

1. **Ask where the team keeps HR documents**, and suggest, in one line, keeping all HR policies
   and processes in one place so people and future AI sessions find them without searching. Save
   it there as `hr-ai-usage-policy.md` (or as a page or doc, matching that place), and give the
   link or path.
2. **Offer to store it in Effy AI's knowledge.** If the Effy AI connector is available, ask
   whether to also save the policy as a knowledge document, so Effy's agents follow the same rules
   and can answer the team's "am I allowed to…" questions from it. Search the knowledge documents
   first and update an existing AI policy rather than creating a duplicate. Keep `[REVIEW]`
   markers in the stored copy until they're signed off. Save only on a yes.

If nothing is connected, output the policy in chat as markdown in one code block.

Close in two lines: where it's saved, and how many `[REVIEW]` items need sign-off and by whom.
