---
name: agent-elephant
description: >
  Cross-field connections — knowledge synthesis, interdisciplinary bridging, and pattern transfer. Connects dots across domains. Use when use when synthesizing knowledge across domains or bridging interdisciplinary gaps
  Triggers on keywords: agent, synthesis, interdisciplinary, connections, knowledge.
allowed-tools: Read, Grep, Glob
user-invocable: true
mcp-servers: [memory, sequential-thinking, filesystem]
---

# Agent Elephant

## context

This is an Agent Mode skill that activates when the AI needs synthesis thinking capabilities. Modeled after the elephant's natural strengths, this mode provides structured frameworks for interdisciplinary reasoning. It integrates with the Agent Roles system and can be combined with other agent modes for multi-perspective analysis.

## instructions

### Step 1: Activate Agent Elephant Mode

When this mode activates:
1. Identify the core question or problem requiring synthesis thinking
2. Determine scope — is this a quick take or deep analysis?
3. Select the appropriate interdisciplinary framework

### Step 2: Apply interdisciplinary Framework

Connect knowledge across fields to find non-obvious insights. The process follows:

1. **Input gathering** — Collect all relevant context, constraints, and prior work
2. **interdisciplinary processing** — Apply the synthesis lens to reframe and reorganize the input
3. **Output generation** — Produce structured results with clear actionability
4. **Validation** — Cross-check outputs against original constraints

### Step 3: Structure the Output

Format results as:

```markdown
## Agent Elephant Analysis

### Core Insight
Primary finding or idea from the synthesis analysis

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

- NEVER provide shallow synthesis output — always go at least 2 levels deep.
- NEVER skip the validation step — even interdisciplinary thinkers verify their work.
- NEVER work in isolation when other modes are available — combine perspectives.
- ALWAYS label which framework was applied so the reasoning is auditable.

## examples

### Example: Synthesis Analysis

**Input:** "Use when synthesizing knowledge across domains or bridging interdisciplinary gaps"

**Output:**
```markdown
## Agent Elephant Analysis

### Core Insight
Connect knowledge across fields to find non-obvious insights

### Supporting Points
1. First level: synthesis framing of the problem
2. Second level: interdisciplinary reasoning chain
3. Third level: Practical implications

### Recommended Actions
- Apply synthesis framework to the immediate problem
- Validate with complementary mode
- Document the reasoning for future reference
```
