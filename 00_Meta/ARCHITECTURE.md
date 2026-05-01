# Project2Jarvis: System Architecture Blueprint

**Version**: 1.0.0  
**Date**: 2026-04-28  
**Status**: Complete & Validated by Council  

---

## Table of Contents

1. [Overview](#overview)
2. [System Architecture](#system-architecture)
3. [Directory Structure](#directory-structure)
4. [Agent System](#agent-system)
5. [Memory Architecture](#memory-architecture)
6. [Workflow System](#workflow-system)
7. [Configuration](#configuration)
8. [Replication Guide](#replication-guide)
9. [Decision Log](#decision-log)

---

## Overview

Project2Jarvis is an AI Agency system built on two core technologies:
- **OpenCode**: AI coding agent with multi-agent support
- **Obsidian**: Knowledge management vault (markdown-based)

### Core Principles (Don't Break These)

1. **Simple > Complex**: Use native OpenCode features, no custom frameworks
2. **Markdown Everything**: All state in human-readable, git-versioned markdown
3. **Memory Layered**: 3-layer memory architecture prevents context loss
4. **Council + Autonomous**: Review agents (read-only) + Build agents (full access)
5. **Isolated Tasks**: Per-task folders prevent cross-contamination

### Why This Architecture?

| Problem | Solution |
|---------|----------|
| Previous agencies broke | Native features only (ADR-002) |
| Memory loss on restart | 3-layer memory (ADR-001) |
| Context window overflow | MEMORY.md <200 lines (ADR-001) |
| Unauthorized changes | Council agents read-only (ADR-003) |
| Shared state conflicts | Isolated 04_Active_Work/ folders |

---

## System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    OpenCode + Obsidian                       │
│  ┌─────────────────────────────────────────────────────┐  │
│  │                  Agent Layer                          │  │
│  │  Primary: builder, researcher, maintainer,          │  │
│  │           council-orchestrator, council-system-      │  │
│  │           architect                                 │  │
│  │  Subagents: council-architect, council-security,    │  │
│  │             council-performance, council-quality,     │  │
│  │             council-docs                            │  │
│  └─────────────────────────────────────────────────────┘  │
│  ┌─────────────────────────────────────────────────────┐  │
│  │                  Memory Layer                         │  │
│  │  Layer 1: Session (in-context, ephemeral)          │  │
│  │  Layer 2: Working (MEMORY.md <200 lines)           │  │
│  │  Layer 3: Permanent (03_Knowledge_Base/, etc.)      │  │
│  └─────────────────────────────────────────────────────┘  │
│  ┌─────────────────────────────────────────────────────┐  │
│  │                  Storage Layer                        │  │
│  │  Obsidian Vault = Git Repo = OpenCode Working Dir  │  │
│  │  All markdown, all version-controlled               │  │
│  └─────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Component Interaction

```
User → OpenCode TUI/CLI
  ↓
Primary Agent (builder/researcher/maintainer/orchestrator)
  ↓ (can invoke)
Subagents (council-*)
  ↓ (read/write)
Obsidian Vault (markdown files)
  ↓ (version control)
Git Repository
```

### Technology Stack

| Component | Technology | Rationale |
|-----------|-------------|-----------|
| AI Agent Runtime | OpenCode | Native multi-agent support, free models available |
| Knowledge Management | Obsidian | Markdown-native, graph view, human-readable |
| Version Control | Git | Full audit trail, rollback capability |
| Config Format | JSON/Markdown | OpenCode native, no custom parsers |
| Memory Format | Markdown | Obsidian-compatible, git-versioned |
| Security | Windows Credential Manager | OS-native, no repo secrets |

---

## Directory Structure

### Complete File Tree

```
Project2Jarvis/ (Obsidian Vault Root = Git Root = OpenCode Working Dir)
├── .git/                           # Version control
├── .gitignore                       # Ignore node_modules, .env, etc.
├── .opencode/                       # OpenCode configuration
│   ├── agents/                      # Agent definitions (markdown)
│   │   ├── builder.md               # Autonomous builder (FULL ACCESS)
│   │   ├── researcher.md            # Autonomous researcher (FULL ACCESS)
│   │   ├── maintainer.md            # Autonomous maintainer (FULL ACCESS)
│   │   ├── council-orchestrator.md  # Council coordinator (edit:ask)
│   │   ├── council-system-architect.md # System architect (edit:ask)
│   │   ├── council-architect.md     # Architecture reviewer (edit:deny)
│   │   ├── council-security.md      # Security reviewer (edit:deny)
│   │   ├── council-performance.md   # Performance reviewer (edit:deny)
│   │   ├── council-quality.md       # Quality reviewer (edit:deny)
│   │   ├── council-docs.md         # Documentation reviewer (edit:deny)
│   │   ├── ui-ux-pro-max.md        # UI/UX design intelligence (edit:ask)
│   │   └── personal-development-coach.md # Personal development coach (edit:ask)
│   ├── skills/                      # Skill definitions
│   │   ├── council/
│   │   │   └── SKILL.md             # Council system skill
│   │   └── ui-ux-pro-max/         # UI/UX Pro Max skill
│   │       └── SKILL.md
│   └── (future) plugins/           # OpenCode plugins (if needed)
├── .obsidian/                      # Obsidian configuration
│   └── (Obsidian auto-generated config)
├── 00_Meta/                        # Project metadata
│   ├── AGENTS.md                   # Agent roster & quick start (THIS FILE)
│   ├── ARCHITECTURE.md             # This document
│   └── (future) blueprints/       # System design documents
├── 01_Agents/                      # Agent-specific memory
│   ├── builder.md                  # Builder's learned patterns
│   ├── researcher.md               # Researcher's knowledge
│   ├── maintainer.md               # Maintainer's history
│   └── (future) council/          # Council shared memory
├── 02_Workflows/                   # Standardized checklists
│   ├── task-lifecycle.md           # Create → Execute → Review → Archive
│   ├── code-review.md              # Council review checklist
│   ├── memory-maintenance.md       # Daily/weekly/monthly tasks
│   └── (future) deployment.md     # Deployment workflow
├── 03_Knowledge_Base/              # Semantic memory (permanent)
│   ├── decisions-log.md            # ADRs (Architecture Decision Records)
│   ├── lessons-learned.md         # Accumulated insights
│   ├── agent-memory-solutions.md   # Research documents
│   └── (future) tech-stack.md    # Technology decisions
├── 04_Active_Work/                 # Episodic memory (sessions & tasks)
│   ├── session-2026-04-28.md      # Today's session log
│   ├── session-template.md         # Template for new sessions
│   ├── (future) feature-x/        # Task-specific folders
│   └── (future) research-y/       # Research task folders
├── 05_Archive/                     # Completed work (dated)
│   └── (future) 2026/            # Year-based archiving
├── MEMORY.md                       # Working memory (<200 lines)
└── AGENTS.md                       # Project rules (loaded by OpenCode)
```

### Directory Purposes

| Directory | Memory Layer | Lifetime | Git Versioned |
|-----------|--------------|----------|----------------|
| `00_Meta/` | Permanent | Permanent | ✅ |
| `01_Agents/` | Working | Months | ✅ |
| `02_Workflows/` | Permanent | Permanent | ✅ |
| `03_Knowledge_Base/` | Permanent | Permanent | ✅ |
| `04_Active_Work/` | Episodic | Days→Months | ✅ |
| `05_Archive/` | Permanent (old) | Permanent | ✅ |
| `.opencode/` | Config | Permanent | ✅ |

---

## Agent System

### Agent Roster

#### Primary Agents (Switch with Tab Key)

| Agent | Role | Permissions | Use When |
|-------|------|-------------|----------|
| `builder` | Autonomous feature implementation | **FULL ACCESS** (edit:allow, bash:allow, etc.) | Implementing features, fixing bugs |
| `researcher` | Autonomous investigation & docs | **FULL ACCESS** | Research, documentation, feasibility studies |
| `maintainer` | Autonomous system maintenance | **FULL ACCESS** | Updates, cleanup, health checks |
| `council-orchestrator` | Coordinates council reviews | edit:ask, bash:ask | Multi-agent code reviews |
| `council-system-architect` | System architecture design | edit:ask, bash:ask | Architecture decisions, system design |
| `ui-ux-pro-max` | UI/UX design intelligence (Pro Max) | edit:ask, bash:ask | UI/UX design, components, accessibility |
| `personal-development-coach` | Personal development coaching | edit:ask, bash:ask | Solihull College PPD coaching |
| `ui-ux-pro-max` | UI/UX design intelligence (Pro Max) | claude-opus-4-5 | edit:ask, bash:ask | UI/UX design, components, accessibility |
| `personal-development-coach` | Personal development coaching | claude-sonnet-4-5 | edit:ask, bash:ask | Solihull College PPD coaching |

#### Council Subagents (Invoke with @)

| Agent | Role | Permissions | Use When |
|-------|------|-------------|----------|
| `council-architect` | Architecture review | edit:deny, bash:ask | Reviewing system design |
| `council-security` | Security assessment | edit:deny, bash:ask | Security audits, vulnerability scans |
| `council-performance` | Performance review | edit:deny, bash:ask | Performance optimization |
| `council-quality` | Code quality review | edit:deny, bash:deny | Best practices, maintainability |
| `council-docs` | Documentation review | edit:deny, bash:deny | Documentation completeness |

### Agent Permissions Matrix

| Agent | read | edit | bash | task | external_dir | webfetch | websearch |
|-------|------|------|------|------|-------------|----------|----------|
| builder | allow | allow | allow | allow | allow | allow | allow |
| researcher | allow | allow | allow | allow | allow | allow | allow |
| maintainer | allow | allow | allow | allow | allow | allow | allow |
| council-orchestrator | allow | ask | ask | allow | deny | ask | ask |
| council-system-architect | allow | ask | ask | allow | deny | allow | allow |
| ui-ux-pro-max | allow | ask | ask | allow | deny | allow | allow |
| personal-development-coach | allow | ask | ask | allow | deny | allow | allow |
| council-architect | allow | deny | ask | allow | deny | allow | allow |
| council-security | allow | deny | ask | allow | deny | allow | allow |
| council-performance | allow | deny | ask | allow | deny | allow | allow |
| council-quality | allow | deny | deny | allow | deny | ask | ask |
| council-docs | allow | deny | deny | allow | deny | ask | ask |

### Agent File Template

All agents in `.opencode/agents/` follow this structure:

```markdown
---
description: [One-line description]
mode: primary|subagent
model: provider/model-id
temperature: 0.1-1.0
permission:
  read: allow|ask|deny
  edit: allow|ask|deny
  bash: allow|ask|deny
  task: allow|ask|deny
  external_directory: allow|ask|deny
---

## Memory Protocol
[Instructions for reading/updating memory files]

## Your Role
[Detailed description of agent's purpose]

## When to Use This Agent
[Scenarios and use cases]

## Your Process
[Step-by-step workflow]

## Guidelines
[Best practices and rules]

## Tools at Your Disposal
[What tools are available]

## Example Usage
[Sample commands and expected behavior]
```

---

## Memory Architecture

### 3-Layer Memory Model

```
┌─────────────────────────────────────────────────────────────┐
│ Layer 1: SESSION STATE (Ephemeral)                      │
│ • In-context messages array (OpenCode session)             │
│ • Lifetime: Current session only                          │
│ • No action needed - automatic                             │
└─────────────────────────────────────────────────────────────┘
                           ↓ (distillation at session end)
┌─────────────────────────────────────────────────────────────┐
│ Layer 2: WORKING MEMORY (Curated)                        │
│ • MEMORY.md (<200 lines, in project root)                 │
│ • 01_Agents/{agent}.md (per-agent memory)                │
│ • Lifetime: Months (actively maintained)                   │
│ • Action: Update after every session                       │
└─────────────────────────────────────────────────────────────┘
                           ↓ (promotion of important facts)
┌─────────────────────────────────────────────────────────────┐
│ Layer 3: PERMANENT MEMORY (Version-Controlled)           │
│ • 03_Knowledge_Base/ (research, ADRs, lessons)           │
│ • 04_Active_Work/session-YYYY-MM-DD.md (session logs)    │
│ • 01_Agents/ (agent-specific memory)                      │
│ • Lifetime: Permanent, git-versioned                       │
│ • Action: Update after major findings/tasks                │
└─────────────────────────────────────────────────────────────┘
```

### Memory Files Reference

| File | Layer | Purpose | Update When | Max Size |
|------|-------|----------|------------|----------|
| (in-context) | 1 | Active conversation | Automatic | Context window |
| `MEMORY.md` | 2 | Working memory, project context | End of session | 200 lines |
| `01_Agents/{agent}.md` | 2 | Agent-specific patterns | After tasks | 100 lines/agent |
| `04_Active_Work/session-YYYY-MM-DD.md` | 3 | Session logs | End of session | 300 lines/log |
| `03_Knowledge_Base/decisions-log.md` | 3 | Architecture decisions (ADRs) | Major decisions | Unlimited |
| `03_Knowledge_Base/lessons-learned.md` | 3 | Accumulated insights | After tasks | Unlimited |
| `03_Knowledge_Base/*.md` | 3 | Research documents | After research | Unlimited |

### Memory Protocol (What Agents Do)

#### Session Start (Every Agent Does This)
1. Read `MEMORY.md` → Project context and active tasks
2. Read `AGENTS.md` → Project rules and agent roster
3. Read `03_Knowledge_Base/decisions-log.md` → Recent decisions
4. Check `04_Active_Work/` → Recent session logs

#### During Task
1. Keep notes of key findings
2. Update `01_Agents/{agent}.md` with lessons learned
3. Cross-link using Obsidian wiki-links `[[like this]]`

#### Session End (Every Agent Does This)
1. Update `MEMORY.md` with new facts (keep <200 lines)
2. Create/update `04_Active_Work/session-YYYY-MM-DD.md`
3. Log decisions in `03_Knowledge_Base/decisions-log.md` (ADR format)
4. Update task status in `04_Active_Work/{task}/` (if applicable)

### Progressive Summarization

When `MEMORY.md` exceeds 200 lines:

```python
# Pseudo-code for summarization
def progressive_summarize(content, level):
    lines = content.split('\n')
    if level == 1:
        return '\n'.join(lines[:int(len(lines) * 0.4)])  # Keep 40%
    elif level == 2:
        return '\n'.join(lines[:int(len(lines) * 0.15)]) # Keep 15%
    else:
        return f"Summary as of {date}: [auto-summarized]"
```

**Manual approach**: Move older content to `03_Knowledge_Base/lessons-learned.md`

---

## Workflow System

### Standard Workflows

#### 1. Task Lifecycle (`02_Workflows/task-lifecycle.md`)

```
Create → Assign → Execute → Review → Complete → Archive
```

| Step | Action | Files |
|------|--------|-------|
| Create | Define task in `04_Active_Work/{task}/README.md` | `04_Active_Work/{task}/` |
| Assign | Choose agent (builder/researcher/maintainer) | `AGENTS.md` |
| Execute | Do the work, update memory | Task folder |
| Review | Invoke `@council-orchestrator` for review | Council agents |
| Complete | Update `MEMORY.md`, commit | Git |
| Archive | Move to `05_Archive/` | `05_Archive/{task}/` |

#### 2. Code Review (`02_Workflows/code-review.md`)

Council review process:

1. **Invoke**: `/task council-orchestrator`
2. **Delegates to**:
   - `@council-security` → Security (Critical/High/Medium/Low)
   - `@council-performance` → Performance (Critical/High/Medium/Low)
   - `@council-quality` → Quality (Must Fix/Should Fix/Consider)
   - `@council-docs` → Documentation (Critical/Important/Helpful)
3. **Synthesizes**: Orchestrator combines all feedback
4. **Verdict**: APPROVE / APPROVE WITH MINOR FIXES / REQUEST CHANGES

#### 3. Memory Maintenance (`02_Workflows/memory-maintenance.md`)

| Frequency | Tasks |
|-----------|-------|
| **Daily** (end of session) | Update MEMORY.md, create session log, update agent memory |
| **Weekly** | Summarize MEMORY.md if >200 lines, review lessons-learned.md |
| **Monthly** | Archive old session logs, review decisions-log.md, clean 04_Active_Work/ |
| **Quarterly** | Evaluate vault size, consider RAG/MCP if >1000 files |

---

## Configuration

### OpenCode Config (`~/.config/opencode/opencode.json` or `opencode.json`)

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "models": {
        "phi3": {"_launch": true, "name": "phi3"},
        "qwen3-vl:2b": {"_launch": true, "name": "qwen3-vl:2b"}
      },
      "npm": "@ai-sdk/openai-compatible",
      "options": {"baseURL": "http://127.0.0.1:11434/v1"}
    }
  },
  "permission": {
    "external_directory": "deny"
  },
  "autoupdate": true
}
```

**Note**: Don't set `model` in config to allow last-used model to load.

### Agent Config (`.opencode/agents/*.md`)

See [Agent File Template](#agent-file-template) above.

### Obsidian Config (`.obsidian/`)

Auto-generated. Recommended settings:
- Enable "Auto update internal links"
- Enable "Auto rename headers"
- Set attachment folder: `05_Archive/attachments/`

---

## Replication Guide

### How to Replicate This System on a New Project

#### Step 1: Initialize Project

```bash
# Create project directory
mkdir MyNewProject
cd MyNewProject

# Initialize git
git init

# Initialize OpenCode
opencode
/init
```

#### Step 2: Create Directory Structure

```bash
# Create all directories
mkdir -p .opencode/agents .opencode/skills/council
mkdir -p .obsidian
mkdir -p 00_Meta 01_Agents 02_Workflows
mkdir -p 03_Knowledge_Base 04_Active_Work 05_Archive
```

#### Step 3: Copy Agent Definitions

Copy all files from `.opencode/agents/` in Project2Jarvis to your new project's `.opencode/agents/`.

**Core agents to copy**:
- `builder.md`
- `researcher.md`
- `maintainer.md`
- `council-orchestrator.md`
- `council-system-architect.md`
- `council-architect.md`
- `council-security.md`
- `council-performance.md`
- `council-quality.md`
- `council-docs.md`

#### Step 4: Copy Skills

```bash
cp -r .opencode/skills/council /path/to/MyNewProject/.opencode/skills/
```

#### Step 5: Create Memory Files

Create these files in your new project:

**MEMORY.md** (in project root):
```markdown
# Working Memory

*Last updated: YYYY-MM-DD by [agent]*

## Project Context
- Project: [Your Project Name]
- Tech stack: [Your tech stack]
- Current focus: [What you're working on]

## Key Decisions Made
- [YYYY-MM-DD] [Decision] - [Rationale]

## Active Tasks
- [status] [Task name]

## Things to Remember
- [Fact 1]
- [Fact 2]
```

**03_Knowledge_Base/decisions-log.md**:
```markdown
# Decision Log

*Architecture Decision Records (ADRs) for [Project Name]*

---

## ADR-001: [Title]

**Status**: Accepted  
**Date**: YYYY-MM-DD  
**Deciders**: [agents]

### Context
[Background]

### Decision
[What was decided]

### Consequences
- **Positive**: [Benefits]
- **Negative**: [Drawbacks]
```

**03_Knowledge_Base/lessons-learned.md**:
```markdown
# Lessons Learned

*Accumulated insights from building and breaking things*

---

## Technical Lessons

- **Lesson**: [What was learned]
  - **Solution**: [How to handle it]
  - **Date**: YYYY-MM-DD
```

#### Step 6: Create Workflow Files

Copy from Project2Jarvis:
```bash
cp 02_Workflows/*.md /path/to/MyNewProject/02_Workflows/
```

#### Step 7: Create Documentation

**AGENTS.md** (in project root):
```markdown
# [Project Name]

## Project Overview
[Describe your project]

## Agent Roster
[Copy table from Project2Jarvis AGENTS.md, modify as needed]

## Quick Start
[How to use the agents]
```

**00_Meta/ARCHITECTURE.md**:
- Copy this file and modify for your project

#### Step 8: Create .gitignore

```
node_modules/
.env
*.log
.DS_Store
Thumbs.db
05_Archive/attachments/
```

#### Step 9: Test the Setup

```bash
# Start OpenCode
opencode

# Switch to builder agent
/task builder

# Test memory loading
"Read MEMORY.md and tell me what this project is about"
```

#### Step 10: Commit Everything

```bash
git add .
git commit -m "feat: initial AI agency setup with council agents and 3-layer memory"
```

---

## Decision Log

Key decisions made during development (see `03_Knowledge_Base/decisions-log.md` for full ADRs):

| ADR | Decision | Rationale |
|-----|----------|-----------|
| 001 | Adopt 3-layer memory architecture | Prevents context loss, persists across sessions |
| 002 | Use OpenCode native features only | No custom frameworks to break |
| 003 | Council read-only, Autonomous full access | Balance safety with capability |
| 004 | All state in markdown + Git | Human-readable, version-controlled |

---

## Appendix: Quick Reference

### Agent Commands

| Action | Command |
|--------|----------|
| Switch to builder | `/task builder` or **Tab** key |
| Switch to researcher | `/task researcher` or **Tab** key |
| Switch to maintainer | `/task maintainer` or **Tab** key |
| Switch to orchestrator | `/task council-orchestrator` or **Tab** key |
| Invoke security review | `@council-security [prompt]` |
| Invoke performance review | `@council-performance [prompt]` |
| Full council review | `/task council-orchestrator` then describe review |

### Memory Commands

| Action | File |
|--------|------|
| Read working memory | `cat MEMORY.md` |
| Read session logs | `ls 04_Active_Work/session-*.md` |
| Read decisions | `cat 03_Knowledge_Base/decisions-log.md` |
| Read lessons | `cat 03_Knowledge_Base/lessons-learned.md` |

### File Creation Checklist for New Projects

- [ ] `.opencode/agents/*.md` (10 agent files)
- [ ] `.opencode/skills/council/SKILL.md`
- [ ] `MEMORY.md`
- [ ] `AGENTS.md`
- [ ] `00_Meta/ARCHITECTURE.md`
- [ ] `01_Agents/*.md` (3 agent memory files)
- [ ] `02_Workflows/*.md` (3 workflow files)
- [ ] `03_Knowledge_Base/decisions-log.md`
- [ ] `03_Knowledge_Base/lessons-learned.md`
- [ ] `04_Active_Work/session-template.md`
- [ ] `.gitignore`

---

**End of Architecture Blueprint**

*This document serves as the canonical reference for the Project2Jarvis system. Replicate by following the [Replication Guide](#replication-guide).*

*Last updated: 2026-04-28 by council-orchestrator*  
*Version: 1.0.0*  
*Status: Validated by full council review*
