#!/usr/bin/env python3
"""
Bootstrap 5 Migration Script - Uses CDN links

This script migrates HTML from Bootstrap 3 to Bootstrap 5,
updates class names, data attributes, and converts custom spacing
to Bootstrap 5 utilities.
"""

import re

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def update_bootstrap_cdn_links(html):
    """Replace local Bootstrap 3 files with Bootstrap 5 CDN links."""
    
    # Replace Bootstrap 3 CSS with Bootstrap 5 CDN
    html = re.sub(
        r'<link href="css/bootstrap\.min\.css" rel="stylesheet">',
        '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">',
        html
    )
    
    # Replace Bootstrap 3 JS with Bootstrap 5 bundle CDN
    html = re.sub(
        r'<script src="js/bootstrap\.min\.js"></script>',
        '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>',
        html
    )
    
    return html

def migrate_html_classes(html):
    """Update Bootstrap 3 classes to Bootstrap 5 equivalents."""
    
    replacements = {
        # Float utilities (Bootstrap 5 uses start/end for RTL support)
        r'\bpull-left\b': 'float-start',
        r'\bpull-right\b': 'float-end',
        
        # Visibility
        r'\bhidden\b': 'd-none',
        
        # Text alignment
        r'\btext-left\b': 'text-start',
        r'\btext-right\b': 'text-end',
        
        # Buttons
        r'\bbtn-default\b': 'btn-secondary',
        r'\bbtn-xs\b': 'btn-sm',
        
        # Forms
        r'\bcontrol-label\b': 'form-label',
        r'\bhelp-block\b': 'form-text',
        r'\binput-group-addon\b': 'input-group-text',
    }
    
    changes = {}
    for pattern, replacement in replacements.items():
        matches = len(re.findall(pattern, html))
        if matches > 0:
            html = re.sub(pattern, replacement, html)
            changes[pattern] = (replacement, matches)
    
    return html, changes

def migrate_data_attributes(html):
    """Update Bootstrap 3 data attributes to Bootstrap 5."""
    
    replacements = [
        ('data-toggle=', 'data-bs-toggle='),
        ('data-target=', 'data-bs-target='),
        ('data-dismiss=', 'data-bs-dismiss='),
        ('data-parent=', 'data-bs-parent='),
        ('data-slide=', 'data-bs-slide='),
        ('data-slide-to=', 'data-bs-slide-to='),
    ]
    
    changes = {}
    for old, new in replacements:
        count = html.count(old)
        if count > 0:
            html = html.replace(old, new)
            changes[old] = (new, count)
    
    return html, changes

def convert_spacing_to_bootstrap5(html):
    """Convert custom spacing classes to Bootstrap 5 equivalents."""
    
    # Bootstrap 5 spacing scale (0-5): 0, 0.25rem, 0.5rem, 1rem, 1.5rem, 3rem
    spacing_map = {
        # Margin
        'mt-5': 'mt-2', 'mt-10': 'mt-3', 'mt-15': 'mt-4', 'mt-20': 'mt-4',
        'mb-4': 'mb-2', 'mb-5': 'mb-2', 'mb-6': 'mb-2', 'mb-8': 'mb-3', 
        'mb-10': 'mb-3', 'mb-15': 'mb-4',
        'ml-8': 'ms-3', 'ml-10': 'ms-3',
        'mr-10': 'me-3', 'mr-15': 'me-4',
        'mx-10': 'mx-3', 'my-6': 'my-2',
        
        # Padding
        'p-2': 'p-1', 'p-4': 'p-2', 'p-6': 'p-2', 'p-8': 'p-3', 'p-10': 'p-3',
        'pt-4': 'pt-2', 'pt-5': 'pt-2', 'pt-6': 'pt-2', 'pt-10': 'pt-3', 'pt-15': 'pt-4',
        'pb-10': 'pb-3', 'pb-15': 'pb-4',
        'pl-6': 'ps-2', 'pl-8': 'ps-3', 'pl-20': 'ps-4',
        'pr-6': 'pe-2', 'pr-20': 'pe-4',
        'px-20': 'px-4', 'py-6': 'py-2',
    }
    
    changes = {}
    for old, new in spacing_map.items():
        pattern = r'\b' + re.escape(old) + r'\b'
        matches = len(re.findall(pattern, html))
        if matches > 0:
            html = re.sub(pattern, new, html)
            changes[old] = (new, matches)
    
    return html, changes

def main():
    html_path = '/home/runner/work/technitium/technitium/DnsServerCore/www/index.html'
    
    print("=" * 70)
    print("Bootstrap 5 Migration (CDN)")
    print("=" * 70)
    
    print("\nReading HTML...")
    html = read_file(html_path)
    
    print("\n1. Updating Bootstrap links to CDN...")
    html = update_bootstrap_cdn_links(html)
    print("   ✓ Bootstrap 5.3.3 CDN links added")
    
    print("\n2. Migrating class names...")
    html, class_changes = migrate_html_classes(html)
    for pattern, (replacement, count) in sorted(class_changes.items()):
        print(f"   {pattern:30} → {replacement:25} ({count:3}x)")
    
    print("\n3. Migrating data attributes...")
    html, data_changes = migrate_data_attributes(html)
    for old, (new, count) in sorted(data_changes.items()):
        print(f"   {old:30} → {new:25} ({count:3}x)")
    
    print("\n4. Converting spacing utilities...")
    html, spacing_changes = convert_spacing_to_bootstrap5(html)
    shown = 0
    for old, (new, count) in sorted(spacing_changes.items()):
        if shown < 15:
            print(f"   {old:30} → {new:25} ({count:3}x)")
            shown += 1
    if len(spacing_changes) > 15:
        print(f"   ... and {len(spacing_changes) - 15} more")
    
    print("\n5. Writing updated HTML...")
    write_file(html_path, html)
    print(f"   ✓ {html_path}")
    
    total = (sum(c for _, c in class_changes.values()) + 
             sum(c for _, c in data_changes.values()) +
             sum(c for _, c in spacing_changes.values()))
    
    print("\n" + "=" * 70)
    print(f"Migration Complete: {total} total changes")
    print("=" * 70)
    print("\nBootstrap 5.3.3 CDN now active!")
    print("Next: Run cleanup script to remove redundant custom CSS")

if __name__ == '__main__':
    main()
