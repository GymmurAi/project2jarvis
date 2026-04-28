# Decision Log

*Architecture Decision Records (ADRs) for Project2Jarvis*

---

## ADR-001: Adopt 3-Layer Memory Architecture

**Status**: Accepted  
**Date**: 2026-04-28  
**Deciders**: researcher, council-orchestrator

### Context
AI agents suffer from memory loss due to context window truncation and session restarts. Previous agencies broke partly due to this issue.

### Decision
Implement a 3-layer memory system:
1. **Layer 1 (Session)**: In-context messages (ephemeral)
2. **Layer 2 (Working)**: MEMORY.md + agent-specific files (months)
3. **Layer 3 (Permanent)**: Obsidian vault (03_Knowledge_Base/, 01_Agents/, etc.) - permanent, version-controlled

### Consequences
- **Positive**: Agents can persist knowledge across sessions, markdown is human-readable and git-versioned
- **Negative**: Requires disciplined maintenance (agents must update memory files)
- **Risk**: MEMORY.md can grow too large (>200 lines) - needs periodic summarization

---

## ADR-002: Use OpenCode Native Features (No Custom Frameworks)

**Status**: Accepted  
**Date**: 2026-04-28  
**Deciders**: systemarchitect

### Context
Previous AI agencies broke due to custom frameworks that became unmaintainable or had hidden state.

### Decision
Use only native OpenCode features:
- Agent definitions in `.opencode/agents/*.md`
- Skills in `.opencode/skills/*/SKILL.md`
- Config in `opencode.json`
- No custom Python/Node.js frameworks

### Consequences
- **Positive**: Less code to break, easier to understand, upgrades are simple
- **Negative**: Limited to OpenCode's built-in capabilities
- **Mitigation**: Can add MCP servers if native features are insufficient

---

## ADR-003: Council Agents Read-Only, Autonomous Agents Full Access

**Status**: Accepted  
**Date**: 2026-04-28  
**Deciders**: council-orchestrator

### Context
Need balance between safety (preventing accidental damage) and capability (allowing autonomous work).

### Decision
- **Council agents** (council-*): `edit: deny` or `edit: ask` - review-only, safe
- **Autonomous agents** (builder, researcher, maintainer): `edit: allow, bash: allow` - full system access

### Consequences
- **Positive**: Safety for reviews, power for implementation
- **Negative**: Autonomous agents could cause damage if prompted incorrectly
- **Mitigation**: Use git for rollback, branch protection for main

---

## ADR-004: All State in Markdown + Git

**Status**: Accepted  
**Date**: 2026-04-28  
**Deciders**: systemarchitect, researcher

### Context
Previous agencies broke due to databases, hidden state, or unpublished changes.

### Decision
- All agent state, memory, knowledge in markdown files
- All changes committed to Git within 24 hours
- No binary state, no databases, no hidden files

### Consequences
- **Positive**: Full audit trail, human-readable, can use Obsidian for visualization
- **Negative**: Markdown can be slower for large datasets (>1000 files)
- **Mitigation**: Use RAG/MCP if vault exceeds 1000 documents

---

## Template for New ADRs

```
## ADR-XXX: [Title]

**Status**: Proposed/Accepted/Deprecated  
**Date**: YYYY-MM-DD  
**Deciders**: [agent names]

### Context
[Background and problem statement]

### Decision
[What we decided to do]

### Consequences
- **Positive**: [Benefits]
- **Negative**: [Drawbacks]
- **Risk**: [Risks and mitigations]
```
