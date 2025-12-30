#!/usr/bin/env python3
"""
Phase 2: Further Bootstrap 5 Migration
Removes overly-specific custom classes in favor of Bootstrap 5 defaults
"""

import re

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def migrate_typography(html, css):
    """Replace custom typography with Bootstrap 5 equivalents."""
    
    replacements = {
        'text-lg-bold': 'fs-5 fw-bold',
        'text-xs-bold': 'fs-6 fw-bold',
        'text-lg': 'fs-5',
        'text-xl': 'fs-4',
        'text-sm': 'fs-6',
        'text-xs': 'fs-6',
        'font-bold': 'fw-bold',
        'label-bold': 'fw-bold',
    }
    
    changes = {}
    for old, new in replacements.items():
        pattern = r'\b' + re.escape(old) + r'\b'
        count = len(re.findall(pattern, html))
        if count > 0:
            html = re.sub(pattern, new, html)
            changes[old] = (new, count)
            
            # Remove from CSS
            css_pattern = r'\.' + re.escape(old) + r'\s*\{[^}]+\}\s*\n?'
            css = re.sub(css_pattern, '', css)
    
    return html, css, changes

def migrate_buttons(html, css):
    """Replace custom button classes with Bootstrap 5 equivalents."""
    
    replacements = {
        'btn-narrow': 'btn-sm px-2',
        'btn-narrow-alt': 'btn-sm px-2',
        'btn-narrow-120': 'btn-sm',
        'btn-narrow-170': 'btn-sm',
        'btn-compact': 'btn-sm p-1',
    }
    
    changes = {}
    for old, new in replacements.items():
        pattern = r'\b' + re.escape(old) + r'\b'
        count = len(re.findall(pattern, html))
        if count > 0:
            html = re.sub(pattern, new, html)
            changes[old] = (new, count)
            
            # Remove from CSS
            css_pattern = r'\.' + re.escape(old) + r'[,\s]*\{[^}]+\}\s*\n?'
            css = re.sub(css_pattern, '', css)
            
            # Also remove if it's grouped with others
            css = re.sub(r'\.' + re.escape(old) + r',\s*\n?', '', css)
            css = re.sub(r',\s*\.' + re.escape(old) + r'\b', '', css)
    
    return html, css, changes

def migrate_columns(html, css):
    """Replace custom column classes with Bootstrap 5 utilities."""
    
    replacements = {
        'col-left-50': 'float-start w-50 pe-2',
        'col-right-50': 'float-end w-50 ps-2',
    }
    
    changes = {}
    for old, new in replacements.items():
        pattern = r'\b' + re.escape(old) + r'\b'
        count = len(re.findall(pattern, html))
        if count > 0:
            html = re.sub(pattern, new, html)
            changes[old] = (new, count)
            
            # Remove from CSS
            css_pattern = r'\.' + re.escape(old) + r'\s*\{[^}]+\}\s*\n?'
            css = re.sub(css_pattern, '', css)
    
    return html, css, changes

def migrate_backgrounds(html, css):
    """Replace custom background classes with Bootstrap 5 equivalents."""
    
    replacements = {
        'bg-lighter': 'bg-light bg-opacity-50',
    }
    
    changes = {}
    for old, new in replacements.items():
        pattern = r'\b' + re.escape(old) + r'\b'
        count = len(re.findall(pattern, html))
        if count > 0:
            html = re.sub(pattern, new, html)
            changes[old] = (new, count)
            
            # Remove from CSS
            css_pattern = r'\.' + re.escape(old) + r'\s*\{[^}]+\}\s*\n?'
            css = re.sub(css_pattern, '', css)
    
    return html, css, changes

def migrate_padding(html, css):
    """Replace custom padding classes with Bootstrap 5 equivalents."""
    
    replacements = {
        'p-2-6': 'p-2',
        'p-4-0': 'px-2 py-0',
        'p-6-0': 'px-3 py-0',
    }
    
    changes = {}
    for old, new in replacements.items():
        pattern = r'\b' + re.escape(old) + r'\b'
        count = len(re.findall(pattern, html))
        if count > 0:
            html = re.sub(pattern, new, html)
            changes[old] = (new, count)
            
            # Remove from CSS
            css_pattern = r'\.' + re.escape(old) + r'\s*\{[^}]+\}\s*\n?'
            css = re.sub(css_pattern, '', css)
    
    return html, css, changes

def remove_unused_classes(css, html):
    """Remove CSS classes that are no longer used in HTML."""
    
    # Find all class definitions in CSS
    class_pattern = r'\.([a-zA-Z0-9_-]+)\s*(?:[,{])'
    css_classes = set(re.findall(class_pattern, css))
    
    removed = []
    for cls in css_classes:
        # Skip pseudo-classes and special selectors
        if ':' in cls or '>' in cls or '+' in cls:
            continue
            
        # Check if used in HTML
        if not re.search(r'\b' + re.escape(cls) + r'\b', html):
            # Remove this class definition
            pattern = r'\.' + re.escape(cls) + r'\s*\{[^}]+\}\s*\n?'
            if re.search(pattern, css):
                css = re.sub(pattern, '', css)
                removed.append(cls)
    
    return css, removed

def main():
    html_path = '/home/runner/work/technitium/technitium/DnsServerCore/www/index.html'
    css_path = '/home/runner/work/technitium/technitium/DnsServerCore/www/css/main.css'
    
    print("=" * 80)
    print("Phase 2: Further Bootstrap 5 Migration")
    print("Removing overly-specific custom classes")
    print("=" * 80)
    
    html = read_file(html_path)
    css = read_file(css_path)
    
    original_css_lines = css.count('\n')
    
    # Migrate typography
    print("\n1. Migrating typography classes...")
    html, css, typo_changes = migrate_typography(html, css)
    for old, (new, count) in sorted(typo_changes.items()):
        print(f"   {old:25} → {new:25} ({count:3}x)")
    
    # Migrate buttons
    print("\n2. Migrating button classes...")
    html, css, btn_changes = migrate_buttons(html, css)
    for old, (new, count) in sorted(btn_changes.items()):
        print(f"   {old:25} → {new:25} ({count:3}x)")
    
    # Migrate columns
    print("\n3. Migrating column layout classes...")
    html, css, col_changes = migrate_columns(html, css)
    for old, (new, count) in sorted(col_changes.items()):
        print(f"   {old:25} → {new:25} ({count:3}x)")
    
    # Migrate backgrounds
    print("\n4. Migrating background classes...")
    html, css, bg_changes = migrate_backgrounds(html, css)
    for old, (new, count) in sorted(bg_changes.items()):
        print(f"   {old:25} → {new:25} ({count:3}x)")
    
    # Migrate padding
    print("\n5. Migrating padding classes...")
    html, css, pad_changes = migrate_padding(html, css)
    for old, (new, count) in sorted(pad_changes.items()):
        print(f"   {old:25} → {new:25} ({count:3}x)")
    
    # Clean up extra whitespace
    css = re.sub(r'\n{3,}', '\n\n', css)
    
    # Remove unused classes
    print("\n6. Removing unused CSS classes...")
    css, removed = remove_unused_classes(css, html)
    if removed[:5]:
        for cls in removed[:5]:
            print(f"   Removed: .{cls}")
        if len(removed) > 5:
            print(f"   ... and {len(removed) - 5} more")
    
    # Write files
    print("\n7. Writing updated files...")
    write_file(html_path, html)
    write_file(css_path, css)
    
    final_css_lines = css.count('\n')
    removed_lines = original_css_lines - final_css_lines
    
    total_changes = (
        sum(c for _, c in typo_changes.values()) +
        sum(c for _, c in btn_changes.values()) +
        sum(c for _, c in col_changes.values()) +
        sum(c for _, c in bg_changes.values()) +
        sum(c for _, c in pad_changes.values())
    )
    
    print("\n" + "=" * 80)
    print("Migration Complete")
    print("=" * 80)
    print(f"Total HTML changes: {total_changes}")
    print(f"CSS lines: {original_css_lines} → {final_css_lines} (-{removed_lines})")
    print(f"Unused classes removed: {len(removed)}")
    print("\nNow using Bootstrap 5 defaults for:")
    print("  - Typography: .fs-{1-6}, .fw-bold instead of custom sizes")
    print("  - Buttons: .btn-sm, .px-*, .p-* instead of custom button sizes")
    print("  - Layout: .w-{25|50|75|100}, .float-*, .pe-*, .ps-* instead of custom columns")
    print("  - Backgrounds: .bg-opacity-* instead of custom lighter backgrounds")
    print("  - Padding: .p-*, .px-*, .py-* instead of custom combinations")
    print("=" * 80)

if __name__ == '__main__':
    main()
