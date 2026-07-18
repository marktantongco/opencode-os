# 🏗️ Skill Architect

A production-ready **meta-skill** for creating, optimizing, and packaging AI agent skills. Drop this into your Design OS and any AI agent can now design other skills following the Agent Skills open standard (agentskills.io).

## What's Inside

```
skill-architect/
├── SKILL.md                              # Core skill (triggers on skill creation tasks)
├── README.md                             # This file
├── scripts/
│   └── validate-skill.py                 # Validates any skill against the open standard
├── references/
│   ├── skill-templates.md                # 5 copy-paste templates (code gen, review, docs, data, design system)
│   ├── description-optimization.md       # How to write trigger-optimized descriptions
│   └── evaluation-guide.md               # How to test skills with evals and benchmarks
└── assets/
    └── (empty — add your own templates here)
```

## Installation

### Option A: Claude Code
```bash
# Copy to your skills directory
cp -r skill-architect ~/.claude/skills/

# Or package and install
zip -r skill-architect.skill skill-architect/
# Then use /plugin install or drag into Claude Code
```

### Option B: Cursor
```bash
# Copy to Cursor skills directory
cp -r skill-architect ~/.cursor/skills/

# Or use the / menu — skills auto-register as slash commands
```

### Option C: Direct Use (Any Agent)
Simply paste the contents of `SKILL.md` into your agent's context when you need to create a skill. The instructions are self-contained.

## How to Use

Once installed, the skill auto-triggers when you say things like:
- "I want to create a skill for..."
- "Turn this workflow into a skill"
- "Help me write a SKILL.md"
- "Why isn't my skill triggering?"
- "Package this skill for distribution"

The skill will guide you through:
1. **Intent capture** — Interview you to understand what the skill should do
2. **Structure design** — Choose the right directory layout
3. **SKILL.md writing** — Craft trigger-optimized frontmatter + instructions
4. **Supporting files** — Add scripts, references, and assets as needed
5. **Validation** — Run `validate-skill.py` to catch issues
6. **Testing** — Create evals and iterate
7. **Packaging** — Zip into a `.skill` file for sharing

## Quick Validation

Test any skill before deployment:

```bash
cd skill-architect/
python scripts/validate-skill.py /path/to/your-skill/
```

Checks:
- ✅ SKILL.md exists with valid YAML frontmatter
- ✅ Required fields (name, description) present
- ✅ Description length optimal (50-800 chars)
- ✅ Body under 500 lines
- ✅ No security red flags
- ✅ No leftover template placeholders

## Skill Templates Included

| Template | Use Case | File |
|---|---|---|
| **Code Generator** | Scaffold components, modules, boilerplate | `references/skill-templates.md` § Template A |
| **Code Review** | Enforce team standards during review | `references/skill-templates.md` § Template B |
| **Documentation** | Generate READMEs, API docs, ADRs | `references/skill-templates.md` § Template C |
| **Data Processing** | Transform, validate, analyze data | `references/skill-templates.md` § Template D |
| **Design System** | Enforce tokens, spacing, motion, a11y | `references/skill-templates.md` § Template E |

## Design OS Integration

This skill fits into your modular v8.1.0 Design OS as:

```
skills/
├── skill-architect/          # This skill — creates all other skills
│   ├── SKILL.md
│   ├── scripts/
│   └── references/
├── motion/                   # Animation skill (created by skill-architect)
├── gsap/                     # Animation skill (created by skill-architect)
├── design-system-enforcer/   # Design skill (created by skill-architect)
└── ...                       # Any other skill
```

**Validation Pipeline Rule:**
```yaml
rule: skill-validation
trigger: on_skill_create
action:
  - run: python skills/skill-architect/scripts/validate-skill.py {new_skill_path}
  - gate: exit_code == 0
  - on_fail: block_commit, show_errors
```

## License

MIT — Use, modify, and distribute freely. Compatible with the Agent Skills open standard.
