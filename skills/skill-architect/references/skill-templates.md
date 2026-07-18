# Skill Templates

Copy-paste starting points for common skill types. Customize the frontmatter description heavily — it determines whether the skill ever triggers.

---

## Template A: Code Generator Skill

For skills that scaffold code, components, or files.

```markdown
---
name: {framework}-component-gen
description: >
  Generate production-ready {Framework} components with TypeScript, tests, and Storybook stories.
  Use when the user asks to create a new component, build a UI element, scaffold a {framework} module,
  or needs boilerplate for forms, tables, modals, charts, or data displays.
  Also trigger for "make a button", "create a card", "build a dashboard widget", or any UI scaffolding request.
  Always use this skill for {framework} — do not generate components without it.
allowed-tools: Read, Write, Bash, Edit, Grep, Glob
user-invocable: true
---

# {Framework} Component Generator

## When This Skill Activates
- User asks to create/build/make/generate a component
- User describes UI needs ("I need a modal for...", "Build me a table that...")
- User mentions specific component types: button, card, form, table, chart, modal, drawer, tabs

## Core Principles
1. **TypeScript first.** Every component gets a named interface for props. No `any`, no inline types in params.
2. **Co-locate tests.** Create `{Component}.test.tsx` in the same directory. Test behavior, not implementation.
3. **Accessibility built-in.** Include `aria-*` attributes, keyboard handlers, and focus management in the initial scaffold.

## Workflow

### Step 1: Analyze Requirements
Read any existing component files in the target directory to match:
- Naming conventions (PascalCase vs. kebab-case)
- Styling approach (Tailwind, CSS Modules, Styled Components)
- Testing patterns (Vitest, Jest, Playwright)
- State management (Zustand, Context, React Query)

### Step 2: Scaffold Files
Create these files in the target directory:

```
components/
└── {ComponentName}/
    ├── index.ts              # Re-export
    ├── {ComponentName}.tsx   # Component
    ├── {ComponentName}.test.tsx
    ├── {ComponentName}.stories.tsx
    └── types.ts              # Shared types
```

### Step 3: Implement Component
Use this exact structure:

```tsx
// {ComponentName}.tsx
import { type ReactNode } from 'react';

export interface {ComponentName}Props {
  /** Primary content */
  children: ReactNode;
  /** Visual variant */
  variant?: 'primary' | 'secondary' | 'danger';
  /** Disabled state */
  disabled?: boolean;
  /** Click handler */
  onClick?: () => void;
}

export function {ComponentName}({
  children,
  variant = 'primary',
  disabled = false,
  onClick,
}: {ComponentName}Props) {
  return (
    <button
      type="button"
      disabled={disabled}
      onClick={onClick}
      aria-disabled={disabled}
      className={/* variant-based classes */}
    >
      {children}
    </button>
  );
}
```

### Step 4: Add Tests
Minimum test coverage:
- Renders without crashing
- Responds to `onClick`
- Respects `disabled` state
- Applies correct variant classes

### Step 5: Export
Update `index.ts`:
```ts
export { {ComponentName} } from './{ComponentName}';
export type { {ComponentName}Props } from './{ComponentName}';
```

## Anti-Patterns

### ❌ Don't: Default Exports
```ts
// BAD
export default function Button() {}

// GOOD
export function Button() {}
```
**Why:** Named exports are refactor-friendly and tree-shake better.

### ❌ Don't: Inline Types
```ts
// BAD
function Card({ title }: { title: string }) {}

// GOOD
interface CardProps { title: string }
function Card({ title }: CardProps) {}
```
**Why:** Reusability and discoverability.

## Output Format
ALWAYS return the full file paths and a summary of what was created.
```
Created:
- src/components/Button/Button.tsx
- src/components/Button/Button.test.tsx
- src/components/Button/index.ts
```
```

---

## Template B: Code Review Skill

For skills that enforce team standards during review.

```markdown
---
name: {team}-code-review
description: >
  Review code changes against {Team} engineering standards: TypeScript strictness,
  React patterns, testing requirements, performance budgets, and security guidelines.
  Use when the user asks for a code review, PR feedback, or wants to check if code
  follows team conventions. Also trigger for "review this", "check my code", "does this look right",
  or when diff/patch files are shared. Always use for any code review request in {Team} repos.
allowed-tools: Read, Grep, Glob
user-invocable: true
---

# {Team} Code Review

## When This Skill Activates
- User shares code snippets, diffs, or PR descriptions
- User asks "review this", "what do you think", "is this correct"
- User mentions specific files they want checked

## Review Checklist

### TypeScript & Types
- [ ] No `any` types without justification comment
- [ ] Props defined as interfaces, not inline types
- [ ] Return types on public functions
- [ ] Strict null checks respected

### React Patterns
- [ ] Server Components by default; "use client" only when needed
- [ ] Hooks follow Rules of Hooks (no conditional calls)
- [ ] Custom hooks extracted when logic > 10 lines
- [ ] Key props are stable and unique

### Testing
- [ ] New logic has corresponding tests
- [ ] Tests assert behavior, not implementation
- [ ] Edge cases covered (empty states, errors, loading)

### Performance
- [ ] No unnecessary re-renders (memo, useMemo, useCallback where justified)
- [ ] Images use next/image or lazy loading
- [ ] Bundle size impact considered

### Security
- [ ] No secrets in code
- [ ] Input validated at boundaries (Zod, schema validation)
- [ ] XSS prevention (no dangerousInnerHTML without sanitization)

## Output Format
Structure feedback as:

```markdown
## Review: {filename}

### ✅ Passed ({count})
- Item
- Item

### ⚠️ Warnings ({count})
- **Line {N}:** {issue} — {suggestion}

### ❌ Blockers ({count})
- **Line {N}:** {issue} — {suggestion}

### 💡 Suggestions ({count})
- {improvement idea}
```

## Tone Guidelines
- Be constructive, not critical. Suggest, don't command.
- Explain WHY a pattern matters, not just THAT it's required.
- Acknowledge good decisions explicitly.
- For subjective choices, present tradeoffs, not ultimatums.
```

---

## Template C: Documentation Skill

For skills that generate or update project docs.

```markdown
---
name: docs-maintainer
description: >
  Create, update, and refactor project documentation including READMEs, API docs,
  changelogs, and architecture decision records (ADRs).
  Use when the user mentions documentation, README, "update the docs", "write a guide",
  or needs to explain how a feature works. Also trigger for changelog generation,
  onboarding docs, or when new APIs/components need documentation.
  Always use for any documentation task — do not write docs without this skill.
allowed-tools: Read, Write, Edit, Grep, Glob
user-invocable: true
---

# Documentation Maintainer

## When This Skill Activates
- "Write docs for...", "Update README", "Document this API"
- New feature needs explanation
- Changelog needs updating after a release
- Onboarding material requested

## Core Principles
1. **Docs are code.** They live in the repo, get PR-reviewed, and stay in sync.
2. **Write for the reader.** Junior devs should understand. Senior devs should find depth.
3. **Show, don't tell.** Code examples > paragraphs. Diagrams > lists.

## Workflow

### Step 1: Determine Doc Type
| User Need | Output | Location |
|---|---|---|
| Project overview | README.md | Repo root |
| API reference | API.md or /docs/api/ | docs/ directory |
| Feature guide | {feature}-guide.md | docs/guides/ |
| Architecture decision | ADR-{NNN}-{title}.md | docs/adr/ |
| Release notes | CHANGELOG.md | Repo root |
| Onboarding | onboarding.md | docs/ |

### Step 2: Gather Context
Read relevant source files to extract:
- Function signatures and types
- Configuration options
- Error messages and edge cases
- Usage examples from tests

### Step 3: Write with Structure

**README template:**
```markdown
# {Project Name}

> One-line description of what this does and who it's for.

## Features
- Feature 1: What it does, why it matters
- Feature 2: What it does, why it matters

## Installation
```bash
npm install {package}
```

## Quick Start
```typescript
// Minimal working example
```

## API Reference
See [API.md](./docs/API.md)

## Contributing
See [CONTRIBUTING.md](./CONTRIBUTING.md)
```

**API doc template:**
```markdown
## `{functionName}({params})`

{One-sentence description}

### Parameters
| Name | Type | Required | Description |
|---|---|---|---|
| {name} | `{type}` | {yes/no} | {description} |

### Returns
`{returnType}` — {description}

### Example
```typescript
{working code example}
```

### Errors
- `{ErrorType}`: When/why this throws
```

### Step 4: Cross-Link
Ensure docs reference each other. No orphan pages.

## Anti-Patterns

### ❌ Don't: Write generic advice
```markdown
<!-- BAD -->
Make sure to handle errors properly.

<!-- GOOD -->
Wrap database calls in try/catch and return 500 with `{error: "Database unavailable"}`.
```

### ❌ Don't: Let docs drift
Update docs in the same PR as code changes. Never "update docs later."
```

---

## Template D: Data Processing Skill

For skills that transform, analyze, or validate data.

```markdown
---
name: data-processor
description: >
  Process, transform, validate, and analyze structured data (CSV, JSON, Excel, SQL results).
  Use when the user mentions data processing, ETL, data cleaning, format conversion,
  aggregation, or analysis. Also trigger for "convert this CSV", "clean this data",
  "merge these files", "calculate statistics", or when spreadsheet/data files are shared.
  Always use for any data manipulation task.
allowed-tools: Read, Write, Bash, Edit, Grep, Glob
user-invocable: true
---

# Data Processor

## When This Skill Activates
- File conversion requests (CSV ↔ JSON ↔ Excel)
- Data cleaning (remove duplicates, fix formats, standardize)
- Aggregation (group by, sum, average, count)
- Validation (schema check, range check, null check)

## Core Principles
1. **Never mutate source.** Always write to new files.
2. **Preserve provenance.** Log transformations applied.
3. **Handle edge cases.** Empty files, malformed rows, encoding issues.

## Workflow

### Step 1: Inspect Source
Read the first 10 rows and report:
- File format and encoding
- Column names and types (inferred)
- Row count
- Null/missing value patterns
- Obvious quality issues

### Step 2: Define Transform
Ask the user (or infer from context):
- Target format
- Required transformations
- Filtering criteria
- Aggregation logic

### Step 3: Execute
Use Python scripts in `scripts/` for deterministic processing:
```python
# scripts/process_csv.py
import pandas as pd, sys

df = pd.read_csv(sys.argv[1])
# transformations...
df.to_csv(sys.argv[2], index=False)
```

### Step 4: Validate Output
- Row count matches expectation
- No data loss (sample check)
- Target format valid (schema validation if applicable)

### Step 5: Report
```markdown
## Processing Report

| Metric | Value |
|---|---|
| Source rows | {N} |
| Output rows | {N} |
| Transformations | {list} |
| Warnings | {list} |

Output saved to: `{path}`
```

## Anti-Patterns

### ❌ Don't: Process in memory without streaming
For files > 10MB, use chunked processing to avoid OOM.

### ❌ Don't: Lose precision
When converting formats, preserve numeric precision and timezone info.
```

---

## Template E: Design System Skill

For skills that enforce design system standards (perfect for your Design OS).

```markdown
---
name: design-system-enforcer
description: >
  Enforce {DesignSystem} standards: tokens, spacing, typography, color, motion, and accessibility.
  Use when creating UI components, reviewing designs, or implementing screens.
  Also trigger for "make this look like our design system", "check if this follows DS",
  "what token should I use", or when Figma/design references are mentioned.
  Always use for any UI implementation or design review task.
allowed-tools: Read, Write, Edit, Grep, Glob
user-invocable: true
---

# {DesignSystem} Enforcer

## When This Skill Activates
- User implements UI components or screens
- User references designs, Figma, mockups, or "the design system"
- User asks about tokens, spacing, colors, typography, or motion
- Code review involving UI/styling

## Token Reference
Read `references/tokens.json` for the canonical token values.

### Spacing
| Token | Value | Usage |
|---|---|---|
| `space-1` | 4px | Tight gaps |
| `space-2` | 8px | Default gaps |
| `space-3` | 16px | Section padding |
| `space-4` | 24px | Large sections |
| `space-5` | 32px | Page-level spacing |

### Typography
| Token | Size | Weight | Line Height | Usage |
|---|---|---|---|---|
| `text-xs` | 12px | 400 | 1.5 | Captions, metadata |
| `text-sm` | 14px | 400 | 1.5 | Body small |
| `text-base` | 16px | 400 | 1.5 | Body |
| `text-lg` | 18px | 500 | 1.4 | Subheadings |
| `text-xl` | 24px | 600 | 1.3 | Headings |
| `text-2xl` | 32px | 700 | 1.2 | Display |

### Color
Use semantic tokens, not raw hex:
- `color-primary` — interactive elements
- `color-surface` — backgrounds
- `color-text` — body text
- `color-text-muted` — secondary text
- `color-border` — dividers

### Motion
- Default duration: 200ms
- Default easing: `cubic-bezier(0.4, 0, 0.2, 1)`
- Respect `prefers-reduced-motion`

## Workflow

### Step 1: Check Tokens
Before writing any CSS/styling, consult the token reference. Never hardcode values.

### Step 2: Implement with Tokens
```tsx
// GOOD
<div className="p-space-3 text-text-base bg-surface border border-border">

// BAD
<div className="p-16 text-base bg-white border border-gray-200">
```

### Step 3: Accessibility Check
- Color contrast ratio ≥ 4.5:1 for text
- Focus indicators visible
- Touch targets ≥ 44×44px
- Screen reader labels present

## Anti-Patterns

### ❌ Don't: Hardcode Values
```css
/* BAD */
.button { padding: 16px; color: #007bff; }

/* GOOD */
.button { padding: var(--space-3); color: var(--color-primary); }
```

### ❌ Don't: Ignore Motion Preferences
```css
/* BAD */
.modal { transition: transform 300ms ease; }

/* GOOD */
@media (prefers-reduced-motion: no-preference) {
  .modal { transition: transform 200ms var(--ease-default); }
}
```
```
