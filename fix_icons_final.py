import re

# Fix SaaS landing page icons
with open('04_Active_Work/saas-landing/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace hamburger menu icon with Heroicon v2.0 menu
old_menu = '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <line x1="3" y1="12" x2="21" y2="12"></line>
            <line x1="3" y1="6" x2="21" y2="6"></line>
            <line x1="3" y1="18" x2="21" y2="18"></line>
          </svg>'''

new_menu = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'

if old_menu in content:
    content = content.replace(old_menu, new_menu)
    print('✅ Replaced menu icon with Heroicon v2.0')
else:
    print('⚠️ Menu icon pattern not found')

# Replace close icon with Heroicon x
old_close = '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>'''

new_close = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M6 18L18 6M6 6l12 12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'

if old_close in content:
    content = content.replace(old_close, new_close)
    print('✅ Replaced close icon with Heroicon v2.0')
else:
    print('⚠️ Close icon pattern not found')

# Write back
with open('04_Active_Work/saas-landing/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ Updated saas-landing/index.html with Heroicons v2.0')

# Also update dashboard icon
with open('04_Active_Work/project2jarvis-dashboard/index.html', 'r', encoding='utf-8') as f:
    content2 = f.read()

# Count SVGs in dashboard
svgs = re.findall(r'<svg.*?</svg>', content2, re.DOTALL)
print(f'Dashboard has {len(svgs)} SVGs - needs full Heroicon replacement later')

print('\n⚡ Quick fix complete! Full icon replacement needs more time.')
print('📚 Resources bookmarked: Heroicons v2.0, AdminLTE, NexTask, MUI')
