# OpenCode OS

> Your all-in-one AI agent platform — 276 skills, 17 agents, 223 MCP servers, 9 pre-built stacks

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
- **276 skills** in `.opencode/skills/` — loaded on-demand when you use them
- **17 agents** in `.opencode/agents/` — available via `@mention`
- **AGENTS.md** — loaded as project instructions
- **11 MCP servers** — pre-configured in `opencode.jsonc`

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

### 17 Agents

Agents are specialized AI assistants you can call with `@name`:

| Agent | Type | What it does |
|-------|------|-------------|
| `@orchestrator` | primary | Coordinates everything — your main assistant |
| `@blueprint` | primary | Strategic planning and architecture design |
| `@explorer` | subagent | Searches codebases and finds patterns |
| `@librarian` | subagent | Looks up documentation and APIs |
| `@oracle` | subagent | Strategic technical advice |
| `@designer` | subagent | UI/UX design |
| `@fixer` | subagent | Code refinement and optimization |
| `@observer` | subagent | System monitoring and metrics |
| `@council` | subagent | Multi-perspective deliberation |
| `@researcher` | subagent | Web research and analysis |
| `@brainstorming` | subagent | Creative ideation |
| `@plan` | subagent | Plan structure validation |

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
- **17 agents** — specialized AI assistants you can call with `@name`
- **223 MCP servers** — tools your agents can use (databases, APIs, browsers, etc.)
- **9 pre-built MCP stacks** — curated server combinations with synergy scoring
- **35 agent workflows** — battle-tested patterns for common tasks
- **A Next.js PWA** — web app with skill catalog and animation demos

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
│   ├── agents/ → ../agents/    17 agent definitions
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
├── agents/                  17 agent definitions (symlinked to .opencode/)
├── profiles/                10 role profiles (loaded as instructions)
├── workflows/               4 workflow definitions (loaded as instructions)
├── app/                     Next.js 15 PWA
├── public/                  Static assets (PWA manifest, KB HTML)
├── AGENTS.md                Operating doctrine (loaded as instructions)
├── stacks.json              9 MCP stack configs with synergy scoring
├── mcp-registry.json        223 free MCP servers across 15 categories
└── opencode.jsonc           Platform configuration
```

---

## Agents

Agents are specialized AI assistants. Call any agent with `@name` in opencode.

### Primary Agents (your main assistants)

| Agent | Model | What it does |
|-------|-------|-------------|
| `@orchestrator` | deepseek-v4-flash-free | Coordinates everything — task decomposition, multi-agent workflows |
| `@blueprint` | nemotron-3-super-free | Strategic planning, architecture design, research synthesis |

### Subagents (call with @name)

| Agent | Model | What it does |
|-------|-------|-------------|
| `@explorer` | deepseek-v4-flash-free | Searches codebases and finds patterns |
| `@librarian` | deepseek-v4-flash-free | Looks up documentation and APIs |
| `@oracle` | claude-opus-4-7 | Strategic technical advice |
| `@designer` | gpt-5.5 | UI/UX design |
| `@fixer` | deepseek-v4-flash-free | Code refinement and optimization |
| `@observer` | gpt-5.5 | System monitoring |
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

- **17 agents** with their models, permissions, and system prompts
- **11 MCP servers** with connection details
- **11 plugins** for extended functionality
- **Skills paths** — where to find skills
- **Instructions** — additional context files to load

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

The `AGENTS.md` file defines how AI agents should behave in this project:

- **Zero fluff** — working code only, no placeholders
- **Quality gates** — every response is checked before submission
- **Silent Protocol** — parse the real need, find blind spots, give the simplest true answer
- **Depth-seeking** — for complex problems, show reasoning and alternatives
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

The `AGENTS.md` file defines how AI agents behave:

- **Zero fluff** — working code only, no placeholders
- **Quality gates** — every response checked before submission
- **Silent Protocol** — parse the real need, find blind spots
- **Depth-seeking** — show reasoning, explore alternatives
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

The `AGENTS.md` file defines how AI agents behave in this project. Key principles:

- **Zero fluff** — working code only, no pseudocode, no placeholders
- **Quality gates** — every response checked before submission
- **Silent Protocol** — parse the real need, find blind spots, give the simplest true answer
- **Depth-seeking** — for complex problems, show reasoning and explore alternatives
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
