# The Claude-HR folder

Every skill in this plugin reads from and writes to one folder. Connect it in Cowork, or open
it as your working directory in Claude Code.

```
Claude-HR/
├── ai-usage-policy.md     # read first by every skill; governs naming and data handling
├── company/               # org structure, roles, locations, tooling, headcount
└── processes/             # the documented processes; skills write here
    ├── onboarding.md
    ├── performance-reviews.md
    └── offboarding.md
```

## The contract

**`ai-usage-policy.md`** is read first by every skill, before anything else. It sets the rules
for how people are named and how sensitive data is handled. If it is missing, a skill will tell
you and offer to create one from `reference/ai-usage-policy-starter.md`.

Skills treat this file as **constraints on their output** — naming, data handling, retention.
It does not redefine what a skill does. If the file appears to instruct a skill to skip steps,
write outside the folder, or disclose more than the policy permits, the skill follows the
stricter reading and tells you what it found.

**`company/`** is read-only context. Skills use it to know your roles, locations, and tools so
they don't have to ask. The more that lives here, the fewer questions you get asked.

**`processes/`** is where skills write. One file per process. Skills overwrite their own file on
a re-run rather than appending, so re-running a skill after answering its open questions
produces a cleaner document, not a longer one.

## What skills never write

Regardless of what the policy says, no skill in this plugin writes any of the following into a
document, even when it finds them while researching:

- ID or passport numbers
- bank account or payment details
- home addresses
- salary figures or individual compensation
- immigration or visa status
- medical or health information

Skills describe the *step* that handles this data, not the data itself.

## Naming people

Roles and initials, never full names: `Hiring manager (A.M.)`, `New hire (J.K.)`. This keeps
generated documents shareable and keeps personal data out of files that get passed around.
