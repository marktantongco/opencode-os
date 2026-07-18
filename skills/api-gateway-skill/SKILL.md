---
name: api-gateway-skill
description: >
  API gateway orchestration skill — design, deploy, and manage API gateways with rate limiting, authentication, request transformation, and observability for AI-powered microservices. Use when use when building api gateways, managing rate limiting for ai services, implementing authentication layers for multi-provider ai endpoints, or designing microservice api architectures
  Triggers on keywords: api, gateway, rate-limit, authentication, microservice, proxy, observability.
allowed-tools: Read, Write, Bash, Edit, Grep, Glob
user-invocable: true
mcp-servers: [filesystem, github, docker]
---

# API Gateway Skill

## context

API gateway orchestration skill — design, deploy, and manage API gateways with rate limiting, authentication, request/response transformation, and observability for AI-powered microservices. Acts as the front-door orchestrator for all AI provider endpoints, providing unified access control, traffic management, and operational visibility. Complements proxy stacks by adding application-layer intelligence that raw proxy routing cannot provide.

## instructions

### Step 1: Gateway Architecture Design

1. **Identify service topology** — map all AI microservices and their endpoints
2. **Define routing rules** — URL patterns, header-based routing, weight-based canary
3. **Select authentication strategy** — API key, OAuth2, JWT, mTLS, or hybrid
4. **Design rate limiting** — per-user, per-service, per-provider, global quotas

### Step 2: Gateway Configuration

1. **Route definitions** — configure upstream targets and path matching:
   ```yaml
   routes:
     - path: /v1/chat/completions
       upstream: claude-provider
       methods: [POST]
       rate_limit: 100/min
       auth: jwt
     - path: /v1/generate
       upstream: gemini-provider
       methods: [POST]
       rate_limit: 60/min
       auth: api-key
   ```
2. **Middleware stack** — configure request/response pipeline:
   - Authentication middleware
   - Rate limiting middleware
   - Request transformation (header injection, body rewriting)
   - Response caching
   - Logging and metrics
3. **Health checks** — per-upstream liveness and readiness probes

### Step 3: Integration with Proxy Stack

1. **9Router/OpenRelay** — gateway sits above proxy stack as L7 orchestrator
2. **Owl Proxy Defense** — gateway delegates anti-bot concerns to Owl
3. **Combined Proxy Billing** — gateway exports per-route metrics for billing
4. **Secret Vault** — gateway retrieves credentials from vault, never stores locally

### Step 4: Generate Gateway Specification

```markdown
## API Gateway Specification

### Architecture
- Gateway implementation: [Kong/Nginx/Go/custom]
- Deployment: [Docker/Kubernetes/binary]
- Protocols: HTTP/1.1, HTTP/2, WebSocket

### Routes
| Path | Upstream | Rate Limit | Auth | Methods |
|------|----------|------------|------|---------|
| /v1/chat | Claude | 100/min | JWT | POST |
| /v1/generate | Gemini | 60/min | API-Key | POST |

### Middleware
- [x] Authentication (JWT + API-Key)
- [x] Rate limiting (sliding window)
- [x] Request transformation
- [x] Response caching (TTL: 300s)
- [x] Logging (structured JSON)
- [x] Metrics (Prometheus format)

### Security
- TLS 1.3 minimum
- CORS configured per route
- Input validation on all endpoints
- Secret vault integration verified

### Observability
- Health endpoint: GET /health
- Metrics endpoint: GET /metrics
- Log format: structured JSON
- Alert rules: 5xx rate > 1%, latency P99 > 5s
```

## constraints

- NEVER expose upstream service URLs directly — all traffic must go through the gateway.
- NEVER store API keys or secrets in gateway configuration — use the secret vault.
- NEVER disable rate limiting in production — protect upstream services from abuse.
- ALWAYS implement circuit breakers for all upstream services.
- ALWAYS validate and sanitize all incoming requests before forwarding.
- ALWAYS maintain request tracing IDs for end-to-end observability.

## examples

### Example: Multi-Provider AI Gateway

**Input:** "Set up an API gateway for Claude and Gemini with JWT auth and rate limiting"

**Output:**
```markdown
## API Gateway Specification

### Architecture
- Gateway implementation: Go custom gateway
- Deployment: Docker container
- Protocols: HTTP/1.1, HTTP/2

### Routes
| Path | Upstream | Rate Limit | Auth | Methods |
|------|----------|------------|------|---------|
| /v1/chat/completions | Claude | 100/min | JWT | POST |
| /v1/models/generate | Gemini | 60/min | JWT | POST |

### Security
- TLS 1.3 enforced
- JWT validation with RS256
- Rate limiting: sliding window, 429 on exceed
- Secret vault: all keys retrieved at runtime

### Observability
- Health: GET /health → 200 OK
- Metrics: GET /metrics → Prometheus
- Logs: structured JSON with trace IDs
```
