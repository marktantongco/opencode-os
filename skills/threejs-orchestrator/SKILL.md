---
name: threejs-orchestrator
description: >
  Gates ALL 3D work — routes to r3f-react for UI, vanilla Three.js for compute, Babylon.js for games. Prevents vanilla Three.js in React anti-pattern. Enforces lazy-load, ssr:false, transpilePackages. Use when use when any 3d work is requested — this skill routes to the correct 3d tool before implementation. developers must never default to what they know
  Triggers on keywords: threejs, orchestrator, 3d, routing, gate, r3f, webgpu.
allowed-tools: Read, Write, Bash, Edit, Grep, Glob
user-invocable: true
mcp-servers: [filesystem, github, docker]
---

# Three.js Orchestrator

## context

Routes ALL 3D work — uses React Three Fiber for UI-integrated 3D, vanilla Three.js for standalone scenes, and handles WebGL context management, scene graphs, and performance optimization. This skill provides structured workflows and production-ready patterns that ensure code quality, maintainability, and developer experience.

## instructions

### Step 1: Understand Requirements

1. Identify the core development task — new feature, bug fix, refactor, or integration
2. Determine technical constraints — language, framework, existing architecture patterns
3. Assess scope — is this a quick fix or a significant implementation?
4. Check for existing patterns in the codebase before writing new code

### Step 2: Apply Development Framework

1. **Plan** — Break the task into small, testable units of work
2. **Implement** — Write clean, well-documented code following project conventions
3. **Validate** — Test the implementation against requirements and edge cases
4. **Document** — Add inline comments and update relevant documentation

### Step 3: Generate Implementation

Structure output following this format:

```markdown
## Implementation Plan

### Approach
Description of the chosen approach and why it was selected

### Code Changes
Files to modify/create with rationale for each change

### Testing Strategy
- Unit tests: what to test at the function level
- Integration tests: how components interact together
- Edge cases: boundary conditions and error states

### Dependencies
- New dependencies if any with justification
- Existing dependencies to leverage
```

### Step 4: Quality Gates

Before completing any implementation:
- [ ] Code follows project style guide and conventions
- [ ] All new code has appropriate test coverage
- [ ] Error handling covers all failure modes
- [ ] Performance implications are documented
- [ ] Security considerations are addressed
- [ ] Documentation is updated

## constraints

- NEVER skip error handling — every external call must handle failure gracefully.
- NEVER introduce breaking changes without explicit version bumps and migration guides.
- NEVER hardcode configuration — use environment variables or config files.
- ALWAYS write tests before or alongside implementation (not after).
- ALWAYS consider backward compatibility when modifying existing APIs.

## examples

### Example: Development Task

**Input:** "Use when ANY 3D work is requested — this skill routes to the correct 3D tool before implementation. Developers must never default to what they know"

**Output:**
```markdown
## Implementation Plan

### Approach
Use the established threejs orchestrator pattern to implement the feature with minimal coupling and maximum testability.

### Code Changes
1. Create new module following project structure conventions
2. Add configuration to existing settings
3. Wire up dependency injection

### Testing Strategy
- Unit tests: Core logic with mocked dependencies
- Integration tests: Full workflow with real dependencies
- Edge cases: Empty inputs, concurrent access, error recovery
```
