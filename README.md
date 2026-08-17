# HR Skills

A library of Claude Agent Skills for HR and people leaders at small and mid-sized companies.
Built by [Effy AI](https://effy.ai).

Most people processes at a 30–500 person company are undocumented. They live in one person's
head and only surface when something is late. These skills turn that into documentation you can
hand to someone else — by reading the evidence of what actually happened, asking you about the
rest, and marking clearly which parts they are unsure about.

## Skills

| Skill | What it does | Writes to |
| --- | --- | --- |
| [`document-onboarding`](skills/document-onboarding/SKILL.md) | Documents your real onboarding process, split by owner (HR, hiring manager, buddy, IT, new hire). Reads your docs and recent-hire email evidence, interviews you, then writes. | `processes/onboarding.md` |

## Install

Each skill is a self-contained folder. Copy the ones you want into your skills directory.

**For all your projects:**

```bash
git clone https://github.com/Effy-AI/hr-skills.git
cp -r hr-skills/skills/document-onboarding ~/.claude/skills/
```

**For one project only:**

```bash
cp -r hr-skills/skills/document-onboarding .claude/skills/
```

Restart Claude Code, or run `/reload-plugins`. The skill is then available as
`/document-onboarding`, and Claude will also invoke it on its own when you describe the task.

**To try it without installing:**

```bash
claude --plugin-dir /path/to/hr-skills
```

This loads every skill in the library for that session only. It works because a skill library
and a plugin root are the same layout — see below.

## The Claude-HR folder

Every skill reads from and writes to one folder. Connect it in Cowork, or open it as your
working directory in Claude Code.

```
Claude-HR/
├── ai-usage-policy.md     # read first by every skill; governs naming and data handling
├── company/               # org structure, roles, locations, tooling
└── processes/             # the documented processes; skills write here
```

If you don't have one, create the folders and copy the skill's
[`ai-usage-policy-starter.md`](skills/document-onboarding/reference/ai-usage-policy-starter.md)
in as `ai-usage-policy.md`. Skills offer to do this for you if the file is missing.

Full contract:
[`claude-hr-folder.md`](skills/document-onboarding/reference/claude-hr-folder.md).

## How these skills handle uncertainty

Nothing is stated as fact unless it is one. Every line in a generated document carries a tag:

| Tag | Meaning |
| --- | --- |
| `[CONFIRMED]` | You said it, or an email shows it happening |
| `[GUESS: verify]` | Inferred from evidence — plausible but unproven |
| `[SUGGESTED]` | A standard step proposed to fill a gap, not something your company does |

Each run ends with the `[GUESS]` and `[SUGGESTED]` lines collected as open questions. The output
is a draft with its uncertainty visible, not a finished artifact pretending to be authoritative.

## Privacy

These skills read your email and files to understand your processes. They run wherever Claude
runs — nothing is sent to Effy AI. They are instructed never to write ID numbers, bank details,
home addresses, or salary figures into any document, and to refer to people by role and
initials.

Review generated documents before sharing them. The skills are careful, not infallible.

## Repository layout

```
.
├── skills/                          # the library — one folder per skill
│   └── document-onboarding/
│       ├── SKILL.md
│       └── reference/               # files this skill needs, travel with it
├── docs/
│   ├── skill-template.md            # starting point for a new skill
│   └── convert-to-plugin.md         # how to ship this as a plugin
└── scripts/validate-skills.py       # frontmatter and naming checks
```

`skills/` sits at the repository root on purpose. That is the same place Claude Code looks for
skills inside a plugin, so this library is already plugin-shaped: `claude --plugin-dir .` loads
it today, with no manifest. Turning it into a distributable plugin means adding two small files
and changing nothing else — see [docs/convert-to-plugin.md](docs/convert-to-plugin.md).

Each skill folder is self-contained, including the files it depends on. That is what makes
`cp -r skills/document-onboarding ~/.claude/skills/` work as an install.

## Development

```bash
python3 scripts/validate-skills.py     # frontmatter, naming, self-containment
claude --plugin-dir .                  # load every skill for one session
/reload-plugins                        # pick up edits without restarting
```

CI runs the validator on every push and pull request. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT
