# Theme Factory Skill

## Overview
Theme Factory is a Claude Code skill that **automates the generation of customizable themes** for applications, documents, slides, and HTML pages. It streamlines the design process by applying professional color palettes and typography systems from 10 pre-set themes.

**Source**: Shyft.ai + Anthropic Labs Claude Design

---

## Capabilities

### 1. Theme Generation
- **10 Pre-set Themes** with curated color/font combinations
- **Custom Themes** from user descriptions
- **Brand Alignment** - automatically applies team design systems
- **Multi-format Export** - CSS, Figma variables, HTML, PDF, PPTX

### 2. Supported Artifacts
| Artifact Type | Theme Applied To |
|---------------|-------------------|
| **HTML Landing Pages** | Full semantic token system (colors, typography, spacing) |
| **Slide Decks (PPTX)** | Master slide themes with brand colors |
| **Documents (DOCX)** | Heading/body typography, color accents |
| **Reports (PDF)** | Professional themes with data visualization colors |
| **Figma Files** | Auto-apply to Figma styles/variables |
| **React Apps** | CSS custom properties + Tailwind config |

### 3. Theme Categories (10 Pre-sets)
| Theme Name | Palette | Typography | Best For |
|------------|----------|------------|----------|
| **Executive** | Violet + Stone neutrals | Inter (300-900) | C-suite dashboards, reports |
| **Modern SaaS** | Indigo + Cool grays | Plus Jakarta Sans | Landing pages, web apps |
| **Enterprise** | Blue + Warm neutrals | Ubuntu + Oswald | Internal tools, admin panels |
| **Fintech** | Navy + Gold accents | SF Pro Display | Financial dashboards, reports |
| **Healthcare** | Teal + Soft neutrals | Nunito | Medical apps, patient portals |
| **Dark Mode Pro** | Dark navy + Cyan | Inter | Developer tools, night usage |
| **Minimal** | Pure neutrals + 1 accent | Helvetica Now | Content sites, blogs |
| **Brand Bold** | Custom brand colors | Custom brand fonts | Marketing sites, campaigns |
| **Academic** | Serif + muted colors | Crimson + Lato | Research papers, docs |
| **Startup** | Vibrant + playful | Poppins + Manrope | Pitch decks, MVPs |

---

## Usage Instructions

### Command Syntax
```
/theme-factory [artifact-type] [theme-name] [customizations]
```

### Examples

#### 1. Apply Pre-set Theme to HTML Page
```
/theme-factory html-landing-page executive --accent=violet --output=index.html
```
**Result**: Applies Executive theme (violet/stone, Inter font) to `index.html` with full semantic tokens.

#### 2. Generate Custom Theme for Slides
```
/theme-factory slides "Modern AI Startup" --colors="#6366F1,#F59E0B,#10B981" --fonts="Plus Jakarta Sans,Inter" --export=pptx
```
**Result**: Creates a custom theme with indigo, gold, emerald palette and exports to PowerPoint.

#### 3. Apply Theme to Figma
```
/theme-factory figma executive --file=<FIGMA_FILE_URL> --apply-variables
```
**Result**: Applies Executive theme to all Figma styles/variables in the file.

#### 4. Bulk Theme Application
```
/theme-factory bulk --files="saas-landing/index.html,dashboard/index.html" --theme=modern-saas
```
**Result**: Applies Modern SaaS theme to multiple HTML files at once.

---

## Implementation Details

### Theme Structure (CSS Output)
```css
:root {
  /* Semantic Color Tokens */
  --color-primary-50: #F5F3FF;
  --color-primary-500: #6366F1;  /* NOT raw #6366F1 */
  --color-primary-900: #1E1B4B;
  
  --color-neutral-50: #F8FAFC;
  --color-neutral-500: #64748B;
  --color-neutral-900: #0F172A;
  
  --color-accent-500: #F59E0B;
  
  /* Typography Scale */
  --font-family-base: 'Inter', system-ui, sans-serif;
  --font-weight-light: 300;
  --font-weight-normal: 400;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  --font-weight-extrabold: 800;
  
  /* Spacing Scale */
  --space-1: 4px;
  --space-2: 8px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  
  /* Border Radius */
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 14px;
}
```

### Quality Rules (Enforced)
✅ **Semantic tokens ONLY** - Never use raw hex values in component CSS
✅ **WCAG 2.1 AA** - 4.5:1 contrast minimum on all text
✅ **44x44px touch targets** - All interactive elements
✅ **`prefers-reduced-motion`** - Respected
✅ **BEM/Utility classes** - Consistent naming
✅ **Mobile-first** - 375px → 1440px responsive

---

## Integration with Project2Jarvis

### Current Files That Need Theming
| File | Current State | Recommended Theme |
|------|------------------|-------------------|
| `04_Active_Work/saas-landing/index.html` | Amateur purple/neon | **Modern SaaS** (Indigo + Plus Jakarta Sans) |
| `04_Active_Work/project2jarvis-dashboard/index.html` | Basic dark/light | **Enterprise** (Blue + Ubuntu) |
| `04_Active_Work/executive-command-center/index.html` | Executive violet/gold | **Executive** (Violet/Stone + Inter) ✅ Already applied |
| `04_Active_Work/session-report-2026-04-28.html` | Animated blue | **Executive** (Violet/Gold) |

### Quick Commands for Our Files
```
/theme-factory html saas-landing/index.html modern-saas
/theme-factory html project2jarvis-dashboard/index.html enterprise
/theme-factory html executive-command-center/index.html executive --validate
```

---

## Advanced Features

### 1. Brand Kit Import
Automatically extract brand colors/fonts from:
- Website URL (scrapes CSS variables)
- Figma file (reads styles/variables)
- PDF/PPTX (extracts theme colors)
- Image (uses AI to identify dominant colors)

### 2. Theme Validation
```
/theme-factory validate --file=index.html --check=wcag-aa,contrast,tokens
```
Checks:
- ✅ All colors use semantic tokens
- ✅ Contrast ratios ≥ 4.5:1
- ✅ Touch targets ≥ 44x44px
- ✅ Responsive breakpoints defined
- ✅ `prefers-reduced-motion` media query

### 3. Theme Diff
```
/theme-factory diff --old=index.html --new=index-themed.html
```
Shows exact changes that will be applied before committing.

---

## References (Your "Bible")
- **Shyft.ai Theme Factory**: https://shyft.ai/skills/theme-factory
- **Anthropic Claude Design**: https://www.anthropic.com/news/claude-design-anthropic-labs
- **SAP Design System**: https://www.sap.com/design/design-system
- **ServiceNow Horizon**: https://horizon.servicenow.com/
- **Atlassian Design**: https://atlassian.design/design-system
- **Microsoft Atlas**: https://design.learn.microsoft.com/

---

## Success Metrics
When you run `/theme-factory`, the output should be:
1. **"Theme applied successfully"** - No errors
2. **"All WCAG 2.1 AA checks passed"** - Accessibility validated
3. **"Semantic tokens: 100% coverage"** - No raw hex values
4. **"Export ready: HTML, CSS, Figma"** - Multi-format available

**User reaction**: *"THIS THEME LOOKS ENTERPRISE-GRADE. SHIP IT!"* 🚀
