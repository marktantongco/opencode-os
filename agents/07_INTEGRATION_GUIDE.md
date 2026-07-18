# 🔗 INTEGRATION GUIDE

**Connect Claude system to your existing tools. Automate everything.**

---

## INTEGRATION 1: Notion (Save Work + Organize)

### Setup (10 minutes)

**Get Notion Token:**
1. Go to notion.so/my-integrations
2. Create new integration
3. Copy "Internal Integration Token"

**Add to Python:**
```python
import os
from notion_client import Client

NOTION_TOKEN = os.getenv('NOTION_TOKEN')
notion = Client(auth=NOTION_TOKEN)

def save_to_notion_database(data: dict, database_id: str):
    """Save design, code, or project to Notion."""
    
    notion.pages.create(
        parent={"database_id": database_id},
        properties={
            "Name": {"title": [{"text": {"content": data['title']}}]},
            "Content": {"rich_text": [{"text": {"content": data['content']}}]},
            "Status": {"status": {"name": data.get('status', 'New')}},
            "Skill": {"select": {"name": data.get('skill', 'Unknown')}},
            "Date": {"date": {"start": data.get('date', '2024-05-17')}},
        }
    )
    
    print(f"Saved to Notion: {data['title']}")
```

### Use Cases

**Save design specs:**
```python
save_to_notion_database({
    'title': 'InsuranceHub Landing Page',
    'content': design_specs_markdown,
    'skill': 'Design',
    'status': 'In Progress'
}, database_id='abc123...')
```

**Save code reviews:**
```python
save_to_notion_database({
    'title': 'Premium Calculation API - Code Review',
    'content': code_review_feedback,
    'skill': 'Code',
    'status': 'Approved'
}, database_id='def456...')
```

**Save project status:**
```python
save_to_notion_database({
    'title': 'InsuranceHub v2.0 - Week 1 Status',
    'content': weekly_status_report,
    'skill': 'Agentic',
    'status': 'On Track'
}, database_id='ghi789...')
```

---

## INTEGRATION 2: Google Drive (Store Files)

### Setup (15 minutes)

**Get Google Credentials:**
1. Go to console.cloud.google.com
2. Create project
3. Enable Google Drive API
4. Create service account
5. Download JSON key

**Add to Python:**
```python
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

credentials = service_account.Credentials.from_service_account_file(
    'service_account.json'
)
drive = build('drive', 'v3', credentials=credentials)

def save_to_google_drive(filename: str, content: str, folder_id: str):
    """Save file to Google Drive."""
    
    file_metadata = {
        'name': filename,
        'parents': [folder_id],
        'mimeType': 'text/markdown'
    }
    
    media = MediaFileUpload(
        filename,
        mimetype='text/markdown',
        resumable=True
    )
    
    file = drive.files().create(
        body=file_metadata,
        media_body=media,
        fields='id, webViewLink'
    ).execute()
    
    return file['webViewLink']
```

### Use Cases

**Save design mockups:**
```python
save_to_google_drive(
    'InsuranceHub_Mockups_v1.md',
    design_mockups_content,
    folder_id='1a2b3c4d5e...'
)
# Returns shareable link
```

**Save API documentation:**
```python
save_to_google_drive(
    'InsuranceHub_API_Docs.md',
    api_documentation,
    folder_id='1x2y3z4w5v...'
)
```

---

## INTEGRATION 3: GitHub (Version Control + Issues)

### Setup (5 minutes)

**Get GitHub Token:**
1. Go to github.com/settings/tokens
2. Create "Personal Access Token"
3. Select scopes: repo, workflow

**Add to Python:**
```python
from github import Github

gh = Github(GITHUB_TOKEN)
repo = gh.get_user().get_repo('insurancehub')

def create_github_issue(title: str, body: str, labels: list = []):
    """Create issue in GitHub."""
    
    issue = repo.create_issue(
        title=title,
        body=body,
        labels=labels
    )
    
    return issue.html_url

def create_github_pr(branch: str, title: str, body: str):
    """Create pull request."""
    
    pr = repo.create_pull(
        title=title,
        body=body,
        head=branch,
        base='main'
    )
    
    return pr.html_url
```

### Use Cases

**Log bugs from testing:**
```python
create_github_issue(
    title='Bug: Quote calculation returns 0 on edge case',
    body='Steps: 1. Enter age > 100, 2. Select FlexiShield\n\nExpected: Calculate premium\nActual: Returns 0',
    labels=['bug', 'high-priority']
)
```

**Create feature requests:**
```python
create_github_issue(
    title='Feature: One-click quote sharing',
    body='Users want to share quote via WhatsApp/Email\n\nBenefit: Increase conversion\nEstimate: 4 hours',
    labels=['feature', 'enhancement']
)
```

---

## INTEGRATION 4: Slack (Notifications + Updates)

### Setup (10 minutes)

**Get Slack Webhook:**
1. Go to api.slack.com/apps
2. Create new app
3. Enable "Incoming Webhooks"
4. Create webhook URL

**Add to Python:**
```python
import requests
import json

SLACK_WEBHOOK = 'https://hooks.slack.com/services/YOUR/WEBHOOK/URL'

def send_slack_message(channel: str, message: str, thread_ts: str = None):
    """Send message to Slack."""
    
    payload = {
        'channel': channel,
        'text': message,
        'thread_ts': thread_ts
    }
    
    response = requests.post(SLACK_WEBHOOK, json=payload)
    return response.status_code == 200

def send_slack_status(status: str, details: str, color: str = 'good'):
    """Send status update to Slack."""
    
    payload = {
        'channel': '#project-status',
        'attachments': [
            {
                'color': color,
                'title': status,
                'text': details,
                'ts': int(time.time())
            }
        ]
    }
    
    response = requests.post(SLACK_WEBHOOK, json=payload)
    return response.status_code == 200
```

### Use Cases

**Daily standup:**
```python
send_slack_message(
    '#daily-standup',
    '✅ Status Update\n\n'
    '• InsuranceHub landing page: 90% complete\n'
    '• API testing: 2 edge cases found, fixing\n'
    '• Blockers: None'
)
```

**Deploy notifications:**
```python
send_slack_status(
    '🚀 InsuranceHub v1.0 Deployed',
    'Deployed to Vercel. All tests passing. Monitoring metrics.',
    color='good'
)
```

---

## INTEGRATION 5: Email (Alerts + Reports)

### Setup (5 minutes)

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_report(to: str, subject: str, body: str):
    """Send email report."""
    
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'system@yourdomain.com'
    msg['To'] = to
    
    msg.attach(MIMEText(body, 'html'))
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to, msg.as_string())
    
    print(f"Email sent to {to}")
```

### Use Cases

**Weekly metrics report:**
```python
html_report = f"""
<h1>Weekly System Report</h1>
<p>Routing Accuracy: 94%</p>
<p>Continuity Success: 92%</p>
<p>Error Rate: 0.6%</p>
"""

send_email_report(
    'mark@powerup.ai',
    'Weekly System Report - May 13-19',
    html_report
)
```

---

## INTEGRATION 6: Discord (Team Communication)

### Setup (5 minutes)

```python
import discord
from discord.ext import tasks

class DiscordBot(discord.Client):
    async def on_ready(self):
        print(f'Connected as {self.user}')
    
    async def send_to_channel(self, channel_id: int, message: str):
        channel = self.get_channel(channel_id)
        await channel.send(message)

bot = DiscordBot(intents=discord.Intents.default())

# Send message
asyncio.run(bot.send_to_channel(123456789, 'InsuranceHub deployed! ✅'))
```

---

## INTEGRATION 7: Database (Store Results)

### PostgreSQL Example

```python
import psycopg2

conn = psycopg2.connect(
    host="your-db.com",
    database="insurancehub",
    user="admin",
    password=os.getenv('DB_PASSWORD')
)

def save_prompt_result(skill: str, input_text: str, output_text: str, tokens: int):
    """Save Claude interaction to database."""
    
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO claude_results (skill, input, output, tokens, timestamp)
        VALUES (%s, %s, %s, %s, NOW())
    """, (skill, input_text, output_text, tokens))
    conn.commit()
    cur.close()

# Usage
save_prompt_result('design', 'Design a landing page', design_output, 2048)
```

---

## INTEGRATION 8: Zapier (No-Code Automation)

**Automate without code:**

1. Go to zapier.com
2. Create Zap: Claude API → Action
3. Set up trigger: New email in Gmail
4. Call Claude API to draft response
5. Send to Slack

**Example workflow:**
```
Email arrives → Zapier calls Claude → Claude drafts response
→ Post to Slack → You review → Send email
```

---

## FULL AUTOMATION EXAMPLE

**Scenario: Client feedback → Design iteration → Deploy**

```python
def full_workflow():
    # 1. Get feedback from email
    feedback = get_latest_email()
    
    # 2. Log in Notion
    save_to_notion_database({
        'title': f'Feedback: {feedback["subject"]}',
        'content': feedback['body'],
        'status': 'New'
    }, database_id)
    
    # 3. Send to Slack for team
    send_slack_message('#feedback', f'New feedback: {feedback["subject"]}')
    
    # 4. Call Claude to analyze
    analysis = call_claude(f'Analyze this feedback: {feedback["body"]}', skill='design')
    
    # 5. Save analysis to GitHub as issue
    create_github_issue(
        title=f'Design improvement: {feedback["subject"]}',
        body=analysis,
        labels=['design', 'feedback']
    )
    
    # 6. Save to Google Drive
    save_to_google_drive(
        f'Feedback_Analysis_{date.today()}.md',
        analysis,
        folder_id
    )
    
    # 7. Send summary to email
    send_email_report(
        'mark@powerup.ai',
        'Feedback Processed',
        f'Feedback logged, analyzed, and filed. See GitHub issue #{issue_number}'
    )

# Run once per day
schedule.every().day.at("09:00").do(full_workflow)
```

---

## INTEGRATION MATRIX

| Tool | Purpose | Setup Time | Cost | Automation |
|------|---------|-----------|------|-----------|
| Notion | Database + org | 10 min | Free | Medium |
| Google Drive | File storage | 15 min | Free | Medium |
| GitHub | Code + issues | 5 min | Free | High |
| Slack | Team comms | 10 min | Free | High |
| Email | Alerts | 5 min | Free | High |
| Discord | Community | 5 min | Free | High |
| Database | Data storage | 20 min | Paid | High |
| Zapier | No-code automation | 15 min | Paid | High |

---

## RECOMMENDED INTEGRATION STACK

**For Solo:**
- Notion (organize work)
- Google Drive (store files)
- GitHub (version control)
- Email (alerts)

**For Teams:**
- Add: Slack (team comms)
- Add: Discord (external updates)

**For Scale:**
- Add: Database (structured data)
- Add: Zapier (complex automation)

---

**End of Integration Guide**

Pick 2-3 integrations. Start simple. Add more as needed.

Each integration multiplies your leverage.
