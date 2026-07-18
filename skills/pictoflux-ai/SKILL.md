---
name: pictoflux-ai
description: >
  AI-powered image generation and visual editing via MCP protocol — create, transform, and composite images through standardized tool calls. Use when use when generating or editing images via mcp protocol tool calls
  Triggers on keywords: mcp, image, visual, generation, editing.
allowed-tools: Read, Write, Bash, Edit, Grep, Glob
user-invocable: true
mcp-servers: [filesystem, github]
---

# AI Image Generation via MCP

## context

AI-powered image generation and visual editing via MCP protocol. Generate, modify, and transform images using natural language prompts with support for multiple styles, sizes, and formats. This skill operates within the MCP (Model Context Protocol) ecosystem, providing tools for server discovery, configuration, security, and orchestration.

## instructions

### Step 1: Identify MCP Requirements

1. Determine what MCP capability is needed — image generation, server discovery, security audit, or stack recommendation
2. Assess compatibility — which MCP client (Claude Desktop, Cursor, VS Code) is being used
3. Check existing MCP configuration — what servers are already installed

### Step 2: Execute MCP Operation

1. **Discovery** — Search available MCP servers matching the requirement
2. **Evaluation** — Assess server quality, maintenance status, and security posture
3. **Configuration** — Generate client-specific configuration entries
4. **Validation** — Test the server connection and verify functionality

### Step 3: Generate MCP Configuration

```markdown
## MCP Server Configuration

### Recommended Server
- Name: server name
- Package: npm/pip package identifier
- Version: latest stable version
- Category: server category

### Client Configuration
Configuration JSON for Claude Desktop, Cursor, and VS Code clients.

### Capabilities
- Tool 1: description
- Tool 2: description

### Security Notes
- Permission requirements
- Data handling considerations
```

### Step 4: Validate and Test

- [ ] Server starts without errors
- [ ] All advertised tools are accessible
- [ ] Authentication works correctly
- [ ] Rate limits are documented
- [ ] Error handling is graceful

## constraints

- NEVER install MCP servers from unverified sources without security review.
- NEVER expose sensitive credentials in MCP server configuration.
- NEVER assume MCP server compatibility across clients — always test.
- ALWAYS check server maintenance status before recommending.
- ALWAYS document security implications of each MCP server.

## examples

### Example: MCP Server Setup

**Input:** "Use when generating or editing images via MCP protocol tool calls"

**Output:**
```markdown
## MCP Server Configuration

### Recommended Server
- Name: Pictoflux Ai
- Category: MCP Servers
- Status: Active, well-maintained

### Client Configuration
Configuration entries for Claude Desktop, Cursor, and VS Code provided.

### Capabilities
- Core tools documented and tested
- Authentication verified
- Rate limits documented

### Security Notes
- Review permissions before enabling
- Test in isolated environment first
- Monitor for unusual activity
```
