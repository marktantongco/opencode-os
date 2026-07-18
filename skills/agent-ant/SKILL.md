---
name: agent-ant
description: >
  Break into steps — task decomposition, work breakdown structures, and sequential execution planning. Ships incrementally. Use when use when decomposing tasks, planning work breakdowns, or shipping incrementally
  Triggers on keywords: agent, decompose, steps, planning, incremental.
allowed-tools: Read, Grep, Glob
user-invocable: true
mcp-servers: [memory, sequential-thinking, filesystem]
---

# Agent Ant

## context

This is an Agent Mode skill that activates when the AI needs decomposition thinking capabilities. Modeled after the ant's natural strengths, this mode provides structured frameworks for structured reasoning. It integrates with the Agent Roles system and can be combined with other agent modes for multi-perspective analysis.

## instructions

### Step 1: Activate Agent Ant Mode

When this mode activates:
1. Identify the core question or problem requiring decomposition thinking
2. Determine scope — is this a quick take or deep analysis?
3. Select the appropriate structured framework

### Step 2: Apply structured Framework

Break complex tasks into small, executable work packages. The process follows:

1. **Input gathering** — Collect all relevant context, constraints, and prior work
2. **structured processing** — Apply the decomposition lens to reframe and reorganize the input
3. **Output generation** — Produce structured results with clear actionability
4. **Validation** — Cross-check outputs against original constraints

### Step 3: Structure the Output

Format results as:

```markdown
## Agent Ant Analysis

### Core Insight
Primary finding or idea from the decomposition analysis

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

- NEVER provide shallow decomposition output — always go at least 2 levels deep.
- NEVER skip the validation step — even structured thinkers verify their work.
- NEVER work in isolation when other modes are available — combine perspectives.
- ALWAYS label which framework was applied so the reasoning is auditable.

## examples

### Example: Decomposition Analysis

**Input:** "Use when decomposing tasks, planning work breakdowns, or shipping incrementally"

**Output:**
```markdown
## Agent Ant Analysis

### Core Insight
Break complex tasks into small, executable work packages

### Supporting Points
1. First level: decomposition framing of the problem
2. Second level: structured reasoning chain
3. Third level: Practical implications

### Recommended Actions
- Apply decomposition framework to the immediate problem
- Validate with complementary mode
- Document the reasoning for future reference
```
