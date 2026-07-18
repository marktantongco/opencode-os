---
name: combined-proxy-billing
description: >
  Unified billing and cost management for multi-proxy stacks — aggregates usage, cost, and quota data across 9Router, Owl, Antigravity, and Triune proxies with per-provider spend tracking, budget alerts, and optimization recommendations. Use when use when managing billing across multiple proxy stacks, tracking ai model costs across providers, or optimizing proxy stack spending
  Triggers on keywords: billing, cost, proxy, quota, budget, optimization, spend.
allowed-tools: Read, Write, Bash, Edit, Grep, Glob
user-invocable: true
mcp-servers: [filesystem, github, docker]
---

# Combined Proxy Billing

## context

Unified billing and cost management for multi-proxy stacks — aggregates usage metrics, cost data, and quota information across all proxy layers (9Router, Owl Proxy Defense, Antigravity, and Triune Proxy Stack). Provides a single dashboard for per-provider spend tracking, budget alerts, cost anomaly detection, and optimization recommendations. Designed for teams running multiple AI proxy layers who need financial visibility and control.

## instructions

### Step 1: Proxy Stack Inventory

1. Discover all active proxy stacks in the environment
2. For each stack, identify:
   - AI providers being routed through
   - Current billing plans (free-tier, paid, enterprise)
   - API key associations and quota limits
3. Map the cost structure — per-request, per-token, flat-rate, or hybrid

### Step 2: Usage Data Aggregation

1. **Collect metrics** from each proxy stack:
   - 9Router: request counts, tier distribution, failover frequency
   - Owl Proxy: tier escalation counts, protocol distribution
   - Antigravity: account rotation frequency, MITM interception rate
   - Triune: redundancy utilization, health check frequency
2. **Normalize data** — standardize units (requests, tokens, GB, hours)
3. **Calculate costs** — apply pricing models to usage data
4. **Detect anomalies** — flag spending that deviates from baseline by >20%

### Step 3: Budget Management

1. **Set budgets** — per-provider, per-stack, and overall limits
2. **Configure alerts** — warning at 80%, critical at 95%, hard stop at 100%
3. **Track quotas** — free-tier limits, rate limits, and throttling thresholds
4. **Generate forecasts** — project monthly spend based on current trajectory

### Step 4: Generate Billing Report

```markdown
## Combined Proxy Billing Report

### Period: [date range]

### Summary
- Total Spend: $[amount]
- Budget Utilization: [percentage]%
- Largest Provider: [name] ($[amount])
- Cost Trend: [increasing/stable/decreasing]

### Per-Stack Breakdown
| Stack | Requests | Tokens | Cost | Budget % |
|-------|----------|--------|------|----------|
| 9Router   | [count] | [count] | $[amt] | [%] |
| Owl Proxy | [count] | [count] | $[amt] | [%] |
| Antigravity | [count] | [count] | $[amt] | [%] |
| Triune    | [count] | [count] | $[amt] | [%] |

### Per-Provider Breakdown
| Provider | Requests | Cost | Free Tier Remaining | Paid Tier |
|----------|----------|------|---------------------|-----------|
| Claude   | [count]  | $[amt] | [%]               | [plan]    |
| Gemini   | [count]  | $[amt] | [%]               | [plan]    |
| GPT      | [count]  | $[amt] | [%]               | [plan]    |

### Optimization Recommendations
1. [Recommendation with estimated savings]
2. [Recommendation with estimated savings]

### Alerts
- [Active alert: description]
- [Active alert: description]
```

## constraints

- NEVER expose billing API keys in reports — use masked references.
- NEVER aggregate billing data across different organizations without consent.
- NEVER delete historical billing data — maintain audit trail for 7 years minimum.
- ALWAYS calculate costs using the latest pricing from each provider.
- ALWAYS differentiate between free-tier and paid-tier usage in reports.
- ALWAYS flag cost anomalies within 1 hour of detection.

## examples

### Example: Monthly Billing Summary

**Input:** "Generate billing report for all proxy stacks this month"

**Output:**
```markdown
## Combined Proxy Billing Report

### Period: 2026-05-01 to 2026-05-31

### Summary
- Total Spend: $47.32
- Budget Utilization: 63%
- Largest Provider: Claude ($28.14)
- Cost Trend: decreasing (-12% vs last month)

### Per-Stack Breakdown
| Stack | Requests | Tokens | Cost | Budget % |
|-------|----------|--------|------|----------|
| 9Router   | 12,450 | 2.1M | $18.22 | 72% |
| Owl Proxy | 8,320  | 1.4M | $14.08 | 56% |
| Antigravity | 3,100 | 890K | $9.44 | 47% |
| Triune    | 1,890  | 620K | $5.58 | 31% |

### Optimization Recommendations
1. Move 30% of Claude requests to Gemini free-tier (est. savings: $8.40/mo)
2. Reduce Triune redundancy from 3-layer to 2-layer for non-critical routes (est. savings: $2.10/mo)
```
