---
name: openhuman-owl-install-proxy
description: >
  OpenHuman-optimized Owl proxy installer — automated setup of Owl proxy defense stack for OpenHuman agent platform with human-in-the-loop escalation, consent-gated tier progression, and privacy-first credential management. Use when use when installing owl proxy for openhuman platform, configuring privacy-first anti-bot defense for human-agent workflows, or setting up consent-gated proxy escalation
  Triggers on keywords: openhuman, owl, install, proxy, privacy, consent, human-in-the-loop.
allowed-tools: Read, Write, Bash, Edit, Grep, Glob
user-invocable: true
mcp-servers: [filesystem, github, docker]
---

# OpenHuman Owl Install Proxy

## context

OpenHuman-optimized Owl proxy installer — automated setup of Owl proxy defense stack tailored for the OpenHuman agent platform. Unlike the OpenCode variant, this installation emphasizes human-in-the-loop consent gates for tier escalation, privacy-first credential management with zero-knowledge encryption, and audit trails for every proxy action. Designed for environments where human oversight of automated agent actions is a requirement, not an option.

## instructions

### Step 1: Environment Assessment

1. Verify OpenHuman platform is installed and running (`openhuman status`)
2. Check existing proxy and privacy configuration in `~/.openhuman/config.yaml`
3. Identify target AI providers and their data residency requirements (GDPR, CCPA)
4. Assess compliance requirements — SOC2, HIPAA, or organizational policies

### Step 2: Owl Proxy Stack Installation (Privacy-First)

1. **Clone and build** the Owl proxy defense stack with privacy extensions
2. **Configure consent-gated tiers** — each tier escalation requires human approval:
   - Tier 1: HTTP/1.1 standard requests (auto-approved, lowest risk)
   - Tier 2: HTTP/2 with header rotation (requires notification)
   - Tier 3: JA3 TLS fingerprint spoofing (requires explicit consent)
   - Tier 4: WebSocket browser emulation (requires explicit consent + reason)
   - Tier 5: Full headless browser (requires manager-level approval)
3. **Set up zero-knowledge credential vault** — keys encrypted client-side, never transmitted
4. **Configure audit logging** — every proxy action logged with timestamp, tier, and consent status

### Step 3: OpenHuman Integration

1. **Modify OpenHuman config** — route agent API calls through Owl proxy
2. **Set up consent UI hooks** — integrate with OpenHuman's approval dashboard
3. **Configure privacy zones** — define which data types bypass proxy (PII, medical, legal)
4. **Test consent flow** — verify escalation triggers consent prompt correctly
5. **Set up breach detection** — alert if proxy detects unauthorized data exfiltration

### Step 4: Generate Installation Report

```markdown
## OpenHuman Owl Proxy Installation Report

### Environment
- OpenHuman version: [detected version]
- Compliance requirements: [GDPR/CCPA/SOC2/HIPAA]
- Data residency: [region(s)]

### Proxy Configuration
- Owl version: [installed version]
- Consent tier: enabled (gated escalation)
- Zero-knowledge vault: [status]
- Audit logging: [status]

### Consent Gates
| Tier | Protocol | Consent Level | Auto-Escalate |
|------|----------|---------------|---------------|
| 1    | HTTP/1.1 | Auto-approved | No |
| 2    | HTTP/2   | Notification  | After 30s     |
| 3    | JA3      | Explicit      | No            |
| 4    | WS       | Explicit+Reason | No          |
| 5    | Browser  | Manager       | No            |

### Privacy Verification
- [ ] Zero-knowledge encryption verified
- [ ] Consent flow tested end-to-end
- [ ] Audit trail completeness verified
- [ ] Privacy zones configured and tested
- [ ] Breach detection alerts firing correctly
```

## constraints

- NEVER auto-escalate to Tier 3+ without explicit human consent.
- NEVER store credentials in plaintext — zero-knowledge encryption is mandatory.
- NEVER disable audit logging — every proxy action must be traceable.
- ALWAYS respect data residency requirements when routing through proxy tiers.
- ALWAYS provide a human-readable explanation for each tier escalation request.
- ALWAYS maintain a separate audit trail from the OpenCode variant.

## examples

### Example: Privacy-First Installation

**Input:** "Install Owl proxy for OpenHuman with GDPR compliance and Claude provider"

**Output:**
```markdown
## OpenHuman Owl Proxy Installation Report

### Environment
- OpenHuman version: 1.2.0
- Compliance requirements: GDPR
- Data residency: EU-West

### Proxy Configuration
- Owl version: 2.1.0-privacy
- Consent tier: enabled (gated escalation)
- Zero-knowledge vault: active (age + client-side)
- Audit logging: active (append-only, 90-day retention)

### Consent Gates
| Tier | Protocol | Consent Level | Auto-Escalate |
|------|----------|---------------|---------------|
| 1    | HTTP/1.1 | Auto-approved | No            |
| 2    | HTTP/2   | Notification  | After 30s     |
| 3    | JA3      | Explicit      | No            |

### Privacy Verification
- [x] Zero-knowledge encryption verified
- [x] Consent flow tested end-to-end
- [x] Audit trail completeness verified
- [x] Privacy zones configured (PII bypass active)
- [x] Breach detection alerts firing correctly
```
