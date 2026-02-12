# Claude Code - F1 2026 Rules Site

## Project Overview
F1 watch party website with 11 team-themed designs featuring the 2026 F1 regulation changes.

## Known Issues & Fixes

### Mobile Horizontal Overflow Issue
**Problem:** Grid-based sections (particularly "Basic Terms") cause horizontal scrolling on mobile devices.

**Root Cause:** Grid templates using `repeat(auto-fit, minmax(300px, 1fr))` can create containers wider than the viewport on mobile devices when the minimum size (300px) exceeds available space.

**Solution (Applied to all team designs):**
1. **Force single-column layout on mobile:**
   ```css
   @media (max-width: 768px) {
       .terms-grid,
       .card-grid {
           grid-template-columns: 1fr;
       }
   }
   ```

2. **Prevent body/container overflow:**
   ```css
   body {
       overflow-x: hidden;
       width: 100%;
       max-width: 100vw;
   }

   .container {
       max-width: min(1400px, 100%);
       overflow-x: hidden;
   }
   ```

3. **Reduce grid minimum width:**
   ```css
   .terms-grid {
       grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
   }
   ```

**Files Fixed:**
- index-ferrari.html
- index-mercedes.html
- index-redbull.html
- index-astonmartin.html

**Note for Future Team Designs:**
Always include these mobile overflow protections when creating new team-themed pages. Test on mobile viewport (390x844 - iPhone 12 Pro) to verify no horizontal scroll.

## Team Designs Created

### Completed (5/11):
1. ✅ **McLaren** - "Speed Slice" - Diagonal cuts, papaya atmosphere
2. ✅ **Ferrari** - "Scuderia Velocity" - Italian flag stripes, elegant serif typography
3. ✅ **Mercedes** - "Silver Arrows Precision" - Technical grid, metallic silver, hexagonal elements
4. ✅ **Red Bull Racing** - "Championship Voltage" - Aggressive energy, bold championship dominance
5. ✅ **Aston Martin** - "British Racing Prestige" - Wing motifs, luxury green, hexagonal nav

### Remaining (6/11):
- Alpine
- Williams
- Audi
- Haas
- Racing Bulls (RB)
- Cadillac

## Design Principles

### Typography
- **AVOID:** Inter, Roboto, Arial, Space Grotesk, system fonts
- **USE:** Distinctive display fonts paired with refined body fonts
- Each team should have unique typography that matches their brand identity

### Mobile-First Requirements
- Single-column grids below 768px
- No horizontal overflow
- Font scaling with clamp()
- Touch-friendly button sizes (minimum 60x60px)
- Adequate spacing for readability

### Color Usage
- Dominant team color creates atmosphere
- Sharp accent colors (not timid/evenly distributed)
- Use CSS variables for consistency

### Memorable Elements
Each design needs ONE unforgettable visual element:
- McLaren: Diagonal papaya atmosphere
- Ferrari: Vertical Italian flag racing stripes
- Mercedes: Metallic gradient text + technical grid
- Red Bull: Rotating diamond nav + diagonal energy bursts
- Aston Martin: Hexagonal nav + wing silhouette

## Git Workflow
- Commit message format: Descriptive title + "Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
- Always test mobile responsive before committing
- Push to main branch for Netlify auto-deploy

## Deployment
- Hosted on Netlify
- Auto-deploys from GitHub main branch
- Primary file: index.html (random selector)
- Individual team files: index-{teamname}.html

## Content Source
All team designs use identical content from `index2.html` - only visual styling differs.
