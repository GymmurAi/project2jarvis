# UI/UX Pro Max Skill Research

**Researcher**: Researcher Agent (OpenCode)  
**Date**: 2026-04-28  
**Sources**: [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (71.8k ⭐, 7.4k 🍴)

---

## Repository Overview

**UI/UX Pro Max** is an AI skill that provides design intelligence for building professional UI/UX across multiple platforms and frameworks. It acts as a "design co-pilot" that gives AI agents structured knowledge to produce "legendary" UI output.

### What Makes It "Pro Max"

| Feature | Count | Description |
|---------|-------|-------------|
| Industry Reasoning Rules | 161 | Product-type → design system mapping with anti-patterns |
| UI Styles | 67 | Glassmorphism, Claymorphism, Bento Grid, Dark Mode, AI-Native UI, etc. |
| Color Palettes | 161 | Industry-specific, 1:1 aligned with product types |
| Font Pairings | 57 | Curated Google Fonts combinations |
| Chart Types | 25 | Dashboard and analytics recommendations |
| UX Guidelines | 99 | Best practices, anti-patterns, accessibility rules |
| Tech Stacks | 15 | React, Next.js, Vue, Svelte, SwiftUI, React Native, Flutter, etc. |

### Core Architecture

```
User Request → Multi-Domain Search (5 parallel) → Reasoning Engine (BM25 ranking)
→ Design System Output (Pattern + Style + Colors + Typography + Effects + Anti-Patterns)
→ Pre-Delivery Checklist Validation
```

---

## SKILL.md Analysis

The `SKILL.md` file is the instruction set loaded into the AI agent's context. It uses a structured format:

### Trigger Conditions

**Must Use (Required activation):**
- Designing new pages (Landing, Dashboard, Admin, SaaS, Mobile App)
- Creating/refactoring UI components (buttons, modals, forms, tables, charts)
- Choosing color schemes, typography, spacing, layout systems
- Reviewing UI for UX, accessibility, visual consistency
- Implementing navigation, animations, responsive behavior
- Product-level design decisions (style, hierarchy, brand expression)

**Recommended:**
- UI looks "not professional enough" but reason unclear
- Usability feedback received
- Pre-launch quality optimization
- Cross-platform design alignment
- Building design systems or component libraries

**Skip (No activation needed):**
- Pure backend logic, API/database design, infrastructure, DevOps, non-visual scripts

### Rule Priority System (1-10)

| Priority | Category | Impact | Key Checks |
|----------|----------|--------|------------|
| 1 | Accessibility | CRITICAL | Contrast 4.5:1, Alt text, Keyboard nav, Aria-labels |
| 2 | Touch & Interaction | CRITICAL | Min 44×44px targets, 8px+ spacing, Loading feedback |
| 3 | Performance | HIGH | WebP/AVIF, Lazy loading, CLS < 0.1 |
| 4 | Style Selection | HIGH | Match product type, SVG icons (no emoji), consistency |
| 5 | Layout & Responsive | HIGH | Mobile-first, breakpoints, no horizontal scroll |
| 6 | Typography & Color | MEDIUM | Base 16px, Line-height 1.5, Semantic color tokens |
| 7 | Animation | MEDIUM | Duration 150–300ms, Motion conveys meaning |
| 8 | Forms & Feedback | MEDIUM | Visible labels, Error near field, Progressive disclosure |
| 9 | Navigation Patterns | HIGH | Predictable back, Bottom nav ≤5, Deep linking |
| 10 | Charts & Data | LOW | Legends, Tooltips, Accessible colors |

### Workflow Injected Into Agent

**Step 1: Analyze Requirements**
- Extract product type, target audience, style keywords, tech stack

**Step 2: Generate Design System (REQUIRED)**
```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "<query>" --design-system -p "Project Name"
```

**Step 3: Supplement with Domain Searches**
```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "<keyword>" --domain <domain>
```

**Step 4: Apply Stack Guidelines**
```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "<keyword>" --stack <stack>
```

### Design System Persistence (Master + Overrides)

The skill supports hierarchical design system storage:
```
design-system/
├── MASTER.md           # Global Source of Truth
└── pages/
    └── dashboard.md    # Page-specific overrides
```

---

## Tools & Scripts Found

| Tool | Purpose | How to Use |
|------|---------|------------|
| `search.py` | BM25-based search engine for all design data | `python3 search.py "query" --domain <domain>` |
| `uipro-cli` | CLI installer for 19+ AI assistants | `npm install -g uipro-cli && uipro init --ai opencode` |
| `--design-system` | Generate complete design system | `--design-system -p "Project Name"` |
| `--persist` | Save design system to files | `--persist --page "dashboard"` |
| `--domain` | Search specific domain | `--domain style\|color\|typography\|ux\|chart\|product\|react\|web\|prompt` |
| `--stack` | Get stack-specific guidelines | `--stack react-native\|react\|swiftui\|etc` |
| `-f markdown` | Output format toggle | `-f markdown` (default: ASCII box) |
| `skill.json` | Skill metadata for Claude Marketplace | Defines name, description, activation triggers |

---

## Modern Elements & Techniques

### UI Styles (67 Total)

**General Styles (49):**
- Minimalism & Swiss Style, Neumorphism, Glassmorphism, Brutalism
- 3D & Hyperrealism, Vibrant & Block-based, Dark Mode (OLED)
- Accessible & Ethical, Claymorphism, Aurora UI, Retro-Futurism
- Flat Design, Skeuomorphism, Liquid Glass, Motion-Driven
- Micro-interactions, Inclusive Design, Zero Interface, Soft UI Evolution
- Neubrutalism, Bento Box Grid, Y2K Aesthetic, Cyberpunk UI
- Organic Biophilic, AI-Native UI, Memphis Design, Vaporwave
- Dimensional Layering, Exaggerated Minimalism, Kinetic Typography
- Parallax Storytelling, Swiss Modernism 2.0, HUD / Sci-Fi FUI
- Pixel Art, Bento Grids, Spatial UI (VisionOS), E-Ink / Paper
- Gen Z Chaos / Maximalism, Biomimetic / Organic 2.0, Anti-Polish / Raw Aesthetic
- Tactile Digital / Deformable UI, Nature Distilled, Interactive Cursor Design
- Voice-First Multimodal, 3D Product Preview, Gradient Mesh / Aurora Evolved
- Editorial Grid / Magazine, Chromatic Aberration / RGB Split, Vintage Analog / Retro Film

**Landing Page Styles (8):**
- Hero-Centric Design, Conversion-Optimized, Feature-Rich Showcase
- Minimal & Direct, Social Proof-Focused, Interactive Product Demo
- Trust & Authority, Storytelling-Driven

**BI/Analytics Dashboard Styles (10):**
- Data-Dense Dashboard, Heat Map & Heatmap Style, Executive Dashboard
- Real-Time Monitoring, Drill-Down Analytics, Comparative Analysis Dashboard
- Predictive Analytics, User Behavior Analytics, Financial Dashboard
- Sales Intelligence Dashboard

### Interaction Patterns
- Spring/physics-based animations (Apple HIG)
- Shared element transitions (Material Design)
- Interruptible animations (user can cancel mid-animation)
- Staggered list entrance (30-50ms per item)
- Scale feedback on press (0.95-1.05)
- Real-time gesture tracking (drag/swipe/pinch visual response)
- Haptic feedback for confirmations (iOS HIG)

### Accessibility Techniques
- `prefers-reduced-motion` support
- Dynamic Type / system text scaling
- VoiceOver/screen reader logical reading order
- Escape routes in modals (cancel/back)
- Color-not-only (supplement with icons/text)
- Tab order matches visual order
- aria-live regions for toasts/errors

### Performance Techniques
- Virtualized lists (50+ items)
- Skeleton screens / shimmer for >1s operations
- font-display: swap/optional
- Critical CSS inlining
- Route-level code splitting (React Suspense)
- WebP/AVIF with fallbacks
- `aspect-ratio` to prevent CLS
- `touch-action: manipulation` to reduce 300ms delay

---

## Tech Stack

### Languages (Repository)
- **Python 78.5%** — Search engine, reasoning engine, CLI scripts
- **JavaScript 11.4%** — CLI tool (uipro-cli)
- **TypeScript 6.6%** — Type definitions
- **HTML 3.5%** — Documentation/examples

### Supported Target Stacks (15)
| Stack | Focus |
|-------|-------|
| React, Next.js, shadcn/ui | React Ecosystem |
| Vue, Nuxt.js, Nuxt UI | Vue Ecosystem |
| Angular | Angular |
| Svelte, Astro | Other Web |
| Laravel (Blade, Livewire, Inertia.js) | PHP |
| SwiftUI | iOS |
| Jetpack Compose | Android |
| React Native, Flutter | Cross-Platform |
| HTML + Tailwind | Default Web |

### Key Libraries Referenced
- **Heroicons, Lucide** — SVG icon sets (never emojis)
- **Google Fonts** — 57 curated pairings
- **shadcn/ui** — Component reference (MCP integration available)

---

## Design Principles

### The "Pro Max" Principles

1. **Industry Alignment** — Design systems must match product type (fintech ≠ neon colors; wellness ≠ AI purple gradients)
2. **Anti-Pattern Awareness** — Explicitly teach what NOT to do per industry
3. **Semantic Tokens Over Raw Hex** — `primary-500` not `#3B82F6` in components
4. **No Emoji as Icons** — Use SVG icon libraries (Heroicons, Lucide)
5. **Touch-First** — 44×44pt minimum, 8px spacing, no hover-only reliance
6. **Accessibility by Default** — 4.5:1 contrast, keyboard nav, aria-labels, reduced-motion
7. **Motion with Meaning** — Every animation expresses cause-effect, not decorative
8. **Style Consistency** — One icon style, one stroke width, one elevation scale globally
9. **Mobile-First Responsive** — 375px → 768px → 1024px → 1440px breakpoints
10. **Performance Budget** — <16ms main thread work, CLS <0.1, lazy load non-critical

### Hierarchy of Rules
```
CRITICAL (must pass): Accessibility, Touch & Interaction
HIGH (should pass):   Performance, Style Selection, Layout, Navigation
MEDIUM (aim for):     Typography, Color, Animation, Forms, Feedback
LOW (nice to have):   Charts & Data
```

---

## Adaptation for OpenCode

### Key Differences: Claude Code vs OpenCode

| Aspect | Claude Code | OpenCode |
|--------|-------------|----------|
| Skill Location | `.claude/skills/` | `.opencode/skills/` |
| Agent Defs | `CLAUDE.md` | `.opencode/agents/*.md` |
| CLI Install | `uipro init --ai claude` | `uipro init --ai opencode` |
| Skill Format | SKILL.md in `.claude/skills/<name>/` | SKILL.md in `.opencode/skills/<name>/` |
| Agent Model | Claude only | Multi-model (Claude, GPT, etc.) |

### Steps to Adapt

1. **Create OpenCode Skill Directory**
   ```
   .opencode/skills/ui-ux-pro-max/SKILL.md
   ```

2. **Download the Skill Data**
   ```bash
   uipro init --ai opencode
   ```
   This auto-creates `.opencode/skills/ui-ux-pro-max/` with all scripts/data.

3. **Modify SKILL.md for OpenCode Agents**
   - Change references from "Claude" to "OpenCode agent"
   - Update paths from `.claude/skills/` to `.opencode/skills/`
   - Add multi-model guidance (different agents may use different models)

4. **Create Dedicated Agent (Optional but Recommended)**
   - Create `.opencode/agents/ui-ux-pro-max.md`
   - Set appropriate model (claude-sonnet-4-5 for balanced, claude-opus-4-5 for architect-level)
   - Grant appropriate permissions (edit:ask for review, edit:direct for autonomous)

5. **Integrate with Existing Agents**
   - Builder agent: invoke via `@ui-ux-pro-max` when doing UI work
   - Council agents: use as reference for reviewing UI/UX quality

### OpenCode-Specific Enhancements

```yaml
# .opencode/skills/ui-ux-pro-max/skill.json (OpenCode format)
{
  "name": "ui-ux-pro-max",
  "description": "Design intelligence for professional UI/UX across platforms",
  "agents": ["builder", "researcher", "maintainer", "council-quality"],
  "trigger_on": ["build", "design", "create", "review", "fix", "improve"],
  "paths": {
    "scripts": ".opencode/skills/ui-ux-pro-max/scripts/",
    "data": ".opencode/skills/ui-ux-pro-max/data/"
  }
}
```

---

## Recommendation for Our Agent

### Proposed: `ui-ux-pro-max` Agent for OpenCode

**Agent Role**: Specialized UI/UX design intelligence agent that delivers "very high tier" results on first attempt.

**Core Capabilities:**
1. **Auto-Design-System Generation** — Every UI task starts with `--design-system` call
2. **Industry-Specific Rules** — 161 product types mapped to styles/colors/typography
3. **Pre-Delivery Validation** — Runs Quick Reference §1-§3 checklist before delivering
4. **Stack-Aware** — Adapts guidance for React, Vue, SwiftUI, React Native, etc.
5. **Accessibility-First** — WCAG AA minimum, reduced-motion, keyboard nav built-in

**Integration with Existing Agents:**
- **Builder**: Invoke `@ui-ux-pro-max` when building UI components/pages
- **Council-Quality**: Use as reference for UI/UX code reviews
- **Researcher**: Can deep-dive design trends and update the knowledge base

**File Structure:**
```
.opencode/
├── agents/
│   └── ui-ux-pro-max.md          # Agent definition (optional dedicated agent)
└── skills/
    └── ui-ux-pro-max/
        ├── SKILL.md               # Full instruction set (from GitHub)
        ├── scripts/
        │   └── search.py         # BM25 search engine
        ├── data/
        │   ├── ui-styles.csv     # 67 styles
        │   ├── ui-colors.csv     # 161 palettes
        │   ├── ui-typography.csv # 57 pairings
        │   ├── ui-product-types.csv # 161 product types
        │   ├── ui-reasoning.csv  # 161 reasoning rules
        │   ├── ui-ux-guidelines.csv # 99 UX rules
        │   └── ui-charts.csv     # 25 chart types
        └── skill.json            # OpenCode skill metadata
```

**Usage Pattern:**
```
# User: "Build a landing page for my SaaS product"

# Agent automatically:
1. Runs: python3 .opencode/skills/ui-ux-pro-max/scripts/search.py "SaaS" --design-system -p "MySaaS"
2. Gets: Pattern (Hero-Centric), Style (Soft UI Evolution), Colors, Typography, Effects
3. Checks: Anti-patterns for SaaS (avoid: neon, emojis, harsh animations)
4. Implements: Code with proper tokens, hover states, accessibility
5. Validates: Pre-delivery checklist (§1-§3 priority rules)
```

**Success Metric**: "Legendary" UI output that requires minimal iteration — professional quality on first delivery.

---

## Data Assets Summary

| Asset File | Records | Purpose |
|------------|---------|---------|
| `ui-styles.csv` | 67 | Style definitions, best-for, keywords, effects |
| `ui-colors.csv` | 161 | Industry-aligned color palettes with hex values |
| `ui-typography.csv` | 57 | Font pairings with Google Fonts links |
| `ui-product-types.csv` | 161 | Product categories with style/color priorities |
| `ui-reasoning.csv` | 161 | Decision rules: pattern → style → color → typography |
| `ui-ux-guidelines.csv` | 99 | UX best practices with priority levels |
| `ui-charts.csv` | 25 | Chart type recommendations by data type |
| `ui-stacks.csv` | 15 | Stack-specific implementation guidelines |

---

## Key Takeaways for Project2Jarvis

1. **"Pro Max" = Structured Knowledge + Reasoning Engine** — Not magic, just comprehensive data + priority rules
2. **BM25 Search ranking** — Scripts use BM25 (not vector search) for fast, relevant results
3. **Anti-Patterns are Critical** — Teaching what NOT to do per industry prevents "amateur" output
4. **Pre-Delivery Checklist** — Agent self-validates before showing work (§1-§3 priority rules)
5. **Design System Persistence** — Master + Overrides pattern enables multi-session consistency
6. **CLI Tool Already Supports OpenCode** — `uipro init --ai opencode` exists!
7. **71.8k Stars** — This is a proven, widely-adopted approach

---

**Next Steps:**
1. Run `npm install -g uipro-cli && uipro init --ai opencode` to install in our project
2. Create dedicated `.opencode/agents/ui-ux-pro-max.md` agent definition
3. Test with a sample UI task to validate the workflow
4. Document lessons learned in `03_Knowledge_Base/`
