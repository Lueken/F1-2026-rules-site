# F1 2026 Watch Party Site - Project Status

## Overview
Creating 11 team-specific F1 watch party page designs for the 2026 season. Each design uses identical content but features unique visual styling that captures each team's brand identity and racing heritage.

## Tool & Workflow
- **Using:** `frontend-design` skill/plugin for all team designs
- **Content Source:** All designs use exact content from `index2.html`
- **Testing:** Mobile viewport 390x844 (iPhone 12 Pro)
- **Deployment:** Netlify auto-deploy from GitHub main branch

## Teams Completed (5/11)

### ✅ 1. McLaren - "Speed Slice"
- **File:** `index-mclaren.html`
- **Colors:** Papaya orange (#FF8700) dominant, electric blue accent
- **Typography:** Racing Sans One, IBM Plex Mono, Archivo Black
- **Memorable Element:** Diagonal atmosphere with skewed elements
- **Status:** Complete, mobile optimized

### ✅ 2. Ferrari - "Scuderia Velocity"
- **File:** `index-ferrari.html`
- **Colors:** Rosso Corsa red (#DC0000), Italian flag (green/white/red)
- **Typography:** Playfair Display (italic), Libre Baskerville, Teko
- **Memorable Element:** Vertical Italian flag racing stripes on edges
- **Status:** Complete, mobile optimized

### ✅ 3. Mercedes - "Silver Arrows Precision"
- **File:** `index-mercedes.html`
- **Colors:** Silver (#C0C0C0), Petronas teal (#00D2BE)
- **Typography:** Orbitron, Rajdhani, Saira
- **Memorable Element:** Technical grid background + three-pointed star watermark
- **Status:** Complete, mobile optimized

### ✅ 4. Red Bull Racing - "Championship Voltage"
- **File:** `index-redbull.html`
- **Colors:** Red Bull blue (#0600EF), red (#E50010), yellow (#FCD700)
- **Typography:** Russo One, Teko, Quantico
- **Memorable Element:** Rotating diamond nav button + diagonal energy burst stripes
- **Status:** Complete, mobile optimized

### ✅ 5. Aston Martin - "British Racing Prestige"
- **File:** `index-astonmartin.html`
- **Colors:** British Racing Green (#006F62, #00352F), lime green (#00F5B8, #CEDC00)
- **Typography:** Cinzel, Cormorant Garamond, Lato
- **Memorable Element:** Hexagonal nav button + wing silhouette
- **Status:** Complete, mobile optimized, text overflow fixed

## Teams Remaining (6/11)

### 6. Alpine
- **Expected Theme:** "French Racing Elegance"
- **Colors:** French blue (#0090FF), pink/fuchsia (#FF1E7E), white
- **Concept:** Mountain heritage meets French sophistication, sporty elegance
- **Design Notes:** Tricolor accents, alpine aesthetics, modern European racing

### 7. Williams
- **Expected Theme:** "Classic British Heritage"
- **Colors:** Williams blue (#005AFF), white, red accents
- **Concept:** Classic British racing tradition, legendary heritage, clean lines
- **Design Notes:** Sophisticated minimalism, racing purity, iconic simplicity

### 8. Audi
- **Expected Theme:** "German Precision Engineering"
- **Colors:** Audi red (#FF1E00), black, silver/grey
- **Concept:** German engineering excellence, technical perfection, "Vorsprung durch Technik"
- **Design Notes:** Four rings inspiration, precision geometry, technical sophistication

### 9. Haas
- **Expected Theme:** "American Industrial Racing"
- **Colors:** Grey (#B6BABD), red, white, black
- **Concept:** American manufacturing muscle, industrial strength, stars and stripes
- **Design Notes:** Bold American identity, machinery aesthetics, industrial power

### 10. Racing Bulls (RB)
- **Expected Theme:** "Youthful Energy Thunder"
- **Colors:** Navy blue, cyan/turquoise, white
- **Concept:** Junior team energy, fresh talent, youthful dynamism
- **Design Notes:** Modern, energetic, sister team to Red Bull but distinct identity

### 11. Cadillac
- **Expected Theme:** "American Luxury Performance"
- **Colors:** Grey/black/silver (#666666), gold accents, white
- **Concept:** American luxury meets racing performance, premium heritage
- **Design Notes:** Art deco inspiration, luxury car showroom, classic American elegance

## Critical Requirements for All Designs

### Mobile-First Optimization (MANDATORY)
Every design MUST include these mobile overflow protections:

1. **Grid Pattern (use minmax with min()):**
   ```css
   .terms-grid {
       grid-template-columns: repeat(auto-fit, minmax(min(280px, 100%), 1fr));
   }
   .card-grid {
       grid-template-columns: repeat(auto-fit, minmax(min(320px, 100%), 1fr));
   }
   ```

2. **Single-column on mobile:**
   ```css
   @media (max-width: 768px) {
       .terms-grid,
       .card-grid {
           grid-template-columns: 1fr;
           gap: 1.5rem;
       }
   }
   ```

3. **Prevent overflow:**
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

4. **Text wrapping in cards:**
   ```css
   .term-card,
   .content-card {
       word-wrap: break-word;
       overflow-wrap: break-word;
       min-width: 0;
   }
   ```

5. **Header sizing for single-line fit:**
   ```css
   .term-card strong {
       font-size: 1rem; /* Keep headers on one line */
       letter-spacing: 1.5px;
   }
   ```

### Typography Rules
- **FORBIDDEN:** Inter, Roboto, Arial, Space Grotesk, system fonts
- **REQUIRED:** Distinctive display fonts + refined body fonts
- Each team must have unique typography matching brand identity
- Use Google Fonts for accessibility

### Design Principles
- **Color:** Dominant team color creates atmosphere with sharp accents
- **Memorable Element:** ONE unforgettable visual element per design
- **Consistency:** Use CSS variables for theming
- **Motion:** Scroll animations via Intersection Observer
- **Navigation:** Quick Nav menu with themed button (custom shapes encouraged)

### Content Requirements
- Use EXACT content from `index2.html`
- Only change visual styling, never content
- Include all sections: Power Units, Basic Terms, New Terminology, What's Different, Australian GP
- Include Quick Nav menu functionality

## Git Workflow
```bash
git add [filename]
git commit -m "Message

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
git push
```

## Testing Checklist (Before Committing)
- [ ] No horizontal overflow on mobile (390x844)
- [ ] All text readable and properly sized
- [ ] Headers fit on single lines in term cards
- [ ] Grid containers don't exceed viewport width
- [ ] Animations work smoothly
- [ ] Quick Nav functions properly
- [ ] Design has ONE memorable visual element
- [ ] Typography is distinctive (not generic AI fonts)

## Next Steps
1. Create Alpine design using frontend-design skill
2. Test mobile responsiveness thoroughly
3. Apply all overflow fixes preemptively
4. Continue through remaining 5 teams
5. Final review of all 11 designs
6. Deploy to Netlify

## Notes
- Mobile optimization is NON-NEGOTIABLE - test before committing
- Each design should feel completely unique while using identical content
- Avoid generic "AI slop" aesthetics - be BOLD and CREATIVE
- Match implementation complexity to aesthetic vision
