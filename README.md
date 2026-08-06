# OpenCode OS

> Your all-in-one AI agent platform — 276 skills, 20 agents, 223 MCP servers, 9 pre-built stacks. Operating doctrine: **System Master Prompt v8.0 Adaptive Kernel**.

[![Config & Doctrine Check](https://github.com/marktantongco/opencode-os/actions/workflows/config-doctrine-check.yml/badge.svg)](https://github.com/marktantongco/opencode-os/actions/workflows/config-doctrine-check.yml)

OpenCode OS is a unified platform that turns [opencode](https://opencode.ai) into a powerful AI agent system. It combines two open-source repositories into one cohesive toolkit with skills, agents, MCP servers, and workflows — all pre-configured and ready to use.

---

## Quick Start (5 minutes)

### Prerequisites

- [opencode CLI](https://opencode.ai) installed
- Node.js 20+ (for the web app)
- Git

### Step 1: Clone the repo

```bash
git clone https://github.com/marktantongco/opencode-os.git
cd opencode-os
```

### Step 2: Open in opencode

```bash
opencode
```

That's it. opencode will automatically discover:
- **276 skills** in `skills/` (symlinked to `.opencode/skills/`) — loaded on-demand when you use them
- **20 agents** in `agents/` (symlinked to `.opencode/agents/`) — available via `@mention`
- **AGENTS.md** — loaded as project instructions
- **11 MCP servers** — pre-configured in `opencode.jsonc`

### Step 2b: Set up git hooks (recommended)

```bash
make setup-hooks
```

Installs shared pre-commit hooks (via `core.hooksPath`) that run on every commit, scoped to the files you stage:

- **Agent model audit** — `opencode.jsonc` agent↔model assignments vs `profiles/MODEL_ASSIGNMENT_MATRIX.md` (runs when `opencode.jsonc` / the matrix / the audit script change)
- **v8.0 doctrine compliance** — flags v5-era closing patterns (`⚡⚡`, `🔗 Hidden Assumption`, unconditional `✨ 3 Suggestions`, `Zero fluff`, `RESPONSE FRAMEWORK`) across `skills/`, `agents/`, `profiles/` (frozen v4/v5.1 profiles are exempt)
- **Config drift** — `opencode.jsonc` must stay in sync with `models.yaml` (runs when either changes)

Requires Python deps: `pip install json5 pyyaml` (the hook skips with a warning if missing).

**Manual checks:** `make audit` · `make check-doctrine` · `make check-config`

**CI:** the same three checks run on every push/PR via the [Config & Doctrine Check](https://github.com/marktantongco/opencode-os/actions/workflows/config-doctrine-check.yml) workflow.

### Step 3: Try it

Once opencode is running, try these:

```
@orchestrator help me plan a new project
@blueprint design the architecture for a web app
@explorer find all animation-related skills
```

Or use slash commands (if configured):
```
/plan "build a landing page"
/research "best MCP servers for data pipelines"
```

---

## What's Inside

### 276 Skills

Skills are reusable AI workflows. They're loaded on-demand when you need them.

```
@explorer find skills for animation
```

Then use a skill by name:
```
@orchestrator run the gsap-animator skill to create a scroll animation
```

### 20 Agents

Agents are specialized AI assistants you can call with `@name`. All models use the **Zen Free** provider (no API keys needed).

| Agent | Type | Model | What it does |
|-------|------|-------|-------------|
| `@orchestrator` | primary | mimo-v2.5-free | Coordinates everything — your main assistant |
| `@blueprint` | primary | north-mini-code-free | Strategic planning and architecture design |
| `@explorer` | subagent | laguna-s-2.1-free | Searches codebases and finds patterns |
| `@librarian` | subagent | laguna-s-2.1-free | Looks up documentation and APIs |
| `@oracle` | subagent | mimo-v2.5-free | Strategic technical advice |
| `@designer` | subagent | laguna-s-2.1-free | UI/UX design |
| `@fixer` | subagent | north-mini-code-free | Code refinement and optimization |
| `@observer` | subagent | deepseek-v4-flash-free | System monitoring and metrics |
| `@council` | subagent | longcat-2.0-free | Multi-perspective deliberation |
| `@researcher` | subagent | mimo-v2.5-free | Web research and analysis |
| `@brainstorming` | subagent | longcat-2.0-free | Creative ideation |
| `@plan` | subagent | north-mini-code-free | Plan structure validation |
| `@compaction` | subagent | ling-3.0-flash-free | Context compression and session compaction |
| `@owl-dns` | subagent | laguna-s-2.1-free | Web scraping with proxy rotation |
| `@browser-use` | subagent | ling-3.0-flash-free | Natural-language browser automation |
| `@agent-browser` | subagent | ling-3.0-flash-free | Structured CDP browser automation |
| `@oracle-lite` | subagent | deepseek-v4-flash-free | Strategic advice (lightweight) |
| `@designer-lite` | subagent | deepseek-v4-flash-free | UI/UX design (lightweight) |
| `@observer-lite` | subagent | deepseek-v4-flash-free | System monitoring (lightweight) |
| `@council-lite` | subagent | deepseek-v4-flash-free | Deliberation (lightweight) |

### Step 3: Set up environment variables

Copy the example env file and fill in your keys:

```bash
cp .env.example .env.local
```

Required for some MCP servers:
- `GITHUB_TOKEN` — for the GitHub MCP server
- `CONTEXT7_API_KEY` — for the Context7 MCP server
- `DATABASE_URL` — for the Postgres MCP server (optional)

### Step 4: Run the web app (optional)

```bash
npm install
npm run dev
```

Opens at `http://localhost:3000` — a PWA with the Knowledge-Base catalog and layered animation demo.

---

## What is OpenCode OS?

OpenCode OS is a **ready-to-use AI agent platform** for [opencode](https://opencode.ai). It gives you:

- **276 skills** — reusable AI workflows for animation, design, development, research, content, infrastructure, and more
- **20 agents** — specialized AI assistants you can call with `@name`
- **223 MCP servers** — tools your agents can use (databases, APIs, browsers, etc.)
- **9 pre-built MCP stacks** — curated server combinations with synergy scoring
- **35 agent workflows** — battle-tested patterns for common tasks
- **A Next.js PWA** — web app with skill catalog and animation demos
- **Configuration-as-code** — `models.yaml` single source of truth with `make` targets for audit/fix/generate

It's the result of merging two popular opencode repositories:
- **opencodelinux** (214 skills, breadth-first)
- **opencode-accomplishments** (108 skills, depth-focused system architecture)

---

## How It Works

### The 3-Layer Architecture

```
┌─────────────────────────────────────────────────┐
│                   opencode CLI                   │
│  (your AI assistant — reads .opencode/ config)   │
└──────────────────────┬──────────────────────────┘
                        │
┌───────────────────────┴──────────────────────────┐
│              opencode-os Repository               │
│                                                   │
│  .opencode/agents/    → 17 specialized AI agents  │
│  .opencode/skills/    → 276 reusable workflows    │
│  opencode.jsonc       → MCP servers + config      │
│  AGENTS.md            → Operating doctrine         │
└───────────────────────┬──────────────────────────┘
                        │
┌───────────────────────┴──────────────────────────┐
│              MCP Servers (tools)                   │
│  GitHub, Postgres, Puppeteer, Memory,              │
│  Sequential Thinking, Context7, Podman, ...        │
└──────────────────────────────────────────────────┘
```

### Agents

Call any agent with `@name`:

```
@orchestrator build a React component
@blueprint design the database schema
@explorer find all animation skills
@researcher research the best MCP servers for data pipelines
```

### Skills

Skills are reusable AI workflows. They're loaded on-demand:

```
@orchestrator run the gsap-animator skill
@orchestrator use the deployment-manager skill to deploy this app
```

### MCP Servers

MCP servers give your agents superpowers — databases, browsers, GitHub, memory, and more. 11 are pre-configured in `opencode.jsonc`. Enable/disable them in your config.

---

## Architecture

```
opencode-os/
│
├── .opencode/              ← opencode auto-discovers this
│   ├── agents/ → ../agents/    20 agent definitions
│   ├── skills/ → ../skills/    276 skill directories
│   ├── commands/               Custom slash commands
│   ├── plugins/                Plugin hooks
│   └── tools/                  Custom tools
│
├── skills/                  276 skill directories
│   ├── animation-*          Animation pipeline
│   ├── agent-*              7-agent MASTER pipeline
│   ├── design-*             Design system skills
│   ├── infra-*              Infrastructure & proxy skills
│   ├── research-*           Research & analysis skills
│   └── ...                  11 categories total
│
├── agents/                  20 agent definitions (symlinked to .opencode/)
├── models.yaml              ← Single source of truth for agent models
├── profiles/                10 role profiles (loaded as instructions)
├── workflows/               4 workflow definitions (loaded as instructions)
├── scripts/                 Audit + generation scripts
│   ├── audit_agent_models.py   Audit / fix / generate-matrix
│   ├── generate_config.py      models.yaml → opencode.jsonc
│   └── restore_models.sh       Point-in-time recovery
├── Makefile                 make audit / fix / matrix / generate-config
├── app/                     Next.js 15 PWA
├── public/                  Static assets (PWA manifest, KB HTML)
├── AGENTS.md                Operating doctrine (loaded as instructions)
├── stacks.json              9 MCP stack configs with synergy scoring
├── mcp-registry.json        223 free MCP servers across 15 categories
└── opencode.jsonc           Platform configuration (generated from models.yaml)
```

---

## Agents

Agents are specialized AI assistants. Call any agent with `@name` in opencode.

### Primary Agents (your main assistants)

| Agent | Model | What it does |
|-------|-------|-------------|
| `@orchestrator` | mimo-v2.5-free | Coordinates everything — task decomposition, multi-agent workflows |
| `@blueprint` | north-mini-code-free | Strategic planning, architecture design, research synthesis |

### Subagents (call with @name)

| Agent | Model | What it does |
|-------|-------|-------------|
| `@explorer` | laguna-s-2.1-free | Searches codebases and finds patterns |
| `@librarian` | laguna-s-2.1-free | Looks up documentation and APIs |
| `@oracle` | mimo-v2.5-free | Strategic technical advice |
| `@designer` | laguna-s-2.1-free | UI/UX design |
| `@fixer` | north-mini-code-free | Code refinement and optimization |
| `@observer` | deepseek-v4-flash-free | System monitoring |
| `@council` | longcat-2.0-free | Multi-perspective deliberation |
| `@researcher` | mimo-v2.5-free | Web research and analysis |
| `@brainstorming` | longcat-2.0-free | Creative ideation |
| `@plan` | north-mini-code-free | Plan structure validation |
| `@compaction` | ling-3.0-flash-free | Context compression |
| `@owl-dns` | laguna-s-2.1-free | Web scraping with proxy rotation |
| `@browser-use` | ling-3.0-flash-free | Natural-language browser automation |
| `@agent-browser` | ling-3.0-flash-free | Structured CDP browser automation |
| `@oracle-lite` | deepseek-v4-flash-free | Strategic advice (lightweight) |
| `@designer-lite` | deepseek-v4-flash-free | UI/UX design (lightweight) |
| `@observer-lite` | deepseek-v4-flash-free | System monitoring (lightweight) |
| `@council-lite` | deepseek-v4-flash-free | Deliberation (lightweight) |
| `@council` | claude-sonnet-4-6 | Multi-perspective deliberation |
| `@researcher` | deepseek-v4-flash-free | Web research and analysis |
| `@brainstorming` | deepseek-v4-flash-free | Creative ideation |
| `@plan` | deepseek-v4-flash-free | Plan structure validation |
| `@compaction` | deepseek-v4-flash-free | Context compression |
| `@oracle-lite` | qwen3.6-plus-free | Lightweight strategic advice |
| `@designer-lite` | qwen3.6-plus-free | Lightweight design |
| `@observer-lite` | qwen3.6-plus-free | Lightweight monitoring |
| `@council-lite` | qwen3.6-plus-free | Lightweight deliberation |

### How agents work

1. **Primary agents** (`@orchestrator`, `@blueprint`) are your main assistants. They have full tool access.
2. **Subagents** are specialists you call for specific tasks. They have limited permissions.
3. Agents can call other agents — `@orchestrator` can delegate to `@explorer` to search, then `@designer` to build.

---

## Skills

Skills are reusable AI workflows. Each skill is a `SKILL.md` file with:
- **context** — when to use it
- **instructions** — step-by-step workflow
- **constraints** — hard rules
- **examples** — sample output

### Skill categories

| Category | Count | What you can do |
|----------|-------|-----------------|
| Animation | 24 | Motion, GSAP, Three.js animations |
| Agent | 18 | MASTER pipeline, decision agents |
| Design | 22 | UI/UX, landing pages, Supanova engine |
| Development | 31 | TDD, deployment, browser automation |
| Research | 15 | Deep research, feature analysis |
| Infrastructure | 18 | Proxy stacks, routing, secrets |
| Content | 12 | SEO, social media, humanizer |
| Data | 14 | Web reader, audit analyzer |
| Creative | 8 | Photography AI, output formatting |
| MCP | 11 | Builder, curator, security scanner |
| System | 19 | Memory, context compressor, roles |

### How skills work

1. opencode discovers skills from `.opencode/skills/` (symlinked to `skills/`)
2. When you ask for something, opencode suggests relevant skills
3. You call a skill: `@orchestrator run the <skill-name> skill`
4. The skill's `SKILL.md` guides the AI through the workflow

---

## MCP Servers

MCP servers give your agents tools to interact with the world. 11 are pre-configured:

| Server | What it does | Enabled |
|--------|-------------|---------|
| `sequential-thinking` | Step-by-step reasoning chains | ✅ |
| `memory` | Persistent knowledge storage | ✅ |
| `github` | GitHub API access | ✅ (needs GITHUB_TOKEN) |
| `puppeteer` | Browser automation | ✅ |
| `podman` | Container management | ✅ |
| `context7` | Always-current API docs | ✅ (needs CONTEXT7_API_KEY) |
| `mcp-search` | Web search | ✅ |
| `pictoflux-ai` | AI image generation | ✅ |
| `mcp-catalog` | MCP server catalog | ✅ |
| `mcp-security-scanner` | Security auditing | ✅ |
| `postgres` | Database access | ❌ (disabled, needs DATABASE_URL) |

### MCP Stacks

9 pre-built server combinations with synergy scores. Each stack pairs 4 servers that work well together:

| Stack | Synergy | Servers | Best for |
|-------|---------|---------|----------|
| Full-Stack Web Studio | 94 | filesystem, github, vercel, postgres | Building web apps |
| DevOps Command Center | 92 | github, docker, kubernetes, slack | Infrastructure |
| AI Research Lab | 91 | brave-search, fetch, memory, sqlite | Research |
| Data Pipeline Studio | 89 | postgres, sqlite, fetch, filesystem | Data work |
| Mobile App Workshop | 88 | filesystem, github, fetch, memory | Mobile dev |
| Content Engine | 87 | filesystem, brave-search, google-drive, slack | Content creation |
| Security Audit Toolkit | 86 | filesystem, github, brave-search, docker | Security |
| Creative Studio | 85 | filesystem, fetch, google-drive, slack | Creative work |
| Unified AI Gateway | 96 | filesystem, github, docker, fetch | Infrastructure |

---

## Skills

Skills are reusable AI workflows. Each skill has a `SKILL.md` file with:
- **context** — when to use it
- **instructions** — step-by-step workflow
- **constraints** — hard rules
- **examples** — sample output

### How to use a skill

```
@orchestrator run the deployment-manager skill to deploy this project
```

The AI reads the skill's `SKILL.md` and follows its instructions.

### Skill categories

| Category | Count | Example skills |
|----------|-------|---------------|
| Animation | 24 | gsap-animator, motion-animator, threejs-orchestrator |
| Agent | 18 | agent-master, agent-decision, agent-simulator |
| Design | 22 | supanova-premium-aesthetic, landing-page-generator |
| Development | 31 | mcp-builder, deployment-manager, browser-use |
| Research | 15 | deep-research, jtbd-research, feature-research |
| Infrastructure | 18 | 9router-gateway, owl-proxy-defense, secret-vault |
| Content | 12 | seo-content-writer, humanizer, social-media-manager |
| Data | 14 | web-reader, audit-analyzer, explore |
| Creative | 8 | photography-ai, output-formatter |
| MCP | 11 | mcp-builder, mcp-stack-curator, mcp-security-scanner |
| System | 19 | persistent-memory, context-compressor, feedback-loop |

---

## MCP Servers

MCP servers give your agents tools to interact with the world. 11 are pre-configured:

| Server | What it does | How to enable |
|--------|-------------|--------------|
| `sequential-thinking` | Step-by-step reasoning chains | Enabled by default |
| `memory` | Persistent knowledge storage | Enabled by default |
| `github` | GitHub API access | Set `GITHUB_TOKEN` env var |
| `puppeteer` | Browser automation | Enabled by default |
| `podman` | Container management | Enabled by default |
| `context7` | Always-current API docs | Set `CONTEXT7_API_KEY` env var |
| `mcp-search` | Web search | Enabled by default |
| `pictoflux-ai` | AI image generation | Enabled by default |
| `mcp-catalog` | MCP server catalog | Enabled by default |
| `mcp-security-scanner` | Security auditing | Enabled by default |
| `postgres` | Database access | Disabled (set DATABASE_URL to enable) |

### MCP Stacks

9 pre-built server combinations with synergy scoring. Each stack pairs 4 servers that work well together:

| Stack | Synergy | Servers | Best for |
|-------|---------|---------|----------|
| Full-Stack Web Studio | 94 | filesystem, github, vercel, postgres | Building web apps |
| DevOps Command Center | 92 | github, docker, kubernetes, slack | Infrastructure |
| AI Research Lab | 91 | brave-search, fetch, memory, sqlite | Research |
| Data Pipeline Studio | 89 | postgres, sqlite, fetch, filesystem | Data work |
| Mobile App Workshop | 88 | filesystem, github, fetch, memory | Mobile dev |
| Content Engine | 87 | filesystem, brave-search, google-drive, slack | Content |
| Security Audit Toolkit | 86 | filesystem, github, brave-search, docker | Security |
| Creative Studio | 85 | filesystem, fetch, google-drive, slack | Creative |
| Unified AI Gateway | 96 | filesystem, github, docker, fetch | Infrastructure |

---

## Configuration

### opencode.jsonc

The main config file at the project root. It defines:

- **20 agents** with their models, permissions, and system prompts
- **11 MCP servers** with connection details
- **11 plugins** for extended functionality
- **Skills paths** — where to find skills
- **Instructions** — additional context files to load

### models.yaml (single source of truth)

Agent model assignments are defined in `models.yaml` and synced to `opencode.jsonc`:

```bash
# Edit models.yaml, then regenerate config
make generate-config

# Audit for drift
make audit

# Fix drift automatically
make fix
```

The full pipeline: `models.yaml` → `generate_config.py` → `opencode.jsonc` → `audit_agent_models.py` → `MODEL_ASSIGNMENT_MATRIX.md` → CI enforces sync.

### Environment variables

| Variable | Required for | How to get it |
|----------|-------------|---------------|
| `GITHUB_TOKEN` | GitHub MCP server | GitHub Settings → Developer settings → Personal access tokens |
| `CONTEXT7_API_KEY` | Context7 MCP server | https://context7.com |
| `DATABASE_URL` | Postgres MCP server | Your database connection string |

### Customizing agents

Edit `opencode.jsonc` to change agent models, permissions, or prompts:

```jsonc
"agent": {
  "orchestrator": {
    "model": "anthropic/claude-sonnet-4-5",  // change model
    "permission": { "edit": "allow", "bash": "allow" }
  }
}
```

### Adding MCP servers

Add to the `"mcp"` section of `opencode.jsonc`:

```jsonc
"mcp": {
  "my-server": {
    "type": "local",
    "command": ["npx", "-y", "@org/mcp-server"],
    "enabled": true
  }
}
```

Browse the full catalog of 223 servers in `mcp-registry.json`.

---

## MCP Stacks

9 pre-built server combinations. Each stack pairs 4 servers that work well together:

| Stack | Synergy | Servers | Best for |
|-------|---------|---------|----------|
| Full-Stack Web Studio | 94 | filesystem, github, vercel, postgres | Building web apps |
| DevOps Command Center | 92 | github, docker, kubernetes, slack | Infrastructure |
| AI Research Lab | 91 | brave-search, fetch, memory, sqlite | Research |
| Data Pipeline Studio | 89 | postgres, sqlite, fetch, filesystem | Data work |
| Mobile App Workshop | 88 | filesystem, github, fetch, memory | Mobile dev |
| Content Engine | 87 | filesystem, brave-search, google-drive, slack | Content |
| Security Audit Toolkit | 86 | filesystem, github, brave-search, docker | Security |
| Creative Studio | 85 | filesystem, fetch, google-drive, slack | Creative |
| Unified AI Gateway | 96 | filesystem, github, docker, fetch | Infrastructure |

To use a stack, enable its servers in `opencode.jsonc`:

```jsonc
"mcp": {
  "memory": { "type": "local", "command": ["npx", "-y", "@modelcontextprotocol/server-memory"], "enabled": true },
  "sequential-thinking": { "type": "local", "command": ["npx", "-y", "@modelcontextprotocol/server-sequential-thinking"], "enabled": true }
}
```

---

## MCP Registry

The `mcp-registry.json` file catalogs **223 free MCP servers** across 15 categories. This is a reference catalog — not auto-loaded. To use any server from the registry, add it to the `"mcp"` section of your `opencode.jsonc`.

Browse the registry:
```
@explorer read the mcp-registry.json file and find servers for data pipelines
```

---

## Web App

The repo includes a Next.js 15 PWA with:

- **Knowledge-Base** (`/`) — browse all 276 skills with search and filters
- **Knowledge-Base HTML** (`/kb.html`) — standalone HTML version
- **Layered Animation Demo** (`/demo`) — Three.js + GSAP + Framer Motion demo
- **MCP Stack Curator** — interactive stack exploration

```bash
npm install
npm run dev
```

---

## Customization

### Add your own agent

Create `.opencode/agents/my-agent.md`:

```markdown
---
description: My custom agent
mode: subagent
model: opencode/deepseek-v4-flash-free
---
You are a custom agent that specializes in...
```

### Add your own skill

Create `.opencode/skills/my-skill/SKILL.md`:

```markdown
---
name: my-skill
description: What this skill does
---

## context
When to use this skill

## instructions
Step-by-step workflow

## constraints
Hard rules

## examples
Sample output
```

### Add an MCP server

Edit `opencode.jsonc`:

```jsonc
"mcp": {
  "my-server": {
    "type": "local",
    "command": ["npx", "-y", "@org/mcp-server"],
    "enabled": true
  }
}
```

Browse the full catalog of 223 servers in `mcp-registry.json`.

---

## MCP Stacks

9 pre-built server combinations with synergy scoring:

| Stack | Synergy | Servers | Best for |
|-------|---------|---------|----------|
| Full-Stack Web Studio | 94 | filesystem, github, vercel, postgres | Building web apps |
| DevOps Command Center | 92 | github, docker, kubernetes, slack | Infrastructure |
| AI Research Lab | 91 | brave-search, fetch, memory, sqlite | Research |
| Data Pipeline Studio | 89 | postgres, sqlite, fetch, filesystem | Data work |
| Mobile App Workshop | 88 | filesystem, github, fetch, memory | Mobile dev |
| Content Engine | 87 | filesystem, brave-search, google-drive, slack | Content |
| Security Audit Toolkit | 86 | filesystem, github, brave-search, docker | Security |
| Creative Studio | 85 | filesystem, fetch, google-drive, slack | Creative |
| Unified AI Gateway | 96 | filesystem, github, docker, fetch | Infrastructure |

---

## Customization

### Add your own agent

Create `.opencode/agents/my-agent.md`:

```markdown
---
description: My custom agent
mode: subagent
model: opencode/deepseek-v4-flash-free
---
You are a custom agent that specializes in...
```

### Add your own skill

Create `.opencode/skills/my-skill/SKILL.md`:

```markdown
---
name: my-skill
description: What this skill does
---

## context
When to use this skill

## instructions
Step-by-step workflow

## constraints
Hard rules

## examples
Sample output
```

### Add an MCP server

Edit `opencode.jsonc`:

```jsonc
"mcp": {
  "my-server": {
    "type": "local",
    "command": ["npx", "-y", "@org/mcp-server"],
    "enabled": true
  }
}
```

Browse the full catalog of 223 servers in `mcp-registry.json`.

---

## Web App

The repo includes a Next.js 15 PWA at `https://opencode-os.vercel.app`:

- **Knowledge-Base** — browse all 276 skills with search and filters
- **Layered Animation Demo** (`/demo`) — Three.js + GSAP + Framer Motion
- **MCP Stack Curator** — interactive stack exploration

Run locally:

```bash
npm install
npm run dev
```

---

## Operating Doctrine

The `AGENTS.md` file defines how AI agents should behave in this project. It runs on the **System Master Prompt v8.0 Adaptive Kernel** (supersedes v5):

- **Compiled execution** — every word triggers action/constraint/state; responses open with `[Mode: X+Y | Conf: 0.0-1.0 | Gates: All/None | TOK: X]`
- **State machine** — PREP (default) → DISCOVERY (exception) → EXECUTE → VALIDATE → REVIEW → COMPLETE, with ROLLBACK when assumptions break
- **Quality gates** — Clarity, Code, Reasoning, Efficiency (<2000-token output), Safety; ✨ suggestions are design/architecture-only (skipped on pure code)
- **Silent Protocol** — parse the real need, find blind spots, give the simplest true answer
- **JSON telemetry** — sessions self-report `turns` / `pruned` / `next_check`
- **No one-off work** — if you do something twice, it should become a skill

---

## Customization

### Change agent models

Edit `opencode.jsonc`:

```jsonc
"agent": {
  "orchestrator": {
    "model": "anthropic/claude-sonnet-4-5",  // change this
    "permission": { "edit": "allow", "bash": "allow" }
  }
}
```

### Add MCP servers

Browse `mcp-registry.json` for 223 servers, then add to `opencode.jsonc`:

```jsonc
"mcp": {
  "my-server": {
    "type": "local",
    "command": ["npx", "-y", "@org/mcp-server"],
    "enabled": true
  }
}
```

### Create custom commands

Create `.opencode/commands/deploy.md`:

```markdown
---
description: Deploy the app to production
---
Run the deployment pipeline:
1. Build: `npm run build`
2. Deploy: `vercel --prod`
3. Verify: check https://opencode-os.vercel.app
```

Then use `/deploy` in opencode.

---

## Web App

The Next.js PWA is live at **https://opencode-os.vercel.app**:

- **Knowledge-Base** — browse all 276 skills with search and filters
- **Layered Animation Demo** (`/demo`) — Three.js + GSAP + Framer Motion
- **MCP Stack Curator** — interactive stack exploration

Run locally:

```bash
npm install
npm run dev
```

---

## Troubleshooting

### "Skills not found"

Make sure `.opencode/skills` is a symlink to `skills/`:

```bash
ls -la .opencode/skills
# Should show: .opencode/skills -> ../skills
```

### "Agent not found"

Agents are defined in `opencode.jsonc` under the `"agent"` key. Make sure the name matches:

```
@orchestrator    → matches "orchestrator" in config
@blueprint       → matches "blueprint" in config
```

### "MCP server not found"

The server needs to be in the `"mcp"` section of `opencode.jsonc`. Check the name matches exactly.

### "Command not found"

Custom commands go in `.opencode/commands/`. Create a `.md` file there and restart opencode.

---

## Advanced

### The 7-Agent MASTER Pipeline

The `agent-master` skill orchestrates 7 specialized agents in sequence:

1. **MASTER** — orchestrates all agents
2. **DECISION** — routes tasks to the right specialist
3. **SIMULATOR** — dry-runs implementations
4. **AUDITOR** — validates against standards
5. **PROFILER** — finds actual bottlenecks
6. **OPTIMIZER** — applies targeted fixes
7. **MAINTENANCE** — monitors production

### Operating Doctrine

The `AGENTS.md` file defines how AI agents behave (System Master Prompt **v8.0 Adaptive Kernel**):

- **Compiled execution** — responses open with `[Mode: X+Y | Conf | Gates | TOK]`
- **Quality gates** — Clarity, Code, Reasoning, Efficiency, Safety; ✨ skipped on pure code
- **Silent Protocol** — parse the real need, find blind spots
- **State machine** — PREP → EXECUTE → VALIDATE → REVIEW → COMPLETE (ROLLBACK)
- **No one-off work** — if you do something twice, it becomes a skill

---

## Troubleshooting

### "Skills not found"

Make sure `.opencode/skills` is a symlink:

```bash
ls -la .opencode/skills
# → .opencode/skills -> ../skills
```

If missing, recreate it:

```bash
ln -sf ../skills .opencode/skills
```

### "Agent not found"

Agents are defined in `opencode.jsonc` under `"agent"`. The name must match what you type:

```
@orchestrator  → "orchestrator" in config
@blueprint     → "blueprint" in config
```

### "MCP server not found"

The server must be in the `"mcp"` section of `opencode.jsonc`. Check the name matches exactly.

### "Command not found"

Custom commands go in `.opencode/commands/`. Create a `.md` file there and restart opencode.

---

## Advanced

### The 7-Agent MASTER Pipeline

The `agent-master` skill orchestrates 7 agents in sequence:

1. **MASTER** — orchestrates all agents
2. **DECISION** — routes tasks to the right specialist
3. **SIMULATOR** — dry-runs implementations
4. **AUDITOR** — validates against standards
5. **PROFILER** — finds actual bottlenecks
6. **OPTIMIZER** — applies targeted fixes
7. **MAINTENANCE** — monitors production

### Operating Doctrine

The `AGENTS.md` file defines how AI agents behave in this project (System Master Prompt **v8.0 Adaptive Kernel**). Key principles:

- **Compiled execution** — responses open with `[Mode: X+Y | Conf | Gates | TOK]`; prune unfired logic
- **Quality gates** — Clarity, Code, Reasoning, Efficiency, Safety; ✨ suggestions design/architecture-only
- **Silent Protocol** — parse the real need, find blind spots, give the simplest true answer
- **State machine** — PREP → EXECUTE → VALIDATE → REVIEW → COMPLETE (ROLLBACK)
- **No one-off work** — if you do something twice, it becomes a skill

---

## Links

- **GitHub**: https://github.com/marktantongco/opencode-os
- **Vercel**: https://opencode-os.vercel.app
- **opencode**: https://opencode.ai
- **MCP Registry**: 223 servers in `mcp-registry.json`

---

## License

MIT
