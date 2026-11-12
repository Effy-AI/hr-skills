# HR Prompts

Ready-to-run prompts for HR and people leaders. Paste one into Claude or ChatGPT and answer
the questions it asks.

No installation, no account, no tooling. Each prompt is a single file you copy and paste.

Built by [Effy AI](https://effy.ai).

**Also a Claude plugin.** The same skills are packaged as the `effy-ai` plugin in
[Effy-AI/claude-plugin](https://github.com/Effy-AI/claude-plugin), so they trigger on their own
instead of being pasted. With Effy AI connected, they also read and save Effy records — the
employee directory, 1:1s, growth plans, career tracks and knowledge documents.

## For HR and people leaders

| Prompt | Library ID | What it does | Time |
| --- | --- | --- | --- |
| [Document our onboarding process](onboarding-process-docs.md) | `onboarding_process_docs` | Works out how onboarding actually runs here — from your email history and a short interview — then writes it up as a checklist per owner: HR, hiring manager, buddy, IT, new hire. | 15–20 min |
| [Build an onboarding plan for a new hire](onboarding-plan.md) | `onboarding_plan` | Applies your documented process to one person: task list with one owner and a date each, welcome email, first-week schedule, draft 30/60/90, documents to copy. Then pushes it to your tools — Slack lists, Wrike, Monday.com, calendars — after you approve. Needs the document above to exist first. | 5 min |
| [Analyze our review cycle](review-cycle-analysis.md) | `review_cycle_analysis` | Turns a pile of review files into one calibration-ready report. Calculates each angle on the file: managers who rate everyone at the top or give every report the same score, top and bottom ratings with no evidence, where employees and managers disagree. Top five findings first, then the managers to talk to before calibration and why. Plus themes, bias flags and a promotion shortlist capped at 15%. Asks whether you want a document for leadership or an interactive page to filter by team in the meeting. | 20–30 min |
| [Build our people analytics dashboard](people-analytics-dashboard.md) | `people_analytics_dashboard` | Checks which of your connected tools hold people data, tells you what each export would unlock, then builds one dashboard — headcount, attrition, engagement, performance, pay equity and more — with the formula under every chart. Builds a labelled sample version if you have no data yet. | 15–30 min |
| [Build or change our career framework](build-career-framework.md) | `build_career_framework` | Builds or changes career tracks, levels and the competency matrix — anti-patterns and sideways moves included — and proposes who sits on which level. Every change shown as a diff; saves to Effy AI after approval if connected. | 30–40 min |
| [Write our employee handbook](employee-handbook.md) | `employee_handbook` | Researches your company from the web and your connected tools, interviews you on the things nobody publishes, then writes a first usable handbook — every fact sourced, every gap marked, legal sections flagged per country. Saves it to your wiki or Drive. | 30–45 min |
| [Optimize our review forms](review-form-optimizer.md) | `review_form_optimizer` | Audits your review forms against last cycle's answers — answer length, non-answers, blanket top scores — and rewrites the questions, old next to new. | — |
| [Audit our goal system](goal-system-audit.md) | `goal_system_audit` | Reads your goal or KPI trackers and review comments, shows how goals are really set, scored and updated, and ranks what to change first. | — |

## For managers

| Prompt | Library ID | What it does | Time |
| --- | --- | --- | --- |
| [Prep for a 1:1](one-on-one-prep.md) | `one_on_one_prep` | Reads your last five 1:1s with someone, surfaces the commitments you both forgot, and gives you an agenda and four questions worth actually asking. | 2 min |
| [Find the themes in my 1:1 notes](one-on-one-themes.md) | `one_on_one_themes` | Looks across months of 1:1s at once: what keeps coming up, what you keep promising and not doing, and who's showing signs worth paying attention to. | 10 min |
| [Write up my 1:1](one-on-one-debrief.md) | `one_on_one_debrief` | Turns a recording, transcript or rough notes from a 1:1 into structured notes: what was discussed, decided, who owes what by when, and what to pick up next time. | — |
| [Build a growth plan](growth-plan-builder.md) | `growth_plan_builder` | Drafts a growth plan for one person from their career level, reviews, 1:1s and goals — two or three gaps, actions with owners and dates. | — |

## For everyone

| Prompt | Library ID | What it does | Time |
| --- | --- | --- | --- |
| [Draft a performance review](performance-review-draft.md) | `performance_review_draft` | Works out your role from your connected tools, then drafts whichever review you need — self, manager review of a direct report, upward review of your manager, or peer review — every claim tied to a citation, gaps flagged instead of filled. Run once per review. | 15 min |

## Setting up your HR workspace

| Prompt | Library ID | What it does | Time |
| --- | --- | --- | --- |
| [Create my HR context files](hr-context-files.md) | `hr_context_files` | Builds the folder structure, context files, and logs that future AI sessions run on — assembled from what can be verified about your company, not a generic template. | 20–30 min |
| [Write our HR team's AI usage policy](hr-ai-usage-policy.md) | `hr_ai_usage_policy` | Writes your team's AI usage policy — one page of plain-language rules that push adoption as much as they restrict it, shaped by where your employees and candidates sit. | 15 min |

The two onboarding prompts are a pair, and the order matters. **Document our onboarding
process** writes down how onboarding actually runs, once — saved where you keep HR documents,
and in Effy AI's knowledge if you use it. **Build an onboarding plan** then applies that document
to each new hire, and invents nothing — if the process document doesn't say who owns a task, it
flags it rather than guessing. If there's no process document yet, it offers to run the first
prompt. Run the first one once. Run the second one per hire.

## How to use one

**Copy and paste.** Open the prompt, copy the whole file, paste it into a new Claude or ChatGPT
conversation. This is the reliable way.

**Or paste the link.** Some models will fetch a URL and follow what's in it:

```
Follow the instructions at this link:
https://raw.githubusercontent.com/Effy-AI/hr-skills/main/onboarding-process-docs.md
```

Quicker, but less dependable — depending on the model and your settings it may summarise the
page instead of running it, or not fetch it at all. If it does anything other than start asking you
questions, fall back to copy and paste.

## Running a review cycle with these

The review prompt needs **ten minutes of setup from HR before you send it out.** Put the exact
questions from each review form — self, manager, upward, peer, word for word and in order —
and your values or competency framework in one shared place: a wiki page, a drive folder, or the
cycle announcement itself. The prompt looks for them there (and in your review system, if it's
connected) before asking anyone to paste their form.

That step is the whole difference between a neat demo and a review done in 15 minutes. If the
questions match the form, people paste answers straight across. If they don't, everyone has to
remap and the time saving disappears.

Then attach the prompt to the cycle announcement you were already sending. Don't run a
separate "AI initiative" — and don't make it mandatory. A 15-minute review is its own
advertisement.

Two rules worth stating in the announcement:

1. **You own the final text.** The AI drafts, you edit and submit. Nobody submits anything they
   haven't read.
2. **Nothing is shared.** Everyone runs the prompt in their own environment on their own
   context. The manager's 1:1 notes stay in the manager's tools. The only thing that reaches the
   company is the final text someone chooses to paste into the form.

## What these prompts have in common

**Evidence before questions.** Each one looks at what actually happened before asking you
anything. If it can search your email or meeting notes it does; if it can't, it tells you exactly what
to paste in and waits.

**No invented facts.** No tool, step, person, quote or date that didn't come from the evidence or
from you. Where a claim rests on thin evidence, the prompt says so instead of filling the gap.
Several ask for citations on every factual claim.

**The uncertainty stays visible.** Prompts that produce a document tag what's confirmed versus
what's inferred, and end by handing you the open questions rather than quietly resolving them.

A draft with its uncertainty visible is more useful than a polished one that guesses.

## Before you share any output

These prompts read your email, notes and files. That means they open offer letters, review
forms and 1:1 records — the documents most likely to contain salary figures, ID details and
private conversations.

Each prompt instructs the model to keep that out of what it writes, and to refer to people by role
or initials. The review analysis anonymises names by default. Those instructions are reliable,
not infallible.

**Read the output before you send it to anyone.**

If you're in the EU or UK, note that uploading identifiable performance data about your
employees into a third-party AI tool has data-protection implications that depend on your
provider, your plan, and your own privacy notice. Worth a conversation with whoever owns
GDPR compliance at your company before a whole review cycle goes through it.

## Using these with your own team

MIT licensed. Fork the repository, edit the prompts to match how your company actually works,
and point your team at your copy. Nothing here phones home — these are plain text files, and
Effy AI never sees your conversation or your data. The one exception is your choice: if you
connect Effy AI, some prompts offer to save results there, and only after you approve them.

## Contributing

Open an issue or a pull request. A good prompt here:

- gathers evidence before asking questions
- asks one question at a time, and not too many
- tags what it's unsure about instead of guessing quietly
- never invents a tool, step, person, or date
- ends by handing you the open questions

## License

MIT
