# HR Prompts

Ready-to-run prompts for HR and people leaders. Paste one into Claude or ChatGPT and answer
the questions it asks.

No installation, no account, no tooling. Each prompt is a single file you copy and paste.

Built by [Effy AI](https://effy.ai).

## For HR and people leaders

| Prompt | Library ID | What it does | Time |
| --- | --- | --- | --- |
| [Document our onboarding process](onboarding-docs.md) | `onboarding_process_docs` | Works out how onboarding actually runs here — from your email history and a short interview — then writes it up as a checklist per owner: HR, hiring manager, buddy, IT, new hire. | 15–20 min |
| [Build an onboarding plan for a new hire](onboarding-plan.md) | `onboarding_plan` | Applies your documented process to one person: task list with one owner and a date each, welcome email, first-week schedule, draft 30/60/90, documents to copy. Then pushes it to your tools — Slack lists, Wrike, Monday.com, calendars — after you approve. Needs the document above to exist first. | 5 min |
| [Analyze our review cycle](review-cycle-analysis.md) | `review_cycle_analysis` | Turns a pile of review files into one leadership report: scores with evidence, themes, calibration and bias flags, and a promotion-ready shortlist capped at 15% of headcount. | 20–30 min |
| [Build a career track](career-track.md) | `career_track_builder` | Interviews you, then builds one function's level ladder and competency matrix — including the anti-patterns and sideways moves most frameworks leave blank. | 30–40 min |

## For managers

| Prompt | Library ID | What it does | Time |
| --- | --- | --- | --- |
| [Prep for a 1:1](1-1-prep.md) | `one_on_one_prep` | Reads your last five 1:1s with someone, surfaces the commitments you both forgot, and gives you an agenda and four questions worth actually asking. | 2 min |
| [Find the themes in my 1:1 notes](1-1-themes.md) | `one_on_one_themes` | Looks across months of 1:1s at once: what keeps coming up, what you keep promising and not doing, and who's showing signs worth paying attention to. | 10 min |
| [Draft a manager review](manager-review.md) | `manager_review_draft` | Drafts your review of a direct report from your own meeting history, every claim tied to a citation. Run once per report. | 15 min |

## For everyone

| Prompt | Library ID | What it does | Time |
| --- | --- | --- | --- |
| [Draft my self-review](self-review.md) | `self_review_draft` | Drafts your self-review from six months of your own work, with citations and honest gaps instead of invented achievements. | 15 min |

## Setting up your HR workspace

| Prompt | Library ID | What it does | Time |
| --- | --- | --- | --- |
| [Create my HR context files](hr-context-files.md) | `hr_context_files` | Builds the folder structure, context files, and logs that future AI sessions run on — assembled from what can be verified about your company, not a generic template. | 20–30 min |
| [Write our HR team's AI usage policy](ai-usage-policy.md) | `hr_ai_usage_policy` | Writes your team's AI usage policy — one page of plain-language rules that push adoption as much as they restrict it, shaped by where your employees and candidates sit. | 15 min |

The two onboarding prompts are a pair, and the order matters. **Document our onboarding
process** writes `processes/onboarding.md` once, and fills gaps with suggestions you accept or
cut. **Build an onboarding plan** then instantiates that document for each new hire, and invents
nothing — if the process document doesn't say who owns a task, it flags it rather than guessing.
Run the first one once. Run the second one per hire.

## How to use one

**Copy and paste.** Open the prompt, copy the whole file, paste it into a new Claude or ChatGPT
conversation. This is the reliable way.

**Or paste the link.** Some models will fetch a URL and follow what's in it:

```
Follow the instructions at this link:
https://raw.githubusercontent.com/Effy-AI/hr-skills/main/onboarding-docs.md
```

Quicker, but less dependable — depending on the model and your settings it may summarise the
page instead of running it, or not fetch it at all. If it does anything other than start asking you
questions, fall back to copy and paste.

## Running a review cycle with these

The two review prompts need **ten minutes of setup from HR before you send them out.** Each
one ends with a `SECTION 2` holding sample review questions. Replace those with the exact
questions from your review form — word for word, in the same order they appear — and swap the
values block for your own competency framework, or delete it.

That step is the whole difference between a neat demo and a review done in 15 minutes. If the
questions match the form, people paste answers straight across. If they don't, everyone has to
remap and the time saving disappears.

Then attach both prompts to the cycle announcement you were already sending. Don't run a
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
Effy AI never sees your conversation or your data.

## Contributing

Open an issue or a pull request. A good prompt here:

- gathers evidence before asking questions
- asks one question at a time, and not too many
- tags what it's unsure about instead of guessing quietly
- never invents a tool, step, person, or date
- ends by handing you the open questions

## License

MIT
