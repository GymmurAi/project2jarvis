# Project2Jarvis Design System MASTER.md
## Style
Data-Dense Dashboard: High information density, clean layout, minimal chrome, focus on readability and quick scanning.

## Colors
### Primary (Indigo)
--primary-50: #EEF2FF
--primary-100: #E0E7FF
--primary-200: #C7D2FE
--primary-300: #A5B4FC
--primary-400: #818CF8
--primary-500: #6366F1
--primary-600: #4F46E5
--primary-700: #4338CA
--primary-800: #3730A3
--primary-900: #312E81
--primary-950: #1E1B4B

### Accent (Emerald)
--accent-50: #ECFDF5
--accent-100: #D1FAE5
--accent-200: #A7F3D0
--accent-300: #6EE7B7
--accent-400: #34D399
--accent-500: #10B981
--accent-600: #059669
--accent-700: #047857
--accent-800: #065F46
--accent-900: #064E3B
--accent-950: #022C22

### Warning (Amber)
--warning-50: #FFFBEB
--warning-100: #FEF3C7
--warning-200: #FDE68A
--warning-300: #FCD34D
--warning-400: #FBBF24
--warning-500: #F59E0B
--warning-600: #D97706
--warning-700: #B45309
--warning-800: #92400E
--warning-900: #78350F
--warning-950: #451A03

### Danger (Red)
--danger-50: #FEF2F2
--danger-100: #FEE2E2
--danger-200: #FECACA
--danger-300: #FCA5A5
--danger-400: #F87171
--danger-500: #EF4444
--danger-600: #DC2626
--danger-700: #B91C1C
--danger-800: #991B1B
--danger-900: #7F1D1D
--danger-950: #450A0A

### Neutral (Slate)
--neutral-50: #F8FAFC
--neutral-100: #F1F5F9
--neutral-200: #E2E8F0
--neutral-300: #CBD5E1
--neutral-400: #94A3B8
--neutral-500: #64748B
--neutral-600: #475569
--neutral-700: #334155
--neutral-800: #1E293B
--neutral-900: #0F172A
--neutral-950: #020617

### Dark Mode
Background: --neutral-900 (#0F172A)
Surface: --neutral-800 (#1E293B)
Text: --neutral-50 (#F8FAFC)
Border: --neutral-700 (#334155)

## Typography
Font Family: Inter (Google Fonts, font-display: swap)
Sizes:
- Caption: 12px/16px
- Body: 14px/20px
- Subheading: 16px/24px
- Heading: 20px/28px
- Title: 24px/32px
- Hero: 32px/40px
Weights: 400 (regular), 500 (medium), 600 (semibold), 700 (bold)

## Spacing
Base unit: 8px. All margins, paddings, gaps are multiples of 8px.

## Touch Targets
Minimum 44x44px for all interactive elements.

## Effects
### Shadows
--shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05)
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)
--shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)

### Border Radius
--radius-sm: 4px
--radius-md: 8px
--radius-lg: 12px
--radius-full: 9999px

### Transitions
--transition-base: 150ms ease
--transition-slow: 300ms ease

## Accessibility
- WCAG AA 4.5:1 contrast ratio for all text
- prefers-reduced-motion: all animations disabled
- Focus visible: 2px solid --primary-500, offset 2px
