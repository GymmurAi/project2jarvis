# Working Memory
*Last updated: 2026-04-29 by Council-Orchestrator (Architecture Scalability Review)*

## Project Context
- **Project**: Project2Jarvis (OpenCode + Obsidian multi-agent AI agency)
- **Tech stack**: OpenCode AI agents, Obsidian vault, Git versioning, MCP servers
- **Architecture**: 3-layer memory (Session/Working/Permanent) + Council system

## Key Decisions Made
- [2026-04-28] Adopted 3-layer memory architecture (ADR-001)
- [2026-04-28] Using markdown files for memory (ADR-004)
- [2026-04-28] Council agents read-only, Autonomous full access (ADR-003)
- [2026-04-28] All state in markdown + Git (ADR-002)
- [2026-04-29] Executive Command Center: High-grade Navy/Teal/Gold palette (ADR-005)
- [2026-04-29] All icons = Heroicons v2.0 only (1.5px stroke) (ADR-006)
- [2026-04-29] External CSS with semantic tokens only (no raw hex) (ADR-007)
- [2026-04-29] CRITICAL: Shared MEMORY.md must be replaced with per-agent memory (Phase 0)
- [2026-04-29] CRITICAL: RAG/MCP vector search needed before 1000 KB files (Phase 1)
- [2026-04-29] CRITICAL: Autonomous agents need sandboxing + audit logs (Phase 0)

## AI/UI Resources (Bible)
- **Heroicons v2.0**: https://heroicons.com/ - 316 icons, 24x24, 1.5px stroke (NOT 2px)
- **SAP Fiori Design System**: https://experience.sap.com/fiori-design-web/ - Enterprise-grade, WCAG AAA
- **Bloomberg Terminal Colors**: Navy (#1E293B) + Amber (#FFA028) - Financial industry standard
- **AdminLTE**: https://adminlte.io/ - Card-based layouts, clean borders
- **Material UI**: https://mui.com/ - Design system reference

## Session 2026-04-29 (02:00 - 04:00, ~2h)
### Executive Command Center Revamp (COMPLETED)
- Extracted 299 lines of inline CSS to external `styles.css`
- Replaced ALL emoji icons (12 KPI + 4 action cards) with Heroicons v2.0 (stroke-width="1.5")
- Fixed CSS syntax errors: `prefers-reduced-motion` selector, `scroll-behavior` typo
- Fixed touch targets: Theme toggle 44x44px, Skip link min-height: 44px (WCAG 2.1 AA)
- Replaced 17 raw `rgba()` values with semantic token RGB variables (`var(--gold-500-rgb)`)
- **Upgraded color scheme to HIGH-GRADE** (per council recommendation):
  - OLD: Violet/Stone/Gold (low-grade, consumer feel)
  - NEW: Navy (#1E293B) + Teal (#14B8A6) + Gold (#F59E0B) (executive/financial)
  - Gold = SIGNAL ONLY (revenue KPIs), not decoration
  - Navy = Authority (Bloomberg-style, C-suite standard)
- Added RGB token definitions for dynamic opacity control
- Verified WCAG 2.1 AA compliance (4.5:1 contrast ratios)
- File sizes: `index.html` 698 lines, `styles.css` 345 lines

## Session 2026-04-29 (Architecture Scalability Review, ~1h)
### Council Review for Growth (COMPLETED)
**Council Members Consulted**: @council-architect, @council-performance, @council-security, @council-quality

**Critical Findings (Phase 0 - IMMEDIATE)**:
- Shared `MEMORY.md` causes git conflicts (80% with 2+ agents) → Move to per-agent memory
- No RAG/semantic search → Deploy MCP vector server before 1000 KB files
- Unrestricted autonomous agents (`bash:allow`) → Sandbox + audit logging required
- No git branch isolation → Per-agent branches (`agent/builder`, etc.)

**Key Recommendations**:
- Phase 0 (7 days): Fix shared memory, add audit logs, branch protection, sandbox agents
- Phase 1 (30 days): Deploy RAG, standardize agent formats, automate workflows
- Phase 2 (90 days): Permission tiers, secret manager migration, task registry

**Verdict**: 🟡 APPROVE WITH CRITICAL FIXES - Do NOT scale until Phase 0 complete

## Session 2026-04-29 (Builder: Executive Command Center + SaaS Landing v2, ~3h)
### Executive Command Center (COMPLETED - Ready for Deploy)
- Created Next.js 16.2.4 app: `04_Active_Work/exec-command-center`
- Stack: Next.js + Tailwind CSS v4 + shadcn/ui (card, badge, separator)
- Theme: Dark minimalist (`#0F172A` bg, `#1E293B` cards, `#0EA5E9` primary)
- Layout: Inverted pyramid (4 KPI cards → AI overview + activity feed → quick actions)
- Features: Real-time activity feed (6 mock items), AI agent trends with bars, KPI trend indicators
- **Drill-down feature**: Click KPI → expands chart with 7-day trend + detail text
- Component architecture: Server (`page.tsx`) + Client (`dashboard-client.tsx`) for Next.js 16
- Research-based: Stripe Dashboard, Google Analytics 4, AppDeck patterns
- Build: ✅ 4.7s (optimized from 15.1s), TypeScript: ✅ 4.0s, Static gen: ✅ 337ms
- Responsive: mobile-first, WCAG AA contrast, print-friendly
- **Next**: Deploy to Vercel, add real-time data, integrate recharts

### SaaS Landing Page v2 (COMPLETED)
- Overwrote `04_Active_Work/saas-landing/index.html` with Tailwind CDN v4
- Design: Sky Blue (`#0EA5E9`) + Orange (`#F97316`) accent, Plus Jakarta Sans font
- Features: 44px touch targets, SVG icons only (Heroicons 1.5px stroke), no emojis
- Research: ui-ux-pro-max skill Steps 3+4 (competitor analysis, accessibility)
- File: 464 lines, Tailwind CDN (no build step)

### Agent System Fixes (COMPLETED)
- Removed invalid model tags from 12 agent files (fixed `ProviderModelNotFoundError`)
- Fixed memory loading: Layer 2 (MEMORY.md, AGENTS.md, 01_Agents/{agent}.md) + Layer 3
- Configured filesystem MCP in `opencode.json` (replaced broken fetch MCP)
- Created session logs: `session-2026-04-29-v2-impl.md`, `session-2026-04-29-exec-dashboard.md`
- Logged ADR-008 (SaaS Landing v2), ADR-009 (Executive Command Center architecture)

## Things to Remember
- **High-Grade Executive = Navy/Teal/Gold** (NOT violet/stone/gold)
- **Heroicons v2.0 ONLY** (1.5px stroke, 24x24 viewBox)
- **Semantic tokens ONLY**: `--navy-500` NOT `#64748B` outside token defs
- **Color as SIGNAL**: Gold for revenue ONLY, Teal for data viz, Navy for authority
- **Council agents**: @council-architect, @council-quality, @council-security (use for reviews)
- All API keys in Windows Credential Manager (never in repo)
- **Landing theme**: Light with Sky Blue/Orange, Plus Jakarta Sans (Tailwind CDN v4)
- **CRITICAL FAILURE**: Executive Command Center (dark #0F172A, inverted pyramid) is REJECTED. User feedback: "design is beyond help, awful". NEVER build this type of dashboard again. Mechanics (Next.js, drill-down) worked, design is nonsense.

## Quick Reference
- **Start session**: Read AGENTS.md → MEMORY.md → decisions-log.md
- **End session**: Update MEMORY.md (<200 lines), create session log, update decisions-log
- **Executive dashboards**: Light theme > dark (conference rooms, printing)
- **Growth products**: Personal Development Coach (first product, £5k-£15k)
