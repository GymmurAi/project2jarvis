# Council Review: Plan Agent Creation by @researcher

**Date**: 2026-05-01  
**Reviewed By**: @council-orchestrator, @council-architect, @council-quality  
**Final Rating**: ⚠️ **APPROVE WITH CHANGES** (P0 changes required)

---

## Executive Summary

The council conducted a comprehensive review of @researcher's completed work on the Plan Agent creation. The work demonstrates **exceptional research depth**, **strong failure prevention design**, and **comprehensive documentation**. However, critical gaps exist in **project type coverage**, **architectural robustness**, and **maintainability** that must be addressed.

**Final Council Rating**: ⚠️ **APPROVE WITH CHANGES** (P0 changes required before full deployment)

---

## Council Member Summaries

| Council Member | Rating | Key Strengths | Critical Issues |
|---------------|--------|---------------|-----------------|
| **@researcher** (self-review) | APPROVE WITH CHANGES | Failure prevention rules, dependency matrices, 6-phase process | Limited project type coverage, no Agile/Scrum, missing MCP/CLI templates |
| **@council-architect** | APPROVE WITH CHANGES | 6-phase process, postmortem integration | Contradictory registry policy, no state persistence, no concurrency control, single point of failure |
| **@council-quality** | APPROVE WITH CHANGES | Research depth, documentation completeness | Dependency matrix duplicated 3x, memory protocol deviation, missing ADR, no examples/troubleshooting |

---

## What @researcher Excelled At (Above & Beyond)

1. **Deep Failure Analysis**: Git archaeology analyzing specific commits (`7ee69b7`, `84b1889`) with root cause extraction
2. **Postmortem Integration**: Embedded `ai-saas-landing-postmortem.md` directly into Plan Agent's memory protocol
3. **Dependency Matrices**: Complete compatibility matrices embedded in **3 locations** (plan-agent.md, working-memory.md, planning-template.md)
4. **Agent Coordination Map**: Created novel coordination matrix mapping task types to agents (not requested but high value)
5. **Six-Phase Process**: Complete planning methodology with verification steps
6. **Memory Triggers**: Proactive contextual decision-making rules (Lines 351-357 of plan-agent.md)

---

## What Was Missed**

#### 1. **Project Type Coverage Gaps** (Critical for "MANDATORY for ALL ideas")
- ❌ **No MCP Server template** - `agency-mcp-builder` exists but no planning guidance
- ❌ **No CLI Tool template** - Commander.js/yargs setup, argument parsing missing
- ❌ **No API planning** - REST vs GraphQL vs gRPC decision framework missing
- ❌ **No External Repo integration** - Fork workflow, upstream sync, license checks missing
- ❌ **No Digital Products framework** - User story mapping, MVP (MoSCoW), A/B testing

#### 2. **Architectural Risks** (Critical for 20+ agent ecosystem)
- ❌ **Contradictory registry policy**: `active-registry.md` says "Maintainer only", Plan Agent told to update it
- ❌ **No state persistence**: 6-phase process state lost if session crashes (Jeomon's LangGraph has state machine)
- ❌ **Single point of failure**: Plan Agent is mandatory gatekeeper with NO fallback
- ❌ **No concurrency control**: Multiple `/task plan-agent` invocations will conflict
- ❌ **Circular dependency risk**: Plan Agent can spawn another Plan Agent (no guard)

#### 3. **Maintainability Issues** (Critical for long-term sustainability)
- ❌ **Dependency matrix duplicated 3 times** - Violates DRY, error-prone updates
- ❌ **Memory protocol deviation** - plan-agent.md uses different order than MEMORY.md standard
- ❌ **Missing ADR** - No Architecture Decision Record for Plan Agent creation
- ❌ **Planning template too long** - 287 lines discourages usage for simple tasks

#### 4. **Missing Methodologies** (Should have for completeness)
- ❌ **No Agile/Scrum options** - Only Waterfall-like 6-phase process
- ❌ **No risk management frameworks** - Missing FAIR, OCTAVE, NIST
- ❌ **No quantitative risk assessment** - Only "high/medium/low" tables

---

## Council ADR-Style Recommendations**

### ADR-012: Create ADR for Plan Agent Implementation**
**Status**: Proposed  
**Date**: 2026-05-01  
**Deciders**: council-orchestrator, council-quality  

#### Context
The Plan Agent was created by @researcher but no Architecture Decision Record (ADR) was added to `decisions-log.md`. All major architectural changes should be documented via ADR per the template at decisions-log.md lines 93-111.

#### Decision
Create **ADR-012** documenting:
- Why a Plan Agent was needed (past failures: dependency hell, design rejection)
- Why the 6-phase planning process was chosen
- Why the agent has `edit:ask, bash:ask` permissions (not full access)
- Integration with postmortem knowledge
- Comparison to Jeomon/Plan-Agent-with-Meta-Agent

#### Consequences
- **Positive**: Proper architectural documentation, traceability, ADR log completeness
- **Negative**: None (documentation only)
- **Risk**: None

---

### ADR-013: Centralize Dependency Compatibility Matrices**
**Status**: Proposed  
**Date**: 2026-05-01  
**Deciders**: council-orchestrator, council-quality  

#### Context
The Three.js/R3F/drei compatibility matrix is duplicated across three files: `plan-agent.md`, `working-memory.md`, and `planning-template.md`. This violates DRY principles and creates a maintenance burden - when versions change, all three files must be updated.

#### Decision
Centralize all dependency compatibility matrices in `03_Knowledge_Base/active-registry.md` under a new "**Verified Dependency Stacks**" section. Reference this section from:
- `plan-agent.md` (remove embedded matrices, add reference)
- `working-memory.md` (remove embedded matrices, add reference)
- `planning-template.md` (remove embedded matrices, add reference)

#### Consequences
- **Positive**: Single source of truth, easier maintenance, reduced error risk
- **Negative**: Additional file to read during agent startup (minimal overhead)
- **Risk**: Registry becomes stale → Mitigation: Maintainer agent updates weekly per ADR-008**

---

### ADR-014: Reconcile Registry Access Policy**
**Status**: Proposed  
**Date**: 2026-05-01  
**Deciders**: council-orchestrator, council-architect  

#### Context
There is a direct contradiction in registry access:
- `active-registry.md` line 3: "**DO NOT EDIT this file (Maintainer only)**"
- `plan-agent.md` Session End step 5: "Update `03_Knowledge_Base/active-registry.md` if plan status changed"
- Plan Agent has `edit: ask` permission, meaning every registry update requires user approval

This will cause stale registry data or user fatigue from constant approval prompts.

#### Decision
**Option A (Recommended)**: Change `active-registry.md` policy:
- Allow Plan Agent to update registry (`edit: allow` for registry file only)
- Keep "Maintainer only" for other agents
- Document in ARCHITECTURE.md that Plan Agent has registry write privilege

**Option B**: Remove registry update from Plan Agent duties:
- Plan Agent creates plan in `04_Active_Work/plan-{name}.md`
- Maintainer agent periodically syncs plans to registry (weekly cron)

#### Consequences
- **Positive**: Resolves contradiction, enables autonomous coordination
- **Negative**: Option A requires permission refinement; Option B adds latency
- **Risk**: Registry corruption from bad Plan Agent updates → Mitigation: Git versioning + daily backups**

---

### ADR-015: Add Project Type Detection and Missing Templates**
**Status**: Proposed  
**Date**: 2026-05-01  
**Deciders**: council-orchestrator, researcher  

#### Context
The current Plan Agent has excellent support for 3D/UI projects but lacks templates for MCP servers, CLI tools, APIs, and other types. This limits usefulness as "MANDATORY first step for ALL ideas" (AGENTS.md line 24).

#### Decision
1. **Add Project Type Detection**: Analyze idea → auto-detect project type → load appropriate template
2. **Create MCP Server Template**: Tool/resource/prompt definitions, MCP inspector testing, `agency-mcp-builder` coordination
3. **Create CLI Tool Template**: Commander.js/yargs setup, argument parsing, exit codes, `builder` coordination
4. **Create API Planning Template**: REST vs GraphQL vs gRPC decision framework, authentication planning (API keys, OAuth, JWT)
5. **Add External Repo Integration Protocol**: License Check → Fork Strategy → Upstream Sync → Attribution → Integration Pattern
6. **Update Agent Coordination Map**: Add missing task types (security updates, performance optimization, docs updates, bug fixes, refactoring)

#### Consequences
- **Positive**: Truly universal Plan Agent, consistent planning across all project types
- **Negative**: Increases complexity, more templates to maintain
- **Risk**: Incorrect detection → wrong template → Mitigation: Add manual override option in Phase 1**

---

### ADR-016: Add State Persistence and Fallback Mechanism**
**Status**: Proposed  
**Date**: 2026-05-01  
**Deciders**: council-orchestrator, council-architect  

#### Context
The Plan Agent's 6-phase process has no formal state machine. State exists only in the agent's ephemeral context window. If the session crashes mid-plan, all state is lost. Additionally, Plan Agent is mandatory gatekeeper with **NO fallback** - if it fails, nothing executes.

#### Decision
1. **State Persistence**: Create `04_Active_Work/plan-{idea-name}/state.json` with current phase, delegated agents, and verification status. Add "Resume Plan" capability.
2. **Fallback Chain**: Implement `plan-agent` → `council-orchestrator` → `researcher` (in order of preference). Add health check: If Plan Agent hasn't responded in 5 minutes, escalate to fallback.
3. **Circular Guard**: Add to Plan Agent: "NEVER spawn `plan-agent` (prevents recursion). NEVER spawn more than 3 agents simultaneously."

#### Consequences
- **Positive**: Survives crashes, no single point of failure, prevents infinite recursion
- **Negative**: Additional files to manage (`state.json`), slightly more complex
- **Risk**: JSON schema versioning → Mitigation: Include `schema_version` field**

---

### ADR-017: Create Two-Tier Planning Templates**
**Status**: Proposed  
**Date**: 2026-05-01  
**Deciders**: council-orchestrator, council-quality  

#### Context
The current `planning-template.md` is 287 lines long - comprehensive but overwhelming for simple tasks. Not all ideas need a 6-phase plan with detailed risk assessment, timeline estimates, and rollback plans.

#### Decision
Create two planning templates:
1. **Lite Plan Template** (50-75 lines): For simple tasks (bug fixes, small features, docs updates)
   - Idea summary
   - Risk checklist (3-5 items)
   - 3-phase execution: Research → Implement → Verify
   - Success criteria (3-5 items)

2. **Full Plan Template** (current 287-line version): For complex tasks (3D projects, architecture changes, new agents)
   - Keep existing comprehensive template

Plan Agent should choose template based on task complexity (simple vs. complex) during Phase 1.

#### Consequences
- **Positive**: Encourages plan usage for all tasks, not just complex ones
- **Negative**: Two templates to maintain
- **Risk**: Agents may use Lite for complex tasks → Mitigation: Plan Agent validates template choice in Phase 1**

---

### ADR-018: Standardize Memory Protocol Across All Agents**
**Status**: Proposed  
**Date**: 2026-05-01  
**Deciders**: council-orchestrator, council-quality  

#### Context
`MEMORY.md` line 44 specifies: "Start session: Read AGENTS.md → MEMORY.md → decisions-log.md". However, `plan-agent.md` lines 22-34 uses a different order: working-memory.md → active-registry.md → AGENTS.md → decisions-log.md → lessons-learned.md → agent-memory-solutions.md → 04_Active_Work/ → ARCHITECTURE.md → postmortem.

#### Decision
Standardize memory protocol order for ALL agents:
1. `AGENTS.md` (project rules)
2. `MEMORY.md` (project overview)
3. `01_Agents/{agent}/working-memory.md` (per-agent memory)
4. `03_Knowledge_Base/active-registry.md` (cross-agent registry)
5. `03_Knowledge_Base/decisions-log.md` (ADRs)
6. `03_Knowledge_Base/lessons-learned.md` (insights)
7. `04_Active_Work/` (recent sessions)
8. `00_Meta/ARCHITECTURE.md` (system architecture)
9. Domain-specific files (e.g., postmortem for 3D projects - keep in agent's working-memory.md as "Important Notes")

#### Consequences
- **Positive**: Consistency across agents, predictable startup sequence
- **Negative**: Plan Agent loses its specialized "read postmortem first" advantage
- **Risk**: Agents may skip domain-specific files → Mitigation: Keep domain-specific files in agent's working-memory.md as "Important Notes"**

---

## Final Council Verdict**

### Rating: ⚠️ **APPROVE WITH CHANGES**

### Justification:

**Why APPROVE** ✅:
1. Addresses root causes of past failures (Three.js hell, design rejection)
2. Exceptional research depth (GitHub analysis + git history)
3. Complete documentation (4 new files, 3 modified)
4. Innovative features (memory triggers, coordination map, dependency matrices)
5. 6-phase process is well-designed for complex projects

**Why WITH CHANGES** ❌:
1. **P0 Issues**: Contradictory registry policy, no state persistence, no fallback mechanism
2. **P0 Issues**: Dependency matrix duplicated 3x, missing ADR, memory protocol deviation
3. **P1 Issues**: No MCP/CLI/API templates, no project type detection, planning template too long
4. **P1 Issues**: No concurrency control, circular spawning risk, incomplete coordination map**

---

## Required Changes Before Full Deployment**

### P0 (Must Fix - Blocking Merge to Main)

1. **Fix registry access contradiction** (ADR-014)
   - Either give Plan Agent registry write access OR remove registry update duty
   - Update `active-registry.md` policy or `plan-agent.md` instructions

2. **Centralize dependency matrix** (ADR-013)
   - Create "Verified Dependency Stacks" section in `active-registry.md`
   - Remove duplicates from plan-agent.md, working-memory.md, planning-template.md

3. **Create ADR-012** (ADR-012)
   - Document Plan Agent creation in `decisions-log.md`
   - Follow template at decisions-log.md lines 93-111

4. **Fix memory protocol order** (ADR-018)
   - Update plan-agent.md lines 22-34 to match MEMORY.md line 44
   - Standardize across all agents

5. **Add state persistence** (ADR-016)
   - Create `state.json` for 6-phase process resilience
   - Add "Resume Plan" capability

6. **Add fallback mechanism** (ADR-016)
   - Plan Agent must not be a single point of failure
   - Implement fallback chain: plan-agent → council-orchestrator → researcher**

### P1 (Should Fix - Before Full "MANDATORY" Enforcement)**

7. **Add MCP Server planning template** (ADR-015)
8. **Add CLI Tool planning template** (ADR-015)
9. **Add project type detection** (ADR-015)
10. **Create Lite Plan Template** (ADR-017) - 50-75 lines for simple tasks
11. **Add concurrency control** (ADR-016) - UUID-based plan IDs, lock files
12. **Add circular spawning guard** (ADR-016) - Prevent plan-agent → plan-agent recursion
13. **Expand Agent Coordination Map** (ADR-015) - Add missing task types**

### P2 (Nice to Have - Future Iterations)**

14. **Add Agile/Scrum methodology option** (researcher review)
15. **Add quantitative risk assessment** (council-architect)
16. **Add completed plan examples** (council-quality)
17. **Add troubleshooting section** (council-quality)
18. **Implement Obsidian wiki-links** (council-quality)**

---

## Council Vote**

| Council Member | Vote | Confidence |
|---------------|------|------------|
| @researcher (self-review) | APPROVE WITH CHANGES | High |
| @council-architect | APPROVE WITH CHANGES | High |
| @council-quality | APPROVE WITH CHANGES | High |
| **@council-orchestrator (final)** | **APPROVE WITH CHANGES** | **High** |

---

**Final Recommendation to @researcher**:  
The Plan Agent concept is **excellent and desperately needed**. These changes are about **polishing for maintainability, completeness, and architectural robustness** - not rejecting the core idea. Address P0 issues immediately, then P1 issues before full deployment. Well done on the research and design! 🎉

---

*Council Verdict delivered by @council-orchestrator on 2026-05-01*  
*Next step: @researcher to implement P0 changes, then notify council for re-review*
