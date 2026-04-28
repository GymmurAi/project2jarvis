# AI Agent Memory Solutions: Obsidian + OpenCode

**Research Date:** 2026-04-28  
**Researcher:** Autonomous Researcher Agent  
**Status:** Complete

---

## 1. Executive Summary

AI agents suffer from two types of memory loss: **context window truncation** (losing information within a session) and **session amnesia** (losing all context between sessions). This research evaluated solutions and found that **a layered markdown-based memory architecture using Obsidian + OpenCode** is the most practical approach for our project.

### Key Findings

| Approach | Complexity | Effectiveness | Best For |
|----------|------------|---------------|----------|
| AGENTS.md / CLAUDE.md | Low | Medium | Rules, instructions, project context |
| MEMORY.md + auto-memory | Low-Medium | High | Persistent facts, preferences, decisions |
| Obsidian vault (3-layer) | Medium | Very High | Long-term knowledge, relationships, graphs |
| MCP memory server | Medium | High | Structured memory with tool access |
| Vector RAG | High | High (at scale) | Large document collections (>1000 files) |
| Hybrid (recommended) | Medium | Very High | Production agent systems |

### Recommended Architecture
**A 3-layer memory system** combining OpenCode's native AGENTS.md, a curated MEMORY.md file, and a structured Obsidian vault with daily notes, agent logs, and knowledge graphs.

---

## 2. Obsidian-Based Memory Architecture

### 2.1 The Three-Layer Model

Adapted from research by Moun R. (Towards AI, 2026) and obsidian-memory-for-ai:

```
┌─────────────────────────────────────────────────────────────┐
│                    LAYER 1: Session State                    │
│  Temporary, ephemeral context during active conversation     │
│  Location: In-context messages array (OpenCode session)     │
│  Lifetime: Current session only                             │
└─────────────────────────────────────────────────────────────┘
                              ↓ (distillation)
┌─────────────────────────────────────────────────────────────┐
│                    LAYER 2: Working Memory                  │
│  Curated facts, decisions, preferences that persist          │
│  Location: MEMORY.md + .opencode/memory/*.md               │
│  Lifetime: Months, actively maintained                      │
└─────────────────────────────────────────────────────────────┘
                              ↓ (promotion)
┌─────────────────────────────────────────────────────────────┐
│                    LAYER 3: Permanent Memory                │
│  Structured knowledge base in Obsidian vault                │
│  Location: 03_Knowledge_Base/, 01_Agents/, etc.           │
│  Lifetime: Permanent, version-controlled, graph-connected   │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Memory Types (Cognitive Science Taxonomy)

Research confirms AI agents follow human memory models:

| Type | Description | Storage | Example |
|------|-------------|----------|---------|
| **Episodic** | Specific events, sessions, conversations | `04_Active_Work/session-logs/` | "Fixed auth bug on 2026-04-28" |
| **Semantic** | Facts, concepts, relationships | `03_Knowledge_Base/` | "JWT tokens expire in 24h" |
| **Procedural** | How-to knowledge, workflows | `02_Workflows/` | "Council review process" |
| **Working** | Current task context | `MEMORY.md`, session state | "Currently implementing X" |

### 2.3 Obsidian Vault Structure for Agent Memory

```
Project2Jarvis/ (Obsidian Vault)
├── 00_Meta/
│   ├── AGENTS.md                 # Rules, identity, loading instructions
│   ├── MEMORY.md                 # Curated working memory (200 lines max)
│   └── ARCHITECTURE.md           # System design (static)
│
├── 01_Agents/                    # Agent-specific memory
│   ├── builder.md                # Builder agent's persistent context
│   ├── researcher.md             # Researcher agent's knowledge
│   ├── maintainer.md             # Maintainer agent's history
│   └── council/                  # Council agent shared memory
│       ├── security-findings.md
│       └── architecture-decisions.md
│
├── 02_Workflows/                 # Procedural memory
│   ├── code-review-checklist.md
│   ├── feature-implementation.md
│   └── memory-maintenance.md     # How to curate memory
│
├── 03_Knowledge_Base/            # Semantic memory
│   ├── agent-memory-solutions.md # This document
│   ├── tech-stack.md             # Project technical decisions
│   ├── lessons-learned.md        # Accumulated insights
│   └── decisions-log.md         # ADR (Architecture Decision Records)
│
├── 04_Active_Work/               # Episodic memory (current)
│   ├── session-2026-04-28.md
│   ├── session-2026-04-27.md
│   └── [task-specific folders]
│
└── 05_Archive/                   # Old/completed work
    └── [dated archives]
```

---

## 3. Implementation Guide for Project2Jarvis

### 3.1 Phase 1: Foundation (AGENTS.md + MEMORY.md)

**Step 1: Enhance AGENTS.md with Memory Instructions**

Add to the existing `AGENTS.md`:

```markdown
## Memory Protocol

### Startup Sequence (every session)
1. Read `AGENTS.md` (this file) - identity and rules
2. Read `MEMORY.md` - curated working memory
3. Read `03_Knowledge_Base/decisions-log.md` - recent decisions
4. Read today's session file: `04_Active_Work/session-YYYY-MM-DD.md`

### Memory Maintenance (end of session)
1. Update `MEMORY.md` with new facts/decisions (keep under 200 lines)
2. Append session summary to `04_Active_Work/session-YYYY-MM-DD.md`
3. If significant knowledge discovered: update `03_Knowledge_Base/` files
4. Log decisions in `03_Knowledge_Base/decisions-log.md`

### Memory Files Purpose
- `AGENTS.md` - Rules and identity (NEVER auto-modify)
- `MEMORY.md` - Working memory, actively curated (AI can update)
- `04_Active_Work/session-*.md` - Episodic logs (append-only)
- `03_Knowledge_Base/` - Permanent semantic knowledge (AI-maintained)
```

**Step 2: Create MEMORY.md**

```markdown
# Working Memory

*Last updated: 2026-04-28 by researcher*

## Project Context
- Project: Project2Jarvis (OpenCode + Obsidian multi-agent system)
- Tech stack: OpenCode, Obsidian, MCP servers
- Current focus: Solving agent memory loss problem

## Key Decisions Made
- [2026-04-28] Adopted 3-layer memory architecture (session/working/permanent)
- [2026-04-28] Using markdown files (no vector DB yet - may add later if >1000 docs)

## Active Tasks
- Implementing memory solution (researcher agent, in progress)

## Things to Remember
- Council agents are read-only (edit:deny)
- Autonomous agents (builder/researcher/maintainer) have FULL ACCESS
- API keys in Windows Credential Manager (not in repo)
```

### 3.2 Phase 2: Agent-Specific Memory Files

Create per-agent memory in `01_Agents/`:

**File: `01_Agents/builder.md`**
```markdown
---
agent: builder
last_updated: 2026-04-28
permissions: full
---

# Builder Agent Memory

## My Role
Autonomous feature implementation with full system access.

## Project Patterns I've Learned
- Always update AGENTS.md when adding new agents
- Council review required after major features
- Use `04_Active_Work/` for work-in-progress

## Recent Work
- (Will be appended after each task)

## Preferences
- User prefers concise code
- Always run lint/typecheck after changes
```

### 3.3 Phase 3: Session Logging

Create a session template in `04_Active_Work/session-YYYY-MM-DD.md`:

```markdown
---
date: 2026-04-28
agent: researcher
task: Investigate AI agent memory solutions
---

# Session Log: 2026-04-28

## Task Description
Investigate how to solve AI agent memory loss using Obsidian + OpenCode.

## Actions Taken
1. Searched web for "AI agent persistent memory Obsidian"
2. Searched web for "OpenCode memory techniques"
3. Researched mem0, RAG, progressive summarization
4. Compiled findings into 03_Knowledge_Base/agent-memory-solutions.md

## Key Findings
- 3-layer memory architecture is emerging standard
- Markdown files sufficient for <1000 document collections
- MEMORY.md should stay under 200 lines
- Obsidian vault = permanent layer with graph connections

## Decisions Made
- Adopt hybrid approach: AGENTS.md + MEMORY.md + Obsidian vault
- No vector DB initially (can add via MCP later)

## Next Steps
- Implement Phase 1 (AGENTS.md + MEMORY.md)
- Create agent-specific memory files
- Set up automated session logging
```

### 3.4 Phase 4: Automated Memory Operations (Optional Enhancement)

Using OpenCode's MCP support, integrate with memory MCP servers:

**Option A: obsidian-memory-layer-mcp**
```json
// opencode.json
{
  "mcp": {
    "obsidian-memory": {
      "command": "npx",
      "args": ["obsidian-memory-layer-mcp"],
      "env": {
        "VAULT_PATH": "D:\\Projects\\Project2Jarvis"
      }
    }
  }
}
```

**Option B: Simple shell hook (no extra dependencies)**
```bash
# .opencode/hooks/session-end.sh
#!/bin/bash
# Auto-save session summary to Obsidian
echo "## Session $(date +%Y-%m-%d)" >> 04_Active_Work/session-$(date +%Y-%m-%d).md
echo "Agent: $AGENT_NAME" >> 04_Active_Work/session-$(date +%Y-%m-%d).md
```

---

## 4. Code Examples and File Structures

### 4.1 OpenCode Agent with Memory Instructions

**File: `.opencode/agents/researcher.md`**
```markdown
---
name: researcher
description: Autonomous investigation & documentation
model: gpt-5.1-codex
tools:
  bash: true
  write: true
  edit: true
---

# Researcher Agent

You are an autonomous research agent with full system access.

## Memory Protocol
Before starting any task:
1. Read MEMORY.md for project context
2. Read 03_Knowledge_Base/ relevant files
3. Check 04_Active_Work/ for recent session logs

After completing any task:
1. Append findings to appropriate 03_Knowledge_Base/ file
2. Update MEMORY.md if new persistent facts discovered
3. Create session log in 04_Active_Work/session-$(date +%Y-%m-%d).md

## Research Workflow
1. Web search for current best practices (year: 2026)
2. Read existing documentation
3. Compile findings into markdown
4. Save to 03_Knowledge_Base/
5. Update related memory files
```

### 4.2 MEMORY.md Maintenance Script (Progressive Summarization)

```python
# .opencode/scripts/summarize_memory.py
# Run periodically to compress MEMORY.md using progressive summarization

import datetime
import os

MEMORY_FILE = "MEMORY.md"
MAX_LINES = 200
SUMMARY_FILE = "03_Knowledge_Base/lessons-learned.md"

def progressive_summarize(content, level=1):
    """Tiago Forte's progressive summarization adapted for AI memory"""
    if level == 1:
        # Keep 40% most important content
        lines = content.split('\n')
        return '\n'.join(lines[:int(len(lines) * 0.4)])
    elif level == 2:
        # Extract critical points (15%)
        lines = content.split('\n')
        return '\n'.join(lines[:int(len(lines) * 0.15)])
    else:
        # Executive summary (5%)
        return f"Summary as of {datetime.date.today()}: [auto-summarized]"

# Usage: Agent runs this when MEMORY.md exceeds 200 lines
```

### 4.3 RAG-Enhanced Memory (Future Option)

If the vault grows beyond 1000 documents, add semantic search via MCP:

```json
// opencode.json - Add RAG-MCP server
{
  "mcp": {
    "markdown-rag": {
      "command": "uvx",
      "args": ["ragdocs-mcp"],
      "env": {
        "DOCUMENTS_PATH": "D:\\Projects\\Project2Jarvis",
        "INDEX_PATH": ".index_data"
      }
    }
  }
}
```

Agent can then use:
```
@markdown-rag search "authentication best practices"
```

---

## 5. Comparison of Approaches

### 5.1 Detailed Comparison

| Approach | Pros | Cons | When to Use |
|----------|------|------|-------------|
| **AGENTS.md only** | Simple, built-in, auto-loads | Limited to rules/instructions, not dynamic state | Small projects, simple agents |
| **MEMORY.md + auto-memory** | Persistent facts, learning over time, built-in | Can grow large, needs curation | Medium projects, coding agents |
| **Obsidian 3-layer** | Permanent, graph-connected, human-readable, version-controlled | More complex setup | Production agents, knowledge work |
| **MCP Memory Server** | Structured tools, session management, automated | Extra dependency, learning curve | Teams, multi-agent systems |
| **Vector RAG** | Scales to millions of docs, semantic search | Complex, latency, cost, overkill for small vaults | Large document collections |
| **mem0 / Mem0** | Managed service, graph+vector, benchmarks | Cloud dependency, cost, less control | Enterprise, multi-user |
| **Hybrid (recommended)** | Best of all worlds, progressive enhancement | More files to manage | This project |

### 5.2 Recommendations for Project2Jarvis

**Immediate Implementation (This Week):**
1. ✅ Enhance `AGENTS.md` with memory protocol section
2. ✅ Create `MEMORY.md` with curated working memory
3. ✅ Set up `04_Active_Work/` for session logs
4. ✅ Create agent-specific memory in `01_Agents/`

**Short Term (Next Month):**
1. Implement automated session logging (shell hook or MCP)
2. Create `03_Knowledge_Base/decisions-log.md` for ADRs
3. Train agents to update memory files after tasks
4. Add `lessons-learned.md` for accumulated insights

**Medium Term (If Needed):**
1. Add MCP memory server (obsidian-memory-layer-mcp)
2. Implement semantic search if vault exceeds 1000 files
3. Consider mem0 integration for graph memory features

**Long Term (Research Only):**
1. Evaluate memory compression algorithms (ReSum, Agent Memory Compressor)
2. Implement memory decay for stale facts
3. Add multi-agent shared memory with conflict resolution

### 5.3 Key Principles to Follow

1. **Start Simple** - AGENTS.md + MEMORY.md is enough for most use cases
2. **Be Selective** - Don't store everything; curate what's worth remembering
3. **Metadata Matters** - Use YAML frontmatter for filtering and organization
4. **Human-Readable** - Markdown files can be inspected, edited, version-controlled
5. **Progressive Enhancement** - Add complexity only when the simpler solution is insufficient
6. **Recall Before Act** - Agents should load memory before making decisions
7. **Manage Decay** - Delete or archive stale memories (don't let them accumulate forever)

---

## 6. Research Sources

1. Moun R., "I Gave My AI Agent a Three-Layer Memory. Here's How It Thinks Now." (Towards AI, 2026-03-12)
2. "How Claude Code Remembers (And Forgets)" (Dev.to, 2026-04-10)
3. obsidian-memory-for-ai GitHub repository (jrcruciani, 2026)
4. obsidian-memory-layer-mcp GitHub repository (honam867, 2026)
5. "AI Agent Memory Architectures: From Context Windows to Persistent Knowledge" (Zylos Research, 2026-04-05)
6. "State of AI Agent Memory 2026" (Mem0.ai, 2026-04-01)
7. "Give Your AI Agent Persistent Memory in 2026" (kjetilfuras.com, 2026-04-10)
8. "Progressive Summarization" (Tiago Forte, Building a Second Brain, 2022)
9. OpenCode Documentation - Agents, Rules (AGENTS.md), Config
10. "How to Build AI Agents with Persistent Memory" (RetainDB, 2026)

---

## 7. Next Steps

1. **This document is complete** - share with team for review
2. **Implement Phase 1** - enhance AGENTS.md, create MEMORY.md
3. **Train agents** - update agent prompts with memory protocol
4. **Test** - start new session, verify agents load memory correctly
5. **Iterate** - refine based on what works/fails in practice

---

*End of research document. Last updated: 2026-04-28 by researcher agent.*
