# F1 2026 Watch Party Site - Project Status

## Overview
Creating 11 team-specific F1 watch party page designs for the 2026 season. Each design uses identical content but features unique visual styling that captures each team's brand identity and racing heritage.

## Tool & Workflow
- **Using:** `frontend-design` skill/plugin for all team designs
- **Content Source:** All designs use exact content from `index2.html`
- **Testing:** Mobile viewport 390x844 (iPhone 12 Pro)
- **Deployment:** Netlify auto-deploy from GitHub main branch

## Teams Completed (11/11) ✅

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

### ✅ 4. Red Bull Racing - "Heritage Gloss"
- **File:** `index-redbull.html`
- **Colors:** Blue gradient background (#1E3A8A to #0F172A), lighter blue jacquard (#60A5FA), yellow accent (#FFE500), red accent (#FF1801)
- **Typography:** Oswald (bold display), Barlow (clean body), JetBrains Mono (technical)
- **Memorable Element:** Jacquard woven pattern in lighter blue + glossy shine sweep animation across page + yellow highlight box (Basic Terms) + red GP callout section
- **Design Philosophy:** Matches 2026 RB22 livery - BLUE DOMINANT with gloss finish, lighter blue jacquard pattern like bodywork, yellow/red Red Bull branding accents, Ford partnership badge, glassmorphic cards
- **Status:** Complete, redesigned to match actual 2026 livery, mobile optimized

### ✅ 5. Aston Martin - "British Racing Prestige"
- **File:** `index-astonmartin.html`
- **Colors:** British Racing Green (#006F62, #00352F), lime green (#00F5B8, #CEDC00)
- **Typography:** Cinzel, Cormorant Garamond, Lato
- **Memorable Element:** Hexagonal nav button + wing silhouette
- **Status:** Complete, mobile optimized, text overflow fixed

### ✅ 6. Alpine - "Altitude Bleue"
- **File:** `index-alpine.html`
- **Colors:** Alpine blue (#0090FF), hot pink (#FF87BC/#FF1E7E), deep navy (#0B1428), French tricolor
- **Typography:** Syne (French-designed geometric display), Outfit (modern body), Source Code Pro (technical monospace)
- **Memorable Element:** Mountain ridge clip-path hero silhouette + diagonal French tricolor sash + mountain-peak shaped nav button
- **Status:** Complete, mobile optimized, all overflow protections applied

### ✅ 7. Williams - "Classic British Heritage"
- **File:** `index-williams.html`
- **Colors:** Williams blue (#005AFF), navy (#0A1628), cream (#F8F9FC), red accent (#E10600)
- **Typography:** Bodoni Moda (elegant British serif), DM Sans (clean body), JetBrains Mono (technical monospace)
- **Memorable Element:** Vertical racing stripe on right edge (blue with red segment) + "9 Championships" heritage badge + horizontal speed lines background + "W" nav button with racing stripe inset
- **Status:** Complete, mobile optimized, team selector added

### ✅ 8. Audi - "German Premium Sophistication"
- **File:** `index-audi.html`
- **Colors:** Silver palette (#D0D3D4, #E8EAEB), charcoal (#333333), Audi red (#BB0A1E) as subtle accent only
- **Typography:** Lexend (refined, light weight display), Nunito Sans (clean body)
- **Memorable Element:** Four rings watermark (subtle interlocking circles) + light silver gradient background + red accent appears only on hover + "Vorsprung durch Technik" tagline + circular "A" nav button
- **Design Philosophy:** Understated luxury, premium showroom feel, red as accent not dominant
- **Status:** Complete, redesigned for brand authenticity, mobile optimized

### ✅ 9. Haas - "American Precision"
- **File:** `index-haas.html`
- **Colors:** White (#FFFFFF), off-white (#F8F9FA), black (#1A1A1A), Haas red (#E10600) as accent
- **Typography:** Montserrat (clean professional body), Bebas Neue (bold display), IBM Plex Mono (technical)
- **Memorable Element:** Red accent line at top of page + clean minimalist cards with red hover accent + black/white contrast sections
- **Design Philosophy:** Clean, professional, white-dominant (matching 2026 VF-26 livery direction) - precision American engineering, not industrial/gritty
- **Status:** Complete, redesigned to match actual Haas brand language, mobile optimized

### ✅ 10. Racing Bulls (RB) - "Culture First"
- **File:** `index-rb.html`
- **Colors:** White base, RB blue (#3B82F6), navy (#1E3A5F), light blue accents (#60A5FA)
- **Typography:** Sora (modern geometric display), Outfit (clean body), JetBrains Mono (technical)
- **Memorable Element:** Parallelogram/skewed accents (Red Bull energy drink branding nod) + blue gradient accent bar + skewed nav button + diagonal decorative shapes
- **Design Philosophy:** Culture-first youthful identity, clean white base matching 2026 VCARB livery, blue accents (Ford partnership), modern rounded corners, energetic but refined
- **Status:** Complete, mobile optimized, team selector added

### ✅ 11. Cadillac - "Bold & Modern"
- **File:** `index-cadillac.html`
- **Colors:** Monochrome black (#0A0A0A) and white (#FFFFFF), chrome accents (#D4D4D4)
- **Typography:** Cormorant Garamond (elegant serif display), Manrope (clean modern body), JetBrains Mono (technical)
- **Memorable Element:** Split black/white hero (yin-yang livery concept) + chevron pattern backgrounds + split GP callout section + chrome gradient accent bar
- **Design Philosophy:** Monochrome high-performance branding (Cadillac's F1 approach), split design representing balance of bold attitude (black) and American optimism (white), chrome details like the actual car
- **Status:** Complete, redesigned to match 2026 livery, mobile optimized

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
1. ✅ All 11 team designs complete
2. Final review of all designs for mobile responsiveness
3. Deploy to Netlify

## Notes
- Mobile optimization is NON-NEGOTIABLE - test before committing
- Each design should feel completely unique while using identical content
- Avoid generic "AI slop" aesthetics - be BOLD and CREATIVE
- Match implementation complexity to aesthetic vision
