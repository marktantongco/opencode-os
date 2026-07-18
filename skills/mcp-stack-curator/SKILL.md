---
name: mcp-stack-curator
description: >
  Recommends which 4 MCP servers to use together — solves the unsolved problem of server combination synergy with conflict detection. Use when use when deciding which mcp servers to combine for maximum synergy
  Triggers on keywords: mcp, stacks, synergy, curation, combinations.
allowed-tools: Read, Write, Bash, Edit, Grep, Glob
user-invocable: true
mcp-servers: [filesystem, github]
---

# MCP Stack Curator

## context

Recommends which 4 MCP servers to use together — solves the "which MCP servers should I install" problem by analyzing project needs and recommending optimal server combinations. This skill operates within the MCP (Model Context Protocol) ecosystem, providing tools for server discovery, configuration, security, and orchestration.

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

**Input:** "Use when deciding which MCP servers to combine for maximum synergy"

**Output:**
```markdown
## MCP Server Configuration

### Recommended Server
- Name: Mcp Stack Curator
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
