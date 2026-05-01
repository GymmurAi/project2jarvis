# Active Registry

*Global registry for cross-agent reference*

**Last updated**: 2026-05-01 by @researcher (Plan Agent creation)  
**Maintainer**: Update weekly or after major changes

---

## Verified Dependency Stacks (ADR-013)
*Centralized compatibility matrices - DO NOT DUPLICATE elsewhere*

### Stack A: 3D React Projects (Recommended - Stable)
```json
{
  "three": "^0.170.0",
  "@react-three/fiber": "^8.17.0",
  "@react-three/drei": "^9.117.0",
  "framer-motion": "^11.15.0",
  "react": "^18.3.1",
  "next": "^14.2.35"
}
```
**Check command**: `npm ls three @react-three/fiber @react-three/drei framer-motion`
**Source**: `03_Knowledge_Base/ai-saas-landing-postmortem.md`

### Stack B: 3D React Projects (Legacy - If you must)
```json
{
  "three": "^0.160.0",
  "@react-three/fiber": "^8.15.0",
  "@react-three/drei": "^9.92.0",
  "framer-motion": "^10.16.0",
  "react": "^18.2.0",
  "next": "^14.0.0"
}
```

---

## Active Tasks
*Currently in-progress tasks across all agents*

| Task | Agent | Status | Branch | Priority |
|------|-------|--------|--------|----------|
| Phase 0 Critical Fixes | council-orchestrator | IN PROGRESS | master | P0 |
| Executive Command Center | builder | COMPLETED | agent/builder | - |

---

## Recent Decisions (Last 7 Days)
*Quick reference for agents - full details in decisions-log.md*

| Date | ADR | Decision |
|------|-----|-----------|
| 2026-05-01 | ADR-012 | Create Plan Agent with PRINCE2 Integration |
| 2026-04-29 | ADR-008 | Replace shared MEMORY.md with per-agent memory |
| 2026-04-29 | ADR-009 | Deploy RAG/MCP vector search for Knowledge Base |
| 2026-04-29 | ADR-010 | Sandbox autonomous agents + add audit logging |
| 2026-04-29 | ADR-007 | Semantic tokens with RGB channel variables |
| 2026-04-29 | ADR-006 | Heroicons v2.0 mandatory for all icons |
| 2026-04-29 | ADR-005 | Executive Command Center high-grade color scheme |

---

## Agent Status
*Current state of all agents*

| Agent | Status | Last Active | Current Task | Branch |
|-------|--------|-------------|-------------|--------|
| plan-agent | Available | 2026-05-01 | None (just created) | agent/plan-agent |
| builder | Available | 2026-04-30 | None (agency-agents implemented) | agent/builder (new) |
| researcher | Available | 2026-04-30 | None (agency-agents eval complete) | agent/researcher |
| maintainer | Available | 2026-04-28 | None | agent/maintainer (new) |
| council-orchestrator | Active | 2026-04-29 | Phase 0 fixes | master |
| council-architect | Available | - | - | - |
| council-security | Available | - | - | - |
| council-performance | Available | - | - | - |
| council-quality | Available | - | - | - |
| council-docs | Available | - | - | - |
| ui-ux-pro-max | Available | 2026-04-29 | - | - |
| personal-development-coach | Available | - | - | - |
| **3d-website-architect** | Available | 2026-04-30 | None | - |
| **agency-code-reviewer** | Available | 2026-04-30 | None | - |
| **agency-mcp-builder** | Available | 2026-04-30 | None | - |
| **agency-security-engineer** | Available | 2026-04-30 | None | - |
| **agency-evidence-collector** | Available | 2026-04-30 | None | - |
| **agency-workflow-architect** | Available | 2026-04-30 | None | - |

---

## Quick Stats
- **Total Agents**: 20 (3 autonomous + 1 plan + 6 council + 2 specialized + 5 agency + 1 skill-based + 2 others)
- **Autonomous Agents**: 4 (plan-agent, builder, researcher, maintainer)
- **Council Agents**: 6 (orchestrator, system-architect, architect, security, performance, quality, docs)
- **Specialized Agents**: 2 (ui-ux-pro-max, personal-development-coach)
- **Agency Agents**: 5 (code-reviewer, mcp-builder, security-engineer, evidence-collector, workflow-architect)
- **Skill-Based Agents**: 1 (3d-website-architect)
- **Other Agents**: 2 (prompt-expert, council-system-architect)
- **Knowledge Base Files**: 5+ (including new Claude Code comparison)
- **Active Tasks**: 0
- **Vault Size**: <100 files (healthy)

---

## Important Reminders for All Agents
- **Read this file** at session start for cross-agent context
- **Plan Agent**: `edit: allow` for registry updates ONLY (ADR-014)
- **Other Agents**: `edit: deny` - DO NOT EDIT (Maintainer only)
- **Your working memory** is in `01_Agents/{agent}/working-memory.md`
- **Branch policy**: Autonomous agents use `agent/{name}` branches
- **Audit logs**: Log all actions to `06_Audit_Logs/audit-YYYY-MM-DD.md`
- **No direct commits** to master (enforced by branch protection)

---

**Note**: This file replaces the shared context that was in MEMORY.md. MEMORY.md now contains project-level overview only.
