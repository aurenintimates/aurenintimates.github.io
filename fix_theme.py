content = open(r'C:\Users\Administrator\WorkBuddy\2026-06-15-08-19-47\website\index.html', 'r', encoding='utf-8').read()

# Product card
content = content.replace('rgba(255,255,255,0.07)', 'rgba(0,0,0,0.08)')
content = content.replace('rgba(255,255,255,0.012)', '#ffffff')
content = content.replace(
    'border-color: rgba(201,169,110,0.25); transform: translateY(-3px);',
    'border-color: rgba(201,169,110,0.4); box-shadow: 0 4px 16px rgba(0,0,0,0.08); transform: translateY(-3px);'
)
content = content.replace('rgba(255,255,255,0.06)', 'rgba(0,0,0,0.06)')
content = content.replace('rgba(255,255,255,0.4)', 'rgba(0,0,0,0.25)')
content = content.replace('rgba(255,255,255,0.7)', 'rgba(0,0,0,0.5)')
content = content.replace('color: #f0ece5;', 'color: #1a1a1a;')

# Product info specs
old_specs = 'color: #999;\n  background: rgba(255,255,255,0.04)'
new_specs = 'color: #666;\n  background: rgba(0,0,0,0.03)'
content = content.replace(old_specs, new_specs)

content = content.replace('rgba(255,255,255,0.06)">', 'rgba(0,0,0,0.06)">')
content = content.replace('rgba(255,255,255,0.15)">', 'rgba(0,0,0,0.12)">')

# Size section
content = content.replace(
    'background: rgba(255,255,255,0.012); border-top: 1px solid rgba(255,255,255,0.05); border-bottom: 1px solid rgba(255,255,255,0.05);',
    'background: #f8f8f5; border-top: 1px solid rgba(0,0,0,0.06); border-bottom: 1px solid rgba(0,0,0,0.06);'
)
content = content.replace(
    'color: #ccc; border-bottom: 1px solid rgba(255,255,255,0.05);',
    'color: #555; border-bottom: 1px solid rgba(0,0,0,0.06);'
)
content = content.replace('background: rgba(255,255,255,0.02);', 'background: rgba(0,0,0,0.02);')

# Contact
content = content.replace('color: #ccc; }', 'color: #333; }')
content = content.replace(
    'background: rgba(255,255,255,0.04);\n  border: 1px solid rgba(255,255,255,0.12)',
    'background: rgba(0,0,0,0.03);\n  border: 1px solid rgba(0,0,0,0.12)'
)
content = content.replace('color: #e0dcd5;', 'color: #333;')

# Footer
content = content.replace(
    'border-top: 1px solid rgba(255,255,255,0.05);\n  color: #555;',
    'border-top: 1px solid rgba(0,0,0,0.08);\n  color: #999;'
)

open(r'C:\Users\Administrator\WorkBuddy\2026-06-15-08-19-47\website\index.html', 'w', encoding='utf-8').write(content)
print('Done! All dark theme values replaced.')
