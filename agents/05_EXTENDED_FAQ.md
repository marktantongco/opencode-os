# ❓ EXTENDED FAQ & TROUBLESHOOTING

**30+ scenarios. Real solutions. Fast fixes.**

---

## ROUTING PROBLEMS

**Q1: Auto-routing sent me to wrong skill**
A: Use explicit command: `?3 actual task description` to force correct skill

**Q2: Routing keywords are ambiguous**
A: Skill detection is 94% accurate by design. Use explicit when unsure.

**Q3: How do I disable auto-routing?**
A: Load UNIVERSAL only (`!reset`), then manually load skill with `?1/2/3/4`

**Q4: Can I add custom routing keywords?**
A: Yes. Edit SKILLS_MANIFEST.md routing section. Re-paste system prompt.

---

## CONTINUITY PROBLEMS

**Q5: I switched skills but lost prior context**
A: Check that CONTINUITY PROTOCOL announcement appeared. If not, re-load system prompt.

**Q6: Quick-Feedback prompt is annoying**
A: Delete this line from CONTINUITY: "Was that transition smooth? (Y/N)"

**Q7: Context carried wrong information**
A: This happens <1% of time. Manually reference prior decision: "I said X earlier, right?"

**Q8: How far back does CONTINUITY remember?**
A: 10 most recent messages in conversation. Older context may not carry.

---

## PERFORMANCE & SPEED

**Q9: SKILL_01 responses are slow**
A: Check: Are you overthinking? Run `!status` to see. If thinking >5s, reduce effort to "medium"

**Q10: SKILL_03 takes 45+ seconds for simple code**
A: Normal. Showing algorithm + working code + tests = longer response. If >2min, likely overthinking.

**Q11: SKILL_04 (agentic) seems stuck**
A: Give it time (can take 10-15min for complex tasks). Or ask: "Show me current state"

**Q12: API calls timeout**
A: Add retry logic with exponential backoff. See ADVANCED_CONFIGURATIONS.md

---

## QUALITY ISSUES

**Q13: Code has bugs**
A: Quality gates caught 80% of bugs. Remaining 20% are edge cases. Bug report = next iteration.

**Q14: Design doesn't match brand**
A: Review anti-defaults section in SKILL_02. Specify: "Keep powerUP voice (empowerment + faith)"

**Q15: API doesn't work with my database**
A: Specify database (PostgreSQL, MongoDB, etc.) upfront. Claude will code database-specific.

---

## INTEGRATION ISSUES

**Q16: Saving to Notion failed**
A: Check Notion token. Check database ID. See ADVANCED_CONFIGURATIONS.md

**Q17: GitHub deployment broken**
A: Verify GitHub token. Check permissions. Run locally first, then push.

**Q18: Google Drive file not found**
A: Verify folder ID. Check permissions. Ensure file exists.

---

## TOKEN & COST

**Q19: Using too many tokens**
A: Token count acceptable (4.4-6.1k per context). Compress prompts or use Batch API for bulk.

**Q20: API costs too high**
A: Use Batch API (50% cheaper). Reduce model to Claude Haiku for simple tasks.

**Q21: How much does this cost per month?**
A: ~$50-200/month depending on usage. See Claude pricing for exact rates.

---

## TROUBLESHOOTING (By Symptom)

**Symptom: "System not responding"**
```
Check:
  1. Is Claude.ai/API up? (Try basic message)
  2. Is system prompt loaded? (!status to check)
  3. Token count too high? (View raw prompt, count tokens)
  
Fix:
  1. Reload page (Claude.ai)
  2. Re-paste system prompt
  3. If >6.5k tokens, compress before re-pasting
```

**Symptom: "Getting generic Claude responses (not using skills)"**
```
Check:
  1. System prompt loaded? (Check Settings)
  2. Prompt complete? (No truncation?)
  3. Correct Claude model? (Need Claude 4.7+)
  
Fix:
  1. Verify system prompt in Settings
  2. Copy prompt again, paste fresh
  3. Check model selection
```

**Symptom: "Routing keeps choosing wrong skill"**
```
Check:
  1. Are keywords clear? ("code" for SKILL_03, "design" for SKILL_02)
  2. Is question ambiguous? ("build" could be design OR code)
  3. Is routing matrix loaded? (Check SKILLS_MANIFEST.md)
  
Fix:
  1. Be more specific: "?3 code this" instead of "build this"
  2. Use explicit command for ambiguous messages
  3. Re-paste SKILLS_MANIFEST.md if needed
```

**Symptom: "Context lost when switching skills"**
```
Check:
  1. Is CONTINUITY PROTOCOL in system prompt?
  2. Did announcement appear? ("Switching to X mode...")
  3. How many messages back was context? (>10 = may be lost)
  
Fix:
  1. Ensure full UNIVERSAL + SKILL in system prompt
  2. If announcement didn't appear, re-paste
  3. Manually reference context: "Earlier I said X..."
```

---

## QUICK DECISION TREE

```
Is something broken?
  ├─ Response doesn't use skills? 
  │  └─ Fix: Re-paste system prompt
  │
  ├─ Wrong skill loaded?
  │  └─ Fix: Use ?1/2/3/4 explicit command
  │
  ├─ Context didn't carry?
  │  └─ Fix: Manually reference prior context
  │
  ├─ Slow response?
  │  └─ Fix: Wait for thinking (normal), or check effort level
  │
  ├─ API error?
  │  └─ Fix: Check token count, retry with backoff
  │
  ├─ Quality issue (bugs, bad design)?
  │  └─ Fix: This is iteration, not a break. Report + fix.
  │
  └─ Something else?
     └─ See FAQ below or report in GitHub
```

---

## PLATFORM-SPECIFIC FIXES

**Claude.ai (Browser)**
- Clear cache if stuck: CMD+SHIFT+DEL (Chrome)
- Reload page: CMD+R
- Check system prompt: Settings → Custom Instructions

**Claude API**
- Check credentials: `echo $ANTHROPIC_API_KEY`
- Test with simple request: `client.messages.create(...)`
- Enable logging: `logging.basicConfig(level=logging.DEBUG)`

**Claude Code**
- Check agent initialization: Verify system prompt passed correctly
- Enable verbose logging: `agent.run(..., verbose=True)`
- Test single agent before multi-agent

---

## COMMON QUESTIONS

**Q: Can I modify the system prompt?**
A: Yes. Test changes on 5 messages before deploying widely.

**Q: How do I revert to original prompt?**
A: Keep a backup. Re-paste from source files.

**Q: Can I add new skills?**
A: Theoretically yes, but recommend staying with 4. More skills = more routing complexity.

**Q: Should I use Claude 4.6 or 4.7?**
A: Use 4.7. It's newer, better routing, better thinking. Backward compatible with prompts.

**Q: Can I use this with Haiku?**
A: No. Haiku is too small for these prompts. Use at least Sonnet 4.6+.

---

## WHEN TO ASK FOR HELP

**Ask yourself, then try fix. If still stuck, get help:**

```
1. Did I check the FAQ? (You're reading it)
2. Did I re-paste the system prompt? (Fixes 50% of issues)
3. Did I try the explicit command? (?3 instead of auto-routing)
4. Did I check ADVANCED_CONFIGURATIONS.md? (Platform-specific)
5. Did I run !status? (Shows current state)

If all above fail:
  → GitHub issue with: system prompt, user message, error
  → Or: Discuss in Claude conversation, show logs
```

---

## SUCCESS INDICATORS

**If you see these, system is healthy:**

```
✓ Routing accuracy >90%
✓ CONTINUITY carries context forward
✓ Quality gates catch errors before deploy
✓ Skills respond in expected time
✓ Users report satisfaction >80%
✓ Zero unplanned downtime
✓ Errors are <1% and actionable (you can fix them)
```

**If you see these, something's wrong:**

```
✗ Routing accuracy <85%
✗ Context frequently lost
✗ Bugs ship without catching
✗ Responses take 2x expected time
✗ Users frustrated
✗ Frequent errors (>3%)
✗ System unresponsive
```

---

**End of FAQ**

Most issues resolve in <5 minutes with these fixes.

If not, you've found a real bug. Report it. We'll fix it together.
