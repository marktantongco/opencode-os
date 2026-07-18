# Description Optimization Guide

The `description` field in SKILL.md frontmatter is the **primary trigger mechanism**. It determines whether an AI agent invokes your skill. A bad description means a dead skill — no matter how good the instructions are.

## How Triggering Works

1. At startup, the agent scans all available skills and loads only `name` + `description` (~100 tokens per skill)
2. When the user gives a task, the agent checks: "Does any skill description match this task?"
3. If yes → full skill loads. If no → skill stays dormant.

**Critical insight:** The agent only consults skills for tasks it can't easily handle on its own. Simple one-step queries ("read this file") won't trigger skills regardless of description quality. Complex, multi-step, or specialized queries reliably trigger skills when the description matches.

## The Under-Triggering Problem

Agents tend to "under-trigger" — they don't use skills even when they'd be useful. To combat this:

### 1. Be Pushy

Instead of passive language, use active, inclusive phrasing:

❌ **Passive:** `How to build dashboards for internal data.`
✅ **Pushy:** `How to build dashboards for internal data. Make sure to use this skill whenever the user mentions dashboards, data visualization, internal metrics, or wants to display any kind of company data, even if they don't explicitly ask for a 'dashboard.'`

### 2. Include Synonyms and Related Terms

Users won't use your exact vocabulary. Cover the semantic space:

❌ **Narrow:** `Generate React components with TypeScript.`
✅ **Broad:** `Generate React components with TypeScript. Use when the user asks to create a new component, build a UI element, scaffold a React module, or needs boilerplate for forms, tables, modals, charts, or data displays. Also trigger for "make a button", "create a card", "build a dashboard widget", or any UI scaffolding request.`

### 3. Mention Edge Cases and Adjacent Domains

Include cases where this skill should win over competing skills:

```yaml
description: >
  Process and analyze CSV data with validation and transformation.
  Use when the user mentions CSV, Excel, spreadsheet, data cleaning,
  format conversion, or data processing. Also trigger for "merge these files",
  "calculate statistics", "clean this data", or when .csv/.xlsx files are shared.
  Always use for data tasks — do not process data without this skill.
```

### 4. Specify "Always Use" Clauses

For critical skills, explicitly tell the agent to prefer this skill:

```yaml
description: >
  Security review for code changes. Check for secrets, injection risks,
  and vulnerability patterns. Always use this skill for any security-related
  code review — do not review security-sensitive code without it.
```

## Description Structure Template

```yaml
description: >
  {What this skill does in one sentence}.
  Use when {trigger condition 1}, {trigger condition 2}, or {trigger condition 3}.
  Also trigger for {related term 1}, {related term 2}, {related term 3}, and {edge case}.
  {Pushy clause: Always use this skill for X — do not do X without it.}
```

## Length Guidelines

| Metric | Minimum | Ideal | Maximum |
|---|---|---|---|
| Characters | 100 | 200-400 | 800 |
| Words | 15 | 30-60 | 120 |

- **Too short (< 50 chars):** Vague, won't match anything
- **Too long (> 800 chars):** Dilutes signal, may confuse trigger logic

## Testing Descriptions

Before finalizing, test with these 20 eval queries (10 should-trigger, 10 should-not-trigger):

### Should-Trigger Examples (realistic, detailed)

Good eval queries include:
- File paths, personal context, backstory
- Casual speech, typos, abbreviations
- Different lengths and formality levels
- Cases where the user doesn't explicitly name the skill

**Example good query:**
```json
{"query": "ok so my boss just sent me this xlsx file (its in my downloads, called something like 'Q4 sales final FINAL v2.xlsx') and she wants me to add a column that shows the profit margin as a percentage. The revenue is in column C and costs are in column D i think", "should_trigger": true}
```

**Example bad query (too easy):**
```json
{"query": "Format this data", "should_trigger": true}
```

### Should-Not-Trigger Examples (near-misses, tricky)

The most valuable negative cases are **genuinely tricky** — not obviously irrelevant:

```json
{"query": "Can you write a Python script that reads a CSV and prints the first 5 rows? I just want to see what's in it.", "should_trigger": false}
```

Why? The user wants a quick preview, not full data processing. A simple `Read` + `Bash` handles this.

```json
{"query": "I need to create a dashboard for my personal fitness tracking. I have CSV files from my Apple Watch.", "should_trigger": false}
```

Why? Personal fitness ≠ internal business data. Wrong domain.

## Optimization Checklist

- [ ] Description includes what the skill does
- [ ] Description includes 3+ specific trigger conditions
- [ ] Description includes 3+ synonyms/related terms
- [ ] Description includes at least one "always use" or "make sure to use" clause
- [ ] Description mentions edge cases where this skill wins
- [ ] Description is 100-800 characters
- [ ] Description is written for an AI making a binary decision, not a human reading docs
- [ ] Tested with 10 should-trigger queries (varied phrasing, some casual/typo-ridden)
- [ ] Tested with 10 should-not-trigger queries (near-misses, adjacent domains)
- [ ] Skill triggers correctly on ≥ 80% of eval queries
