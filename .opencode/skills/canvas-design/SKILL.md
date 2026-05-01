# Canvas Design Skill

## Overview
Canvas Design is a **visual art and layout system** that creates beautiful posters, designs, slides, one-pagers, and data visualizations using design philosophy and AI automation. Originally an Obsidian Canvas plugin (claude-canvas), now evolved into Anthropic's **Claude Design** product.

**Source**: Anthropic Labs + Agrici Daniel (claude-canvas) + Airdev Canvas Design System

---

## Capabilities

### 1. Visual Art Generation
| Output Type | Description | Export Formats |
|-------------|-------------|----------------|
| **Posters** | Event, conference, marketing posters with layout algorithms | PNG, PDF, SVG |
| **Slide Decks** | Full presentations with master slides, speaker notes | PPTX, PDF, HTML |
| **One-Pagers** | Executive summaries, reports, dashboards | PDF, DOCX, HTML |
| **Data Visualizations** | Charts, infographics, dashboards | SVG, PNG, PDF |
| **Mood Boards** | Design exploration, brand identity | PNG, PDF, Figma |
| **Canvas Diagrams** | Flowcharts, architecture diagrams, system maps | SVG, Mermaid, PNG |

### 2. Layout Algorithms (The "Secret Sauce")
| Algorithm | Best For | Spatial Style |
|------------|----------|----------------|
| **Asymmetric Grid** | Mood boards, portfolios | Dynamic positioning with color zones |
| **Z-Pattern** | Landing pages, reports | Eye-tracking optimized flow |
| **F-Pattern** | Dashboards, data viz | Scanning-optimized layout |
| **Clustered** | Related concepts, mind maps | Grouped by semantic relationship |
| **Timeline** | Project plans, roadmaps | Chronological left-to-right |
| **Canvas (Obsidian)** | Knowledge graphs, connected nodes | Auto-routed edges, zone-based |

### 3. Design Philosophy (Anthropic Claude Design)
1. **Your Brand, Built In** - Reads your codebase/design files during onboarding, then auto-applies your colors, typography, components to EVERY project
2. **Import from Anywhere** - Text prompt, images (DOCX, PPTX, XLSX), website URL scrape, Figma file
3. **Refine with Controls** - Inline comments, direct edits, adjustment sliders for spacing/color/layout
4. **Export Anywhere** - Internal URL, folder, Canva, PDF, PPTX, standalone HTML
5. **Handoff to Code** - Packages everything into a bundle you can pass to Claude Code with a single instruction

---

## Usage Instructions

### Command Syntax
```
/canvas-design [artifact-type] [description] [options]
```

### Examples

#### 1. Create Executive Report (One-Pager)
```
/canvas-design one-pager "Q1 2026 Executive Summary for Project2Jarvis" --theme=executive --data=MEMORY.md --export=pdf
```
**Result**: Professional 1-page executive report with KPIs, charts, and violet/gold theme.

#### 2. Build Mood Board
```
/canvas-design mood-board "AI Agency Brand Identity" --colors=violet,stone,gold --fonts=Inter,Plus Jakarta Sans --style=asymmetric-grid
```
**Result**: Canvas with color-coded zones for "Environment," "AI Elements," "Typography," "Logo Concepts."

#### 3. Generate Slide Deck
```
/canvas-design slides "Project2Jarvis Capabilities Overview" --slides=10 --theme=modern-saas --export=pptx
```
**Result**: 10-slide deck with master slides, violet/stone theme, Inter typography.

#### 4. Create Dashboard Visualization
```
/canvas-design dashboard "Agent Ecosystem Overview" --layout=f-pattern --charts=donut,bar,line --export=html
```
**Result**: Executive dashboard HTML with F-pattern layout, interactive charts.

#### 5. Obsidian Canvas (Legacy - claude-canvas)
```
/canvas-design canvas "Project2Jarvis Knowledge Graph" --nodes=agents,memory,workflows --algorithm=clustered
```
**Result**: Fully populated Obsidian canvas with auto-positioned nodes, routed edges, and ≤200 words per node.

---

## Implementation Details

### Canvas Layout Engine (Obsidian-style)
```javascript
// Pseudo-code for layout algorithm
function layoutCanvas(description, template) {
  // 1. Canvas Composer Agent
  // - Analyzes description
  // - Selects optimal template
  // - Plans content strategy
  // - Enforces max 200 words/node for scannability
  
  // 2. Canvas Media Agent
  // - Coordinates batch media generation
  // - Integrates with /banana for AI images
  // - Uses /svg for diagrams
  // - Native Mermaid for flowcharts
  
  // 3. Canvas Layout Agent
  // - Applies spatial algorithm
  // - Creates zones (color-coded)
  // - Routes edges (auto-avoid overlaps)
  // - Validates spacing (≥ 16px gaps)
  
  return canvasJSON;
}
```

### Design System Integration
Canvas Design **automatically reads** your design system from:
- `MEMORY.md` (semantic tokens)
- `.opencode/skills/theme-factory/SKILL.md` (themes)
- Figma file URL (variables/styles)
- CSS files in project (custom properties)

Then **auto-applies** to every canvas:
```css
:root {
  --color-primary: var(--violet-500);  /* From your design system */
  --font-family: 'Inter', sans-serif;
  --spacing-unit: 16px;
  --zone-gap: 24px;
}
```

---

## Integration with Project2Jarvis

### Current Opportunities
| Artifact Needed | Type | Description | Priority |
|-----------------|------|-------------|----------|
| **Session Report** | One-pager | Replace `session-report-2026-04-28.html` with Canvas-designed PDF | High |
| **Agent Ecosystem Diagram** | Canvas | Visual map of all 10 agents + relationships | High |
| **Executive Dashboard** | Dashboard viz | Upgrade `executive-command-center` with Canvas charts | Medium |
| **Growth Department Pitch** | Slide deck | 10-slide deck for investors/clients | Medium |
| **Brand Mood Board** | Mood board | AI agency brand identity exploration | Low |

### Quick Commands for Our Project
```
/canvas-design one-pager "Session 2026-04-28 Report" --theme=executive --data=04_Active_Work/session-report-2026-04-28.html --export=pdf

/canvas-design canvas "Agent Ecosystem" --nodes=10 --algorithm=clustered --zones=council,autonomous,growth

/canvas-design slides "Project2Jarvis Growth Department" --slides=12 --theme=modern-saas --export=pptx
```

---

## Advanced Features

### 1. Multi-Agent Coordination (claude-canvas style)
When generating a canvas, **3 specialized agents** coordinate:
1. **Canvas Composer** - Content strategy, template selection, text limits
2. **Canvas Media** - AI image generation, SVG diagrams, Mermaid charts
3. **Canvas Layout** - Spatial algorithms, zone creation, edge routing

### 2. Import Sources
- **Text Prompt** - "Mood board for cyberpunk game"
- **Documents** - DOCX, PPTX, XLSX (extracts content/styles)
- **Website URL** - Scrapes live site for elements to replicate
- **Figma File** - Reads components, styles, variables
- **Codebase** - Reads CSS custom properties, component files

### 3. Export Destinations
- **Internal URL** - Shareable link within organization (Anthropic)
- **Folder** - Save as files (PNG, PDF, PPTX, HTML)
- **Canva** - Import directly to Canva editor
- **Figma** - Create frames with components
- **Claude Code** - Handoff bundle for development

### 4. Fine-Grained Controls
- **Slider Controls** - Adjust spacing, color opacity, layout density live
- **Inline Comments** - Comment on specific elements like Figma
- **Direct Edits** - Click to edit text, colors, positioning
- **Component Swaps** - Replace buttons, cards, charts with alternatives

---

## References (Your "Bible")

### Core Systems
- **Anthropic Claude Design**: https://www.anthropic.com/news/claude-design-anthropic-labs
- **claude-canvas (Obsidian)**: https://agricidaniel.com/blog/claude-canvas-ai-visual-production
- **Canvas Design System (Figma)**: https://www.figma.com/community/file/1387894540487619534/canvas-design-system
- **Airdev Canvas**: https://airdev.co (Bubble integration)

### Design Philosophy
- **SAP Design System**: https://www.sap.com/design/design-system
- **ServiceNow Horizon**: https://horizon.servicenow.com/
- **Atlassian Design**: https://atlassian.design/design-system
- **Strato (Dynatrace)**: https://developer.dynatrace.com/design

### Tools & Plugins
- **shadcncraft Figma Plugin**: https://www.shadcncraft.com/
- **Theme Composer (Figma)**: https://www.captain-design.com/plugins/theme-composer/
- **Figma MCP Server**: https://github.com/hadi21k/figma-mcp

---

## Success Metrics

When you run `/canvas-design`, the output should be:
1. **"Canvas generated successfully"** - Layout algorithm applied
2. **"Design system auto-applied"** - Your tokens/theme used
3. **"All exports ready"** - PDF/PPTX/HTML/PNG available
4. **"3-agent coordination complete"** - Composer + Media + Layout finished

**User reaction**: *"THIS CANVAS LOOKS LIKE A DESIGN AGENCY MADE IT. SHIP IT!"* 🎨

---

## Comparison: Theme Factory vs Canvas Design

| Feature | Theme Factory | Canvas Design |
|---------|----------------|---------------|
| **Purpose** | Apply themes to existing artifacts | Create new visual artifacts from scratch |
| **Input** | HTML, CSS, Figma, PPTX | Text prompt, docs, URLs, Figma |
| **Output** | Themed files (same format) | New files (PNG, PDF, PPTX, HTML) |
| **Best For** | Quick theme swaps, bulk updates | Visual creation, mood boards, reports |
| **Agents** | 1 (theme applier) | 3 (composer + media + layout) |
| **Time** | Seconds | 1-3 minutes |

**Use Theme Factory when**: You have an HTML file and want to apply a professional theme.
**Use Canvas Design when**: You have a blank canvas and want to create a poster, slide deck, or report from scratch.
