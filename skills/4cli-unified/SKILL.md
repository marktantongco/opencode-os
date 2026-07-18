---
name: 4cli-unified
description: >
  Unified meta-CLI wrapper for OpenCode + Claude Code + Codex + Gemini CLI — one command for four agents with 9Router tier routing and unified credential vault. Use when use when managing multiple ai coding clis, setting up unified routing across opencode/claude/codex/gemini, or building credential vaults
  Triggers on keywords: cli, unified, opencode, claude, codex, gemini, owl.
allowed-tools: Read, Write, Bash, Edit, Grep, Glob
user-invocable: true
mcp-servers: [filesystem, github, docker]
---

# Unified Meta-CLI

## context

Unified meta-CLI wrapper for OpenCode + Claude Code + Codex CLI + Gemini CLI. Provides consistent interface across AI coding assistants with shared config and history. This skill provides infrastructure-as-code patterns and operational procedures that ensure reliability, security, and observability of critical infrastructure components.

## instructions

### Step 1: Assess Infrastructure Requirements

1. Identify the infrastructure need — routing, proxying, credential management, or CLI orchestration
2. Determine deployment target — local, cloud, or hybrid
3. Map dependencies — what services, APIs, or systems must be accessible
4. Establish SLOs — uptime, latency, and error rate targets

### Step 2: Design Infrastructure Layer

1. **Architecture** — Define the component topology and data flow
2. **Configuration** — Set up environment-specific configuration with secrets management
3. **Health checks** — Implement liveness, readiness, and startup probes
4. **Failover** — Design redundancy with automatic recovery procedures

### Step 3: Generate Infrastructure Specification

```markdown
## Infrastructure Specification

### Architecture
Component diagram and data flow description

### Configuration
- Environment variables: list with descriptions
- Secrets: list with rotation policy
- Resource limits: CPU, memory, disk

### Health and Monitoring
- Liveness: health check endpoint and interval
- Readiness: dependency connectivity check
- Metrics: key metrics to track
- Alerts: threshold-based alerting rules

### Failover Procedures
- Primary failure: automatic recovery steps
- Cascading failure: circuit breaker behavior
- Full outage: manual recovery runbook
```

### Step 4: Operational Readiness

- [ ] Configuration is externalized and documented
- [ ] Secrets are encrypted at rest and in transit
- [ ] Health checks cover all critical dependencies
- [ ] Failover is tested and automated
- [ ] Monitoring and alerting are configured
- [ ] Runbook exists for common failure scenarios

## constraints

- NEVER store secrets in code or configuration files — use a vault.
- NEVER deploy without health checks and monitoring.
- NEVER assume network reliability — design for failure at every layer.
- ALWAYS test failover procedures before relying on them.
- ALWAYS maintain audit logs for all credential access.

## examples

### Example: Infrastructure Setup

**Input:** "Use when managing multiple AI coding CLIs, setting up unified routing across OpenCode/Claude/Codex/Gemini, or building credential vaults"

**Output:**
```markdown
## Infrastructure Specification

### Architecture
Multi-layer 4cli unified with automatic failover between primary and backup endpoints.

### Configuration
- PRIMARY_ENDPOINT: configured via environment
- FALLBACK_ENDPOINT: configured via environment
- MAX_RETRIES: 3
- TIMEOUT_MS: 5000

### Health and Monitoring
- Liveness: GET /health every 30s
- Readiness: Dependency connectivity check
- Metrics: request_rate, error_rate, latency_p99
- Alerts: error_rate exceeding threshold for 2 minutes

### Failover Procedures
- Primary failure: Auto-switch to fallback within 5s
- Both down: Queue requests, retry every 30s
- Recovery: Auto-switch back to primary when healthy
```
