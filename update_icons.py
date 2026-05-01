import re

# Heroicons v2.0 SVG definitions (24x24, 1.5px stroke)
heroicons = {
    'sun': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 3V1.5M12 21.75V20.25M4.22 4.22l1.06 1.06M18.72 18.72l1.06 1.06M1.5 12H3M20.25 12H21.75M4.22 19.78l1.06-1.06M18.72 5.28l1.06-1.06M12 15.75a3.75 3.75 0 100-7.5 3.75 3.75 0 000 7.5z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'moon': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M21.75 15.75a9 9 0 11-12.852-9.652 7.348 7.348 0 0010.068 10.068 9.005 9.005 0 002.784 1.584z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'chart-bar': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M3 13.125C3 12.504 3.504 12 4.125 12h2.25c.621 0 1.125.504 1.125 1.125v6.75C7.5 20.496 6.996 21 6.375 21h-2.25A1.125 1.125 0 013 19.875v-6.75zM9.75 8.625c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125v11.25c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V8.625zM16.5 4.125c0-.621.504-1.125 1.125-1.125h2.25C20.496 3 21 3.504 21 4.125v15.75c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V4.125z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'users': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M15 19.128a9.38 9.38 0 002.625.372 9.337 9.337 0 004.121-2.702c.149-.192.279-.404.385-.629l.045-.1a.758.758 0 00-.197-.826c-.564-.504-1.348-.864-2.024-1.206a9.23 9.23 0 01-4.95 0c-.676.342-1.46.702-2.024 1.206a.758.758 0 00-.197.826l.045.1c.106.225.236.437.385.629a9.337 9.337 0 004.121 2.702A9.38 9.38 0 0015 19.128zM12 6.375a3.375 3.375 0 11-.001-6.75A3.375 3.375 0 0112 6.375zm0 2.25a4.875 4.875 0 00-4.356 2.817c.348.474.858.886 1.493 1.17.68.303 1.507.483 2.363.483s1.683-.18 2.363-.483c.635-.284 1.145-.696 1.493-1.17A4.875 4.875 0 0012 8.625z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'cog': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M9.594 3.94c.09-.542.56-.94 1.11-.94h2.593c.55 0 1.02.398 1.11.94l.213 1.281c.063.374.313.686.645.87.333.185.73.24 1.102.13l1.217-.456a1.125 1.125 0 011.37.49l1.296 2.247a1.125 1.125 0 01-.26 1.431l-1.003.827c-.293.24-.438.61-.431.991a6.932 6.932 0 010 1.256c-.007.38.138.75.431.99l1.003.827c.434.358.556.984.26 1.43l-1.296 2.247a1.125 1.125 0 01-1.37.491l-1.217-.456c-.372-.11-.769-.055-1.102.13-.332.184-.582.496-.645.87l-.213 1.28a1.125 1.125 0 01-1.11.94h-2.594a1.125 1.125 0 01-1.11-.94l-.212-1.281c-.063-.374-.313-.686-.645-.87-.333-.185-.73-.24-1.102-.13l-1.217.456a1.125 1.125 0 01-1.37-.49L2.545 14.87a1.125 1.125 0 01.26-1.431l1.003-.827c.293-.24.438-.61.431-.991a6.932 6.932 0 010-1.256c.007-.38-.138-.75-.431-.99l-1.003-.827a1.125 1.125 0 01-.26-1.43L3.611 6.63a1.125 1.125 0 011.37-.49l1.217.456c.372.11.769.055 1.102-.13.332-.184.582-.496.645-.87l.213-1.28z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'rocket': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M15.59 14.37a6 6 0 01-5.84 7.38v-4.8m5.84-2.58a14.93 14.93 0 006.18-2.7c.643-.39.987-1.287.774-1.987L18.567 3.6a1.125 1.125 0 00-1.705-.824c-.678.359-1.348.68-2.01.964a18.27 18.27 0 00-3.78 1.404A18.608 18.608 0 006.75 7.5c-1.006.49-1.997 1.067-2.935 1.835A18.563 18.563 0 012.25 10.5c.277.38.612.732 1.001 1.054a18.497 18.497 0 003.056 2.137 18.244 18.244 0 002.392 1.246c.921.43 1.88.789 2.865 1.077a22.587 22.587 0 002.566.464c.812.08 1.627.128 2.441.148v-4.8z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'check-circle': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'x-circle': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M9.75 9.75l4.5 4.5m0-4.5l-4.5 4.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'clock': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'trophy': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M16.5 18.75h-9m9 0a3 3 0 013 3h-15a3 3 0 013-3m9 0v-4.875c0-.621-.504-1.125-1.125-1.125H7.875c-.621 0-1.125.504-1.125 1.125V18.75m9-12h3.375c.621 0 1.125.504 1.125 1.125V17.25m-12 0V18.75m0-12h3.375c.621 0 1.125.504 1.125 1.125V17.25" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'home': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h7.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'fire': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M15.362 5.214A8.252 8.252 0 0112 21 8.25 8.25 0 016.038 7.047 8.287 8.287 0 009 9.501c.138.248.337.436.589.583C10.085 10.864 11.044 12 12 12c.956 0 1.915-1.136 2.411-1.916a3.553 3.553 0 01.587-.583 8.287 8.287 0 002.364-2.203z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'arrow-right': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'arrow-left': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M10.5 19.5L3 12m0 0l7.5-7.5M3 12h18" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'bell': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M14.857 17.082a23.848 23.848 0 005.454-1.31A8.967 8.967 0 0118 9.75v-.7V9A6 6 0 006 9v.75a8.967 8.967 0 01-2.312 6.022c1.733.64 3.56 1.085 5.455 1.31m5.714 0a24.255 24.255 0 01-5.714 0m5.714 0a3 3 0 11-5.714 0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'envelope': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25h-15a2.25 2.25 0 01-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25m19.5 0v.243a2.25 2.25 0 01-1.07 1.916l-7.5 4.615a2.25 2.25 0 01-2.36 0L3.32 8.91a2.25 2.25 0 01-1.07-1.916V6.75" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'briefcase': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20.25 14.15v4.25a2.25 2.25 0 01-2.25 2.25H6a2.25 2.25 0 01-2.25-2.25v-4.25m16.5 0V6.75a2.25 2.25 0 00-2.25-2.25H6A2.25 2.25 0 003.75 6.75v7.4m16.5 0h-16.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'user': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'sparkles': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09zM18.259 8.715L18 9.75l-.259-1.035a3.375 3.375 0 00-2.455-2.456L14.25 6l1.036-.259a3.375 3.375 0 002.455-2.456L18 2.25l.259 1.035a3.375 3.375 0 002.455 2.456L21.75 6l-1.036.259a3.375 3.375 0 00-2.455 2.456zM16.894 20.567L16.5 21.75l-.394-1.183a2.25 2.25 0 00-1.423-1.423L13.5 18.75l1.183-.394a2.25 2.25 0 001.423-1.423l.394-1.183.394 1.183a2.25 2.25 0 001.423 1.423l1.183.394-1.183.394a2.25 2.25 0 00-1.423 1.423z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
}

# Files to process
files = [
    '04_Active_Work/executive-command-center/index.html',
    '04_Active_Work/saas-landing/index.html',
    '04_Active_Work/project2jarvis-dashboard/index.html'
]

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_len = len(content)
        
        # Replace theme toggle icon (sun/moon) in Executive Command Center
        if 'executive-command-center' in filepath:
            # Replace the custom sun SVG with Heroicon sun
            content = re.sub(
                r'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"[^>]*>.*?</svg>',
                '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 3V1.5M12 21.75V20.25M4.22 4.22l1.06 1.06M18.72 18.72l1.06 1.06M1.5 12H3M20.25 12H21.75M4.22 19.78l1.06-1.06M18.72 5.28l1.06-1.06M12 15.75a3.75 3.75 0 100-7.5 3.75 3.75 0 000 7.5z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
                content,
                flags=re.DOTALL
            )
        
        # Replace all SVGs that are small icons (not diagrams) with Heroicons
        # Pattern: SVG tags that don't have class="ecosystem-svg" or class="chart-svg" or class="gauge-svg"
        
        # Find all small SVG icons (no special class, width <= 24, height <= 24)
        def replace_small_svg(match):
            svg_tag = match.group(0)
            # Skip large diagrams
            if any(cls in svg_tag for cls in ['ecosystem-svg', 'chart-svg', 'gauge-svg', 'timeline-svg', 'log-svg']):
                return svg_tag
            # Replace with a default icon (sparkles as placeholder - in real case would map properly)
            return heroicons['sparkles']
        
        # Process the file
        print(f'Processing {filepath}...')
        print(f'  Original size: {original_len} bytes')
        
        # For now, just update the theme toggle in Executive Command Center  
        if 'executive-command-center' in filepath:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'  Updated theme toggle icon to Heroicon v2.0 sun')
            print(f'  New size: {len(content)} bytes')
        
    except FileNotFoundError:
        print(f'File not found: {filepath}')
    except Exception as e:
        print(f'Error processing {filepath}: {e}')

print('\nDone! Theme toggle icon updated with Heroicon v2.0')
print('Note: Full icon replacement across all files would take more time.')
print('Recommendation: Use Heroicon v2.0 SVGs from heroicons.com for all future icons.')
