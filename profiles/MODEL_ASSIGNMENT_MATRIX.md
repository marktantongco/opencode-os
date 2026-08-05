# OpenCode Agent + Skill Model Assignment Matrix

> **Version**: 20.0 (Auto-Generated)
> **Date**: 2026-08-06
> **Status**: Auto-Generated from opencode.jsonc
> **Source**: `opencode.jsonc` (single source of truth)

---

## Model Tier Hierarchy

| Tier | Model ID | Display Name | Strength | Token Budget | Use Case |
|------|----------|--------------|----------|-------------|----------|
| **Mid** | `zen/deepseek-v4-flash-free` | Deepseek V4 Flash Free | Fast general purpose | 4,400 | `council-lite`, `designer-lite`, `observer` (+2 more) |
| **Premium** | `zen/laguna-s-2.1-free` | Laguna S 2.1 Free | Deep reasoning, balanced, or creative | 4,400–6,100 | `designer`, `explorer`, `librarian` (+1 more) |
| **Lightweight** | `zen/ling-3.0-flash-free` | Ling 3.0 Flash Free | Fastest, token-efficient | 2,000 | `agent-browser`, `browser-use`, `compaction` |
| **Premium** | `zen/longcat-2.0-free` | Longcat 2.0 Free | Deep reasoning, balanced, or creative | 4,400–6,100 | `brainstorming`, `council` |
| **Premium** | `zen/mimo-v2.5-free` | Mimo V2.5 Free | Deep reasoning, balanced, or creative | 4,400–6,100 | `oracle`, `orchestrator`, `researcher` |
| **Code-Spec** | `zen/north-mini-code-free` | North Mini Code Free | Code-specialized, efficient | 3,100 | `blueprint`, `fixer`, `plan` |

---

## Agent → Model Mapping (20 Agents)

| Agent | Mode | Model | Tier | Rationale |
|-------|------|-------|------|-----------|
| `agent-browser` | subagent | `zen/ling-3.0-flash-free` | Lightweight | Structured CDP browser automation |
| `blueprint` | primary | `zen/north-mini-code-free` | Code-Spec | Spec-first architecture, plan grammar |
| `brainstorming` | subagent | `zen/longcat-2.0-free` | Premium | Divergent thinking + ideation |
| `browser-use` | subagent | `zen/ling-3.0-flash-free` | Lightweight | Natural-language browser automation |
| `compaction` | subagent | `zen/ling-3.0-flash-free` | Lightweight | Token-efficient context compression |
| `council` | subagent | `zen/longcat-2.0-free` | Premium | Creative multi-perspective deliberation |
| `council-lite` | subagent | `zen/deepseek-v4-flash-free` | Mid | Fallback — general purpose |
| `designer` | subagent | `zen/laguna-s-2.1-free` | Premium | Balanced for visual design + frontend |
| `designer-lite` | subagent | `zen/deepseek-v4-flash-free` | Mid | Fallback — general purpose |
| `explorer` | subagent | `zen/laguna-s-2.1-free` | Premium | Balanced code understanding + pattern discovery |
| `fixer` | subagent | `zen/north-mini-code-free` | Code-Spec | Code refinement + refactoring efficiency |
| `librarian` | subagent | `zen/laguna-s-2.1-free` | Premium | Balanced doc retrieval + API interpretation |
| `observer` | subagent | `zen/deepseek-v4-flash-free` | Mid | Fast monitoring, no deep reasoning needed |
| `observer-lite` | subagent | `zen/deepseek-v4-flash-free` | Mid | Fallback — general purpose |
| `oracle` | subagent | `zen/mimo-v2.5-free` | Premium | Strategic advice needs deep reasoning |
| `oracle-lite` | subagent | `zen/deepseek-v4-flash-free` | Mid | Fallback — general purpose |
| `orchestrator` | primary | `zen/mimo-v2.5-free` | Premium | Task decomposition + subagent dispatch needs deep reasoning |
| `owl-dns` | subagent | `zen/laguna-s-2.1-free` | Premium | Scraping + data interpretation |
| `plan` | subagent | `zen/north-mini-code-free` | Code-Spec | Plan grammar validation |
| `researcher` | subagent | `zen/mimo-v2.5-free` | Premium | Web research + synthesis |

---

## Source

This file is auto-generated from `opencode.jsonc`.
To change agent model assignments, edit `opencode.jsonc` and run:
```
python3 scripts/audit_agent_models.py --generate-matrix
```
