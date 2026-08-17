#!/usr/bin/env python3
"""Validate the skill library.

Checks the things that fail silently at runtime — a skill whose frontmatter does not parse
loads with no metadata and never triggers, and you get no error.

Also enforces the two rules that keep this library convertible to a plugin without moving
anything: skills live at skills/<name>/SKILL.md, and each skill folder is self-contained.

Usage:  python3 scripts/validate-skills.py
Exit:   0 clean, 1 on any failure.
"""

import os
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("pyyaml required:  pip install pyyaml")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

ok, warn, fail = [], [], []


def check_skill(name):
    d = os.path.join(SKILLS, name)
    md = os.path.join(d, "SKILL.md")

    if not KEBAB.match(name):
        fail.append(f"{name}: folder name is not kebab-case")
    if not os.path.isfile(md):
        fail.append(f"{name}: no SKILL.md — every directory in skills/ must be a real skill")
        return

    text = open(md, encoding="utf-8").read()
    if not text.startswith("---\n"):
        fail.append(f"{name}: no YAML frontmatter")
        return

    parts = text.split("---\n", 2)
    if len(parts) < 3:
        fail.append(f"{name}: frontmatter is not closed")
        return

    try:
        meta = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        fail.append(
            f"{name}: frontmatter does not parse ({e.__class__.__name__}). "
            "A skill with unparseable frontmatter loads with NO metadata and never "
            "triggers. Most common cause: a bare colon in an unquoted description — "
            "use a '>-' block scalar."
        )
        return

    if not isinstance(meta, dict):
        fail.append(f"{name}: frontmatter is not a mapping")
        return

    ok.append(f"{name}: frontmatter parses")

    if meta.get("name") and meta["name"] != name:
        fail.append(f"{name}: frontmatter name '{meta['name']}' != folder name")
    else:
        ok.append(f"{name}: name matches folder")

    desc = meta.get("description")
    if not desc:
        fail.append(f"{name}: description is required — it is all Claude sees when deciding "
                    "whether to use the skill")
    else:
        n = len(desc)
        ok.append(f"{name}: description {n} chars")
        if n < 120:
            warn.append(f"{name}: description is short ({n} chars) — add trigger phrases "
                        "a user would actually type, and what it is NOT for")

    # Self-containment: a skill folder must work after `cp -r` into ~/.claude/skills/
    body = parts[2]
    for ref in set(re.findall(r"(?<![\w./])((?:\.\./)+[\w./-]+)", body)):
        fail.append(f"{name}: references '{ref}' outside its own folder — breaks `cp -r` "
                    "install and breaks when packaged as a plugin")

    for ref in set(re.findall(r"`(reference/[\w./-]+)`", body)):
        if not os.path.exists(os.path.join(d, ref)):
            fail.append(f"{name}: references '{ref}' which does not exist in the skill folder")
        else:
            ok.append(f"{name}: bundled file present — {ref}")


def main():
    if not os.path.isdir(SKILLS):
        sys.exit("no skills/ directory at the repository root")

    names = sorted(e for e in os.listdir(SKILLS) if os.path.isdir(os.path.join(SKILLS, e)))
    if not names:
        sys.exit("skills/ is empty")

    stray = [e for e in os.listdir(SKILLS) if not os.path.isdir(os.path.join(SKILLS, e))
             and not e.startswith(".")]
    for e in stray:
        warn.append(f"skills/{e} is a loose file — skills are directories containing SKILL.md")

    ok.append(f"{len(names)} skill(s): {', '.join(names)}")
    for n in names:
        check_skill(n)

    # The template is copied to start every new skill, so its frontmatter must parse too.
    tpl = os.path.join(ROOT, "docs", "skill-template.md")
    if os.path.isfile(tpl):
        try:
            yaml.safe_load(open(tpl, encoding="utf-8").read().split("---\n", 2)[1])
            ok.append("docs/skill-template.md: frontmatter parses")
        except (yaml.YAMLError, IndexError) as e:
            fail.append(f"docs/skill-template.md: frontmatter broken ({e.__class__.__name__}) "
                        "— every skill copied from it would inherit the fault")

    # Plugin-convertibility: skills/ must be at the repo root, not nested.
    if os.path.isdir(os.path.join(ROOT, ".claude-plugin")):
        for bad in ("skills", "commands", "agents", "hooks"):
            if os.path.exists(os.path.join(ROOT, ".claude-plugin", bad)):
                fail.append(f"'{bad}' must NOT be inside .claude-plugin/ — it belongs at the root")
        ok.append("plugin manifest present, component dirs at root")
    else:
        ok.append("no .claude-plugin/ — library form; `claude --plugin-dir .` still loads it")

    print("PASS")
    for x in ok:
        print("  ok  ", x)
    print("\nWARN")
    print("\n".join(f"  !   {x}" for x in warn) or "   none")
    print("\nFAIL")
    print("\n".join(f"  X   {x}" for x in fail) or "   none")

    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
