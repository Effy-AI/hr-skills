# Course structure — proposal

A course built on the eight prompts in this repo. Not one linear path: **one spine for the HR
leader who takes the course, plus two short tracks they hand to other people.** The repo already
splits three ways (HR / managers / everyone) — a single numbered sequence would force a manager
prompt into an HR leader's lesson 3 and lose both.

---

## The spine — for the HR or people leader (8 lessons)

| # | Lesson | Prompt | Output they keep | Time |
| --- | --- | --- | --- | --- |
| 0 | How these work, and a 2-minute proof | `prep-for-a-1-1.md` | Nothing — just proof the method works | 10 min |
| 1 | Document how onboarding actually runs | `document-onboarding.md` | `processes/onboarding.md` | 20 min |
| 2 | Run it for one real hire | `build-an-onboarding-plan.md` | Per-hire plan pushed to their tools | 10 min |
| 3 | Set up your review cycle | both review prompts | Two prompts edited to match their form | 20 min |
| 4 | Roll it out without an "AI initiative" | — | Cycle announcement + two handout tracks sent | 15 min |
| 5 | Read the cycle | `analyze-review-cycle.md` | Leadership report | 30 min |
| 6 | Build the ladder people asked for | `build-a-career-track.md` | One function's competency matrix | 40 min |
| 7 | Fork it and make it yours | — | Their own edited copy of the repo | 20 min |

**Lesson 0 opens with the 2-minute prompt on purpose.** A course whose first exercise costs 20
minutes loses people before they've seen anything work. `prep-for-a-1-1` is the cheapest proof
in the repo, and an HR leader has 1:1s of their own to prep.

**Lessons 3 and 4 are the ones that don't exist yet.** They're not prompts, they're the ten
minutes of `SECTION 2` editing plus the rollout note already buried in the README. That editing
step is the whole difference between a demo and a review done in 15 minutes, and right now it's
a paragraph most people will skim past. Given a lesson of its own, it gets done.

## Track A — hand to managers (3 lessons)

Sent by HR, not taken by HR. Sequence matters less; each stands alone.

| # | Lesson | Prompt | Time |
| --- | --- | --- | --- |
| A1 | Prep for your next 1:1 | `prep-for-a-1-1.md` | 2 min |
| A2 | What your 1:1 notes have been telling you | `find-themes-in-1-1-notes.md` | 10 min |
| A3 | Draft your review of a direct report | `draft-a-manager-review.md` | 15 min |

## Track B — hand to everyone (1 lesson)

| # | Lesson | Prompt | Time |
| --- | --- | --- | --- |
| B1 | Draft your self-review | `draft-a-self-review.md` | 15 min |

---

## Structure of a single lesson doc

Same seven sections every time. Predictable beats clever — people skim to the part they need.

```markdown
# Lesson N — <verb-first title>

**Time:** X min · **You need first:** <prior lesson output, or "nothing">
**You'll finish with:** <the one artifact, named as a filename or a thing>

## Why this one
Three or four sentences. The specific failure it prevents, not the category of value.
No theory, no "in today's fast-moving workplace".

## Before you start
What to have open or gathered: connectors, files, the last N hires, the review form.
The prompt asks for these anyway — gathering them first is what makes the run short.

## Run it
The copy-paste block, verbatim from the prompt file. Plus one line on what should happen
in the first 30 seconds, so they can tell a working run from a summarising one.

## What good looks like
A real excerpt of real output. Redacted, five to fifteen lines, not a full document.
This is the section that carries the lesson — most people learn the standard by seeing it.

## Where it goes wrong
Two or three named failure modes, each with the fix. Drawn from the prompt's own
weak points, not generic AI caveats.

## Make it yours
The specific edits worth making before you run it again — the SECTION 2 swap, the
skeleton lines, the tag rules. Ends with: this file is yours, edit it.

## Next
One line. What the output of this lesson unlocks.
```

**"What good looks like" is the section that will decide whether the course works.** Everything
else is scaffolding around a prompt they could have found in the repo. A worked example with
real output is the only part they can't get by reading the file.

---

## Two holes worth deciding on before you build this

**The lifecycle has gaps.** Eight prompts cover onboarding, 1:1s, reviews and career tracks —
nothing for hiring, interviewing, or offboarding. If the course is sold as "run your people
processes with AI", the missing pieces will be the first thing people ask about. Either narrow
the promise, or accept that lessons on those topics need prompts that don't exist yet.

**A course implies completion, and this repo doesn't have an ending.** Lessons 1–2 are once-ever,
3–5 are once-a-cycle, A1 is weekly. A learner who finishes lesson 7 has no reason to return.
Worth deciding now whether this is a course you complete or a set of playbooks you return to —
because the two want different structures, and retrofitting one into the other is expensive.
