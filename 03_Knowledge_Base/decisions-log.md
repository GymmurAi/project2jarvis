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

## ADR-005: Executive Command Center High-Grade Color Scheme
**Status**: Accepted  
**Date**: 2026-04-29  
**Deciders**: @council-architect, @council-quality, Builder

### Context
User rated current violet/stone/gold palette as "low-grade" - felt consumer/creative, not executive. Needed financial-industry-standard colors.

### Decision
Implement high-grade Navy/Teal/Gold palette:
- **Navy (#1E293B)**: Authority color (replaces violet)
- **Teal (#14B8A6)**: Data visualization (replaces stone)
- **Gold (#F59E0B)**: Revenue SIGNAL ONLY (not decoration)
- **Light theme mandatory** (conference rooms, printing)

### Consequences
- **Positive**: Executive-standard, Bloomberg-style authority, WCAG 2.1 AA compliant
- **Negative**: All existing violet/stone references needed updating
- **Risk**: Gold loses signaling power if overused → Mitigation: Gold ONLY for revenue KPIs

## ADR-006: Heroicons v2.0 Mandatory for All Icons
**Status**: Accepted  
**Date**: 2026-04-29  
**Deciders**: UI/UX Pro Max, Builder

### Context
Emoji icons and 2px stroke icons look unprofessional. Need consistent, executive-grade icon system.

### Decision
- ALL icons = Heroicons v2.0 only (24x24 viewBox)
- Stroke-width = 1.5px (NOT 2px)
- Available: https://heroicons.com/ (316 icons, MIT license)

### Consequences
- **Positive**: Professional consistency, industry standard, Tailwind makers approved
- **Negative**: Requires manual replacement of emojis
- **Risk**: Accidental use of 2px stroke icons → Mitigation: Audit with grep

## ADR-007: Semantic Tokens with RGB Channel Variables
**Status**: Accepted  
**Date**: 2026-04-29  
**Deciders**: Builder, @council-quality

### Context
Raw hex values (#6366F1) and rgba() values make theming impossible. Need scalable token system.

### Decision
- Define colors as: `--color-500: #HEX; --color-500-rgb: R, G, B;`
- Use `rgba(var(--color-500-rgb), opacity)` for dynamic opacity
- NEVER use raw hex outside token definitions
- NEVER use raw rgba() without var(--*-rgb)

### Consequences
- **Positive**: Infinite scalability, dynamic opacity, WCAG compliance
- **Negative**: More verbose CSS variable declarations
- **Risk**: Developers forget -rgb suffix → Mitigation: Linting rules in Phase2-BLUEPRINT.md

---

## ADR-008: Replace Shared MEMORY.md with Per-Agent Working Memory

**Status**: Accepted  
**Date**: 2026-04-29  
**Deciders**: @council-architect, @council-performance, @council-security, @council-quality

### Context
Shared `MEMORY.md` file causes git merge conflicts (80% with 2+ agents) and Windows file locking (60% write failure with 3+ agents). 200-line limit causes context loss as project grows. System will halt completely at 5+ concurrent agents.

### Decision
- Move to per-agent working memory: `01_Agents/{agent}/working-memory.md`
- Create read-only global registry: `03_Knowledge_Base/active-registry.md`
- Implement file locking for any remaining shared resources
- Keep `MEMORY.md` as project-level overview only (not frequently updated)

### Consequences
- **Positive**: Eliminates git conflicts, no file contention, agents can store more context
- **Negative**: More files to manage, cross-agent memory discovery requires registry
- **Risk**: Registry becomes stale → Mitigation: Maintainer agent updates weekly

---

## ADR-009: Deploy RAG/MCP Vector Search for Knowledge Base

**Status**: Accepted  
**Date**: 2026-04-29  
**Deciders**: @council-architect, @council-performance

### Context
1000+ markdown files require sequential scanning (O(T) complexity). No semantic search capability. Agents must know exact filenames or grep through all files. Context window limits prevent loading all relevant files. Knowledge base will become unusable beyond 1000 files.

### Decision
- Deploy RAG (Retrieval-Augmented Generation) via MCP vector server (ChromaDB or Qdrant)
- Add YAML frontmatter with tags to all markdown files
- Create `03_Knowledge_Base/CATALOG.md` as temporary index
- Index all files in `03_Knowledge_Base/` for semantic search

### Consequences
- **Positive**: O(1) semantic search, reduces context window pressure, scales to 10000+ files
- **Negative**: Additional infrastructure (MCP server), learning curve for agents
- **Risk**: MCP server downtime → Mitigation: Fallback to grep search

---

## ADR-010: Sandbox Autonomous Agents + Add Audit Logging

**Status**: Accepted  
**Date**: 2026-04-29  
**Deciders**: @council-security, @council-performance

### Context
Autonomous agents (builder/researcher/maintainer) have `bash:allow` + `edit:allow` + `external_dir:allow` with no sandboxing. No audit logging of agent actions. Single prompt injection can compromise entire system. No branch protection allows pushing to main.

### Decision
- Change autonomous agents to `bash:ask` with command allowlisting
- Implement comprehensive audit logging to `06_Audit_Logs/audit-YYYY-MM-DD.md`
- Enforce branch protection (no direct commits to main)
- Add pre-commit secret scanning (trufflehog/gitleaks)
- Implement per-agent git branches: `agent/builder`, `agent/researcher`, etc.

### Consequences
- **Positive**: Prevents system compromise, enables compliance, traceability
- **Negative**: Slower agent execution (ask permission), more complex setup
- **Risk**: Agents bypass ask prompts → Mitigation: Regular permission audits

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
