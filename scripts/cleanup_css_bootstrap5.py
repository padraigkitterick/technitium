#!/usr/bin/env python3
"""
CSS Cleanup for Bootstrap 5

This script removes custom CSS that's now redundant with Bootstrap 5,
while keeping app-specific components and CSS variables.
"""

import re

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def remove_spacing_utilities(css):
    """Remove custom spacing utilities (Bootstrap 5 has comprehensive spacing)."""
    
    # Remove margin/padding utility classes
    patterns = [
        r'\.m[tblrxy]?-\d+\s*\{[^}]+\}\s*',
        r'\.p[tblrxy]?-\d+\s*\{[^}]+\}\s*',
    ]
    
    removed_count = 0
    for pattern in patterns:
        matches = re.findall(pattern, css)
        removed_count += len(matches)
        css = re.sub(pattern, '', css)
    
    return css, removed_count

def remove_display_utilities(css):
    """Remove display utilities that Bootstrap 5 provides."""
    
    # Keep .d-inline as it's used 81 times and is in Bootstrap 5 anyway
    # Remove redundant definitions
    patterns = [
        r'\.d-block\s*\{\s*display:\s*block;\s*\}\s*',
        r'\.d-inline-block\s*\{\s*display:\s*inline-block;\s*\}\s*',
        r'\.d-flex\s*\{\s*display:\s*flex;\s*\}\s*',
        r'\.d-none\s*\{\s*display:\s*none;\s*\}\s*',
    ]
    
    removed_count = 0
    for pattern in patterns:
        matches = re.findall(pattern, css)
        removed_count += len(matches)
        css = re.sub(pattern, '', css)
    
    return css, removed_count

def remove_text_utilities(css):
    """Remove text utilities Bootstrap 5 provides."""
    
    patterns = [
        r'\.text-(?:start|center|end|left|right)\s*\{[^}]+\}\s*',
        r'\.text-(?:uppercase|lowercase|capitalize)\s*\{[^}]+\}\s*',
        r'\.text-muted\s*\{[^}]+\}\s*',
    ]
    
    removed_count = 0
    for pattern in patterns:
        matches = re.findall(pattern, css)
        removed_count += len(matches)
        css = re.sub(pattern, '', css)
    
    return css, removed_count

def remove_flex_utilities(css):
    """Remove flex utilities Bootstrap 5 provides."""
    
    patterns = [
        r'\.flex-(?:row|column|wrap|nowrap)\s*\{[^}]+\}\s*',
        r'\.justify-(?:start|center|end|between|around)\s*\{[^}]+\}\s*',
        r'\.align-(?:start|center|end|stretch)\s*\{[^}]+\}\s*',
        r'\.align-items-center\s*\{[^}]+\}\s*',
        r'\.align-center\s*\{[^}]+\}\s*',
        r'\.justify-between\s*\{[^}]+\}\s*',
    ]
    
    removed_count = 0
    for pattern in patterns:
        matches = re.findall(pattern, css)
        removed_count += len(matches)
        css = re.sub(pattern, '', css)
    
    return css, removed_count

def remove_width_height_percentages(css):
    """Remove percentage-based width/height (Bootstrap 5 has .w-25, .w-50, .w-75, .w-100)."""
    
    patterns = [
        r'\.w-(?:25|50|75|100)pct\s*\{[^}]+\}\s*',
        r'\.w-auto\s*\{\s*width:\s*auto;\s*\}\s*',
        r'\.w-full\s*\{\s*width:\s*100%;\s*\}\s*',
        r'\.h-(?:25|50|75|100)\s*\{[^}]+\}\s*',
    ]
    
    removed_count = 0
    for pattern in patterns:
        matches = re.findall(pattern, css)
        removed_count += len(matches)
        css = re.sub(pattern, '', css)
    
    return css, removed_count

def remove_border_utilities(css):
    """Remove border utilities Bootstrap 5 provides."""
    
    patterns = [
        r'\.border-0\s*\{[^}]+\}\s*',
        r'\.rounded\s*\{[^}]+\}\s*',
        r'\.rounded-(?:sm|md|lg)\s*\{[^}]+\}\s*',
    ]
    
    removed_count = 0
    for pattern in patterns:
        matches = re.findall(pattern, css)
        removed_count += len(matches)
        css = re.sub(pattern, '', css)
    
    return css, removed_count

def remove_color_utilities(css):
    """Remove color utilities if they're basic (Bootstrap 5 has comprehensive colors)."""
    
    patterns = [
        r'\.bg-white\s*\{\s*background-color:\s*white;\s*\}\s*',
        r'\.text-white\s*\{\s*color:\s*white;\s*\}\s*',
        r'\.text-black\s*\{\s*color:\s*black;\s*\}\s*',
    ]
    
    removed_count = 0
    for pattern in patterns:
        matches = re.findall(pattern, css)
        removed_count += len(matches)
        css = re.sub(pattern, '', css)
    
    return css, removed_count

def add_bootstrap5_note(css):
    """Add note about Bootstrap 5 at the top of refactored section."""
    
    bootstrap5_note = '''

/* ============================================
   NOTE: Now Using Bootstrap 5.3.3 from CDN
   ============================================
   
   Bootstrap 5 provides extensive utility classes:
   
   Spacing: .m-{0-5}, .mt-*, .mb-*, .ms-*, .me-*, .mx-*, .my-*
            .p-{0-5}, .pt-*, .pb-*, .ps-*, .pe-*, .px-*, .py-*
   
   Display: .d-none, .d-block, .d-inline, .d-inline-block, .d-flex, .d-grid
   
   Flexbox: .d-flex, .flex-row, .flex-column, .flex-wrap
            .justify-content-{start|center|end|between|around}
            .align-items-{start|center|end|stretch}
   
   Sizing:  .w-{25|50|75|100}, .h-{25|50|75|100}, .w-auto, .h-auto
            .mw-100, .mh-100, .vw-100, .vh-100
   
   Text:    .text-{start|center|end}, .text-{uppercase|lowercase|capitalize}
            .fw-{normal|bold|bolder|light}, .fs-{1-6}
            .text-{primary|secondary|success|danger|warning|info|light|dark|muted}
   
   Colors:  .bg-{primary|secondary|success|danger|warning|info|light|dark}
            .text-bg-{color} for colored backgrounds with contrasting text
   
   Borders: .border, .border-{top|end|bottom|start}, .border-{0-5}
            .rounded, .rounded-{top|end|bottom|start|circle|pill}
   
   Position: .position-{static|relative|absolute|fixed|sticky}
             .top-{0|50|100}, .bottom-*, .start-*, .end-*
   
   Shadows: .shadow, .shadow-sm, .shadow-lg
   
   Custom CSS below is for:
   - CSS Variables (theming)
   - Application-specific components
   - Dark mode overrides
   - Styles not in Bootstrap 5
   ============================================ */
'''
    
    # Insert before first class definition after variables
    pattern = r'(/\* Display & Visibility \*/)'
    if re.search(pattern, css):
        css = re.sub(pattern, bootstrap5_note + '\n' + r'\1', css)
    
    return css

def main():
    css_path = '/home/runner/work/technitium/technitium/DnsServerCore/www/css/main.css'
    
    print("=" * 70)
    print("CSS Cleanup for Bootstrap 5")
    print("=" * 70)
    
    print("\nReading CSS...")
    css = read_file(css_path)
    original_lines = css.count('\n')
    
    print(f"Original: {original_lines} lines\n")
    
    print("Removing redundant utilities...")
    
    css, spacing_removed = remove_spacing_utilities(css)
    print(f"  Spacing utilities: {spacing_removed} removed")
    
    css, display_removed = remove_display_utilities(css)
    print(f"  Display utilities: {display_removed} removed")
    
    css, text_removed = remove_text_utilities(css)
    print(f"  Text utilities: {text_removed} removed")
    
    css, flex_removed = remove_flex_utilities(css)
    print(f"  Flex utilities: {flex_removed} removed")
    
    css, sizing_removed = remove_width_height_percentages(css)
    print(f"  Sizing utilities: {sizing_removed} removed")
    
    css, border_removed = remove_border_utilities(css)
    print(f"  Border utilities: {border_removed} removed")
    
    css, color_removed = remove_color_utilities(css)
    print(f"  Color utilities: {color_removed} removed")
    
    print("\nAdding Bootstrap 5 reference note...")
    css = add_bootstrap5_note(css)
    
    # Clean up multiple blank lines
    css = re.sub(r'\n{4,}', '\n\n\n', css)
    
    print("\nWriting cleaned CSS...")
    write_file(css_path, css)
    
    final_lines = css.count('\n')
    removed_lines = original_lines - final_lines
    reduction_pct = (removed_lines / original_lines) * 100
    
    print(f"\n{'=' * 70}")
    print("Cleanup Complete")
    print(f"{'=' * 70}")
    print(f"Original:  {original_lines} lines")
    print(f"Final:     {final_lines} lines")
    print(f"Removed:   {removed_lines} lines ({reduction_pct:.1f}% reduction)")
    print(f"\nTotal utilities removed: {spacing_removed + display_removed + text_removed + flex_removed + sizing_removed + border_removed + color_removed}")
    print("\nRemaining CSS:")
    print("  - CSS Variables for theming")
    print("  - Application-specific components")
    print("  - Dark mode overrides")
    print("  - Custom layouts and styles")
    print(f"{'=' * 70}")

if __name__ == '__main__':
    main()
