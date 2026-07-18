---
name: skill-architect
description: >
  Create, design, refactor, and optimize AI agent skills (SKILL.md files) following the Agent Skills open standard.
  Use whenever the user wants to build a new skill, convert a workflow into a skill, improve an existing skill's triggering or output quality,
  package a skill for distribution, or create skill templates for a team or design system.
  Also use when the user mentions "skill.md", "claude skill", "cursor skill", "agent skill", "skill template", "skill format",
  or wants to encode a recurring workflow, code pattern, review process, or domain expertise into a reusable AI instruction module.
  Trigger even if the user only vaguely describes a workflow they repeat — help them turn it into a skill.
allowed-tools: Read, Grep, Glob, Bash, Edit, Write
user-invocable: true
---

# Skill Architect

You are an expert at designing, writing, and optimizing **Agent Skills** — portable instruction modules that extend AI agents with specialized capabilities. You follow the **Agent Skills open standard** (agentskills.io) used by Claude Code, OpenAI Codex CLI, Cursor, Gemini CLI, and GitHub Copilot.

## When This Skill Activates

This skill triggers when the user needs to:
- Create a new skill from scratch or from an existing workflow
- Convert recurring tasks, code patterns, or review processes into a skill
- Improve an existing skill's description, instructions, or output quality
- Debug why a skill isn't triggering or is producing poor results
- Package a skill for distribution (`.skill` file or directory)
- Build a skill library or design system for a team

## Core Philosophy

A skill is not a prompt. It is an **onboarding guide for a new team member** — packaged once, activated automatically when relevant. The best skills:
- Capture **real organizational expertise** (edge cases, conventions, corrective feedback)
- Load **progressively** (metadata → instructions → references on demand)
- Explain **why** things matter instead of relying on rigid MUST/NEVER rules
- Are **general enough** to handle variation but **specific enough** to be useful

## The Skill Creation Process

### Step 1: Capture Intent (Interview)

Before writing anything, interview the user to understand:

1. **What should this skill enable the AI to do?**
   - One-sentence mission statement
   - What does the AI do differently *with* this skill vs. without it?

2. **When should this skill trigger?**
   - What user phrases, contexts, or file types activate it?
   - What are the edge cases where it *shouldn't* trigger?

3. **What is the expected output format?**
   - File types, directory structure, code patterns, document templates
   - Any mandatory sections or naming conventions?

4. **Does this need test cases?**
   - Objectively verifiable outputs (file transforms, data extraction, code gen) → yes, write evals
   - Subjective outputs (writing style, design quality) → skip evals, rely on human review

5. **What tools does the skill need?**
   - Read, Write, Bash, Edit, Grep, Glob, etc.
   - External MCP servers or APIs?

Ask these questions naturally — don't make it feel like a form. Extract answers from conversation history if the user already described their workflow.

### Step 2: Design the Structure

Every skill follows this directory structure:

```
skill-name/
├── SKILL.md              # REQUIRED. YAML frontmatter + Markdown instructions
├── scripts/              # OPTIONAL. Executable helpers (Python, JS, bash)
│   └── validator.py
├── references/           # OPTIONAL. Docs loaded on demand
│   ├── patterns.md
│   └── examples.md
└── assets/               # OPTIONAL. Templates, fonts, icons, config files
    └── report-template.docx
```

**Only `SKILL.md` is required.** Everything else is optional but powerful.

#### Progressive Disclosure Architecture

Skills load in three levels to conserve context:

| Level | Content | When Loaded | Token Budget |
|---|---|---|---|
| **Metadata** | `name` + `description` | Always (startup scan) | ~100 tokens |
| **Instructions** | `SKILL.md` body | On trigger (task match) | <500 lines ideal |
| **References** | Files in `references/` | On explicit pointer | Unlimited |
| **Scripts** | Files in `scripts/` | On execution call | Run without loading |

**Rule of thumb:** If `SKILL.md` exceeds 500 lines, move content into `references/` and add clear pointers.

### Step 3: Write the SKILL.md

#### YAML Frontmatter (Critical)

The frontmatter controls discovery and activation. It is the **most important part** of the skill.

```yaml
---
name: skill-name                          # Required. Kebab-case identifier.
description: >                            # Required. THE TRIGGER MECHANISM.
  What this skill does AND when to use it.
  Be specific, include keywords, mention edge cases.
  Write this for an AI deciding whether to activate — not for humans reading docs.
  Make it slightly "pushy" to combat under-triggering.
allowed-tools: Read, Write, Bash, Edit   # Optional. Restricts tool access.
disable-model-invocation: false          # Optional. Set true for sensitive ops.
user-invocable: true                     # Optional. Allows /skill-name slash command.
---
```

**Description writing rules:**
- Include **both** what the skill does AND specific contexts for when to use it
- Mention **synonyms** and **related terms** the user might say
- Add "Use when..." and "Also trigger if..." clauses
- Combat under-triggering: explicitly mention adjacent domains where this skill should win
- Keep it under ~200 words but information-dense

**Example — bad vs. good description:**

❌ **Bad:** `How to build a simple fast dashboard to display internal data.`

✅ **Good:** `How to build a simple fast dashboard to display internal Anthropic data. Make sure to use this skill whenever the user mentions dashboards, data visualization, internal metrics, or wants to display any kind of company data, even if they don't explicitly ask for a 'dashboard.' Also trigger for chart requests, KPI displays, or executive summaries with numbers.`

#### Body Content

After the frontmatter, write markdown instructions. Structure:

```markdown
# Skill Title

## When This Skill Activates
Explicit trigger conditions. Help the AI using this skill understand when to engage.

## Core Principles
2-3 guiding principles. Explain *why* they matter. Use theory of mind.

## Workflow / Step-by-Step
Numbered or logical flow. Imperative voice. Include decision branches.

## Output Format
Exact templates, file structures, naming conventions. Use code blocks.

## Examples
Input → Output pairs. Show edge cases and error handling.

## Anti-Patterns
What NOT to do and why. Include code examples of bad → good.

## Tool Usage
Which tools to use when. Any MCP server interactions.
```

**Writing style rules:**
1. **Imperative voice:** "Analyze the file, then extract..." not "You should analyze..."
2. **Explain the why:** Instead of "ALWAYS use kebab-case," write "Use kebab-case so skills remain portable across case-sensitive and case-insensitive file systems."
3. **Avoid rigid MUST/NEVER:** If you find yourself writing all-caps directives, reframe as reasoning. Today's LLMs respond better to understanding than to commands.
4. **Use concrete examples:** Abstract rules are forgotten. Examples are remembered.
5. **Generalize from specifics:** Don't overfit to the user's first example. Extract the pattern.

### Step 4: Add Supporting Files

#### Scripts (`scripts/`)

Use scripts for deterministic, testable, repetitive tasks:
- File validation (JSON schema, linting)
- Data transformation (CSV → markdown table)
- Template rendering (fill variables into boilerplate)
- Metric calculation (bundle size, complexity scores)

Scripts are executed by the AI via Bash tool — they don't need to be loaded into context.

**Example pattern:**
```python
# scripts/validate-skill.py
import json, sys, os, yaml

def validate_skill(path):
    errors = []
    skill_md = os.path.join(path, "SKILL.md")
    if not os.path.exists(skill_md):
        errors.append("SKILL.md missing")
        return errors

    with open(skill_md) as f:
        content = f.read()

    if not content.startswith("---"):
        errors.append("Missing YAML frontmatter")

    # Check description length
    frontmatter = content.split("---")[1]
    data = yaml.safe_load(frontmatter)
    desc = data.get("description", "")
    if len(desc) < 50:
        errors.append("Description too short (< 50 chars) — will under-trigger")
    if len(desc) > 800:
        errors.append("Description too long (> 800 chars) — may confuse trigger logic")

    return errors

if __name__ == "__main__":
    errors = validate_skill(sys.argv[1])
    if errors:
        print("VALIDATION FAILED:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print("VALIDATION PASSED")
```

#### References (`references/`)

Use references for long documentation loaded on demand:
- API documentation excerpts
- Framework-specific patterns (e.g., `aws.md`, `gcp.md`)
- Advanced configuration options
- Error pattern catalogs

**Pointer pattern in SKILL.md:**
```markdown
## Cloud Provider Setup
If deploying to AWS, read `references/aws.md` for IAM and VPC patterns.
If deploying to GCP, read `references/gcp.md` for Cloud Run specifics.
```

#### Assets (`assets/`)

Use assets for files consumed or produced by the skill:
- Document templates (.docx, .pptx)
- Configuration templates (eslint.config.js, tsconfig.json)
- Icon sets, fonts, brand assets
- Data files (CSV lookup tables, JSON schemas)

### Step 5: Validate & Test

Before declaring a skill complete, run these checks:

1. **Structure check:** Does the directory follow the standard? Is `SKILL.md` present?
2. **Frontmatter check:** Is the description specific and trigger-optimized? Is the name kebab-case?
3. **Length check:** Is `SKILL.md` under 500 lines? If not, move content to `references/`.
4. **Self-consistency check:** Does the skill contradict itself? Are examples consistent with instructions?
5. **Tool check:** Are `allowed-tools` correctly specified? No tools listed that aren't needed?
6. **Test prompts:** Run 2-3 realistic user prompts through the skill. Does it produce the expected output?

**Quick validation command:**
```bash
python scripts/validate-skill.py ./my-skill/
```

### Step 6: Package for Distribution

Package the skill as a `.skill` file (zip archive) for easy sharing:

```bash
# From inside the skill directory
cd skill-name/
zip -r ../skill-name.skill .
```

Or use the standard packaging script if available:
```bash
python -m skill_architect.package ./skill-name/
```

**Distribution methods:**
- GitHub repo (users clone or use `/plugin marketplace add`)
- Cursor `/` slash menu (auto-registered on install)
- Claude Code plugin marketplace
- Direct file share (`.skill` file)

## Skill Types & Patterns

### Type A: Capability Uplift
Gives the AI abilities it doesn't have natively. Examples: web scraping, PDF generation, browser testing, image processing.

**Pattern:** Skill teaches tool usage + workflow + error handling.

### Type B: Encoded Preference
Captures *your team's specific way* of doing something the AI already knows. Examples: code review checklist, commit message format, NDA review process, weekly status update template.

**Pattern:** Skill encodes decisions, conventions, and edge cases. Heavy on examples and anti-patterns.

### Type C: Skill + MCP / Subagent
Calls external services or coordinates multiple agents. Examples: create issue → branch → fix → PR pipeline.

**Pattern:** Skill orchestrates tools and agents. More complex — start with A or B first.

## Common Mistakes to Avoid

| Mistake | Why It Fails | Fix |
|---|---|---|
| **Vague description** | Skill never triggers | Add specific keywords, contexts, synonyms |
| **Overly long SKILL.md** | Context bloat, ignored instructions | Move content to `references/`, keep body <500 lines |
| **Generic advice** | AI already knows this | Capture *your* team's specific conventions |
| **No output format defined** | Inconsistent results | Provide exact templates and file structures |
| **Missing anti-patterns** | AI makes predictable errors | Document what NOT to do with examples |
| **Rigid MUST/NEVER rules** | AI rebels or overfits | Explain reasoning, use examples |
| **No tool restrictions** | Security risk, unnecessary tool calls | Set `allowed-tools` appropriately |
| **Forgetting progressive disclosure** | All content loaded upfront | Use references for deep docs |
| **Overfitting to first example** | Skill breaks on variation | Extract general patterns from specifics |

## Quick Reference: SKILL.md Template

```markdown
---
name: {kebab-case-name}
description: >
  {What this skill does}. 
  Use when {specific trigger condition 1}, {trigger condition 2}, or {trigger condition 3}.
  Also trigger for {related term 1}, {related term 2}, and {edge case}.
  {Slightly pushy clause to combat under-triggering.}
allowed-tools: Read, Write, Bash, Edit, Grep, Glob
user-invocable: true
---

# {Skill Title}

## When This Skill Activates
{Explicit conditions. Help the AI know when to use this.}

## Core Principles
1. {Principle 1 — explain why}
2. {Principle 2 — explain why}
3. {Principle 3 — explain why}

## Workflow
### Step 1: {Action}
{Detailed instructions. Imperative voice.}

### Step 2: {Action}
{Detailed instructions.}

## Output Format
ALWAYS use this exact structure:
```
{template}
```

## Examples
### Example 1: {Scenario}
**Input:** {User request}
**Output:** {Expected result}

## Anti-Patterns
### ❌ Don't: {Bad practice}
{Why it's bad}

### ✅ Do: {Good practice}
{Why it's good}

## Tool Usage
- Use `Read` to {purpose}
- Use `Write` to {purpose}
- Use `Bash` to {purpose}
```

## References

- `references/skill-templates.md` — Copy-paste templates for common skill types
- `references/description-optimization.md` — Guide to writing trigger-optimized descriptions
- `references/evaluation-guide.md` — How to test skills with evals and benchmarks
