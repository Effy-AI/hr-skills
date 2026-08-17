# Converting this library to a plugin

This repository is already laid out as a plugin. Nothing needs to move.

Claude Code treats a directory as a plugin root when it finds components in their default
locations — `skills/`, `agents/`, `hooks/`, `.mcp.json` — and the `.claude-plugin/plugin.json`
manifest is **optional** when they are. `skills/` is at this repository's root, so:

```bash
claude --plugin-dir .
```

already loads every skill in the library. That works today, with no manifest.

## What you gain by converting

| | Skill library | Plugin |
| --- | --- | --- |
| Install | `cp -r` a folder | `/plugin install` |
| Updates | user re-copies manually | `/plugin update`, or automatic |
| Namespacing | `/document-onboarding` | `/hr-skills:document-onboarding` |
| Enable/disable as a set | no | yes |
| Ship MCP servers, hooks, agents | no | yes |
| Files shared across skills | must be duplicated per skill | one copy at the plugin root |

## When to convert

Convert when one of these becomes true:

1. **A second skill needs the same reference file.** Today each skill folder is self-contained,
   which is what makes `cp -r` a valid install. Once two skills share a file you either
   duplicate it — and the copies drift — or you promote it to a root `reference/` directory, at
   which point copying a single skill folder no longer gives a working skill. That is the real
   trigger, not a preference.
2. **You need to ship an MCP server, hook, or agent** alongside the skills.
3. **Users are asking for updates.** Manual re-copying does not scale past a handful of people.

Until then the library form is less machinery for the same result.

## Step 1 — Add the plugin manifest

Create `.claude-plugin/plugin.json`:

```json
{
  "name": "hr-skills",
  "description": "Turn undocumented people processes into documented ones. Skills for HR and people leaders working in a Claude-HR folder.",
  "author": {
    "name": "Effy AI",
    "email": "a.makhovskyi@effy.ai",
    "url": "https://effy.ai"
  },
  "homepage": "https://effy.ai",
  "repository": "https://github.com/Effy-AI/hr-skills",
  "license": "MIT",
  "keywords": ["hr", "people-ops", "onboarding", "documentation"]
}
```

Only `plugin.json` goes inside `.claude-plugin/`. `skills/` stays where it is at the root.
Putting `skills/` inside `.claude-plugin/` is the single most common way to break a plugin.

Note there is **no `version` field**. For git-based sources Claude Code falls back to the
resolved commit SHA, so every push ships. If you add a `version` you must bump it on every
release, or existing users keep the cached copy indefinitely with no warning.

Test it:

```bash
claude --plugin-dir .
/hr-skills:document-onboarding
```

## Step 2 — Add the marketplace catalog

A plugin still needs a marketplace for people to install from. The simplest option is to make
this repository its own marketplace. Create `.claude-plugin/marketplace.json`:

```json
{
  "name": "effy",
  "description": "Claude skills for HR and people leaders, by Effy AI.",
  "owner": {
    "name": "Effy AI",
    "email": "a.makhovskyi@effy.ai",
    "url": "https://effy.ai"
  },
  "plugins": [
    {
      "name": "hr-skills",
      "source": "./",
      "displayName": "HR Skills",
      "description": "Turn undocumented people processes into documented ones.",
      "category": "productivity"
    }
  ]
}
```

`"source": "./"` points the single plugin entry at the repository root — the plugin and the
marketplace are the same directory. Users then run:

```bash
claude plugin marketplace add Effy-AI/hr-skills
claude plugin install hr-skills@effy
```

If you later split into several plugins, move each into `plugins/<name>/` with its own
`.claude-plugin/plugin.json`, set `"metadata": { "pluginRoot": "./plugins" }`, and give each
entry a `"source": "<name>"`.

## Naming constraints to respect

- Marketplace and plugin names must be **kebab-case**, no spaces.
- A user can register **only one marketplace per name** — adding a second named `effy` silently
  replaces the first. Keep `effy` for whichever marketplace customers install.
- Reserved marketplace names are rejected: `claude-plugins-official`, `claude-community`,
  `anthropic-plugins`, `agent-skills`, `healthcare`, and lookalikes such as
  `official-claude-plugins`.
- Never set `version` in both `plugin.json` and the marketplace entry. `plugin.json` wins
  silently, and a stale value there masks the one in the catalog.

## Step 3 — Validate before publishing

```bash
claude plugin validate .
```

Add `--strict` to treat warnings as errors. The public community-marketplace review pipeline
runs the same check on every submission, so keeping it clean now avoids a rejection later.

## What changes for existing users

Skills become namespaced. `/document-onboarding` becomes `/hr-skills:document-onboarding`.
Anyone who installed by copying into `~/.claude/skills/` keeps their un-namespaced copy, and
both will exist side by side — the plugin version does not override it. Tell people to delete
the copied folder when they install the plugin, or they will have two.
