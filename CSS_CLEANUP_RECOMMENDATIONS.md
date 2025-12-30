# CSS Cleanup & Bootstrap 5 Migration Recommendations

## Summary of Changes Made

### Removed Unused Definitions (105 total lines)
- **26 unused CSS variables** (colors, spacing, typography)
- **6 unused class definitions** (.w-170, .w-200, .w-240, and incomplete selectors)
- **9 generic utility classes** replaced with Bootstrap 5 equivalents

### HTML Migrations (9 replacements)
- `util-5` → `mb-0 mt-3 pt-3`
- `util-6` → `mb-4`
- `util-7` → `me-3`
- `util-8` → `mt-3 mb-0`
- `util-11` → `mt-2 fw-bold`
- `util-22` → `pb-2`
- `util-23` → `pt-3`
- `util-24` → `pt-2 ps-4 mb-3`
- `util-31` → `text-start`

### Results
- **CSS reduced**: 1,098 → 959 lines (-139 lines, 12.7% reduction)
- All unused classes and variables removed
- Generic utility classes replaced with semantic Bootstrap 5 classes

---

## Recommendations for Further Bootstrap 5 Adoption

### 1. Custom Width Classes (22 classes, 169 usages)

Many custom fixed-width classes could potentially use responsive alternatives:

#### High Usage (Consider Keeping)
- `.w-100` (99x) - 6.25rem / 100px - **Keep**: Widely used for buttons
- `.w-780` (13x) - 48.75rem / 780px - **Keep**: Specific layout width
- `.w-940` (4x) - 58.75rem / 940px - **Keep**: Specific layout width

#### Medium Usage (Evaluate Case-by-Case)
- `.w-36` (17x) - 2.25rem / 36px - Small icon/button width
- `.w-84` (9x) - 5.25rem / 84px - Compact button width
- `.w-65` (6x) - 4.0625rem / 65px - Compact element width
- `.w-80` (4x) - 5rem / 80px - Small button width

#### Low Usage (Consider Bootstrap Alternatives)
- `.w-300` (3x) - Could use inline styles or component-specific classes
- `.w-150`, `.w-120`, `.w-96`, `.w-76` (2x each) - Specific sizing, evaluate if needed
- `.w-130`, `.w-240`, `.w-750`, `.w-800`, `.w-90`, `.w-94`, `.w-95` (1x each) - **Candidate for removal**: Consider inline styles or Bootstrap sizing

**Recommendation**: Keep high and medium usage classes as they represent consistent sizing patterns. For low usage (<3x), consider:
- Using inline styles for one-off sizes
- Using Bootstrap's `.w-25`, `.w-50`, `.w-75`, `.w-100` with custom widths only when necessary
- Creating component-specific classes (e.g., `.btn-icon-sm { width: 2.25rem; }`)

### 2. Custom Height Classes (7 classes, 31 usages)

#### Keep These (Consistent Sizing)
- `.h-500` (12x) - 31.25rem / 500px - Large container height
- `.h-350` (10x) - 21.875rem / 350px - Medium container height
- `.h-400` (6x) - 25rem / 400px - Container height
- `.h-300` (2x) - 18.75rem / 300px - Small container height

#### Consider Alternatives
- `.h-38` (1x) - 2.375rem / 38px - **Could use**: `.h-auto` or component-specific styling
- `.h-auto` (2x) - **Keep**: Useful utility

**Recommendation**: Keep all height classes as they represent consistent container sizing patterns for the application's data viewers (logs, zones, etc.).

### 3. Remaining Generic Utility Classes (3 classes)

#### Can Be Replaced with Bootstrap 5
- `.util-13` (1x) - `max-height: 31.25rem;` → Could use `.mh-100` or inline style
- `.util-14` (1x) - `max-height: 31.25rem; overflow-y: auto;` → Use `.mh-100 overflow-auto`
- `.util-15` (1x) - `max-height: 31.25rem; overflow-y: auto; display: none;` → Use `.mh-100 overflow-auto d-none`

**Recommendation**: Replace these 3 remaining util classes with Bootstrap 5 utilities.

### 4. Rarely Used Custom Classes (72 classes used 1-2 times)

Many custom classes are used only once or twice. These are good candidates for:

#### Application-Specific Component Classes (Keep)
These represent specific UI components and should be kept:
- `.stats-panel`, `.zone-stats-panel` - Stats display components
- `.log-list-pane`, `.log-viewer-pane` - Log viewer UI
- `.panel-filter-form` - Form styling
- `.menu`, `.menu-title` - Navigation
- `.pageLogin`, `.page` - Page layouts
- `.container` - Main container (unless using Bootstrap's `.container`)

#### Status/State Classes (Keep)
These provide semantic meaning and should be kept:
- `.cache-hit`, `.auth-hit` - Cache status indicators
- `.server-failure`, `.nxdomain`, `.refused`, `.blocked`, `.dropped` - DNS query status
- `.no-error` - Success state
- `.total-queries`, `.clients`, `.recursions` - Stats categories

#### Utility Classes (Consider Bootstrap Alternatives)
- `.no-text-decoration` (1x) → Bootstrap: `.text-decoration-none`
- `.text-danger-important` (1x) → Bootstrap: `.text-danger` (use `!important` in HTML if needed)
- `.wrap-anywhere` (1x), `.wrap-normal-break-normal` (1x) → Consider Bootstrap text utilities or inline styles
- `.overflow-y-scroll` (1x) → Bootstrap: `.overflow-auto` or `.overflow-scroll`

#### One-Off Spacing/Sizing (Consider Inline or Bootstrap)
Classes like these are used once and could be replaced:
- `.p-0-15`, `.p-0-25`, `.p-40-0-20-0`, `.p-0-6-0-0-m-10-0-0-0` → Complex padding, consider component-specific or inline
- `.m--6-0-0--12`, `.max-w-800-m-0-auto-10-auto` → Complex margin, consider component-specific or inline
- `.min-w-*` classes (100, 120, 170, 200, 240, 295, 300) → Consider inline `style="min-width: X"` for one-offs

**Recommendation**: 
1. Keep component and state classes (they provide semantic meaning)
2. Replace utility classes with Bootstrap equivalents
3. For one-off complex spacing/sizing, consider:
   - Moving to component-specific classes if they're part of a component
   - Using inline styles for truly one-off cases
   - Simplifying to use Bootstrap spacing utilities where possible

### 5. CSS Variables Review

#### Currently Used Variables (Good to keep)
- `--color-primary` - Primary theme color
- `--gray-500` - Grayscale palette
- `--space-*` (2, 3, 4, 5, 7, 9) - Spacing scale (partially used)
- `--font-md` - Typography scale
- `--container-max` - Layout dimensions
- `--header-height`, `--footer-height` - Component dimensions
- `--bg-body` - Background colors

#### Removed (Were Unused)
All unused variables have been removed in this cleanup.

**Recommendation**: The remaining CSS variables are well-utilized and should be kept for theming and consistency.

---

## Implementation Priority

### High Priority (Do Now)
1. ✅ **Done**: Remove unused CSS variables (26 removed)
2. ✅ **Done**: Remove unused class definitions (6 removed)
3. ✅ **Done**: Replace generic util-* classes with Bootstrap 5 (9 replaced)
4. **Next**: Replace remaining 3 util classes (util-13, util-14, util-15)
5. **Next**: Replace `.no-text-decoration` → `.text-decoration-none`

### Medium Priority (Consider)
1. Review one-off complex spacing classes (p-0-15, m--6-0-0--12, etc.)
2. Consolidate min-w-* classes (8 classes for one-off cases)
3. Consider if `.container` should use Bootstrap's `.container` or `.container-fluid`

### Low Priority (Optional)
1. Evaluate rarely-used width classes (w-90, w-94, w-95, etc.) for inline styles
2. Consider component-based organization for page-specific styles
3. Review if any app-specific components could use Bootstrap card/panel components

---

## Migration Strategy

### For One-Off Classes (Used 1x)
```html
<!-- Before: Custom class -->
<div class="p-0-15">...</div>

<!-- After: Bootstrap utilities -->
<div class="p-0 pe-3">...</div>

<!-- Or: Inline style for truly one-off cases -->
<div style="padding: 0 15px;">...</div>
```

### For Component-Specific Styling
```css
/* Before: Generic utility */
.util-13 { max-height: 31.25rem; }

/* After: Component-specific class */
.log-viewer-content { max-height: 31.25rem; }
```

### For Bootstrap Equivalents
```html
<!-- Before: Custom utility -->
<div class="no-text-decoration">

<!-- After: Bootstrap utility -->
<div class="text-decoration-none">
```

---

## Summary

**Current State After Cleanup:**
- CSS: 959 lines (down from 1,098, -12.7%)
- No unused variables or classes
- Most generic utilities replaced with Bootstrap 5

**Remaining Custom CSS Breakdown:**
- ~60 lines: CSS variables (theming)
- ~600-700 lines: Application components (stats, zones, logs, DHCP, etc.)
- ~150 lines: Custom responsive behaviors
- ~150 lines: Width/height utilities (mostly high usage)

**Next Steps:**
1. Replace final 3 util classes with Bootstrap
2. Consider replacing rarely-used utilities with Bootstrap or inline styles
3. Keep all application-specific component styling (appropriate to have custom CSS for app features)

The codebase now has minimal, focused custom CSS that supports the application's specific needs while maximizing Bootstrap 5 utility usage.
