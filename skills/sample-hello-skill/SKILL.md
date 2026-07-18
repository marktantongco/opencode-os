---
name: sample-hello-skill
description: >
  Hello-world demo skill for testing skill activation and validation. Use when use when testing the skill system or validating installation
  Triggers on keywords: demo, test, validation, hello.
allowed-tools: Read, Write, Bash, Edit, Grep, Glob
user-invocable: true
mcp-servers: [filesystem, github, docker]
---

# Hello World Skill

## context

Hello-world demo skill for testing skill activation and validation. Minimal skill that demonstrates the SKILL.md format, frontmatter structure, and trigger patterns. This skill provides system-level capabilities that maintain agent state, ensure consistency, and optimize resource usage across sessions and projects.

## instructions

### Step 1: Assess System Needs

1. Identify the system operation required — memory, sync, compression, or role management
2. Determine scope — single session, multi-session, or cross-project
3. Map dependencies — what other systems or tools are involved
4. Establish operational parameters — retention, frequency, thresholds

### Step 2: Execute System Operation

1. **Initialize** — Set up or load required state and configuration
2. **Process** — Execute the core operation with proper error handling
3. **Validate** — Verify the operation completed correctly
4. **Report** — Document what was done and any issues encountered

### Step 3: Generate System Report

```markdown
## System Operation Report

### Operation
Type of operation performed

### Input
What was processed

### Output
Results of the operation

### State Changes
- Change 1: before to after
- Change 2: before to after

### Issues Encountered
- Issue: resolution
```

### Step 4: Verify System Health

- [ ] Operation completed without errors
- [ ] State is consistent and valid
- [ ] No resource leaks or orphaned data
- [ ] Logging and monitoring are active
- [ ] Backup/recovery procedures are in place

## constraints

- NEVER modify system state without logging the change.
- NEVER assume operations succeed — always validate results.
- NEVER skip cleanup — system resources must be properly released.
- ALWAYS handle concurrent access and race conditions.
- ALWAYS maintain backward compatibility with existing state.

## examples

### Example: System Operation

**Input:** "Use when testing the skill system or validating installation"

**Output:**
```markdown
## System Operation Report

### Operation
Sample Hello Skill executed successfully

### State Changes
- Configuration updated with new parameters
- State persisted to storage

### Verification
- All health checks passing
- No resource leaks detected
```
