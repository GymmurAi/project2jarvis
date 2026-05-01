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

## ADR-012: Create Plan Agent with PRINCE2 Integration

**Status**: Accepted  
**Date**: 2026-05-01  
**Deciders**: @researcher, @council-orchestrator, @council-architect, @council-quality

### Context
Project2Jarvis suffered cascading failures (Three.js dependency hell, Executive Command Center design rejection) because ideas went directly to Builder without planning. The Jeomon/Plan-Agent-with-Meta-Agent GitHub repo (14 stars) provided inspiration, but past failure prevention was missing.

### Decision
Create a **Plan Agent** (`.opencode/agents/plan-agent.md`) that serves as **MANDATORY first step** for ALL new ideas. Key features:

1. **6-Phase Process**: Analyze → Assess Risks → Create Plan → Delegate → Monitor → Verify
2. **PRINCE2 Integration** (P0 elements):
   - Principle 1: Continued Business Justification (Business Case in Phase 1)
   - Principle 2: Learn from Experience (read lessons-learned.md)
   - Principle 5: Manage by Exception (tolerances table, escalation)
3. **Failure Prevention Rules**:
   - No Direct Execution Rule (plan only, don't build)
   - Dependency Check Rule (mandatory `npm ls` before/after)
   - Design Validation Rule (mockup first, user approval)
   - One Change at a Time Rule (atomic steps)
4. **Files Created**:
   - `.opencode/agents/plan-agent.md` (agent definition)
   - `01_Agents/plan-agent/working-memory.md` (with dependency matrices)
   - `04_Active_Work/planning-template.md` (reusable template with PRINCE2 elements)
   - `03_Knowledge_Base/plan-agent-research.md` (research document)
   - `03_Knowledge_Base/prince2-integration-plan-agent.md` (PRINCE2 research)
5. **Project Updates**:
   - `AGENTS.md` - Added Plan Agent as MANDATORY first step
   - `03_Knowledge_Base/active-registry.md` - Updated (20 agents total)
   - `01_Agents/researcher/working-memory.md` - Added research to recent work

### Consequences
- **Positive**: Prevents dependency hell (Three.js crash), design rejections (Exec Command Center), provides universal planning for ALL project types
- **Negative**: Adds complexity (20th agent), requires P0 changes (registry access, state persistence, centralized matrices)
- **Risk**: Single point of failure → Mitigation: ADR-016 fallback mechanism

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
---

## ADR-013: Centralize Dependency Matrices in Active Registry
**Status**: Accepted  
**Date**: 2026-05-01  
**Deciders**: @council-orchestrator, @plan-agent

### Context
Dependency matrices (Three.js/R3F/drei versions) duplicated in 3+ files. Violates DRY principle. Updates require changing multiple files.

### Decision
- Centralize in `03_Knowledge_Base/active-registry.md` under "Verified Dependency Stacks"
- Remove from `plan-agent.md`, `working-memory.md`, `planning-template.md`
- Reference via wiki-link: `[[active-registry.md#Verified-Dependency-Stacks]]`

### Consequences
- **Positive**: Single source of truth, easier updates, DRY compliance
- **Negative**: Need to update references in multiple files
- **Risk**: Agents forget to check registry → Mitigation: Add to memory protocol

---

## ADR-014: Registry Update Policy - Plan Agent Edit Allow
**Status**: Accepted  
**Date**: 2026-05-01  
**Deciders**: @council-orchestrator, @plan-agent

### Context
`active-registry.md` needs updates when agents complete tasks. Currently only Maintainer can edit. Plan Agent needs ability to update registry after coordinating tasks.

### Decision
- Plan Agent: `edit: allow` for `active-registry.md` ONLY
- All other agents: `edit: deny` for registry (Maintainer only)
- Documented in `active-registry.md` under "Important Reminders"

### Consequences
- **Positive**: Plan Agent can track task completion, automated workflow
- **Negative**: Potential for registry corruption if Plan Agent fails
- **Risk**: Unauthorized edits → Mitigation: Audit logging (ADR-010)

---

## ADR-015: Add MCP/CLI/API Planning Templates
**Status**: Accepted  
**Date**: 2026-05-01  
**Deciders**: @council-orchestrator, @plan-agent

### Context
Current planning template only covers 3D/UI projects. Need templates for MCP servers, CLI tools, and API endpoints.

### Decision
- Add MCP Server template to `planning-template.md` (config, testing, documentation)
- Add CLI Tool template (Commander.js/yargs setup)
- Add API Endpoint template (REST/GraphQL, authentication)
- Implement project type detection (auto-select template)

### Consequences
- **Positive**: Comprehensive coverage, faster planning for diverse projects
- **Negative**: Larger template file, more complexity
- **Risk**: Template bloat → Mitigation: Modular templates (ADR-017)

---

## ADR-016: State Persistence + Fallback Mechanism
**Status**: Accepted  
**Date**: 2026-05-01  
**Deciders**: @council-orchestrator, @plan-agent

### Context
Plan Agent is single point of failure. No crash recovery. No fallback if agent becomes unresponsive. Risk of infinite recursion (spawning itself).

### Decision
- **State Persistence**: Save to `04_Active_Work/plan-{idea-name}/state.json` after each phase
- **Resume Capability**: Check for existing state at session start
- **Fallback Chain**: plan-agent → council-orchestrator → researcher
- **Health Check**: Escalate if no response in 5 minutes
- **Circular Guard**: NEVER spawn `/task plan-agent` (prevents recursion)
- **Concurrency Control**: Max 3 agents simultaneously, UUID-based plan IDs

### Consequences
- **Positive**: Crash recovery, no single point of failure, prevents recursion
- **Negative**: More complex implementation, state file management
- **Risk**: State file corruption → Mitigation: JSON schema validation

---

## ADR-017: Lite Plan Template for Simple Tasks
**Status**: Accepted  
**Date**: 2026-05-01  
**Deciders**: @council-orchestrator, @plan-agent

### Context
Current template is 310 lines - too verbose for simple tasks (bug fixes, small features). Need streamlined version.

### Decision
- Create "Lite Template" (50-75 lines) for simple tasks
- Include: Business Case, Risk Assessment, 3-Phase Plan, Success Criteria
- Keep full template for complex projects (3D, MCP, multi-agent)
- Auto-select based on task complexity assessment

### Consequences
- **Positive**: Faster planning for simple tasks, reduced context usage
- **Negative**: Two templates to maintain
- **Risk**: Wrong template selection → Mitigation: Plan Agent judgment

---

## ADR-018: Standardize Memory Protocol Order
**Status**: Accepted  
**Date**: 2026-05-01  
**Deciders**: @council-orchestrator, @plan-agent

### Context
Each agent reads memory files in different order. No standardization. Causes confusion and missed context.

### Decision
Standardize order across ALL agents:
1. `AGENTS.md` - Project rules and agent roster
2. `MEMORY.md` - Project overview
3. `decisions-log.md` - Recent ADRs
4. `lessons-learned.md` - Past insights
5. `04_Active_Work/` - Recent session logs
6. `ARCHITECTURE.md` - System architecture

### Consequences
- **Positive**: Consistent context, easier cross-agent coordination
- **Negative**: Need to update all agent definitions
- **Risk**: Agents forget new order → Mitigation: Add to agent templates
