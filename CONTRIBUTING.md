# Contributing

## Adding a skill

```bash
mkdir -p skills/my-skill
cp docs/skill-template.md skills/my-skill/SKILL.md
python3 scripts/validate-skills.py
```

Then add a row to the Skills table in `README.md`. Nothing else — there is no manifest to
register a skill in.

Test it before committing:

```bash
claude --plugin-dir .        # loads every skill in the library for one session
/reload-plugins              # pick up edits without restarting
```

## Rules that are not negotiable

**The directory name is the skill name.** `skills/document-onboarding/` becomes
`/document-onboarding`. Kebab-case, no spaces. If you set `name` in the frontmatter it must
match the directory exactly.

**No bare colons in the frontmatter `description`.** YAML reads `foo: bar` inside an unquoted
scalar as a mapping and fails to parse. A skill whose frontmatter fails to parse **loads with no
metadata and never triggers**, and there is no error at load time — it just silently does
nothing. Use a `>-` block scalar, as the template does. This has bitten us once already, and it
is the main reason `scripts/validate-skills.py` exists.

**Every directory in `skills/` must contain a `SKILL.md`.** Anything with a `SKILL.md` loads as
an invocable skill. Templates, notes, and drafts go in `docs/`. This is why the template lives
at `docs/skill-template.md` and not in `skills/`.

**Each skill folder must be self-contained.** A skill's supporting files live in
`skills/<name>/reference/`, and the skill references them as `reference/foo.md`. Never reach
outside the folder with `../`. Two reasons: the documented install is `cp -r skills/<name>
~/.claude/skills/`, which copies only that folder; and when this library is packaged as a
plugin, anything outside the plugin directory is not copied into the cache either. The
validator enforces this.

If two skills genuinely need the same file, duplicate it for now. When duplication starts to
hurt, that is the signal to convert the library into a plugin and hoist the shared files to a
root `reference/` directory — see [docs/convert-to-plugin.md](docs/convert-to-plugin.md).

**Keep `skills/` at the repository root.** That is where Claude Code looks for skills inside a
plugin, which is what makes `claude --plugin-dir .` work today and makes conversion a two-file
change. Do not nest it.

## What makes a good skill here

**Evidence before questions.** Read the folder and search for what actually happened before
asking the user anything. A question you could have answered yourself is a wasted question.

**Tag every claim.** `[CONFIRMED]`, `[GUESS: verify]`, `[SUGGESTED]`. A document that looks
authoritative but is half inference is worse than no document.

**Ship a fallback skeleton.** When the evidence is thin, propose the standard version of the
step marked `[SUGGESTED]` rather than leaving a gap. Users can cut what doesn't apply; they
can't fill in what isn't there.

**End with the open questions.** The user's homework list is part of the deliverable.

**Never invent.** No tool, step, person, or date that didn't come from evidence or the user.

**Respect the data rules.** Read `ai-usage-policy.md` first. Never write ID numbers, bank
details, home addresses, salary figures, immigration status, or health information into any
document — describe the step that handles them instead.

## Writing the description

The `description` is the only thing Claude sees when deciding whether to use your skill. Include
the trigger phrases a real user would type, and state what the skill is *not* for.

Test it: start a fresh session, type the request in the user's own words, and check that the
skill fires without being named.
