# Plan Agent Working Memory

*Last updated: 2026-05-01 by @researcher (Plan Agent creation)*

## Current Task Context
- **Status**: Available
- **Current Task**: None (just created)
- **Active Branch**: agent/plan-agent

## Plan Agent-Specific Patterns Learned
- **MANDATORY FIRST STEP**: All new ideas/features/changes MUST start with Plan Agent
- **Read postmortem**: Always read `03_Knowledge_Base/ai-saas-landing-postmortem.md` before 3D projects
- **Dependency checks**: Always run `npm ls` before and after package changes
- **Design first**: Never let builders create UIs without design mockups approved by user
- **One change at a time**: Follow the "One Change at a Time" rule from postmortem
- **Agent coordination**: Check `active-registry.md` before spawning agents

## Planning Workflow (6 Phases)
1. **Idea Analysis** - Understand request, check project state
2. **Risk Assessment** - Dependency/architecture/design risks
3. **Plan Creation** - Create detailed plan in `04_Active_Work/plan-{idea-name}.md`
4. **Delegation** - Spawn agents via Task tool
5. **Monitoring** - Track progress via session logs
6. **Verification** - Test builds and functionality

## Critical Rules (Learned from Past Failures)

### The "No Direct Execution" Rule
- NEVER implement directly - always plan first, then delegate
- Past failure: Builder agent installed incompatible Three.js → cascading failures

### The "Dependency Check" Rule
- ALWAYS check `npm ls` before suggesting package installs
- ALWAYS verify compatibility matrices (Three.js ↔ R3F ↔ drei)
- Past failure: 3D-Website-Architect used latest packages without checking

### The "Design Validation" Rule
- ALWAYS create design mockups/prototypes before building
- ALWAYS get user approval on design direction
- Past failure: Executive Command Center built, then rejected as "awful design"

### The "One Change at a Time" Rule
- ALWAYS break work into atomic, testable steps
- ALWAYS verify each step before proceeding
- Past failure: Multiple fixes applied simultaneously → couldn't identify root cause

## Dependency Compatibility Matrices (CRITICAL)
 
**Reference ONLY**: `[[03_Knowledge_Base/active-registry.md#Verified-Dependency-Stacks]]` (ADR-013)
 
- Check command: `npm ls three @react-three/fiber @react-three/drei framer-motion`
- **NEVER duplicate matrices** - centralized in active-registry.md (ADR-013)

## Agent Coordination Map

| Task Type | Research Agent | Build Agent | Design Agent | Review Agent |
|-----------|----------------|-------------|--------------|-------------|
| 3D Project | researcher | builder | 3d-website-architect | council-orchestrator |
| UI Project | researcher | builder | ui-ux-pro-max | council-orchestrator |
| MCP Integration | researcher | builder | - | agency-mcp-builder |
| Security Feature | researcher | builder | - | council-security |
| Performance Opt | researcher | builder | - | council-performance |
| Docs Update | researcher | builder | - | council-docs |

## Recent Work
- Created Plan Agent definition (`.opencode/agents/plan-agent.md`)
- Analyzed past failures from `ai-saas-landing-postmortem.md`
- Studied GitHub repo: Jeomon/Plan-Agent-with-Meta-Agent
- Researched Claude Code vs Project2Jarvis architecture

## Things to Remember
- All API keys in Windows Credential Manager (never in repo)
- Create feature branches, never commit directly to main (ADR-010)
- Log all actions to `06_Audit_Logs/audit-YYYY-MM-DD.md`
- **ALWAYS read postmortem before 3D projects**
- **ALWAYS spawn researcher first for dependency checks**
- **ALWAYS get user approval on designs before builder starts**
- Plans go to `04_Active_Work/plan-{idea-name}.md`

## Quick Reference
- **Start**: Read AGENTS.md → MEMORY.md → decisions-log.md → this file → **postmortem**
- **Process**: Analyze → Assess Risks → Create Plan → Delegate → Monitor → Verify
- **End**: Update this file, create session log, add research to 03_Knowledge_Base/
- **Branch**: Always use `agent/plan-agent` branch, merge to main after council review
- **Key Files**: 
  - `03_Knowledge_Base/ai-saas-landing-postmortem.md` (MUST READ for 3D)
  - `03_Knowledge_Base/claude-code-vs-project2jarvis-agent-architecture.md`
  - `04_Active_Work/plan-{idea-name}.md` (where plans live)

## Planning Checklist Template
For every new idea, verify:
- [ ] Read `ai-saas-landing-postmortem.md` (if 3D project)
- [ ] Checked `npm ls` for dependency conflicts
- [ ] Verified version compatibility matrix
- [ ] Created design mockup (if UI project)
- [ ] Got user approval on design
- [ ] Created plan in `04_Active_Work/plan-{name}.md`
- [ ] Checked `active-registry.md` for agent availability
- [ ] Broke work into atomic steps
- [ ] Defined verification criteria for each step
