# ⚙️ ADVANCED CONFIGURATIONS

**Deploy across any platform. Optimize for your environment.**

---

## CONFIGURATION 1: Claude.ai (Browser) — Individual

**Best for:** Mobile chat, quick interactions, exploration

### Setup (5 minutes)

```
1. Open claude.ai in browser
2. Go to Settings → Custom Instructions
3. Paste UNIVERSAL + SKILL_01 into System field
4. Save

Default: SKILL_01 active
To switch: Manually paste different SKILL using text expander
```

### Optimization

**Speed:**
- Use text expander (Alfred, TextExpander, BetterTouchTool)
- Shortcuts: ?1, ?2, ?3, ?4 for instant skill switching
- Keyboard: ⌘1, ⌘2, ⌘3, ⌘4 (if configured)

**Mobile:**
- Keep SKILL_01 active by default
- Use text commands (?1, ?2, etc.) to switch
- Auto-detection handles most context switches

**Best practices:**
```
✓ Keep SKILL_01 loaded for mobile chat
✓ Switch to other skills when needed
✓ Use CONTINUITY to carry context forward
✓ Close browser tab when done (fresh context next time)
✗ Don't manually edit system prompt every time
✗ Don't memorize skill text (use expander)
```

### Monitoring

```
Check weekly:
- Do I overthink on simple questions? (If yes: reduce effort)
- Do I lose context when switching? (If yes: strengthen CONTINUITY)
- Do skills load correctly? (If no: check shortcuts setup)
```

---

## CONFIGURATION 2: Claude API (Programmatic) — Full Automation

**Best for:** Building AI features into products, autonomous workflows, batch processing

### Setup (30 minutes)

**Install Anthropic SDK:**
```bash
pip install anthropic
# or
npm install @anthropic-ai/sdk
```

**Load skills dynamically:**

```python
from anthropic import Anthropic

# Initialize
client = Anthropic()

# Load all prompts
UNIVERSAL = open('UNIVERSAL_PROMPT.md').read()
SKILLS = {
    'conversational': open('SKILL_01.md').read(),
    'design': open('SKILL_02.md').read(),
    'code': open('SKILL_03.md').read(),
    'agentic': open('SKILL_04.md').read(),
}

def detect_skill(message: str) -> str:
    """Automatically detect which skill to use."""
    msg_lower = message.lower()
    
    if any(w in msg_lower for w in ['design', 'ui', 'component', 'visual']):
        return 'design'
    elif any(w in msg_lower for w in ['code', 'debug', 'api', 'function']):
        return 'code'
    elif any(w in msg_lower for w in ['automate', 'orchestrate', 'agent']):
        return 'agentic'
    else:
        return 'conversational'

def get_system_prompt(skill: str) -> str:
    """Combine universal + skill."""
    return UNIVERSAL + '\n\n' + SKILLS[skill]

def call_claude(message: str, skill: str = None) -> str:
    """Call Claude with appropriate skill."""
    skill = skill or detect_skill(message)
    system = get_system_prompt(skill)
    
    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=4096,
        effort="xhigh" if skill in ['code', 'agentic'] else "high",
        system=system,
        messages=[{"role": "user", "content": message}]
    )
    
    return response.content[0].text

# Usage
response = call_claude("Help me design a landing page")
# Auto-detects: 'design'
# Sets effort="high"
# Returns design-mode response

response = call_claude("Debug this function", skill='code')
# Forces skill='code'
# Sets effort="xhigh"
# Returns code-mode response
```

### Production Deployment

**Rate limiting:**
```python
import time

def call_claude_with_backoff(message: str, max_retries: int = 3):
    """Retry with exponential backoff."""
    for attempt in range(max_retries):
        try:
            return call_claude(message)
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            wait = 2 ** attempt  # 1s, 2s, 4s
            print(f"Retry {attempt + 1} after {wait}s: {str(e)}")
            time.sleep(wait)
```

**Logging:**
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def call_claude_logged(message: str, skill: str = None):
    """Log all API calls."""
    skill = skill or detect_skill(message)
    
    logger.info(f"API call: skill={skill}, tokens_approx={len(message)//4}")
    
    start = time.time()
    response = call_claude(message, skill)
    elapsed = time.time() - start
    
    logger.info(f"Completed in {elapsed:.1f}s, output_length={len(response)}")
    
    return response
```

**Error handling:**
```python
from anthropic import APIError, APIConnectionError

def call_claude_safe(message: str) -> dict:
    """Safe call with error handling."""
    try:
        response = call_claude(message)
        return {'success': True, 'response': response}
    except APIConnectionError as e:
        logger.error(f"Connection error: {e}")
        return {'success': False, 'error': 'Connection failed', 'retry': True}
    except APIError as e:
        logger.error(f"API error: {e}")
        return {'success': False, 'error': str(e), 'retry': False}
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return {'success': False, 'error': str(e), 'retry': False}
```

### Monitoring & Metrics

```python
import json
from datetime import datetime

class APIMetrics:
    def __init__(self):
        self.calls = []
    
    def log_call(self, skill: str, input_tokens: int, output_tokens: int, elapsed: float):
        """Log API call metrics."""
        self.calls.append({
            'timestamp': datetime.now().isoformat(),
            'skill': skill,
            'input_tokens': input_tokens,
            'output_tokens': output_tokens,
            'elapsed_seconds': elapsed,
        })
    
    def summary(self):
        """Get summary metrics."""
        if not self.calls:
            return None
        
        total_input = sum(c['input_tokens'] for c in self.calls)
        total_output = sum(c['output_tokens'] for c in self.calls)
        avg_time = sum(c['elapsed_seconds'] for c in self.calls) / len(self.calls)
        
        skills = {}
        for call in self.calls:
            skill = call['skill']
            if skill not in skills:
                skills[skill] = []
            skills[skill].append(call)
        
        return {
            'total_calls': len(self.calls),
            'total_input_tokens': total_input,
            'total_output_tokens': total_output,
            'average_time_seconds': avg_time,
            'calls_by_skill': {k: len(v) for k, v in skills.items()},
        }

# Usage
metrics = APIMetrics()

# After each call:
elapsed = time.time() - start
metrics.log_call(skill, input_tokens, output_tokens, elapsed)

# Weekly review:
summary = metrics.summary()
print(json.dumps(summary, indent=2))
```

---

## CONFIGURATION 3: Claude Code (Agentic) — Autonomous

**Best for:** Building AI agents, autonomous workflows, long-running tasks

### Setup (20 minutes)

**Install Claude Code:**
```bash
pip install claude-code
# or download from claude.ai
```

**Initialize with system prompt:**

```python
from claude_code import Agent

# Create agent with system prompt
agent = Agent(
    name="InsuranceAssistant",
    system_prompt=UNIVERSAL + '\n\n' + SKILLS['agentic'],
    tools=[
        'code_execution',
        'file_creation',
        'web_search',
        'file_read'
    ]
)

# Run autonomous task
result = agent.run(
    task="Build InsuranceHUB landing page. Research market, design system, code React component, deploy to Vercel.",
    max_iterations=50,  # Safety limit
    think_before_acting=True
)

print(result)
# Output: Full InsuranceHUB built autonomously
```

### Advanced: Multi-Agent Orchestration

```python
class OrchestrationAgent:
    """Coordinate multiple subagents."""
    
    def __init__(self):
        self.agents = {
            'researcher': Agent('researcher', SKILLS['agentic']),
            'designer': Agent('designer', SKILLS['design']),
            'coder': Agent('coder', SKILLS['code']),
            'tester': Agent('tester', SKILLS['code']),
        }
        self.state = {}
    
    def run_workflow(self, goal: str):
        """Execute workflow with multiple agents."""
        
        # Step 1: Research
        research_task = f"Research market for: {goal}"
        research_result = self.agents['researcher'].run(research_task)
        self.state['research'] = research_result
        
        # Step 2: Design (waits for research)
        design_task = f"Design based on research: {research_result}"
        design_result = self.agents['designer'].run(design_task)
        self.state['design'] = design_result
        
        # Step 3: Code (parallel with next)
        code_task = f"Code based on design: {design_result}"
        code_result = self.agents['coder'].run(code_task)
        self.state['code'] = code_result
        
        # Step 4: Test (waits for code)
        test_task = f"Test code: {code_result}"
        test_result = self.agents['tester'].run(test_task)
        self.state['tests'] = test_result
        
        return {
            'research': research_result,
            'design': design_result,
            'code': code_result,
            'tests': test_result,
            'status': 'COMPLETE'
        }

# Usage
orchestrator = OrchestrationAgent()
result = orchestrator.run_workflow("Build InsuranceHUB")
print(f"Completed: {result['status']}")
```

### Monitoring Agent Health

```python
class AgentHealthCheck:
    def __init__(self, agent):
        self.agent = agent
        self.errors = []
        self.iterations = 0
    
    def run_with_monitoring(self, task: str):
        """Run task with health monitoring."""
        self.iterations = 0
        max_iterations = 100
        
        while self.iterations < max_iterations:
            self.iterations += 1
            
            try:
                result = self.agent.step(task)
                
                # Check for convergence
                if result.get('done'):
                    return result
                
                # Check for stuck loops
                if self.iterations > 50 and not result.get('progress'):
                    self.errors.append(f"Possible loop at iteration {self.iterations}")
                    break
                    
            except Exception as e:
                self.errors.append(str(e))
                if len(self.errors) > 5:
                    break
        
        return {
            'status': 'FAILED' if self.errors else 'TIMEOUT',
            'iterations': self.iterations,
            'errors': self.errors
        }
```

---

## CONFIGURATION 4: Claude API + Batch Processing

**Best for:** Processing many items in parallel (10-1000s)

### Setup (30 minutes)

**Batch API format:**

```json
[
  {
    "custom_id": "request-1",
    "params": {
      "model": "claude-opus-4-7",
      "max_tokens": 1024,
      "messages": [
        {"role": "user", "content": "Design a landing page for insurance"}
      ]
    }
  },
  {
    "custom_id": "request-2",
    "params": {
      "model": "claude-opus-4-7",
      "max_tokens": 1024,
      "messages": [
        {"role": "user", "content": "Design a landing page for SaaS"}
      ]
    }
  }
]
```

**Submit batch:**

```python
def submit_batch(requests: list) -> str:
    """Submit batch of requests."""
    import jsonl
    
    # Format as JSONL
    jsonl_requests = '\n'.join(json.dumps(r) for r in requests)
    
    # Submit to API
    batch = client.beta.messages.batches.create(
        model="claude-opus-4-7",
        requests=requests
    )
    
    print(f"Batch {batch.id} submitted")
    print(f"Status: {batch.processing_status}")
    
    return batch.id

def check_batch_status(batch_id: str):
    """Check batch progress."""
    batch = client.beta.messages.batches.retrieve(batch_id)
    print(f"Status: {batch.processing_status}")
    print(f"Completed: {batch.request_counts.completed}/{batch.request_counts.total}")

def get_batch_results(batch_id: str):
    """Get results from completed batch."""
    batch = client.beta.messages.batches.retrieve(batch_id)
    
    if batch.processing_status != 'completed':
        print(f"Batch still processing: {batch.processing_status}")
        return None
    
    results = {}
    for result in client.beta.messages.batches.retrieve(batch_id).results:
        custom_id = result.custom_id
        response = result.result.message.content[0].text
        results[custom_id] = response
    
    return results
```

**Example: Batch design requests**

```python
# Create batch of design requests
design_requests = [
    {
        'custom_id': f'design-{i}',
        'params': {
            'model': 'claude-opus-4-7',
            'max_tokens': 2048,
            'system': UNIVERSAL + '\n\n' + SKILLS['design'],
            'messages': [
                {'role': 'user', 'content': f'Design a landing page for {product}'}
            ]
        }
    }
    for i, product in enumerate([
        'Insurance product', 'SaaS tool', 'E-commerce', 'Educational platform'
    ])
]

# Submit
batch_id = submit_batch(design_requests)

# Wait for completion (usually < 1 hour)
time.sleep(5 * 60)  # Check after 5 minutes

# Get results
results = get_batch_results(batch_id)

# Process
for custom_id, design in results.items():
    print(f"{custom_id}: {design[:100]}...")
```

---

## CONFIGURATION 5: Team Workspace (Collaborative)

**Best for:** Team projects, shared prompts, centralized management

### Setup (15 minutes)

**Team workspace structure:**

```
Team: Insurance AI
├─ Resources (Shared)
│  ├─ UNIVERSAL_PROMPT.md (shared by all)
│  ├─ SKILL_01.md (shared conversational)
│  ├─ SKILL_02.md (shared design)
│  ├─ SKILL_03.md (shared code)
│  └─ SKILL_04.md (shared agentic)
│
├─ Projects
│  ├─ InsuranceHUB
│  │  ├─ Requirements.md
│  │  ├─ Design Specs.md
│  │  ├─ Code Review Notes.md
│  │  └─ Deployment Checklist.md
│  │
│  └─ AI Training Portal
│     ├─ Requirements.md
│     ├─ Curriculum.md
│     └─ Student Feedback.md
│
└─ Team Members
   ├─ You (owner, all skills)
   ├─ Designer (SKILL_02 focus)
   ├─ Developer (SKILL_03 focus)
   └─ Product Manager (SKILL_01 focus)
```

**Assign skills by role:**

```
Product Manager: SKILL_01 (conversational) + SKILL_02 (seeing designs)
Designer: SKILL_02 (design) + SKILL_01 (feedback)
Developer: SKILL_03 (code) + SKILL_04 (when automating)
QA: SKILL_03 (testing) + SKILL_04 (automation)
```

**Shared system prompt (for team):**

```
All team members see the same UNIVERSAL + their assigned SKILL.

When Designer opens Claude: UNIVERSAL + SKILL_02
When Developer opens Claude: UNIVERSAL + SKILL_03
When Product Manager opens Claude: UNIVERSAL + SKILL_01
```

**Collaboration workflow:**

```
1. Product Manager (SKILL_01)
   - Define requirements
   - Ask clarifying questions
   - Get market insights

2. Designer (SKILL_02)
   - Takes PM requirements
   - Creates 3 design directions
   - Gets team feedback

3. Developer (SKILL_03)
   - Takes approved design
   - Builds components + API
   - Runs quality gates

4. QA (SKILL_03/04)
   - Tests functionality
   - Creates test suite
   - Automates regression tests

5. Feedback loop
   - Results shared back to PM
   - Iterate based on data
```

**Team communication template:**

```
[In shared workspace]

🔄 DESIGN APPROVED
Designer: "Submitted 3 design directions. PM approved Direction #2.
           Implementation ready."
Status: ✅ Ready for development

📝 IN DEVELOPMENT
Developer: "Building components. API endpoints on track.
            Will have working prototype by Friday."
Status: ⧖ 60% complete

🧪 TESTING
QA: "Created test suite. Found 2 edge cases.
     Will report separately."
Status: ⧖ 50% complete

✅ READY FOR LAUNCH
All teams: "Everything passing. Ready to deploy Friday."
Status: ✅ Go/No-go decision needed
```

---

## CONFIGURATION 6: Integration with External Tools

### Notion Integration

```python
import requests

def save_to_notion(data: dict, database_id: str):
    """Save work to Notion database."""
    
    url = f"https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    
    payload = {
        "parent": {"database_id": database_id},
        "properties": {
            "Name": {"title": [{"text": {"content": data['title']}}]},
            "Description": {"rich_text": [{"text": {"content": data['description']}}]},
            "Status": {"status": {"name": data['status']}},
            "Skill": {"select": {"name": data['skill']}},
        }
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# Usage
save_to_notion({
    'title': 'InsuranceHUB Landing Page',
    'description': 'Built with SKILL_02 - 3 design directions approved',
    'status': 'In Progress',
    'skill': 'Design'
}, database_id='abc123...')
```

### Google Drive Integration

```python
from google.oauth2 import service_account
from googleapiclient.discovery import build

def save_to_drive(filename: str, content: str, folder_id: str):
    """Save file to Google Drive."""
    
    credentials = service_account.Credentials.from_service_account_file(
        'credentials.json'
    )
    drive = build('drive', 'v3', credentials=credentials)
    
    file_metadata = {
        'name': filename,
        'parents': [folder_id]
    }
    
    media = MediaIoBaseUpload(
        io.BytesIO(content.encode('utf-8')),
        mimetype='text/markdown'
    )
    
    file = drive.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    
    return file.get('id')

# Usage
save_to_drive(
    'InsuranceHUB_Design_Spec.md',
    design_spec_content,
    folder_id='1a2b3c4d5e...'
)
```

### GitHub Integration

```python
from github import Github

def create_github_issue(title: str, body: str, labels: list):
    """Create issue in GitHub."""
    
    g = Github(GITHUB_TOKEN)
    repo = g.get_user().get_repo('insurancehub')
    
    issue = repo.create_issue(
        title=title,
        body=body,
        labels=labels
    )
    
    return issue.html_url

# Usage
create_github_issue(
    title='Design landing page with SKILL_02',
    body='Approved design specs attached. Ready for implementation.',
    labels=['design', 'high-priority']
)
```

---

## CONFIGURATION COMPARISON

| Feature | Claude.ai | API | Code | Team | Batch |
|---------|-----------|-----|------|------|-------|
| **Speed** | Fast (manual) | Fast (auto) | Fastest (autonomous) | Medium | Slow (async) |
| **Automation** | None | Full | Full | Partial | Full |
| **Cost** | Included in Pro | Per API call | Included | Shared | Cheap (bulk) |
| **Best for** | Exploration | Products | Agents | Teams | Batch processing |
| **Setup time** | 5 min | 30 min | 20 min | 15 min | 30 min |
| **Team collaboration** | No | No | No | Yes | No |

---

## DEPLOYMENT DECISION TREE

```
Which platform should I use?

Quick exploration?         → Claude.ai
├─ Yes  → Use directly, switch skills with shortcuts
└─ No   → Continue

Building a product feature?  → Claude API
├─ Yes  → Integrate into app, auto-routing
└─ No   → Continue

Autonomous long-horizon?    → Claude Code
├─ Yes  → Multi-agent orchestration
└─ No   → Continue

Team project?               → Team Workspace
├─ Yes  → Shared prompts, assign by role
└─ No   → Continue

Processing 1000s of items?  → Batch API
├─ Yes  → Use batch for cost efficiency
└─ No   → Use Claude API

Default choice: Claude.ai for exploration, Claude API for products
```

---

**End of Advanced Configurations**

Choose your platform. Configure accordingly. Optimize for your workflow.
