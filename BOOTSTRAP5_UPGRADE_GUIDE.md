# Bootstrap 5 Upgrade Guide

## Overview

This guide provides a complete migration plan from Bootstrap 3.4.1 to Bootstrap 5.3.3 for the Technitium DNS Server web UI.

## Step 1: Download Bootstrap 5

Download the latest Bootstrap 5 files:

```bash
# Download Bootstrap 5.3.3 CSS (minified)
curl -o DnsServerCore/www/css/bootstrap.min.css https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css

# Download Bootstrap 5.3.3 CSS source map
curl -o DnsServerCore/www/css/bootstrap.min.css.map https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css.map

# Download Bootstrap 5.3.3 JS Bundle (includes Popper.js, no jQuery needed)
curl -o DnsServerCore/www/js/bootstrap.bundle.min.js https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js
```

## Step 2: Update HTML References

### Remove jQuery Dependency (if only used for Bootstrap)

Bootstrap 5 no longer requires jQuery. Check if jQuery is used elsewhere in your JavaScript files.

**If jQuery is NOT used elsewhere:**
```html
<!-- Remove these lines from index.html -->
<script src="js/jquery.min.js"></script>
<script src="js/bootstrap.min.js"></script>

<!-- Replace with Bootstrap 5 bundle -->
<script src="js/bootstrap.bundle.min.js"></script>
```

**If jQuery IS still needed:**
```html
<!-- Keep jQuery -->
<script src="js/jquery.min.js"></script>

<!-- Replace Bootstrap 3 JS with Bootstrap 5 bundle -->
<script src="js/bootstrap.bundle.min.js"></script>
```

## Step 3: Class Name Migrations

### Float Utilities

| Bootstrap 3 | Bootstrap 5 |
|-------------|-------------|
| `.pull-left` | `.float-start` |
| `.pull-right` | `.float-end` |
| `.clearfix` | `.clearfix` (unchanged) |

**Note:** Bootstrap 5 also supports `.float-left` and `.float-right` for backwards compatibility.

### Visibility Utilities

| Bootstrap 3 | Bootstrap 5 |
|-------------|-------------|
| `.hidden` | `.d-none` |
| `.show` | `.d-block` |
| `.visible-xs` | `.d-block .d-sm-none` |
| `.visible-sm` | `.d-none .d-sm-block .d-md-none` |
| `.visible-md` | `.d-none .d-md-block .d-lg-none` |
| `.visible-lg` | `.d-none .d-lg-block` |
| `.hidden-xs` | `.d-none .d-sm-block` |
| `.hidden-sm` | `.d-sm-none .d-md-block` |
| `.hidden-md` | `.d-md-none .d-lg-block` |
| `.hidden-lg` | `.d-lg-none` |

### Text Alignment

| Bootstrap 3 | Bootstrap 5 |
|-------------|-------------|
| `.text-left` | `.text-start` |
| `.text-right` | `.text-end` |
| `.text-center` | `.text-center` (unchanged) |

**Note:** Bootstrap 5 also supports `.text-left` and `.text-right` for backwards compatibility.

### Grid System

The grid system remains largely compatible, but breakpoints have changed:

| Breakpoint | Bootstrap 3 | Bootstrap 5 |
|------------|-------------|-------------|
| Extra small | `<768px` | `<576px` |
| Small | `≥768px` | `≥576px` |
| Medium | `≥992px` | `≥768px` |
| Large | `≥1200px` | `≥992px` |
| Extra large | N/A | `≥1200px` |
| Extra extra large | N/A | `≥1400px` |

Grid classes are compatible but consider reviewing breakpoints:
- `.col-xs-*` → `.col-*` (Bootstrap 5 mobile-first)
- `.col-sm-*` → `.col-sm-*` (unchanged)
- `.col-md-*` → `.col-md-*` (unchanged)
- `.col-lg-*` → `.col-lg-*` (unchanged)
- New: `.col-xl-*`, `.col-xxl-*`

### Button Utilities

| Bootstrap 3 | Bootstrap 5 |
|-------------|-------------|
| `.btn-default` | `.btn-secondary` |
| `.btn-primary` | `.btn-primary` (unchanged) |
| `.btn-success` | `.btn-success` (unchanged) |
| `.btn-info` | `.btn-info` (unchanged) |
| `.btn-warning` | `.btn-warning` (unchanged) |
| `.btn-danger` | `.btn-danger` (unchanged) |
| `.btn-xs` | `.btn-sm` (xs removed) |
| `.btn-sm` | `.btn-sm` (unchanged) |
| `.btn-lg` | `.btn-lg` (unchanged) |

### Form Classes

Most form classes are compatible, with some changes:

| Bootstrap 3 | Bootstrap 5 |
|-------------|-------------|
| `.form-control` | `.form-control` (unchanged) |
| `.form-group` | `.mb-3` (use margin utility) |
| `.control-label` | `.form-label` |
| `.form-horizontal` | Use grid + `.row .mb-3` |
| `.input-group-addon` | `.input-group-text` |
| `.help-block` | `.form-text` |

## Step 4: Leverage Bootstrap 5 Utilities

Bootstrap 5 has extensive utility classes that can replace most custom CSS.

### Spacing Utilities

Replace custom spacing with Bootstrap 5's comprehensive system:

**Custom → Bootstrap 5:**
- `.mt-10` → `.mt-3` or `.mt-4` (use Bootstrap scale: 0-5)
- `.mb-15` → `.mb-4` or `.mb-5`
- `.p-6` → `.p-2` or `.p-3`
- `.px-20` → `.px-4` or `.px-5`

Bootstrap 5 spacing scale (1rem = 16px):
- `.m-0`, `.p-0` = 0
- `.m-1`, `.p-1` = 0.25rem (4px)
- `.m-2`, `.p-2` = 0.5rem (8px)
- `.m-3`, `.p-3` = 1rem (16px)
- `.m-4`, `.p-4` = 1.5rem (24px)
- `.m-5`, `.p-5` = 3rem (48px)

### Display Utilities

Replace custom display utilities:

**Custom → Bootstrap 5:**
- `.d-inline` → `.d-inline` (unchanged)
- `.d-block` → `.d-block` (unchanged)
- `.d-flex` → `.d-flex` (unchanged)
- `.d-none` → `.d-none` (already using)

### Flexbox Utilities

Bootstrap 5 has comprehensive flexbox utilities:

- `.d-flex`
- `.flex-row`, `.flex-column`
- `.justify-content-start`, `.justify-content-center`, `.justify-content-end`, `.justify-content-between`
- `.align-items-start`, `.align-items-center`, `.align-items-end`
- `.flex-wrap`, `.flex-nowrap`
- `.flex-grow-1`, `.flex-shrink-1`

### Width/Height Utilities

Replace custom sizing:

**Custom → Bootstrap 5:**
- `.w-auto` → `.w-auto` (unchanged)
- `.w-100pct` → `.w-100` (100%)
- Custom `.w-*` → Use `.w-25`, `.w-50`, `.w-75`, `.w-100` or custom CSS

Bootstrap 5 sizing:
- `.w-25` = 25%
- `.w-50` = 50%
- `.w-75` = 75%
- `.w-100` = 100%
- `.w-auto` = auto
- `.h-25`, `.h-50`, `.h-75`, `.h-100` for height

### Text Utilities

Bootstrap 5 provides comprehensive text utilities:

- `.text-start`, `.text-center`, `.text-end`
- `.text-lowercase`, `.text-uppercase`, `.text-capitalize`
- `.fw-bold`, `.fw-normal`, `.fw-light`
- `.fs-1` through `.fs-6` (font sizes)
- `.text-muted`, `.text-primary`, `.text-success`, etc.

### Color Utilities

Background and text colors:

- `.bg-primary`, `.bg-secondary`, `.bg-success`, `.bg-danger`, `.bg-warning`, `.bg-info`, `.bg-light`, `.bg-dark`
- `.text-primary`, `.text-secondary`, `.text-success`, `.text-danger`, `.text-warning`, `.text-info`, `.text-light`, `.text-dark`, `.text-muted`

### Border Utilities

- `.border`, `.border-0`, `.border-top`, `.border-end`, `.border-bottom`, `.border-start`
- `.rounded`, `.rounded-0`, `.rounded-circle`, `.rounded-pill`
- `.border-primary`, `.border-secondary`, etc.

### Position Utilities

- `.position-static`, `.position-relative`, `.position-absolute`, `.position-fixed`, `.position-sticky`
- `.top-0`, `.bottom-0`, `.start-0`, `.end-0`

## Step 5: Remove Custom CSS

After migrating to Bootstrap 5 utilities, remove custom CSS that's now redundant:

### Can Be Removed:

1. **Spacing utilities** (`.mt-*`, `.mb-*`, `.p-*`, etc.) → Use Bootstrap 5's spacing
2. **Display utilities** (`.d-block`, `.d-inline`, etc.) → Use Bootstrap 5's display
3. **Float utilities** (already removed `.float-left`, `.float-right`)
4. **Text alignment** (already using Bootstrap)
5. **Width/height utilities** for percentages → Use Bootstrap 5's sizing

### Keep:

1. **CSS Variables** - For theming and dark mode
2. **Application-specific components** (stats panels, zones, logs)
3. **Custom breakpoints** if different from Bootstrap's
4. **Dark mode overrides**
5. **Complex component styling** that Bootstrap doesn't provide

## Step 6: Estimated CSS Reduction

**Current:** 1,575 lines
**After Bootstrap 5 migration:** ~400-600 lines (60-75% reduction)

**What remains:**
- CSS Variables: ~60 lines
- Dark mode overrides: ~150-200 lines
- App-specific components: ~200-300 lines
- Custom layouts: ~50-100 lines

## Step 7: Testing

After migration, test:

1. **All pages load correctly**
2. **Modals work** (Bootstrap 5 uses different JavaScript API)
3. **Dropdowns function** (may need `data-bs-toggle` instead of `data-toggle`)
4. **Forms validate** and display correctly
5. **Grid system** responsive at all breakpoints
6. **Dark mode** still works
7. **All interactive components** (tabs, collapse, tooltips, popovers)

## Step 8: JavaScript API Changes

Bootstrap 5 has a different JavaScript API:

### Data Attributes

| Bootstrap 3 | Bootstrap 5 |
|-------------|-------------|
| `data-toggle` | `data-bs-toggle` |
| `data-target` | `data-bs-target` |
| `data-dismiss` | `data-bs-dismiss` |
| `data-parent` | `data-bs-parent` |

### JavaScript Methods

```javascript
// Bootstrap 3
$('#myModal').modal('show');

// Bootstrap 5 (without jQuery)
var myModal = new bootstrap.Modal(document.getElementById('myModal'));
myModal.show();

// Or with jQuery adapter (if jQuery is kept)
$('#myModal').modal('show'); // Still works with Bootstrap 5 if jQuery present
```

## Step 9: Dark Mode

Bootstrap 5.3+ has built-in dark mode support via `data-bs-theme="dark"`:

```html
<html data-bs-theme="dark">
<!-- or -->
<body data-bs-theme="dark">
<!-- or on specific components -->
<div class="card" data-bs-theme="dark">
```

Consider migrating custom dark mode implementation to Bootstrap 5's native support.

## Summary

This migration will:
- ✅ Remove jQuery dependency (if not needed elsewhere)
- ✅ Use modern Bootstrap 5 utilities
- ✅ Reduce custom CSS by 60-75%
- ✅ Improve maintainability
- ✅ Enable future Bootstrap updates
- ✅ Access to new Bootstrap 5 features

## Migration Script

A migration script is provided in `scripts/migrate_to_bootstrap5.py` that will:
1. Update class names in HTML
2. Replace data attributes
3. Identify custom CSS that can be removed
4. Generate report of changes needed
