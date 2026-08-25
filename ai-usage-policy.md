# Write our HR team's AI usage policy

Help me write our HR team's AI usage policy, and save it in this folder. One page, plain
language, rules people will actually follow — not legal boilerplate nobody reads.

This is a usage policy, not a ban list. It should push adoption as much as it restricts:
the goal is a team that uses AI daily and knows exactly where the lines are.

## Step 0 — Confirm where the file will live

Check whether you have access to a connected folder named CLAUDE-HR. If you do, that's
where the final file goes. If not, ask me to either (a) create a CLAUDE-HR folder and connect it
to this chat — then wait until I confirm it's connected before saving anything — or (b) name a
different connected folder to use for all HR context and deliverables. Don't write the file
anywhere until this is settled.

## Step 1 — One question first

Ask me: where do our employees and candidates sit? US only, EU/EEA only, both, or
somewhere else. Everything downstream depends on the answer.

## Step 2 — Collect existing policies

Ask me to upload any existing company policies that could influence AI usage — employee
handbook, data protection / privacy policy, information security policy, confidentiality or NDA
terms, acceptable use policy, records retention, works-council agreements, recruiting or
background-check policies.

Read whatever I upload before interviewing me; extract only the sections relevant to data
handling, confidentiality, and technology use. If I upload nothing, say you'll proceed without
them and mark alignment as [REVIEW].

## Step 3 — Interview me

One question at a time, up to 9 questions:

- Who on the team uses Claude, and for what?
- Which account type are we on, and which other AI tools are approved alongside it?
- What do we expect people to use AI *for* — and how do we share what works (a Slack
  channel, a prompt library, a tool budget people can expense against)?
- What data may never be entered?
- When are real names allowed?
- What needs human review before it goes out, and by whom?
- How do we disclose AI use to employees and candidates?
- What do we do when something goes wrong?

Skip or shorten any question the uploaded policies already answer — confirm the answer with
me instead of asking from scratch.

## Step 4 — Write the policy

One page. Numbered rules, each with a one-line "why." Plain language, no legal boilerplate.

Start with a short header block — version, effective date, owner, and a review date six
months out — and two or three "what we expect" lines before the rules: use AI for routine
and repetitive work, share what works with the team, and remember that we outsource
tasks to AI, never responsibility — whoever ran the tool owns the output.

Cover at least:

- Paid, approved accounts only — name the approved tools, and require model-training /
  "improve the model for everyone" settings to be turned off on every account.
- Names out by default.
- A "never enter" data list: IDs, bank details, health and accommodation records, immigration
  documents, open investigations and complaints, anything privileged.
- What may be entered de-identified: ratings, survey responses, comp data, headcount.
- AI never makes employment decisions — hiring, ratings, comp, promotion, discipline,
  termination.
- Screening and candidate scoring need named approval before they happen, and any
  AI-assisted process that touches candidates or employees gets checked for biased or
  uneven outcomes before it runs, not after.
- Comp numbers come from a comp platform, never from AI.
- Anything legal or going to an employee's file gets human review.
- Policy answers must cite the policy.
- How we disclose AI use.
- Where deliverables are saved.

**Align with the uploaded policies.** Where a rule restates or extends an existing policy, name it
in the "why" (e.g. "extends our InfoSec policy §3"). Where this policy would conflict with an
existing one, don't silently pick a side — write the stricter rule, name the conflict, and mark it
[REVIEW] so the older policy can be updated.

**Ground the "why" lines in my region:**

- **US**: the EEOC holds the employer responsible for the outcome of any tool it uses; NYC
  Local Law 144, Illinois HB 3773, and Colorado SB 24-205 add notice, bias-audit, and
  impact-assessment duties; state pay-transparency laws make published ranges something
  we must defend.
- **EU/EEA**: GDPR (data minimisation, special category data, Article 22 on automated
  decisions, 72-hour breach reporting); the EU AI Act treats AI in hiring, promotion,
  termination, and performance monitoring as high risk; works-council consultation where
  required; the EU Pay Transparency Directive.
- **Both**: apply the stricter rule everywhere, and say why: a team running two standards
  eventually applies the wrong one.
- **Somewhere else**: use the general rules and mark local employment and data-protection
  law as [REVIEW] for counsel.

Mark every line that needs sign-off from legal, a DPO, or leadership with [REVIEW]. End with
an incident section — if sensitive data goes into a tool by mistake: stop the conversation,
note what data and which tool, report the same day, no blame, and add a rule so it can't
repeat — and a sign-off table.

## Step 5 — Show me the draft

When I approve it, save it as ai-usage-policy.md in the folder settled in Step 0 and confirm the
full path.
