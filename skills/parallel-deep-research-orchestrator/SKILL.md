---
name: parallel-deep-research-orchestrator
description: >
  Fan-out / fan-in deep research pipeline. Plans N sub-queries, dispatches
  parallel web-search workers (each with own context), dedups URLs, resolves
  conflicts, synthesizes a single cited markdown report. Use ONLY when user
  explicitly asks for "deep", "exhaustive", "comprehensive", or "parallel"
  research — 10-100x slower than a single web_search.
  Triggers: deep research, parallel research, orchestrator, fan-out, exhaustive.
allowed-tools: Read, Write, Bash, Edit, Grep, Glob
user-invocable: true
mcp-servers: [filesystem, web-search, web-reader]
---

# Parallel Deep Research Orchestrator

## context

Canonical fan-out / fan-in research topology: **planner → dispatcher →
merger → synthesizer**. Inspired by Parallel Web Systems' Task API
(parallel.ai), Google ADK `ParallelAgent`, Anthropic's multi-agent Research
system, GPT Researcher, and `langchain-ai/open_deep_research`. The
opencode-accomplishments repo already has a `/api/recommend.ts` Vercel
edge function that uses `Promise.all` for parallel AI-Gateway + 21st.dev
dispatch; this skill extends that pattern into a full research pipeline
without leaving the edge runtime.

This skill is invoked **only when the user explicitly asks for "deep",
"exhaustive", "comprehensive", or "parallel" research**. It is 10–100×
slower than a single `web_search` call and costs proportionally more
tokens. If the user just wants a quick answer, fall back to a single
`web_search` + `web-reader` pass instead.

The four stages are deliberately separable so each can be replaced or
parallelized independently. The orchestrator never executes web searches
itself — that is the workers' job. The orchestrator's job is to plan,
dispatch, merge, and synthesize.

## instructions

1. **Plan** — Decompose the user's query into 3–6 orthogonal sub-queries.
   Each sub-query must be answerable in isolation by a single worker with
   its own context window. Emit:
   ```json
   {
     "sub_queries": ["...", "...", "..."],
     "depth": "fast|standard|ultra",
     "max_workers": 6,
     "budget_usd": 1.00,
     "url_blocklist": ["..."]
   }
   ```
   - `fast` → 3 workers, 5 searches each, ~30s wall clock
   - `standard` → 5 workers, 5 searches each, ~90s wall clock
   - `ultra` → 6 workers, 10 searches each, ~5–25 min wall clock (requires
     async poll pattern — see "failure handling" below)

2. **Dispatch** — Spawn one worker per sub-query via `web-search` +
   `web-reader`. Use **`Promise.allSettled`** — never `Promise.all`. A
   single worker failure must not abort the whole run. Enforce per-worker
   caps:
   - `max_searches = 5` (10 for `ultra`)
   - `max_extracts = 10` (20 for `ultra`)
   - `max_llm_calls = 15`
   - `max_tokens = 8000`
   - `timeout_ms = 120000` (300000 for `ultra`)

3. **Merge** — Once all workers settle (or time out), merge their
   findings:
   - **Dedup by normalized URL** — strip query params, fragment, trailing
     slash, lowercase host. This is the #1 cost saver.
   - **HEAD-check every source URL** — drop 404s and 5xxs.
   - **Substring-match every `evidence_quote`** against the fetched page
     text. Drop quotes that don't appear verbatim (or with ≤5% edit
     distance). This is the #1 hallucination guard.
   - **Resolve conflicts** — if two workers make contradictory claims,
     prefer primary sources (official docs, peer-reviewed papers) over
     secondary (blog posts, Reddit, Twitter). If still unresolved, keep
     both with attribution and flag for the synthesizer.

4. **Synthesize** — Single LLM pass over the merged findings → cited
   markdown report. Use `[^N]` footnote citations. Required sections:
   - Executive summary (3–5 sentences)
   - Findings (one section per sub-query, with citations)
   - Conflicts & limitations
   - Worker stats: `{ worker_id, status, tokens_used, llm_calls }`
   - Total tokens used + estimated cost in USD

## worker interface

Each worker is a self-contained search-extract-reason loop with its own
context window. The orchestrator never reaches into a worker's internals.

**Input:**
```json
{
  "worker_id": "w1",
  "sub_query": "How does React Server Components handle client-side state?",
  "context_seed": "User is comparing RSC vs Astro islands vs Qwik resumability.",
  "max_searches": 5,
  "max_extracts": 10,
  "max_llm_calls": 15,
  "max_tokens": 8000,
  "timeout_ms": 120000,
  "url_blocklist": ["medium.com/tag/javascript"]
}
```

**Output:**
```json
{
  "worker_id": "w1",
  "findings": [
    {
      "claim": "RSC does not ship state to the client; client components do.",
      "evidence_quote": "Server Components never re-render on the client...",
      "source_url": "https://react.dev/reference/rsc/server-components",
      "source_title": "React Docs — Server Components",
      "retrieved_at": "2026-07-01T12:00:00Z",
      "confidence": 0.92
    }
  ],
  "tokens_used": 4200,
  "llm_calls": 8,
  "status": "ok",
  "error": null
}
```

**Status values:** `ok` | `partial` (some findings before timeout) |
`timeout` | `rate_limited` | `error`.

## orchestrator interface

The skill exposes a single HTTP-style entry point that the agent calls:

```
POST /api/research
{
  "query": "Compare RSC, Astro islands, and Qwik resumability.",
  "depth": "standard",
  "max_workers": 5,
  "budget_usd": 1.00
}
```

Response (synchronous for `fast`/`standard`, async for `ultra`):
```json
{
  "run_id": "r_abc123",
  "status": "ok",
  "report_md": "# ...",
  "citations": [{ "n": 1, "url": "...", "title": "...", "retrieved_at": "..." }],
  "tokens_used": 21000,
  "cost_usd": 0.42,
  "worker_stats": [{ "worker_id": "w1", "status": "ok", "tokens_used": 4200 }],
  "monitoring_url": "/api/research/runs/r_abc123"
}
```

For `ultra` depth, the endpoint immediately returns `{ run_id, status:
"running", monitoring_url }` and the agent must poll
`GET /api/research/poll?run_id=r_abc123&timeout=540` until `status` is
`ok`, `partial`, or `error`. Vercel edge CPU limits (30s hobby / 300s pro)
cannot host a 25-minute ultra run synchronously — use KV / Upstash for
intermediate state.

## failure handling

- **Worker timeout** → return partial findings, set `status: "timeout"`.
  Never block the merger on a single worker.
- **Worker 429** → exponential backoff (1s, 2s, 4s), then degrade to
  `status: "rate_limited"`. Skip retries beyond 3.
- **Hallucination** → merger HEAD-checks every URL and substring-matches
  every quote. Drop failures silently — never surface unverified claims.
- **Contradiction** → conflict-resolution pass. Prefer primary sources.
  If unresolved, keep both with attribution and a `⚠ conflict` marker.
- **Context overflow** → context compaction (summarize-and-discard).
  Never abort the worker; compact and continue.
- **`parallel-cli` missing** → if the user wants to delegate to the
  Parallel Web Systems vendor CLI (`parallel-cli research run`),
  instruct them to run `/parallel-setup` first. **Do NOT attempt the
  research yourself if the user asked for the vendor path** — that
  defeats the point of the managed service.

## constraints

These are non-negotiable. Violating any of them is a critical bug:

- **NEVER use `Promise.all`** — always `Promise.allSettled`. A single
  worker failure must not abort the run.
- **NEVER let a worker mutate shared state** — only the merger writes to
  the merged findings array. Workers return their own findings only.
- **NEVER skip URL dedup** — it's the #1 cost saver and the #1 noise
  reducer.
- **NEVER skip quote substring-matching** — it's the #1 hallucination
  guard. If the quote can't be verified against the fetched page text,
  drop the claim.
- **ALWAYS cap per-worker LLM calls and global token budget.** Exceeding
  the budget must degrade gracefully, not crash.
- **ALWAYS emit citations.** Uncited claims are dropped at the synthesis
  stage. No exceptions.
- **ALWAYS include worker_stats and cost_usd in the final report.**
  Without these, the user cannot audit the run.

## concrete use cases

1. **Multi-framework comparison** — "Compare RSC, Astro islands, and
   Qwik resumability across performance, SEO, and DX" → 3 workers (one
   per framework), merge into a single comparison table with citations.
2. **Market landscape scan** — "Map the AI coding agent market: pricing,
   context window, supported models, install base" → 6 workers (one per
   vendor), merge into a leaderboard with sortable columns.
3. **Competitive feature audit** — "What features does Vercel have that
   Netlify doesn't, and vice versa?" → 2 workers (one per vendor's docs),
   merge into a Venn-style diff table.

## references

- Research report: `download/parallel-deep-research-orchestrator-research.md`
- Existing parallel pattern: `api/recommend.ts` (Vercel edge, `Promise.all`)
- Companion skill: `skills/threejs-orchestrator/SKILL.md` (same
  orchestrator pattern, different domain)
- Vendor: Parallel Web Systems — `parallel.ai`,
  `github.com/parallel-web/parallel-agent-skills` (57★, MIT, v0.5.1)
- Pattern references: Google ADK `ParallelAgent`, Anthropic multi-agent
  Research system, `langchain-ai/open_deep_research`, GPT Researcher
