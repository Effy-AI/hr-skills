# HR Prompts

Ready-to-run prompts for HR and people leaders. Paste one into Claude or ChatGPT and answer the
questions it asks.

No installation, no account, no tooling. Each prompt is a single file you copy and paste.

Built by [Effy AI](https://effy.ai).

## Prompts

| Prompt | What it does | Time |
| --- | --- | --- |
| [Document our onboarding process](prompts/document-onboarding.md) | Works out how onboarding actually runs at your company — from your email history and a short interview — then writes it up as a checklist per owner: HR, hiring manager, buddy, IT, new hire. | 15–20 min |

## How to use one

**Copy and paste.** Open the prompt, copy the whole file, paste it into a new Claude or ChatGPT
conversation. This is the reliable way.

**Or paste the link.** Some models will fetch a URL and follow what's in it:

```
Follow the instructions at this link:
https://raw.githubusercontent.com/Effy-AI/hr-skills/main/prompts/document-onboarding.md
```

This is quicker but less dependable — depending on the model and your settings it may summarise
the page instead of running it, or not fetch it at all. If it does anything other than start
asking you questions, fall back to copy and paste.

## What to expect

The prompt does three things in order, and it will not skip ahead:

1. **Looks at what actually happened.** If it can search your email, it finds your last few
   hires and reads the threads around their start dates — especially the reminders you had to
   send, which are the best evidence of where a process breaks. If it can't search anything, it
   asks you to paste the threads in.
2. **Interviews you.** Up to ten questions, one at a time, skipping anything it already worked
   out. If your answer contradicts what it found in your email, it says so and asks which is
   right.
3. **Writes the document**, and tells you what it wasn't sure about.

## Reading the output

Nothing is presented as fact unless it is one. Every line carries a tag:

| Tag | Meaning |
| --- | --- |
| `[CONFIRMED]` | You said it, or an email shows it happening |
| `[GUESS: verify]` | Inferred from evidence — plausible but unproven |
| `[SUGGESTED]` | A standard step proposed to fill a gap, not something your company does |

The run ends with the `[GUESS]` and `[SUGGESTED]` lines collected as a list of open questions.
Work through it and you have a document that is fully `[CONFIRMED]`.

A draft with its uncertainty visible is more useful than a polished one that quietly guesses.

## Before you share the output

These prompts read your email to understand your process, which means they open offer letters
and contracts — the documents most likely to contain salary figures and ID details. Each prompt
instructs the model never to copy that into the document, and to refer to people by role and
initials rather than names.

That instruction is reliable, not infallible. **Read the document before you send it to anyone.**

## Using these with your own team

The prompts are MIT licensed. Fork the repository, edit them to match how your company actually
works, and point your team at your copy. Nothing here phones home — these are plain text files,
and Effy AI never sees your conversation or your data.

## Contributing

Open an issue or a pull request. A good prompt here:

- gathers evidence before asking questions
- asks one question at a time, and not too many
- tags what it is unsure about instead of guessing quietly
- never invents a tool, step, person, or date
- ends by handing you the open questions

## License

MIT
