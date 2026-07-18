# 📚 OPERATIONAL PLAYBOOKS

**Real-world workflows for every context. Copy, adapt, execute.**

---

## PLAYBOOK 1: Build a Complete Product (InsuranceHUB Pattern)

**Scenario:** You need to build a complete product autonomously (research → design → code → deploy)

**Timeline:** 4-6 hours (with subagents handling work in parallel)

### Workflow

**Step 1: Research & Strategy (SKILL_01 or SKILL_04)**

```
You: "@skill_04 build InsuranceHUB from scratch. 
      Research market, design system, build landing page, 
      code API, deploy to Vercel. Full autonomous workflow."

System: [Loads SKILL_04 - Agentic Mode]

Claude shows:
  ┌─────────────────────────────────┐
  │ TASK DECOMPOSITION              │
  ├─────────────────────────────────┤
  │ Task A: Market Research         │
  │ Task B: Brand + Design System   │
  │ Task C: Code Landing Page       │
  │ Task D: Code API Backend        │
  │ Task E: Integration + Testing   │
  │ Task F: Deploy to Vercel        │
  └─────────────────────────────────┘

Parallel flow:
  A → C, D (in parallel after A completes)
  B → C (design specs feed into code)
  C, D → E (both must complete before testing)
  E → F (test first, then deploy)

Estimated time: 4-6 hours
[Confirms? Y/N]
```

**Step 2: Execute with State Tracking**

```
You: Y

Claude: [Begins execution]

T+0m: Task A started (Research market)
      Agent: Research-Bot
      Focus: Filipino market, insurance trends, competitor analysis

T+20m: Task A complete ✓
       Output: Market positioning, feature list, pricing strategy
       
       Tasks B, C, D starting in parallel...

T+20m: Task B started (Design system)
       Agent: Design-Bot
       Input: Market positioning from Task A
       
T+20m: Task C started (Code landing page)
       Agent: Code-Bot
       Input: Design specs (waiting for Task B)
       
T+20m: Task D started (Code API)
       Agent: Backend-Bot
       Input: Product spec from Task A

T+30m: Task B complete ✓
       Output: Color palette (navy + gold), typography, components
       
       Task C now has design specs → continues coding

T+45m: Task C complete ✓
       Output: React landing page with all components
       
T+50m: Task D complete ✓
       Output: FastAPI backend with premium calculation endpoint

T+50m: Task E started (Integration + Testing)
       Agent: QA-Bot
       Input: Landing page from C, API from D
       Action: Wire together, run tests

T+60m: Task E complete ✓
       All tests passing, ready for deploy

T+60m: Task F started (Deploy)
       Agent: DevOps-Bot
       Input: Tested code from E
       Action: Deploy to Vercel, configure domain

T+70m: Task F complete ✓
       InsuranceHUB is LIVE
       
       URL: https://insurancehub.vercel.app
       
WORKFLOW COMPLETE
All tasks finished. Product deployed and live.
```

**Step 3: Validate & Iterate**

```
You: Check that everything works. Run a test quote flow.

Claude: [Validates end-to-end]

Testing:
  ✓ Landing page loads (no errors)
  ✓ Mobile responsive (checked on 3 breakpoints)
  ✓ Quote form calculates correctly
  ✓ API returns accurate premiums
  ✓ Navigation smooth
  ✓ Brand voice consistent (empowerment, clarity)

Result: ✅ Product ready for users

Next steps:
  1. Monitor analytics + performance
  2. Collect user feedback
  3. A/B test messaging variants
  4. Iterate based on data
```

### Key Success Factors

- **Clear task decomposition** (parallel where possible)
- **State tracking at each step** (know where you are)
- **Input/output validation** (catch errors early)
- **Feedback loops** (learn from each completed task)
- **Estimated time vs. actual** (track and improve)

---

## PLAYBOOK 2: Complex Project Management

**Scenario:** Managing a large project with many moving parts (code + design + content + deployment)

**Timeline:** 1-2 weeks (with weekly milestones)

### Weekly Structure

**Week 1: Discovery & Planning**

```
Monday:
  Morning: Define scope
    You: "@skill_01 let's plan the project. 
          What's the goal? What are constraints?"
    Claude: [Conversational mode, asks clarifying questions]
    Output: Clear project definition
  
  Afternoon: Break into tasks
    You: "@skill_04 decompose this into tasks. 
          Create a Gantt chart. What's critical path?"
    Claude: [Agentic mode, shows task breakdown]
    Output: Task list, dependencies, timeline

Tuesday-Wednesday:
  Each day: Execute priority tasks
    Morning standup:
      You: "What's the status? What's blocked?"
      Claude: [Shows state of all tasks]
    
    Work on highest-priority task:
      You: "@skill_03 code this feature" or 
           "@skill_02 design this component"
      Claude: [Works on task with full quality gates]
    
    Evening: Log progress
      You: "Log today's progress and blockers"
      Claude: [Updates project state, flags risks]

Thursday:
  Mid-week checkpoint
    You: "@skill_04 show me project status. 
          Are we on track? What's at risk?"
    Claude: [Full status report, risk assessment]
  
  Adjust plan if needed
    If on track: Continue as planned
    If delayed: Reprioritize, compress non-critical work

Friday:
  Weekly review
    You: "@skill_01 let's review the week. 
          What worked? What didn't? What's next?"
    Claude: [Retrospective + next week plan]
    Output: Weekly report, improvements, next week priorities
```

**Week 2+: Iterate**

- Same structure repeats
- Each week builds on prior week
- Risk mitigation improves
- Velocity increases (team learns)

### Project State Format

```
PROJECT: InsuranceHUB v2.0

Scope: Full redesign + new features
Timeline: 2 weeks (10 working days)
Budget: 80 hours

WEEK 1 STATUS
├─ Design System: Complete ✓
├─ Landing Page: In Progress (70%)
├─ API: In Progress (50%)
├─ Integration: Blocked (waiting on API)
└─ Deployment: Not started

CRITICAL PATH
Landing Page → Integration → Deployment
Finish by Friday (Week 1) to hit timeline

RISKS
⚠️ API complexity higher than expected
   Mitigation: Simplify scope, move features to v2.1
⚠️ Mobile testing reveals layout issues
   Mitigation: Have design ready to adjust
⚠️ Vercel deployment could fail
   Mitigation: Practice deploy on Tuesday

BLOCKERS
🚫 API tests failing on edge cases
   Owner: Code-Bot
   Deadline: Wednesday
   Action: Debug + fix, add test coverage

NEXT STEPS
1. Finish API core functionality (Wed)
2. Wire landing page to API (Thu)
3. Full integration testing (Thu-Fri)
4. Deploy (Friday EOD)
```

---

## PLAYBOOK 3: Production Debugging (Firefighting)

**Scenario:** Something broke in production. Need to diagnose and fix fast.

**Timeline:** 30 min to 2 hours (depending on severity)

### 5-Minute Triage

```
Step 1: UNDERSTAND THE PROBLEM
You: "@skill_01 users are reporting quote calculations 
      returning 0. What could cause this?"

Claude: [Asks clarifying questions]
  - When did it start?
  - All users or specific segments?
  - All products (Blue Royale + FlexiShield) or one?
  - Does it happen always or intermittently?

You: Started 2 hours ago. All users. Both products. Always happens.

Claude: Three likely causes:
  1. Database connection failure (data not loading)
  2. API endpoint returning null (code change broke it)
  3. Formula logic error (calculation returns 0 on all inputs)

Recommendation: Check logs immediately. Which makes most sense?

Step 2: IDENTIFY ROOT CAUSE
You: "@skill_03 API logs show 'premium calculation failed' 
      for all requests. Code changes were deployed 2 hours ago. 
      Show me what broke."

Claude: [Analyzes code changes from 2 hours ago]
  Found it: calculatePremium() now expects 'healthScore' field.
  But frontend still sends 'health'. Type mismatch → null error → returns 0.
  
  Fix: Update API to accept both field names (backward compatible)
       OR Update frontend to send correct field name
  
  Fastest fix: 1-line change in API to accept both
  
  [Shows code diff]

Step 3: IMPLEMENT HOTFIX
You: "@skill_03 implement the 1-line fix. 
      Then test with the failing case."

Claude: [Provides production-ready hotfix]
  
  Change:
    const health = req.body.healthScore || req.body.health;
  
  Test:
    calculatePremium({health: 'good', ...}) → Returns premium ✓
  
  Ready to deploy.

Step 4: DEPLOY & VERIFY
You: "@skill_04 deploy this fix to production. 
      Verify it works for all test cases."

Claude: [Deploys and validates]
  ✓ Deployed to Vercel (1 min)
  ✓ All tests passing
  ✓ Spot-checked 10 quote calculations → All returning correct values
  ✓ Users can now get quotes again
  
  Status: RESOLVED
  Time: 25 minutes
  Impact: 0 data loss, quick recovery
```

### Full Incident Response

```
If issue is more complex:

1. ISOLATE (5 min)
   - Don't panic
   - Stop the bleeding (disable feature if needed)
   - Alert stakeholders

2. DIAGNOSE (10-15 min)
   - Check logs
   - Check metrics
   - Check recent changes
   - Identify root cause

3. PLAN FIX (5 min)
   - Hotfix vs. full fix
   - Impact on other systems
   - Rollback plan

4. IMPLEMENT (varies)
   - Small fix: Deploy immediately
   - Large fix: Deploy to staging first, test, then prod

5. VERIFY (5-10 min)
   - Check metrics return to normal
   - Manual spot checks
   - User feedback

6. POST-MORTEM (next day)
   - Why did this happen?
   - How do we prevent it?
   - What early warnings did we miss?
```

---

## PLAYBOOK 4: Client Work (Selling & Delivering)

**Scenario:** Client needs insurance solution built. Manage from discovery through deployment.

**Timeline:** 2-4 weeks

### Sales Phase (Week 0)

```
Step 1: Discovery Call
  You: "@skill_01 I'm meeting a client today about building 
        their insurance sales platform. 
        What should I ask them?"
  
  Claude: [Gives you 10 discovery questions]
    - What's their current process?
    - Who are their users?
    - What's their pain point?
    - What's their budget/timeline?
    - Who are their competitors?

Step 2: Understand Their Need
  After call:
  You: "@skill_01 client wants to sell insurance online. 
        Target: SMEs in Metro Manila. 
        Pain: Manual quote process, slow.
        Budget: Limited. Timeline: 4 weeks."
  
  Claude: [Asks for clarification]
    - What products do they sell?
    - How many users expected?
    - Do they have existing customer data?
    - What integrations needed?
    - Do they need analytics?

Step 3: Propose Solution
  You: "@skill_02 based on their needs, 
        design a proposal. 3 options: MVP, Standard, Premium."
  
  Claude: [Design-mode, shows 3 tiers]
    MVP: Landing page + quote form + email follow-up
         Cost: $2,000, Timeline: 2 weeks
    
    Standard: MVP + CRM integration + customer dashboard
              Cost: $5,000, Timeline: 4 weeks
    
    Premium: Standard + AI chat + advanced analytics
             Cost: $10,000, Timeline: 6 weeks
  
  Output: Beautiful proposal document

Step 4: Close
  You: Present proposal, address objections, close the deal
  
  Result: Contract signed, project starts
```

### Delivery Phase (Weeks 1-4)

```
Week 1: Discover & Plan
  - Detailed requirements gathering
  - Define success criteria
  - Create project roadmap
  - Show client the plan

Week 2: Design & API
  - Design the user experience
  - Design the database
  - Design the API
  - Get client approval on mockups

Week 3: Build & Test
  - Build frontend (landing page, quote form, dashboard)
  - Build backend (API, integrations)
  - Test everything
  - Create user documentation

Week 4: Deploy & Train
  - Deploy to production
  - Train client on the system
  - Set up monitoring
  - Hand off to client

After: Support & Iteration
  - Monitor for issues (1 month free support)
  - Collect usage data
  - Plan Phase 2 features
  - Expand relationship
```

### Client Communication Template

```
Weekly Status Email:

Subject: InsuranceHub Project - Week 2 Status

Hi [Client],

Here's what we accomplished this week:

✓ COMPLETED
  - Landing page design (3 iterations, approved)
  - Database schema (optimized for scale)
  - API auth system (secure token-based)

⧖ IN PROGRESS
  - Quote form UI (60% complete, designs approved)
  - Premium calculation logic (testing edge cases)

⏳ NEXT WEEK
  - Launch quote form (your feedback needed)
  - Connect frontend to API
  - Mobile testing

⚠️ RISKS
  - Quote logic is more complex than estimated
  - Plan: Simplify scope, move advanced features to Phase 2
  - Impact: No timeline delay, but defer feature X

📊 METRICS
  - Hours used: 28 / 80 budget
  - On track: YES
  - Quality: High (no blockers)

QUESTIONS FOR YOU
  1. Are you happy with landing page design?
  2. Any last-minute feature requests before we code?
  3. Who should we train on the system?

Next sync: Friday 2 PM

Thanks,
[Your name]
```

---

## PLAYBOOK 5: AI Product Development (powerUP Tools)

**Scenario:** Building an AI tool (component library, template, or SaaS)

**Timeline:** 3-6 weeks

### Phase 1: Proof of Concept (1 week)

```
Goal: Validate the idea works. Build minimal version.

Day 1-2: Design & Spec
  You: "@skill_02 design the core user experience for [tool].
        Make it beautiful, simple, powerful."
  
  Output: Wireframes, design tokens, component spec

Day 3-4: Build MVP
  You: "@skill_03 code the MVP for [tool].
        Must work end-to-end. Ship minimum feature set."
  
  Output: Working prototype (maybe 30% features)

Day 5: Test & Iterate
  You: Use the tool yourself.
       Ask 3 people to test it.
       Collect feedback.
       Make 1-2 iteration passes.
  
  Output: Working MVP, user feedback, next iteration plan
```

### Phase 2: Build Core Features (2-3 weeks)

```
Week 1: Architect & Code
  - Build data model (persistence)
  - Code core features (80% of usage)
  - Add error handling & edge cases
  - Add tests

Week 2: Polish & Integrate
  - UI refinement (based on user feedback)
  - Performance optimization
  - Integration with other tools (if needed)
  - Documentation

Week 3: Launch Ready
  - Final testing
  - Monitoring setup
  - Launch communication
  - Pricing/packaging (if commercial)
```

### Phase 3: Launch & Scale (1-2 weeks)

```
Pre-launch: Marketing
  - Create launch video / GIF demo
  - Write compelling copy
  - Set up social media posts
  - Prepare email sequence

Launch Day:
  - Deploy to production
  - Announce on your channels
  - Respond to early feedback
  - Monitor for issues

Post-launch: Iterate
  - Collect usage data
  - Respond to user feedback
  - Fix bugs quickly
  - Plan next features
```

---

## PLAYBOOK 6: Rapid Learning (New Technology)

**Scenario:** You need to learn a new tech stack quickly (e.g., WebGPU, Next.js 15, new AI API)

**Timeline:** 1-3 days per technology

### Learning Sprint

```
Day 1: Foundations
  Morning (2 hours):
    You: "@skill_01 teach me [technology]. 
          What's the core idea? Why would I use it? 
          Real examples?"
    
    Claude: [Conversational explanation + examples]
  
  Afternoon (2 hours):
    You: "@skill_03 show me a 'hello world' example.
          Simplest possible working code."
    
    Claude: [Working example, explained line-by-line]

Day 2: Building
  Morning (3 hours):
    You: "@skill_03 build a real project with [technology].
          Show me best practices, common patterns, gotchas."
    
    Claude: [Production-quality code with comments]
  
  Afternoon (2 hours):
    You: Work with the code. Break it. Fix it. Learn.

Day 3: Deep Dive
  Morning (2 hours):
    You: "@skill_01 what are the advanced patterns for [tech]?
          When do people get this wrong? What's the gotcha?"
    
    Claude: [Deep insights, anti-patterns, mastery tips]
  
  Afternoon (2 hours):
    You: "@skill_03 implement the advanced pattern we discussed."
    
    Claude: [Advanced example]

Result: You've learned the technology at a practical level.
You can build with it. You can teach others.
```

---

## QUICK PLAYBOOK REFERENCE

| Scenario | Primary Skill | Timeline | Complexity |
|----------|--------------|----------|-----------|
| Build complete product | SKILL_04 | 4-6 hours | High |
| Manage complex project | SKILL_04 | 1-2 weeks | High |
| Debug production issue | SKILL_03 | 30 min - 2 hours | Medium |
| Client work (sell + build) | All | 2-4 weeks | High |
| AI product development | SKILL_02/03/04 | 3-6 weeks | High |
| Learn new technology | SKILL_01/03 | 1-3 days | Medium |
| Design a system | SKILL_02 | 1-3 days | High |
| Write an algorithm | SKILL_03 | 2-4 hours | Medium |
| Automate a workflow | SKILL_04 | 2-4 hours | High |

---

## CHOOSING THE RIGHT PLAYBOOK

Ask yourself:

1. **What's the outcome?** (Product, Feature, Fix, Learning, Client Deliverable)
2. **How much time?** (1 hour, 1 day, 1 week, 1 month)
3. **What skills needed?** (Design, Code, Orchestration, Discovery)
4. **What's the risk?** (If this fails, what breaks?)

Match to a playbook. Adapt as needed. Execute.

---

**End of Operational Playbooks**

Use these templates. Modify them. Create new ones. Document what works.
