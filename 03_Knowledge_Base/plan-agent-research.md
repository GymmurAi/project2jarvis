# Research: Plan Agent - Meta-Agent Planning System

## Executive Summary

Based on analysis of the GitHub repository [Jeomon/Plan-Agent-with-Meta-Agent](https://github.com/Jeomon/Plan-Agent-with-Meta-Agent) and deep analysis of Project2Jarvis' past system-breaking failures, I have designed and built a **Plan Agent** that serves as the mandatory first step for ALL new ideas in our project.

**Key Finding**: Our project suffered cascading failures (Three.js dependency hell, Executive Command Center design rejection) because we lacked a planning gatekeeper. The Plan Agent prevents these issues by analyzing, planning, and coordinating BEFORE any execution happens.

**Innovation**: Unlike the GitHub repo's simple planner-meta structure, our Plan Agent is deeply integrated with:
1. **Past failure knowledge** - Reads `ai-saas-landing-postmortem.md` before 3D projects
2. **Dependency matrices** - Embeds verified compatibility tables
3. **Agent coordination** - Uses `active-registry.md` to avoid conflicts
4. **Design validation** - Mandates mockups before building (prevents another Exec Command Center failure)

## Research Questions

1. How does the Plan-Agent-with-Meta-Agent GitHub repo structure its planning?
2. What caused our past system-breaking failures?
3. How can we design a Plan Agent to prevent these failures?
4. What capabilities should the Plan Agent have?
5. How does this compare to Claude Code's approach?

## Findings

### Source 1: Jeomon/Plan-Agent-with-Meta-Agent
- **URL**: https://github.com/Jeomon/Plan-Agent-with-Meta-Agent
- **Stars**: 14 (as of 2026-05-01)
- **Architecture**:
  - **Planner Agent**: Breaks down problem into structured plan
  - **Meta Agent**: Executes tasks sequentially, updates plan
  - **Supporting Agents**: ReAct (tools), CoT (reasoning), Tool Agent (dynamic tool management)
- **Key Features**:
  - Structured planning with sequential task execution
  - Dynamic tool creation/update/deletion
  - Iterative reasoning without tools (CoT)
  - LangGraph-based (Python)
- **Dependencies**: langgraph, colorama, termcolor, requests
- **Relevance**: High - Base inspiration for our Plan Agent

### Source 2: Our Past Failures (Git History Analysis)
- **Commit 7ee69b7**: "fix(ai-saas-landing): resolve dependency stack + upgrade to Heroicons"
  - **Root Cause**: Three.js 0.184.0 incompatible with R3F 8.15.0
  - **Failure Mode**: Builder installed latest packages without checking compatibility
  - **Fix Loop**: Multiple agents tried fixing, made it worse
  - **Resolution**: Systematic dependency alignment (see postmortem)

- **Commit 84b1889**: "docs: Log critical design failure - Executive Command Center rejected"
  - **Root Cause**: Built dark theme dashboard without design approval
  - **User Feedback**: "design is beyond help, awful, never create this type of nonsense"
  - **Failure Mode**: No design validation before building
  - **Result**: Entire project cancelled

### Source 3: Postmortem Analysis (`ai-saas-landing-postmortem.md`)
- **Critical Lessons**:
  1. **Dependency Hell is Real**: Three.js ecosystem requires precise version matching
  2. **Latest ≠ Best**: Latest packages break older ecosystem tools
  3. **Root Cause First**: Don't treat symptoms; analyze dependency tree
  4. **Test After Each Fix**: Prevents fix loops
  5. **Design Validation**: Create mockups, get approval BEFORE building

- **Verified Compatibility Matrix**:
  ```
  Stack A (Recommended - Stable):
  - three: ^0.170.0
  - @react-three/fiber: ^8.17.0
  - @react-three/drei: ^9.117.0
  - framer-motion: ^11.15.0
  - react: ^18.3.1
  ```

### Source 4: Claude Code Architecture Research
- **From previous research** (`claude-code-vs-project2jarvis-agent-architecture.md`)
- Claude Code uses hierarchical parent-child model (no peer-to-peer... yet)
- Our Plan Agent implements similar hierarchical planning
- Key difference: Our Plan Agent is MANDATORY gatekeeper (not optional)

## Analysis

### Comparison: GitHub Repo vs. Our Plan Agent

| Feature | Jeomon/Plan-Agent | Our Plan Agent |
|---------|-------------------|----------------|
| **Planning** | Planner Agent creates plan | Plan Agent analyzes + creates plan |
| **Execution** | Meta Agent executes | Delegates to existing agents (builder, researcher, etc.) |
| **Tool Management** | Dynamic tool creation | Uses existing agent tools |
| **Failure Prevention** | None documented | Deep integration with postmortem knowledge |
| **Dependency Checks** | No | MANDATORY `npm ls` checks |
| **Design Validation** | No | Mandatory mockups + user approval |
| **Agent Coordination** | Creates new agents | Coordinates existing 20 agents |
| **Memory** | No persistent memory | 3-layer memory (working, permanent, registry) |
| **Language** | Python (LangGraph) | Markdown agent definition (OpenCode) |

### Root Causes of Our Past Failures

#### Failure 1: Dependency Hell (ai-saas-landing)
```
Builder Agent installed:
- three: ^0.184.0 (2026-era, breaking changes)
- @react-three/fiber: ^8.15.0 (2024-era, expects ~0.16x)
→ RUNTIME CRASH: "Cannot read properties of undefined (ReactCurrentOwner)"
```

**Why Plan Agent Prevents This**:
1. Reads `ai-saas-landing-postmortem.md` FIRST
2. Checks compatibility matrix BEFORE any install
3. Runs `npm ls` to verify dependency tree
4. Only THEN delegates to builder with verified versions

#### Failure 2: Design Rejection (Executive Command Center)
```
Builder Agent built:
- Next.js dashboard with dark theme
- Drill-down KPI charts (mechanics worked)
→ USER REJECTION: "design is beyond help, awful"
→ RESULT: Project cancelled, never deployed
```

**Why Plan Agent Prevents This**:
1. MANDATES design mockup BEFORE building
2. Requires user approval on design
3. Only THEN delegates to builder for implementation
4. No more building-then-rejecting

### Plan Agent Capabilities (Designed & Built)

#### 1. Mandatory Gatekeeper
- ALL new ideas MUST start with Plan Agent
- No direct execution by other agents
- Enforced by project workflow (not just suggestion)

#### 2. Six-Phase Planning Process
1. **Idea Analysis** - Understand request, check project state
2. **Risk Assessment** - Dependency/architecture/design risks
3. **Plan Creation** - Detailed plan in `04_Active_Work/plan-{name}.md`
4. **Delegation** - Spawn appropriate agents via Task tool
5. **Monitoring** - Track progress, intervene if off-track
6. **Verification** - Test builds and functionality

#### 3. Failure Prevention Rules
- **No Direct Execution Rule** - Never implement, only plan + coordinate
- **Dependency Check Rule** - Always `npm ls` before/after package changes
- **Design Validation Rule** - Mockup first, get approval, then build
- **One Change at a Time Rule** - Atomic steps, verify each
- **Agent Coordination Rule** - Check registry, avoid conflicts

#### 4. Integration with Existing Agents
- **researcher** - For dependency research, compatibility checks
- **3d-website-architect** - For 3D design mockups
- **ui-ux-pro-max** - For UI design validation
- **builder** - For implementation (ONLY after plan + design approval)
- **council-orchestrator** - For code review
- **agency-evidence-collector** - For Playwright testing

## Implementation

### Files Created

1. **Agent Definition**: `.opencode/agents/plan-agent.md`
   - Full system prompt with 6-phase process
   - Embedded dependency matrices
   - Failure prevention rules
   - Planning templates for different project types

2. **Working Memory**: `01_Agents/plan-agent/working-memory.md`
   - Quick reference for Plan Agent
   - Dependency compatibility matrices
   - Agent coordination map
   - Planning checklist template

3. **Planning Template**: `04_Active_Work/planning-template.md`
   - Reusable template for all new ideas
   - Risk assessment sections
   - 6-phase structure
   - Rollback plan section

4. **This Research Document**: `03_Knowledge_Base/plan-agent-research.md`

### Key Features Implemented

#### Feature 1: Postmortem Integration
```markdown
## Memory Protocol
### Session Start (always do first)
...
9. **Read `03_Knowledge_Base/ai-saas-landing-postmortem.md`** - CRITICAL: Past failure analysis
```

#### Feature 2: Dependency Matrix Embedding
```markdown
### Template 2: Dependency-Sensitive Project (3D/React)
| Package | Version | Reason |
|---------|---------|--------|
| three | ^0.170.0 | Stable, R3F-compatible |
| @react-three/fiber | ^8.17.0 | Compatible with Three.js 0.170 |
...
**Check command**: `npm ls three @react-three/fiber @react-three/drei framer-motion`
```

#### Feature 3: Design Validation Mandate
```markdown
### The "Design Validation" Rule
- **ALWAYS** create design mockups/prototypes before building
- **ALWAYS** get user approval on design direction
- Past failure: Executive Command Center was built, then rejected as "awful design"
```

#### Feature 4: Agent Coordination
```markdown
## Agent Coordination Map
| Task Type | Research Agent | Build Agent | Design Agent | Review Agent |
|-----------|----------------|-------------|--------------|-------------|
| 3D Project | researcher | builder | 3d-website-architect | council-orchestrator |
| UI Project | researcher | builder | ui-ux-pro-max | council-orchestrator |
...
```

## Recommendations

### Short Term (Immediate)
1. **MANDATORY USAGE**: Enforce that all new ideas start with `/task plan-agent`
2. **Update AGENTS.md**: Add Plan Agent to the agent roster
3. **Test with 3D Project**: Spawn Plan Agent for next 3D idea, verify it prevents dependency hell

### Medium Term
1. **Workflow Integration**: Create formal workflow in `02_Workflows/planning-workflow.md`
2. **Council Review**: Have council-orchestrator review Plan Agent effectiveness
3. **Metrics Tracking**: Track how many failures Plan Agent prevents

### Long Term
1. **Auto-Learning**: Plan Agent reads new postmortems automatically
2. **Predictive Risks**: ML model to predict risks based on past failures
3. **Integration with Claude Code**: If we adopt Agent Teams, Plan Agent becomes the "lead"

## Comparison to Alternatives

### Why Not Just Use GitHub Repo Directly?
1. **Python vs Markdown** - Repo is Python/LangGraph, we use OpenCode markdown agents
2. **No Failure Knowledge** - Repo doesn't know about our past failures
3. **No Agent Ecosystem** - Repo creates new agents, we coordinate existing 20 agents
4. **No Design Validation** - Repo doesn't prevent design rejections

### Why Not Just Use Builder Directly?
1. **Builder Caused Failures** - Builder installed incompatible Three.js
2. **No Planning Step** - Builder executes immediately
3. **No Dependency Checks** - Builder doesn't run `npm ls`
4. **No Design Approval** - Builder builds first, asks later

## Success Metrics

How to measure Plan Agent effectiveness:
- [ ] **Zero dependency hell incidents** (like Three.js crash)
- [ ] **Zero design rejections** (like Exec Command Center)
- [ ] **100% plans created** before execution
- [ ] **Atomic steps** with verification after each
- [ ] **Proper rollback plans** documented

## Open Questions

1. Should Plan Agent have `edit:allow` to fix issues directly, or keep `edit:ask`?
2. How to enforce MANDATORY usage (technical enforcement vs. workflow convention)?
3. Should Plan Agent spawn sub-agents, or just coordinate existing agents?
4. How to handle urgent bug fixes (should they bypass Plan Agent)?

## Sources

1. [Plan-Agent-with-Meta-Agent GitHub](https://github.com/Jeomon/Plan-Agent-with-Meta-Agent) - Jeomon, 2024-09-29
2. [ai-saas-landing-postmortem.md](file:///D:/Projects/Project2Jarvis/03_Knowledge_Base/ai-saas-landing-postmortem.md) - Project2Jarvis, 2026-04-30
3. [Claude Code vs Project2Jarvis Architecture](file:///D:/Projects/Project2Jarvis/03_Knowledge_Base/claude-code-vs-project2jarvis-agent-architecture.md) - @researcher, 2026-05-01
4. [Git History Analysis](git show 7ee69b7, 84b1889) - Project2Jarvis commits
5. [Active Registry](file:///D:/Projects/Project2Jarvis/03_Knowledge_Base/active-registry.md) - Cross-agent reference

## Metadata

- **Date**: 2026-05-01
- **Researcher**: @researcher (building Plan Agent)
- **Confidence**: High
- **Tags**: `#plan-agent` `#meta-agent` `#planning` `#failure-prevention` `#dependency-management`
- **Related Research**: 
  - `03_Knowledge_Base/agent-memory-solutions.md`
  - `03_Knowledge_Base/claude-code-vs-project2jarvis-agent-architecture.md`
  - `03_Knowledge_Base/ai-saas-landing-postmortem.md`

## Change Log

| Date | Change |
|------|--------|
| 2026-05-01 | Initial research and Plan Agent creation |
| 2026-05-01 | Analyzed GitHub repo: Jeomon/Plan-Agent-with-Meta-Agent |
| 2026-05-01 | Deep analysis of past failures (dependency hell, design rejection) |
| 2026-05-01 | Designed 6-phase planning process |
| 2026-05-01 | Built Plan Agent with failure prevention rules |
| 2026-05-01 | Created working memory, planning template, knowledge base doc |
| 2026-05-01 | Updated active-registry.md (20 agents total now) |
