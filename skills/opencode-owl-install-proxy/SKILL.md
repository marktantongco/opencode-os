---
name: opencode-owl-install-proxy
description: >
  OpenCode-optimized Owl proxy installer — automated setup of Owl proxy defense stack for OpenCode CLI with pre-configured tier routing, anti-bot escalation, and credential vaulting. Use when use when installing owl proxy for opencode cli, configuring anti-bot defense for ai coding agents, or setting up tier-based routing for opencode workflows
  Triggers on keywords: opencode, owl, install, proxy, setup, anti-bot, tier-routing.
allowed-tools: Read, Write, Bash, Edit, Grep, Glob
user-invocable: true
mcp-servers: [filesystem, github, docker]
---

# OpenCode Owl Install Proxy

## context

OpenCode-optimized Owl proxy installer — automated setup of Owl proxy defense stack tailored for OpenCode CLI. Configures 5-tier protocol escalation (HTTP/1.1 core, JA3/WS browser on demand), per-provider routing rules, and integrated credential vaulting. This skill bridges the OpenCode coding agent with the Owl proxy defense infrastructure, ensuring seamless AI model access through hardened, anti-bot-resilient proxy layers.

## instructions

### Step 1: Environment Assessment

1. Verify OpenCode CLI is installed and configured (`opencode --version`)
2. Check existing proxy configuration in `~/.opencode/config.json`
3. Identify target AI providers (Claude, Gemini, GPT, etc.) and their endpoint URLs
4. Assess network environment — corporate firewall, residential, or cloud

### Step 2: Owl Proxy Stack Installation

1. **Clone and build** the Owl proxy defense stack from the repository
2. **Configure tiers** — set up 5-tier escalation:
   - Tier 1: HTTP/1.1 standard requests (lowest profile)
   - Tier 2: HTTP/2 with header rotation
   - Tier 3: JA3 TLS fingerprint spoofing
   - Tier 4: WebSocket browser emulation
   - Tier 5: Full headless browser with session continuity
3. **Set up per-provider routing rules** — map each AI provider to its optimal tier
4. **Configure circuit breaker** — set thresholds for auto-escalation and fallback

### Step 3: OpenCode Integration

1. **Modify OpenCode config** — point API endpoints to local Owl proxy
2. **Set up credential vault** — store API keys with age encryption
3. **Configure token refresh** — staggered OAuth rotation for multi-account setups
4. **Test connectivity** — verify each provider route through the proxy stack

### Step 4: Generate Installation Report

```markdown
## OpenCode Owl Proxy Installation Report

### Environment
- OpenCode version: [detected version]
- Network type: [assessed type]
- Target providers: [list of providers]

### Proxy Configuration
- Owl version: [installed version]
- Active tiers: [1-5 based on setup]
- Circuit breaker threshold: [configured value]
- Credential vault: [status]

### Provider Routing
| Provider | Endpoint | Tier | Status |
|----------|----------|------|--------|
| Claude   | [url]    | [tier] | [ok/fail] |
| Gemini   | [url]    | [tier] | [ok/fail] |

### Health Verification
- [ ] All providers accessible through proxy
- [ ] Tier escalation tested and working
- [ ] Circuit breaker triggers correctly
- [ ] Credential vault encryption verified
- [ ] Token refresh cycle tested
```

## constraints

- NEVER expose raw API keys in configuration files — always use the credential vault.
- NEVER bypass tier escalation to force a higher tier — let the circuit breaker decide.
- NEVER disable the circuit breaker — it is the last line of defense against IP bans.
- ALWAYS test proxy connectivity before marking installation as complete.
- ALWAYS rotate credentials on a schedule — never use static tokens indefinitely.
- ALWAYS verify the Owl proxy defense version is compatible with OpenCode CLI version.

## examples

### Example: Full Installation

**Input:** "Install Owl proxy for OpenCode CLI with Claude and Gemini providers"

**Output:**
```markdown
## OpenCode Owl Proxy Installation Report

### Environment
- OpenCode version: 0.4.2
- Network type: residential
- Target providers: Claude (Anthropic), Gemini (Google)

### Proxy Configuration
- Owl version: 2.1.0
- Active tiers: 1-3 (HTTP/1.1, HTTP/2, JA3)
- Circuit breaker threshold: 5 failures in 60s
- Credential vault: active (age encryption)

### Provider Routing
| Provider | Endpoint | Tier | Status |
|----------|----------|------|--------|
| Claude   | https://api.anthropic.com | 2 | ok |
| Gemini   | https://generativelanguage.googleapis.com | 1 | ok |

### Health Verification
- [x] All providers accessible through proxy
- [x] Tier escalation tested and working
- [x] Circuit breaker triggers correctly
- [x] Credential vault encryption verified
- [x] Token refresh cycle tested
```
