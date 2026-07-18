# OpenCode OS

> Unified AI Agent Platform — 276 skills, 9 MCP stacks, 223 MCP servers, 35 agent workflows, 7-agent MASTER pipeline

## What This Is

OpenCode OS merges two independent AI agent repositories into a single, cohesive platform:

- **opencodelinux** (OCL) — 214 skills, breadth-first skill library
- **opencode-accomplishments** (OCA) — 108 skills, depth-focused system architecture with Next.js PWA

## Architecture

```
opencode-os/
├── skills/              276 skill directories (deduplicated)
│   ├── animation-*      Animation pipeline (Motion + GSAP + Three.js)
│   ├── agent-*          7-agent MASTER pipeline
│   ├── design-*         Design system skills
│   ├── infra-*          Infrastructure & proxy skills
│   ├── research-*       Research & analysis skills
│   └── ...              11 categories total
├── agents/              35 agent workflow files
├── profiles/            10 role profiles
├── scripts/             5 operational scripts
├── workflows/           4 workflow definitions
├── app/                 Next.js 15 PWA (layered animation demo)
├── components/          React components (LayeredAnimationStack)
├── public/              Static assets (PWA manifest, SW, KB HTML)
├── AGENTS.md            Operating doctrine + structural map (v5)
├── stacks.json          9 MCP stack configs with synergy scoring (v10.0)
├── mcp-registry.json    223 free MCP servers across 15 categories (v3.0)
└── opencode.jsonc       Platform configuration
```

## Quick Start

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Validate skills
npm run skills:validate

# Index skills
npm run skills:index

# Audit MCP registry
npm run mcp:audit
```

## Skills Categories

| Category | Count | Focus |
|----------|-------|-------|
| Animation | 24 | Motion, GSAP, Three.js orchestration |
| Agent | 18 | MASTER pipeline, decision, simulation |
| Design | 22 | UI/UX, landing pages, Supanova engine |
| Development | 31 | TDD, deployment, browser automation |
| Research | 15 | Deep research, JTBD, feature analysis |
| Infrastructure | 18 | Proxy stacks, routing, secrets |
| Content | 12 | SEO, social media, humanizer |
| Data | 14 | Web reader, audit analyzer, data pipeline |
| Creative | 8 | Photography AI, output formatting |
| MCP | 11 | Builder, curator, security scanner |
| System | 19 | Memory, context compressor, roles |

## MCP Stacks

9 pre-built server combinations with synergy scoring:

| Stack | Synergy | Servers |
|-------|---------|---------|
| Full-Stack Web Studio | 94 | filesystem, github, vercel, postgres |
| DevOps Command Center | 92 | github, docker, kubernetes, slack |
| AI Research Lab | 91 | brave-search, fetch, memory, sqlite |
| Data Pipeline Studio | 89 | postgres, sqlite, fetch, filesystem |
| Mobile App Workshop | 88 | filesystem, github, fetch, memory |
| Content Engine | 87 | filesystem, brave-search, google-drive, slack |
| Security Audit Toolkit | 86 | filesystem, github, brave-search, docker |
| Creative Studio | 85 | filesystem, fetch, google-drive, slack |

## Agent System

7 functional agents orchestrated by a MASTER pipeline:

| Agent | Role |
|-------|------|
| MASTER | Orchestrates all agents in sequence |
| DECISION | Routes tasks to the right specialist |
| SIMULATOR | Dry-runs implementations |
| AUDITOR | Validates against standards |
| PROFILER | Finds actual bottlenecks |
| OPTIMIZER | Applies targeted fixes |
| MAINTENANCE | Monitors production |

## Operating Doctrine

Zero fluff. Working code. Alignment > execution. Advocacy. Quality gated. Show reasoning. Depth before speed.

See [AGENTS.md](./AGENTS.md) for the full operational doctrine and structural map.

## License

MIT
