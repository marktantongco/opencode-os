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

| Agent | Mode | Model | Prompt | Tier | Rationale |
|-------|------|-------|--------|------|-----------|
| `agent-browser` | subagent | `zen/ling-3.0-flash-free` | `{file:./agents/agent-browser.md}` | Lightweight | Structured CDP browser automation |
| `blueprint` | primary | `zen/north-mini-code-free` | `{file:./agents/blueprint.md}` | Code-Spec | Spec-first architecture, plan grammar |
| `brainstorming` | subagent | `zen/longcat-2.0-free` | `{file:./agents/brainstorming.md}` | Premium | Divergent thinking + ideation |
| `browser-use` | subagent | `zen/ling-3.0-flash-free` | `{file:./agents/browser-use.md}` | Lightweight | Natural-language browser automation |
| `compaction` | subagent | `zen/ling-3.0-flash-free` | `{file:./agents/compaction.md}` | Lightweight | Token-efficient context compression |
| `council` | subagent | `zen/longcat-2.0-free` | `{file:./agents/council.md}` | Premium | Creative multi-perspective deliberation |
| `council-lite` | subagent | `zen/deepseek-v4-flash-free` | `{file:./agents/council-lite.md}` | Mid | Fallback — general purpose |
| `designer` | subagent | `zen/laguna-s-2.1-free` | `{file:./agents/designer.md}` | Premium | Balanced for visual design + frontend |
| `designer-lite` | subagent | `zen/deepseek-v4-flash-free` | `{file:./agents/designer-lite.md}` | Mid | Fallback — general purpose |
| `explorer` | subagent | `zen/laguna-s-2.1-free` | `{file:./agents/explorer.md}` | Premium | Balanced code understanding + pattern discovery |
| `fixer` | subagent | `zen/north-mini-code-free` | `{file:./agents/fixer.md}` | Code-Spec | Code refinement + refactoring efficiency |
| `librarian` | subagent | `zen/laguna-s-2.1-free` | `{file:./agents/librarian.md}` | Premium | Balanced doc retrieval + API interpretation |
| `observer` | subagent | `zen/deepseek-v4-flash-free` | `{file:./agents/observer.md}` | Mid | Fast monitoring, no deep reasoning needed |
| `observer-lite` | subagent | `zen/deepseek-v4-flash-free` | `{file:./agents/observer-lite.md}` | Mid | Fallback — general purpose |
| `oracle` | subagent | `zen/mimo-v2.5-free` | `{file:./agents/oracle.md}` | Premium | Strategic advice needs deep reasoning |
| `oracle-lite` | subagent | `zen/deepseek-v4-flash-free` | `{file:./agents/oracle-lite.md}` | Mid | Fallback — general purpose |
| `orchestrator` | primary | `zen/mimo-v2.5-free` | `{file:./agents/orchestrator.md}` | Premium | Task decomposition + subagent dispatch needs deep reasoning |
| `owl-dns` | subagent | `zen/laguna-s-2.1-free` | `You are an expert web scraping operator using owl-dns v5.1. Use owl-dns fetch <url> for single URLs, owl-dns batch <file> for bulk, owl-dns discover for proxy auto-discovery, and owl-dns doctor for capability diagnostics.` | Premium | Scraping + data interpretation |
| `plan` | subagent | `zen/north-mini-code-free` | `{file:./agents/plan.md}` | Code-Spec | Plan grammar validation |
| `researcher` | subagent | `zen/mimo-v2.5-free` | `{file:./agents/researcher.md}` | Premium | Web research + synthesis |

---

## Source

This file is auto-generated from `opencode.jsonc`.
To change agent model assignments, edit `opencode.jsonc` and run:
```
python3 scripts/audit_agent_models.py --generate-matrix
```
