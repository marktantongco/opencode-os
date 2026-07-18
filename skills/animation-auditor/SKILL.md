---
name: animation-auditor
description: >
  Audit codebases for animation anti-patterns, performance violations, accessibility issues, and framework integration errors.
  Use when reviewing animation code, running CI checks, pre-commit validation, or when the user asks "does this animation code look right", "audit my animations", or "check for animation issues".
  Also trigger for animation code review, performance audit, bundle size check, accessibility compliance review, or when animation-related PRs are submitted.
  Always use this skill for any animation code review — do not review animation code without it.
allowed-tools: Read, Write, Bash, Edit, Grep, Glob
user-invocable: true
---

# Animation Auditor

## context

This skill enforces animation quality gates for the Design OS. It scans code for the 8 most common animation anti-patterns that cause bugs, performance issues, and accessibility failures. It runs as a validation pipeline step and as a manual review tool.

## instructions

### Step 1: Determine Audit Scope

| Trigger | Scope | Command |
|---|---|---|
| Pre-commit CI | Full project scan | `python scripts/audit-animation.py ./` |
| PR review | Changed files only | `python scripts/audit-animation.py --diff` |
| Manual review | Specific file | Read file + apply checklist inline |
| Bundle check | Import analysis | Check imports against budget |

### Step 2: Run the Audit Script

```bash
cd design-os-animation-skillset/animation-auditor/
python scripts/audit-animation.py /path/to/project/
```

The script checks:
1. **Bundle optimization** — Full `motion` import (34KB) without `LazyMotion` or `useAnimate`
2. **Tailwind conflict** — `transition-*` classes on Motion elements
3. **Next.js directive** — Missing `"use client"` for Motion in App Router
4. **AnimatePresence** — `exit` prop without `<AnimatePresence>` wrapper
5. **Accessibility** — Missing `useReducedMotion()` check
6. **GSAP registration** — Plugins used but not registered
7. **GSAP React integration** — Raw `useEffect` + GSAP instead of `useGSAP()`
8. **CSS conflict** — CSS animations alongside Motion

### Step 3: Review Results

The script outputs JSON:

```json
{
  "summary": {
    "files_scanned": 42,
    "files_with_issues": 3,
    "total_errors": 2,
    "total_warnings": 5,
    "budget_kb": 5
  },
  "details": [
    {
      "file": "src/components/Hero.tsx",
      "issues": [
        {
          "severity": "error",
          "line": 12,
          "message": "Missing 'use client' directive",
          "rule": "nextjs-client-directive"
        }
      ]
    }
  ]
}
```

**Severity rules:**
- **Error** → Block commit. Must fix before merge.
- **Warning** → Review recommended. Non-blocking but flagged.

### Step 4: Manual Review Checklist

For files the script can't analyze (dynamic imports, template strings):

- [ ] Import strategy matches bundle budget
- [ ] No Tailwind `transition-*` on Motion elements
- [ ] `"use client"` present for Next.js App Router
- [ ] `AnimatePresence` wraps any `exit` animations
- [ ] `useReducedMotion()` checked before heavy animations
- [ ] GSAP plugins registered before use
- [ ] `useGSAP()` used instead of raw `useEffect`
- [ ] No CSS `@keyframes` mixed with Motion
- [ ] `layout` prop used correctly (not on every element)
- [ ] ScrollTrigger instances cleaned up on unmount

### Step 5: Generate Report

Format findings as:

```markdown
## Animation Audit Report

### Summary
- Files scanned: {N}
- Errors: {N} ❌
- Warnings: {N} ⚠️
- Bundle compliance: ✅ / ❌

### Critical Issues
1. **{file}** (line {N}): {issue} — {fix}

### Recommendations
- {suggestion 1}
- {suggestion 2}
```

## constraints

- NEVER skip the audit for "quick fixes" — animation bugs compound silently.
- NEVER treat warnings as optional — they predict future errors.
- NEVER audit only the happy path — check error states, loading states, and reduced motion.
- NEVER forget to check cleanup — unmounted GSAP ScrollTriggers leak memory.

## examples

### Example 1: CI Audit Failure

**Input:** "Run animation audit on our Next.js project."

**Output:**
```markdown
## Animation Audit Report

### Summary
- Files scanned: 67
- Errors: 4 ❌
- Warnings: 12 ⚠️
- Bundle compliance: ❌ (3 files exceed 5KB budget)

### Critical Issues
1. **src/app/page.tsx** (line 1): Missing 'use client' directive — Motion components won't hydrate
2. **src/components/Modal.tsx** (line 23): `exit` prop without AnimatePresence — modal disappears instantly on close
3. **src/components/CardList.tsx** (line 8): Full motion import (34KB) for simple hover — exceeds budget
4. **src/app/layout.tsx** (line 45): GSAP ScrollTrigger created but not cleaned up — memory leak

### Fixes Required
1. Add `"use client"` to all files using Motion components
2. Wrap modal in `<AnimatePresence mode="wait">`
3. Refactor CardList to use `useAnimate` mini (2.3KB)
4. Add `ctx.revert()` or use `useGSAP()` auto-cleanup

### Recommendations
- Add animation audit to pre-commit hooks
- Create a shared `ReducedMotionProvider` for consistent a11y
- Document bundle budget per route in README
```

## references

- `references/audit-rules.md` — Full rule definitions with code examples
- `references/ci-integration.md` — Pre-commit hook, GitHub Action, and pipeline setup
