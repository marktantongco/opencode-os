---
name: openrelay-go
description: >
  Go-based open relay proxy server — high-performance, concurrent relay proxy written in Go with connection pooling, load balancing, health checking, and zero-config auto-discovery for AI provider endpoints. Use when use when building high-performance proxy relays, implementing go-based ai model routing, or setting up zero-config relay servers for multi-provider ai access
  Triggers on keywords: go, relay, proxy, openrelay, high-performance, concurrent, load-balance.
allowed-tools: Read, Write, Bash, Edit, Grep, Glob
user-invocable: true
mcp-servers: [filesystem, github, docker]
---

# OpenRelay Go

## context

Go-based open relay proxy server — high-performance, concurrent relay proxy written in Go with connection pooling, intelligent load balancing, health checking, and zero-config auto-discovery for AI provider endpoints. Designed as the Go-native alternative to the TypeScript-based 9Router, offering superior concurrency handling, lower memory footprint, and native binary deployment without Node.js runtime dependencies.

## instructions

### Step 1: Build and Deploy

1. **Prerequisites** — Go 1.22+, make, docker (optional)
2. **Build the binary** — `go build -o openrelay ./cmd/openrelay`
3. **Configure providers** — auto-discovery or manual provider endpoints:
   ```yaml
   providers:
     claude:
       endpoint: https://api.anthropic.com
       auth: vault:claude-api-key
       pool_size: 50
     gemini:
       endpoint: https://generativelanguage.googleapis.com
       auth: vault:gemini-api-key
       pool_size: 30
   ```
4. **Set up connection pooling** — configure per-provider pool sizes and timeouts

### Step 2: Configure Load Balancing

1. **Strategy selection** — choose from:
   - Round-robin: simple, even distribution
   - Least-connections: route to least busy connection
   - Weighted: distribute based on provider capacity
   - Latency-based: route to fastest-responding provider
2. **Health checks** — configure per-provider liveness probes:
   - Interval: 30s default
   - Timeout: 5s default
   - Unhealthy threshold: 3 consecutive failures
3. **Circuit breaker** — set per-provider failure thresholds

### Step 3: Integration with Existing Stack

1. **9Router replacement** — configure as drop-in replacement for 9Router
2. **Triune integration** — add as third relay in Triune proxy stack
3. **Secret Vault** — integrate with existing credential vault
4. **Combined Proxy Billing** — export usage metrics for billing aggregation

### Step 4: Generate Deployment Specification

```markdown
## OpenRelay Go Deployment Specification

### Architecture
- Binary: openrelay (Go 1.22+, statically linked)
- Memory: ~20MB base, ~50MB under load
- Goroutines: 1000+ concurrent connections per core
- Latency overhead: <1ms per relay hop

### Configuration
- Providers: [list with pool sizes]
- Load balancer: [strategy]
- Health check interval: [interval]
- Circuit breaker threshold: [threshold]

### Performance Benchmarks
| Metric | Value |
|--------|-------|
| Throughput | [requests/sec] |
| P50 Latency | [ms] |
| P99 Latency | [ms] |
| Memory (idle) | [MB] |
| Memory (loaded) | [MB] |

### Integration Status
- [ ] 9Router compatibility verified
- [ ] Triune stack integration tested
- [ ] Secret Vault credentials loaded
- [ ] Billing metrics exporting correctly
```

## constraints

- NEVER hardcode provider endpoints — use auto-discovery or configuration files.
- NEVER disable health checks in production — always verify provider availability.
- NEVER accept unencrypted connections for API key transmission — TLS required.
- ALWAYS use connection pooling — never create a new connection per request.
- ALWAYS implement graceful shutdown — drain in-flight requests before terminating.
- ALWAYS benchmark performance after configuration changes.

## examples

### Example: Deployment with Claude and Gemini

**Input:** "Deploy OpenRelay Go with Claude and Gemini providers using least-connections strategy"

**Output:**
```markdown
## OpenRelay Go Deployment Specification

### Architecture
- Binary: openrelay v1.0.0 (Go 1.22, statically linked)
- Memory: ~18MB base, ~45MB under load
- Goroutines: 1200 concurrent connections per core

### Configuration
- Providers: Claude (pool: 50), Gemini (pool: 30)
- Load balancer: least-connections
- Health check interval: 30s
- Circuit breaker threshold: 5 failures in 60s

### Performance Benchmarks
| Metric | Value |
|--------|-------|
| Throughput | 8,400 req/sec |
| P50 Latency | 2.1ms |
| P99 Latency | 8.7ms |
| Memory (idle) | 18MB |
| Memory (loaded) | 45MB |
```
