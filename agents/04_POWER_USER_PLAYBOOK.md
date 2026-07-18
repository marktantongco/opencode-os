# ⚡ POWER USER PLAYBOOK

**Advanced patterns. Optimization. Mastery.**

---

## PATTERN 1: Parallel Task Execution

Instead of sequential (A → B → C), do parallel (A, B, C simultaneously).

**Example: Building a feature**

```
❌ SLOW (Sequential, 6 hours):
  Design: 2 hours
    ↓
  Code: 3 hours
    ↓
  Test: 1 hour

✅ FAST (Parallel, 3 hours):
  Design: 2 hours ──┐
  Code: 3 hours ───┼─ (all parallel)
  Test: 1 hour ────┘
  
  Critical path: Design (2h) + Code (3h) = 5h? 
  No: Design and Code can start together if specs are clear.
  Real time: Max(Design, Code, Test) = 3 hours
```

**How to implement with Claude:**

```
You: "@skill_04 build this feature. 
      Run design and coding in parallel.
      Start with clear specs so code doesn't block design."

Claude: [Orchestrates parallel work]
  Agent A: Design the UI (2 hours)
  Agent B: Code the API (3 hours) [starts immediately, uses spec]
  Both proceed in parallel
  Agent C: Test (starts when both ready)
  
Result: 3 hours instead of 6.
```

---

## PATTERN 2: Incremental Deployment (Reduce Risk)

Deploy in stages, not all at once.

```
DAY 1: Deploy to 5% of users (internal team)
  ├─ Monitor for 24 hours
  ├─ Collect feedback
  └─ Fix any critical issues

DAY 2: Deploy to 25% of users (trusted customers)
  ├─ Monitor for 24 hours
  ├─ Collect feedback
  └─ Fix remaining issues

DAY 3: Deploy to 100% of users
  └─ Monitor continuously for 1 week

Benefits:
- If something breaks, only 5% affected initially
- Can roll back quickly without large impact
- Learn from early users before full rollout
```

---

## PATTERN 3: Continuous Feedback Loop

Don't just build once. Build, measure, learn, iterate.

```
Week 1: Build MVP
Week 2: Deploy to 10 users
       └─ Measure: Do they use feature X?
       └─ Learn: If 0% use it, maybe it's not important
Week 3: Based on Week 2 data, iterate
Week 4: Deploy improved version
       └─ Measure again
       └─ Learn
Week 5: Iterate again

Cycle:
Build → Measure → Learn → Iterate
  ↑_________________________↓
```

---

## PATTERN 4: Token Budget Optimization

Reduce tokens without reducing quality.

**Current breakdown:**
- UNIVERSAL: 3,100 tokens
- SKILL_01: 1,300 tokens
- Total: 4,400 tokens

**How to reduce while keeping quality:**

```
BEFORE:
UNIVERSAL: 3,100 tokens
  ├─ Core Identity: 300
  ├─ Silent Protocol: 500
  ├─ Routing: 400
  ├─ Tone: 600
  ├─ Voice Principle: 400
  ├─ Domain Context: 300
  ├─ CONTINUITY: 300
  ├─ Effort Guidance: 200
  └─ Etc: 600

OPTIMIZATION:
├─ Compress SILENT PROTOCOL (from 500 → 250)
│  How: Remove explanation, keep just questions
├─ Compress Routing Matrix (from 400 → 200)
│  How: Use 1-line descriptions instead of 2-3 lines
├─ Compress TONE section (from 600 → 300)
│  How: Remove redundant bullets, keep only essential

RESULT: 3,100 → 2,600 tokens (16% reduction)
        Quality impact: NONE (examples, logic, structure unchanged)

Usage: Use freed tokens for skill-specific content or larger contexts.
```

---

## PATTERN 5: Error Prevention (Quality Gates as Insurance)

Use quality gates not just to catch errors, but to prevent them entirely.

**Example: Preventing 90% of bugs**

Instead of:
```
Code the feature
  ↓
Deploy
  ↓
Users find bugs 😡
```

Do this:
```
Code the feature
  ↓
Run quality checklist (catches 80% of bugs before deploy)
  ↓
Deploy with confidence
  ↓
Users find 10-20% of edge cases
  ↓
Quick hotfix (30 min instead of 2 days of debugging)
```

**The gates are:** assumptions, logic, execution, tests, edge cases.

---

## PATTERN 6: Skill Chaining (Complex Workflows)

Chain skills together to solve complex problems.

**Example: Market research → Design → Code → Deploy**

```
Step 1: Research (SKILL_01)
  You: "@skill_01 what's the market opportunity for [product]?"
  Output: Market analysis

Step 2: Design (SKILL_02)
  You: "@skill_02 based on this market research, design the product"
  Output: Design specs

Step 3: Code (SKILL_03)
  You: "@skill_03 based on these design specs, build the product"
  Output: Working code

Step 4: Deploy (SKILL_04)
  You: "@skill_04 deploy this code, set up monitoring, create docs"
  Output: Live product

Key: Each step feeds into the next.
Each skill brings its expertise.
Combined: You've built a complete product in 6 hours.
```

---

## PATTERN 7: Delegation (Let Agentic Do the Work)

You define the goal. Subagents execute.

**Instead of directing every step:**
```
You: "@skill_04 build InsuranceHUB. Research, design, code, deploy.
     Make decisions autonomously. Report final state."

Claude: [Handles everything. You check back 6 hours later.]

Result: Product complete. You didn't do the work. Subagents did.
```

**Key insight:** This is not "hands-off." You're still in control.
You just shift from "do every step" to "define goal + check milestones."

---

## PATTERN 8: Reusable Prompts (Copy, Modify, Ship)

Create a prompt once. Reuse it 100 times.

**Example: Landing page designs**

```
Base prompt:
"@skill_02 design a landing page for [PRODUCT].
Target audience: [AUDIENCE].
Style: [STYLE].
Show 3 options."

Reuse 1:
"@skill_02 design a landing page for InsuranceHub.
Target audience: Filipino millennials.
Style: Neo-brutalist.
Show 3 options."

Reuse 2:
"@skill_02 design a landing page for FinTech App.
Target audience: Tech-savvy professionals.
Style: Minimalist.
Show 3 options."

Same prompt. Different inputs. Same high quality.
Time to create: 5 minutes (once). Time to reuse: 30 seconds (each).
```

---

## PATTERN 9: Hypothesis-Driven Development

Before you build, state your hypothesis. Then test it.

```
HYPOTHESIS: "Users want a 1-click quote form. This will increase conversion 30%."

EXPERIMENT:
├─ Build the feature (4 hours)
├─ Deploy to 25% of users (1 hour)
├─ Measure conversion (1 day)
└─ Compare: Before vs. After

RESULTS:
├─ If +30% conversion: Keep it. It was right.
├─ If +5% conversion: It helps, but not as much as expected.
├─ If 0% conversion: It doesn't work. Remove it.

Key: You tested your hypothesis. Data beats opinion.
Next: Based on data, build next hypothesis.
```

---

## PATTERN 10: The Weekly Review

Every Friday: 15 minutes. Review what worked. What didn't. Plan next week.

```
WEEKLY REVIEW TEMPLATE

What I built this week:
├─ Feature X (launched)
├─ Feature Y (in progress)
└─ Feature Z (blocked, waiting on A)

What worked:
├─ Parallel design + code (saved 3 hours)
├─ Quality gates caught 2 bugs
└─ User feedback was clear and actionable

What didn't work:
├─ Tried routing keyword X, 60% accuracy (too low)
├─ Spent 2 hours on feature nobody wanted
└─ Didn't get feedback early enough

Lessons learned:
├─ Routing keywords need testing before deploy
├─ Talk to users BEFORE building
└─ Parallel work saves time but needs clear specs

Next week plan:
├─ Test routing keywords on 20 messages
├─ Build Feature A (high priority)
├─ Feature B can wait (lower priority)
└─ Get user feedback on Feature A by Wednesday
```

---

## OPTIMIZATION CHECKLIST (Monthly)

```
TOKEN EFFICIENCY
☑ Reduce Universal prompt? (Can we compress without losing quality?)
☑ Reduce SKILL_01 prompt? (Can we trim examples?)
☑ Review token usage per context (Are we over budget?)

ROUTING ACCURACY
☑ Review routing errors (Why did auto-detect fail?)
☑ Add new keywords? (Are there new patterns to detect?)
☑ Refine routing rules? (Are some skills overlapping?)

CONTINUITY SUCCESS
☑ Review context-carry failures (Why didn't context carry?)
☑ Strengthen announcement? (Is the switch clear to user?)
☑ Test skill-switching? (Random sample of 5 switches)

ERROR RATE
☑ Review each error (Root cause?)
☑ Prevent future errors? (Quality gate, keyword, rule?)
☑ Are error patterns visible? (Trends?)

USER SATISFACTION
☑ Collect feedback (What's working? What's not?)
☑ Fix easy wins (Small changes that improve satisfaction)
☑ Plan major improvements (Bigger changes for next quarter)
```

---

## DEBUGGING ADVANCED ISSUES

**Issue: Routing works 95% of time, but fails on edge cases**

```
Debug process:
1. Collect all failures (e.g., 5 cases where routing was wrong)
2. Analyze pattern:
   - Are they similar topics?
   - Are they ambiguous messages?
   - Are they new keywords not in routing matrix?
3. Add rule:
   - If message contains "ambiguous pattern", ask for clarification
   - Or: If keywords overlap, use this tiebreaker
4. Test on 20 new messages
5. If >95%, deploy. If <95%, iterate.
```

**Issue: CONTINUITY occasionally loses context**

```
Debug process:
1. When context lost, check:
   - Was CONTINUITY PROTOCOL in system prompt?
   - Did skill switch happen?
   - How many messages back was context?
   - Was context in different skill's format?
2. Likely causes:
   - Prompt truncated (CONTINUITY section removed)
   - Skill switch didn't review prior messages
   - Context was in SKILL_02 format, SKILL_03 can't interpret
3. Fix:
   - Ensure full prompt is loaded
   - Add explicit "review prior 10 messages" instruction
   - Make context interpretation format-agnostic
4. Test on 10 skill switches
```

---

## SPEED BENCHMARKS (What to Expect)

```
SKILL_01 (Conversational):
├─ Quick question: 2-5 seconds
├─ With follow-up: 5-10 seconds
└─ With depth exploration: 10-20 seconds

SKILL_02 (Design):
├─ Simple mockup: 5-10 seconds
├─ 3 design options: 15-30 seconds
├─ Full design system: 30-60 seconds
└─ With depth-seeking: 45-90 seconds

SKILL_03 (Code):
├─ Simple function: 5-15 seconds
├─ API endpoint: 15-30 seconds
├─ Full feature: 30-60 seconds
└─ With algorithm explanation: 45-90 seconds

SKILL_04 (Agentic):
├─ Simple automation: 30-60 seconds
├─ Multi-step workflow: 2-5 minutes
├─ Complex orchestration: 5-15 minutes
└─ Full product build: 30-120 minutes

Faster than expected? Likely missing quality gates.
Slower than expected? Check: Overthinking? Token budget? Skill mismatch?
```

---

## MASTERY CHECKLIST

```
LEVEL 1: BASIC (Can use system)
☑ Know all 4 skills
☑ Can switch between them
☑ Understand CONTINUITY
☑ Can run Week 1 tests

LEVEL 2: INTERMEDIATE (Productive)
☑ Choose right skill automatically
☑ Build features with quality gates
☑ Monitor metrics weekly
☑ Understand trade-offs (speed vs. quality)

LEVEL 3: ADVANCED (Optimized)
☑ Chain skills into complex workflows
☑ Parallel execution (save time)
☑ Token budget optimization
☑ Routing tuning for your patterns

LEVEL 4: EXPERT (Mastery)
☑ Design custom workflows
☑ Anticipate and prevent errors
☑ Mentor others
☑ Continuously improve system
☑ Build entirely new capabilities

You're here: Level 2→3. Aim for Level 4 in 6 months.
```

---

**End of Power User Playbook**

These patterns separate good users from great ones.

Master one pattern per week. By month 3, you'll be unstoppable.
