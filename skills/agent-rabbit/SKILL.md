---
name: agent-rabbit
description: >
  Multiply ideas — rapid ideation, brainstorming, and divergent thinking. Generates many options quickly, then clusters and prioritizes. Use when use when brainstorming, ideating, or generating many creative options quickly
  Triggers on keywords: agent, ideation, brainstorm, diverge, creative.
allowed-tools: Read, Grep, Glob
user-invocable: true
mcp-servers: [memory, sequential-thinking, filesystem]
---

# Agent Rabbit

## context

This is an Agent Mode skill that activates when the AI needs ideation thinking capabilities. Modeled after the rabbit's natural strengths, this mode provides structured frameworks for divergent reasoning. It integrates with the Agent Roles system and can be combined with other agent modes for multi-perspective analysis.

## instructions

### Step 1: Activate Agent Rabbit Mode

When this mode activates:
1. Identify the core question or problem requiring ideation thinking
2. Determine scope — is this a quick take or deep analysis?
3. Select the appropriate divergent framework

### Step 2: Apply divergent Framework

Generate many ideas quickly, then cluster and prioritize them. The process follows:

1. **Input gathering** — Collect all relevant context, constraints, and prior work
2. **divergent processing** — Apply the ideation lens to reframe and reorganize the input
3. **Output generation** — Produce structured results with clear actionability
4. **Validation** — Cross-check outputs against original constraints

### Step 3: Structure the Output

Format results as:

```markdown
## Agent Rabbit Analysis

### Core Insight
Primary finding or idea from the ideation analysis

### Supporting Points
1. Point with supporting evidence
2. Point with supporting evidence
3. Point with supporting evidence

### Recommended Actions
- Specific actionable next step
- Specific actionable next step

### Connections
- Related to: cross-domain link
- Precedes: next step in the workflow
```

### Step 4: Collaborate with Other Modes

When working alongside other agent modes:
- **+ Rabbit**: Add more ideas before converging
- **+ Owl**: Add rigor after generating options
- **+ Ant**: Break insights into executable tasks
- **+ Eagle**: Check if insights align with bigger picture
- **+ Dolphin**: Break out of conventional thinking
- **+ Beaver**: Turn ideas into buildable systems
- **+ Elephant**: Find connections to other domains

## constraints

- NEVER provide shallow ideation output — always go at least 2 levels deep.
- NEVER skip the validation step — even divergent thinkers verify their work.
- NEVER work in isolation when other modes are available — combine perspectives.
- ALWAYS label which framework was applied so the reasoning is auditable.

## examples

### Example: Ideation Analysis

**Input:** "Use when brainstorming, ideating, or generating many creative options quickly"

**Output:**
```markdown
## Agent Rabbit Analysis

### Core Insight
Generate many ideas quickly, then cluster and prioritize them

### Supporting Points
1. First level: ideation framing of the problem
2. Second level: divergent reasoning chain
3. Third level: Practical implications

### Recommended Actions
- Apply ideation framework to the immediate problem
- Validate with complementary mode
- Document the reasoning for future reference
```
