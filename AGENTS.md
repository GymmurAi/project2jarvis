# Project2Jarvis

## Project Overview

This project uses OpenCode with a specialized multi-agent system for AI agency work. It includes:
- **Council System**: Collaborative review agents for code quality, security, performance, etc.
- **Autonomous Agents**: Admin-level agents with full system access for building, researching, and maintaining.
- **3-Layer Memory**: Persistent memory across sessions (MEMORY.md → 03_Knowledge_Base/)
- **MCP Integration**: Extensible via Model Context Protocol servers (GitHub, Fetch, etc.)

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

### Memory Management

Run the auto-summary script after each session:
```bash
python .opencode/scripts/auto-summary.py
```

This keeps MEMORY.md lean (<200 lines) and archives old content to `03_Knowledge_Base/lessons-learned.md`.

### Primary Agents (switch with Tab key)

| Agent | Role | Permissions |
|-------|------|-------------|
| `council-orchestrator` | Coordinates council reviews | edit:ask, bash:ask |
| `council-system-architect` | System architecture design | edit:ask, bash:ask |
| `ui-ux-pro-max` | UI/UX design intelligence (Pro Max) | edit:ask, bash:ask |
| `personal-development-coach` | Personal development coaching (Solihull College) | edit:ask, bash:ask |
| `builder` | Autonomous feature implementation | **FULL ACCESS** |
| `researcher` | Autonomous investigation & documentation | **FULL ACCESS** |
| `maintainer` | Autonomous system maintenance | **FULL ACCESS** |

### Council Subagents (invoke with @)

| Agent | Role | Permissions |
|-------|------|-------------|
| `council-architect` | Architecture & design review | edit:deny, bash:ask |
| `council-security` | Security vulnerability assessment | edit:deny, bash:ask |
| `council-performance` | Performance optimization review | edit:deny, bash:ask |
| `council-quality` | Code quality & best practices | edit:deny, bash:deny |
| `council-docs` | Documentation review | edit:deny, bash:deny |

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
│   │   ├── maintainer.md         # Autonomous maintainer
│   │   ├── ui-ux-pro-max.md      # UI/UX design intelligence
│   │   └── personal-development-coach.md
│   └── skills/
│       ├── council/
│       │   └── SKILL.md
│       └── ui-ux-pro-max/         # UI/UX Pro Max skill
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
