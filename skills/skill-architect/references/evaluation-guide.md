# Skill Evaluation Guide

Testing skills before deployment prevents dead skills, broken workflows, and user frustration.

## Evaluation Types

### 1. Qualitative Evaluation (Human Review)

Best for subjective skills (writing style, design quality, creative tasks).

**Process:**
1. Write 2-3 realistic test prompts
2. Run the skill on each prompt
3. Review outputs manually
4. Iterate based on feedback

**Test prompt quality:**
- Realistic: Something an actual user would say
- Detailed: Include file paths, context, backstory
- Varied: Cover edge cases and common cases
- Edge-focused: Include ambiguous phrasings

**Example test prompts:**
```json
{
  "evals": [
    {
      "id": 1,
      "prompt": "I need to create a login form for our app. It should have email, password, a remember me checkbox, and a forgot password link. Use React with TypeScript and Tailwind.",
      "expected_output": "Complete login form component with validation, accessibility, and proper TypeScript types"
    },
    {
      "id": 2,
      "prompt": "Build me a modal that shows user profile info. It should slide in from the right and have a close button. Dark mode support.",
      "expected_output": "Slide-in drawer/modal with profile display, close handler, and dark mode classes"
    },
    {
      "id": 3,
      "prompt": "ok so i need like a really simple button but it needs to have different colors for primary, secondary, and danger. also disabled state. react ts.",
      "expected_output": "Button component with variant prop, disabled state, and TypeScript interface — despite casual/abbreviated input"
    }
  ]
}
```

### 2. Quantitative Evaluation (Automated Assertions)

Best for objective skills (file transforms, data extraction, code generation).

**Process:**
1. Define assertions that check the output programmatically
2. Run skill + baseline (without skill) on same prompts
3. Compare pass rates, token usage, and timing
4. Iterate until skill outperforms baseline

**Assertion types:**

| Type | Example | Use Case |
|---|---|---|
| **File existence** | `assert os.path.exists("output.tsx")` | Code generation |
| **Content match** | `assert "interface" in output` | TypeScript enforcement |
| **Structure check** | `assert output.count("##") >= 3` | Document structure |
| **No bad patterns** | `assert "any" not in output` | Type strictness |
| **Metric threshold** | `assert len(output) < 5000` | Conciseness |

**Example evals.json with assertions:**
```json
{
  "skill_name": "react-component-gen",
  "evals": [
    {
      "id": 1,
      "prompt": "Create a Button component with variants",
      "assertions": [
        {
          "name": "has_typescript_interface",
          "check": "output.contains('interface')",
          "description": "Component must define props as an interface"
        },
        {
          "name": "no_default_export",
          "check": "!output.contains('export default')",
          "description": "Must use named exports only"
        },
        {
          "name": "has_test_file",
          "check": "files.contains('Button.test.tsx')",
          "description": "Must create co-located test file"
        }
      ]
    }
  ]
}
```

### 3. Trigger Evaluation (Description Testing)

Tests whether the skill activates when it should.

**Process:**
1. Create 10 should-trigger queries (varied phrasing, some casual)
2. Create 10 should-not-trigger queries (near-misses, adjacent domains)
3. Run each query 3 times against the agent
4. Calculate trigger rate
5. Optimize description if < 80% accuracy

**Example trigger eval set:**
```json
[
  {"query": "Create a React button component with primary and secondary styles", "should_trigger": true},
  {"query": "I need a card component for our dashboard", "should_trigger": true},
  {"query": "Build me a modal dialog with form inside", "should_trigger": true},
  {"query": "Write a Python script to scrape a website", "should_trigger": false},
  {"query": "How do I center a div with CSS?", "should_trigger": false},
  {"query": "Create a database schema for users", "should_trigger": false}
]
```

## Evaluation Workspace Structure

```
skill-eval-workspace/
├── iteration-1/
│   ├── eval-1-button/
│   │   ├── with_skill/
│   │   │   ├── outputs/
│   │   │   │   └── Button.tsx
│   │   │   └── timing.json
│   │   ├── without_skill/
│   │   │   ├── outputs/
│   │   │   │   └── Button.tsx
│   │   │   └── timing.json
│   │   └── eval_metadata.json
│   ├── eval-2-card/
│   │   └── ...
│   ├── benchmark.json
│   └── benchmark.md
├── iteration-2/
│   └── ...
└── feedback.json
```

## Benchmark Metrics

Track these across iterations:

| Metric | What It Measures | Target |
|---|---|---|
| **Pass rate** | % of assertions passing | ≥ 90% |
| **Trigger rate** | % of should-trigger queries that activate skill | ≥ 80% |
| **False trigger rate** | % of should-not-trigger queries that wrongly activate | ≤ 10% |
| **Token usage** | Average tokens per task | Minimize |
| **Duration** | Average time per task | Minimize |
| **Delta vs baseline** | Skill improvement over no-skill | Positive |

## Iteration Loop

```
Draft skill → Run evals → Human review → Identify issues → 
Improve skill → Run evals (new iteration) → Compare to previous → 
Repeat until satisfied → Optimize description → Package
```

**Stopping conditions:**
- User says they're happy
- All feedback is empty (no issues found)
- No meaningful improvement between iterations
- Pass rate ≥ 90% and trigger rate ≥ 80%

## Common Evaluation Pitfalls

| Pitfall | Why It Happens | Fix |
|---|---|---|
| **Overfitting to test cases** | Skill works perfectly on 3 examples, fails on 4th | Expand test set; extract general patterns |
| **Testing only happy path** | No error cases, edge cases, or malformed input | Add failure-mode tests |
| **Ignoring baseline** | Can't prove skill actually helps | Always run without-skill baseline |
| **Subjective assertions** | Trying to auto-grade writing quality | Use human review for subjective outputs |
| **Stale evals** | Skill changed but tests didn't update | Version evals with skill iterations |
| **Wrong trigger tests** | Queries too simple or too abstract | Make queries realistic and detailed |

## Quick Start: Minimal Eval Setup

For teams without full evaluation infrastructure:

1. **Create 3 test prompts** (save to `evals/prompts.txt`)
2. **Run skill on each** (manually or via subagent)
3. **Review outputs** (human judgment)
4. **List issues** (save to `evals/feedback.md`)
5. **Fix skill** (address top 3 issues)
6. **Re-run** (compare to previous)

This lightweight process catches 80% of skill problems with 20% of the effort.
