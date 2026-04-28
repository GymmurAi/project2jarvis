# Project2Jarvis

## Project Overview

This project uses OpenCode with a specialized multi-agent system for AI agency work. It includes:
- **Council System**: Collaborative review agents for code quality, security, performance, etc.
- **Autonomous Agents**: Admin-level agents with full system access for building, researching, and maintaining.
- **3-Layer Memory**: Persistent memory across sessions (MEMORY.md → 03_Knowledge_Base/)
- **MCP Integration**: Extensible via Model Context Protocol servers (GitHub, Fetch, etc.)

## Quick Start

### Essential Reading
- **Memory Protocol**: Read `MEMORY.md` first (working memory, <200 lines)
- **Agent Roster**: See table below
- **Full Documentation**: `00_Meta/ARCHITECTURE.md`
- **MCP Setup**: `02_Workflows/mcp-setup.md`

### Autonomous Work (Builder/Researcher/Maintainer)

These agents have FULL system access and can make changes without asking:

```
/task builder     # Implement features autonomously
/task researcher   # Investigate and document findings
/task maintainer   # Update and clean up the system
```

Example:
```
/task builder
Implement a user authentication system with JWT tokens. Include login, register, and middleware.
```

### Council Reviews (Orchestrator + Members)

For comprehensive reviews, switch to the orchestrator:

```
/task council-orchestrator
Review the new feature in @src/features for security, performance, and quality.
```

Or invoke specific council members directly:
```
@council-security Review authentication in @src/auth
@council-architect Review the API design in @src/api
```

### Memory Management

Run the auto-summary script after each session:
```bash
python .opencode/scripts/auto-summary.py
```

This keeps MEMORY.md lean (<200 lines) and archives old content to `03_Knowledge_Base/lessons-learned.md`.

### Primary Agents (switch with Tab key)

| Agent | Role | Model | Permissions |
|-------|------|-------|-------------|
| `council-orchestrator` | Coordinates council reviews | claude-sonnet-4-5 | edit:ask, bash:ask |
| `council-system-architect` | System architecture design | claude-opus-4-5 | edit:ask, bash:ask |
| `builder` | Autonomous feature implementation | claude-sonnet-4-5 | **FULL ACCESS** |
| `researcher` | Autonomous investigation & documentation | gpt-5.1-codex | **FULL ACCESS** |
| `maintainer` | Autonomous system maintenance | claude-haiku-4-5 | **FULL ACCESS** |

### Council Subagents (invoke with @)

| Agent | Role | Model | Permissions |
|-------|------|-------|-------------|
| `council-architect` | Architecture & design review | claude-sonnet-4-5 | edit:deny, bash:ask |
| `council-security` | Security vulnerability assessment | claude-sonnet-4-5 | edit:deny, bash:ask |
| `council-performance` | Performance optimization review | claude-sonnet-4-5 | edit:deny, bash:ask |
| `council-quality` | Code quality & best practices | claude-haiku-4-5 | edit:deny, bash:deny |
| `council-docs` | Documentation review | claude-haiku-4-5 | edit:deny, bash:deny |

## Quick Start

### Autonomous Work (Builder/Researcher/Maintainer)

These agents have FULL system access and can make changes without asking:

```
/task builder     # Implement features autonomously
/task researcher   # Investigate and document findings
/task maintainer   # Update and clean up the system
```

Example:
```
/task builder
Implement a user authentication system with JWT tokens. Include login, register, and middleware.
```

### Council Reviews (Orchestrator + Members)

For comprehensive reviews, switch to the orchestrator:

```
/task council-orchestrator
Review the new feature in @src/features for security, performance, and quality.
```

Or invoke specific council members directly:
```
@council-security Review authentication in @src/auth
@council-architect Review the API design in @src/api
```

## Workflow Patterns

### 1. Build with Review
```
1. /task builder
   "Implement feature X"

2. /task council-orchestrator
   "Review feature X for security, performance, quality"
```

### 2. Research → Build → Review
```
1. /task researcher
   "Research best practices for X"

2. /task builder
   "Implement X following research findings"

3. /task council-orchestrator
   "Review implementation"
```

### 3. Maintenance Cycle
```
1. /task maintainer
   "Update dependencies, remove dead code, optimize build"

2. /task council-quality
   "Review code quality after maintenance"
```

## Project Structure

```
Project2Jarvis/ (Obsidian Vault + OpenCode Working Dir)
├── .opencode/
│   ├── agents/                    # All agent definitions
│   │   ├── council-orchestrator.md
│   │   ├── council-system-architect.md
│   │   ├── council-architect.md
│   │   ├── council-security.md
│   │   ├── council-performance.md
│   │   ├── council-quality.md
│   │   ├── council-docs.md
│   │   ├── builder.md             # Autonomous builder
│   │   ├── researcher.md          # Autonomous researcher
│   │   └── maintainer.md         # Autonomous maintainer
│   └── skills/
│       └── council/
│           └── SKILL.md
├── .obsidian/                     # Obsidian config
├── 00_Meta/                      # Project metadata
│   ├── AGENTS.md                 # This file
│   └── ARCHITECTURE.md
├── 01_Agents/                    # Agent registry & docs
├── 02_Workflows/                 # Standardized checklists
├── 03_Knowledge_Base/            # Research & postmortems
├── 04_Active_Work/               # Isolated task folders
└── 05_Archive/                   # Completed work
```

## Security Notes

- **Council agents** are restricted (read-only or ask-before-edit)
- **Autonomous agents** have FULL ACCESS - use with trust
- API keys stored in Windows Credential Manager (not in repo)
- All changes are git-versioned
- Branch protection recommended for main

## Customization

Edit agent files in `.opencode/agents/` to customize:
- System prompts and expertise
- Model and temperature settings
- Permission levels
- Tool access

## Dependencies

- OpenCode AI coding agent
- Obsidian (knowledge management)
- Council skill (auto-loaded from `.opencode/skills/council/SKILL.md`)
