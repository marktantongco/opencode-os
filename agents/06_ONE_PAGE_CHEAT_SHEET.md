# 📄 ONE-PAGE CHEAT SHEET

**Print this. Laminate it. Keep it near your desk.**

```
╔══════════════════════════════════════════════════════════════════════╗
║                         SYSTEM CHEAT SHEET                          ║
╠══════════════════════════════════════════════════════════════════════╣

KEYBOARD SHORTCUTS (Mac)
  ⌘1 = SKILL_01 (Conversational)    |  ?1 = Text command
  ⌘2 = SKILL_02 (Design)             |  ?2 = Text command
  ⌘3 = SKILL_03 (Code)               |  ?3 = Text command
  ⌘4 = SKILL_04 (Agentic)            |  ?4 = Text command

QUICK COMMANDS
  !status  = Show current system state
  !route   = Show routing decision for message
  !reset   = Load UNIVERSAL only (troubleshooting)

SKILLS AT A GLANCE
  SKILL_01  Conversational  Mobile, asking, exploring           4.4k tokens  high
  SKILL_02  Design+Build    Visual, iterative, artifacts        5.6k tokens  high
  SKILL_03  Code+API        Production code, debugging           6.1k tokens  xhigh
  SKILL_04  Agentic         Autonomous, orchestration, subagents 6.0k tokens  xhigh

AUTO-DETECT KEYWORDS
  Design:    "design", "UI", "component", "landing page", "visual"
  Code:      "code", "debug", "api", "function", "refactor", "test"
  Agentic:   "automate", "orchestrate", "agent", "workflow", "parallel"
  Else:      Conversational (default)

CONTINUITY PROTOCOL
  When you switch skills:
    1. System reviews last 10 messages
    2. Context carries forward automatically
    3. System announces: "Switching to [X] mode — noted [context]"
    4. Quick-Feedback Prompt: "Was that smooth? (Y/N)"

CLOSING PATTERNS (All Skills)
  ⚡⚡ Recommended Next Step  = Highest-leverage action (1-2 sentences)
  ✨ 3 Suggestions          = Tactical / Strategic / Reframe
  🔗 Hidden Assumption      = What could change the answer?

QUALITY GATES (Before Shipping)
  ✓ Works on first execution? (No manual setup)
  ✓ No placeholders or TODOs?
  ✓ Assumptions stated?
  ✓ Error handling included?
  ✓ Tests included (happy + sad path)?
  ✓ Type-safe (if code)?
  ✓ Edge cases considered?

WEEKLY HEALTH CHECK
  Routing accuracy:    >90%? ✓
  CONTINUITY success:  >90%? ✓
  Error rate:          <1%?  ✓
  Thinking time:       Normal? ✓
  User satisfaction:   >80%? ✓
  If all yes: System healthy. If any no: Investigate.

RESPONSE TIME EXPECTATIONS
  SKILL_01  2-10 seconds     | SKILL_03  5-90 seconds
  SKILL_02  5-60 seconds     | SKILL_04  30s-15 minutes

TROUBLESHOOTING (Choose 1)
  System not responding?     → Re-paste system prompt
  Wrong skill chosen?        → Use ?1/2/3/4 explicit command
  Context lost?              → Manually reference prior decision
  Slow response?             → Wait for thinking (normal)
  Bugs in code?              → This is iteration, not broken

TOKEN USAGE PER CONTEXT
  SKILL_01  4.4k tokens  (Mobile safe)
  SKILL_02  5.6k tokens  (Desktop design)
  SKILL_03  6.1k tokens  (Desktop code)
  SKILL_04  6.0k tokens  (Autonomous)
  All under 6.5k threshold (Opus 4.7 safe)

DEPLOYMENT TIMELINE
  Tuesday 9 AM   Deploy UNIVERSAL + SKILL_01
  Week 1         Test 6 conversations, log results
  Week 1 EOD     Decide: Build SKILL_02/03/04 or iterate
  Week 2         Build remaining skills (if Week 1 passed)
  Week 3+        All skills in production

FILES TO KEEP HANDY
  00_START_HERE.md                   (Navigation guide)
  MARK_SYSTEM_PROMPT_FINAL.md        (Master guide + prompts)
  SKILL_SHORTCUTS_FUNCTION_CALLS.md  (Keyboard shortcuts)
  01_OPERATIONAL_PLAYBOOKS.md        (Real-world workflows)
  03_MONITORING_METRICS.md           (Weekly tracking)
  05_EXTENDED_FAQ.md                 (Problem solving)

DECISION TREE (Which skill?)
  Is it conversational/exploration?       → SKILL_01
  Is it visual/design/UI?                 → SKILL_02
  Is it code/API/algorithm?               → SKILL_03
  Is it autonomous/orchestration?        → SKILL_04
  If unsure, use SKILL_01 (safest default)

POWER MOVES
  Parallel execution   = Design + Code simultaneously (save 50% time)
  Incremental deploy   = 5% → 25% → 100% (reduce risk)
  Feedback loop        = Build → Measure → Learn → Iterate
  Token optimization   = Reduce prompt without losing quality
  Quality-first        = Gates catch 80% of bugs before deploy

MONTHLY CHECKLIST
  ☐ Routing accuracy still >90%?
  ☐ Any trends in errors?
  ☐ User satisfaction improving?
  ☐ Token efficiency okay?
  ☐ CONTINUITY working well?
  ☐ Any new patterns in usage?
  ☐ Plan next month improvements?

ADVANCED PATTERNS
  1. Skill chaining       Research → Design → Code → Deploy
  2. Parallel execution   Run independent tasks simultaneously
  3. Delegation           Define goal, let subagents execute
  4. Reusable prompts     Write once, reuse 100 times
  5. Hypothesis-driven    State hypothesis, test it, learn

RED ALERTS (Stop Everything)
  Routing <85%           Fix: Add keywords, test new examples
  Context loss >2/day     Fix: Verify CONTINUITY in prompt
  Thinking 2x expected    Fix: Check effort level, reduce complexity
  Error rate >3%          Fix: Debug immediately, don't deploy
  Satisfaction <80%       Fix: Gather feedback, iterate

COMMANDS FOR DIFFERENT SCENARIOS
  Starting day:          "?1 I'm thinking about [topic]"
  Need design:           "?2 show me 3 design directions for [...]"
  Need code:             "?3 build this feature. Show algorithm first."
  Automating task:       "?4 orchestrate this workflow. Show decomposition."
  Check health:          "!status" (See current system state)
  Troubleshoot:          "!reset" then "?1" (Fresh start)

3-WORD SUMMARY OF SYSTEM
  Ask, Route, Execute.

NEXT STEP
  Tuesday 9 AM, deploy.
  Week 1, test.
  Week 1 EOD, decide.
  Ship it.

═══════════════════════════════════════════════════════════════════════════

Questions? See 05_EXTENDED_FAQ.md
Stuck? See ADVANCED_CONFIGURATIONS.md
Need examples? See 01_OPERATIONAL_PLAYBOOKS.md
Ready to go? See 00_START_HERE.md

═══════════════════════════════════════════════════════════════════════════
```

---

**Print, laminate, tape to desk. Reference daily.**
