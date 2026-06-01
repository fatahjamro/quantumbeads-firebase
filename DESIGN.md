# QuantumBeads — Design & Enhancement Roadmap

**Based on:** Comprehensive audit of quantumbeads.com  
**Last updated:** June 2026  
**Purpose:** Step-by-step guide to elevate the website from early-stage startup to premium quantum consultancy. Work through these phases in order. Each step is self-contained — you can stop and deploy at any point.

---

## How to Use This File

Each step includes:
- **Impact** — how much this improves the site (High / Medium / Low)
- **Effort** — realistic time estimate
- **Files** — which files to edit
- **Status** — track your progress: `[ ]` not started · `[x]` done · `[~]` in progress

---

## PHASE 1 — Critical Fixes
> Zero design skill required. Pure code fixes. Do these first.

---

### Step 1.1 — Fix External Link Security
**Impact:** High (security) · **Effort:** 15 minutes · **Files:** All HTML files

Every `target="_blank"` link is missing `rel="noopener noreferrer"`. This allows the opened page to access `window.opener` — a well-documented phishing vector.

**Find every instance of:**
```html
target="_blank"
```

**Replace with:**
```html
target="_blank" rel="noopener noreferrer"
```

**Pages to check:**
- `index.html` (LinkedIn links, Our Team link)
- `html/about.html`
- `blogs/blogs.html` (Engineers Ireland links)
- `fatah-jamro.html`
- `lalarukh.html`
- `events/events.html`

**Status:** `[ ]`

---

### Step 1.2 — Fix Title Inconsistency
**Impact:** Medium · **Effort:** 10 minutes · **Files:** `index.html`

The homepage About section still shows "Founder & Quantum Researcher" for Abdul Fatah. Every other page correctly shows "Co-Founder & CTO". Fix this so the title is consistent everywhere.

**In `index.html`, find:**
```html
<div class="founder-title">Founder & Quantum Researcher</div>
```
**Replace with:**
```html
<div class="founder-title">Co-Founder & CTO</div>
```

**Status:** `[ ]`

---

### Step 1.3 — Fix Footer Team Links
**Impact:** Medium · **Effort:** 10 minutes · **Files:** All HTML files

The footer "Our Team" link goes only to Abdul Fatah's page. There are now two founders. Fix the footer across all pages.

**In every page footer, replace:**
```html
<li><a href="fatah-jamro.html">Our Team</a></li>
```
**With:**
```html
<li><a href="html/about.html">Meet the Team</a></li>
```
*(adjust relative path per page — `../html/about.html` for sub-pages)*

**Status:** `[ ]`

---

### Step 1.4 — Fix the Events Page Stale Date
**Impact:** High (credibility) · **Effort:** 20 minutes · **Files:** `events/events.html`, `index.html`

The Winter School 2024 is the most prominent event on the page with no indication it is past. New visitors think it is upcoming. This damages credibility.

**In `events/events.html`, change the event heading area to:**
```html
<div class="event-date">
  January 2024
  <span style="margin-left: 0.75rem; font-size: 0.75rem; font-weight: 600;
    background: rgba(255,0,153,0.1); border: 1px solid var(--accent-pink);
    color: var(--accent-pink); padding: 0.15rem 0.5rem; border-radius: 20px;">
    Past Event
  </span>
</div>
```

**Then add a "Next Event" placeholder after the Winter School section:**
```html
<section class="about-section" style="text-align: center;
  background: linear-gradient(135deg, rgba(0,212,255,0.08), rgba(124,58,237,0.08));
  border: 1px dashed var(--border-color); border-radius: 12px;">
  <h3 style="color: var(--accent-blue);">Next Event — Coming Soon</h3>
  <p style="color: var(--text-secondary); margin-top: 0.75rem;">
    We are planning our next workshop for 2026. Subscribe to The Quantum Digest
    or contact us to be notified when registration opens.
  </p>
  <a href="mailto:contact@quantumbeads.com" class="btn btn-primary"
    style="margin-top: 1.5rem; display: inline-block;">
    Get Notified →
  </a>
</section>
```

**Also update `index.html` homepage Events section** — the same past date appears there. Add the "Past Event" badge inline.

**Status:** `[ ]`

---

### Step 1.5 — Remove Outdated Meta Keywords
**Impact:** Low · **Effort:** 5 minutes · **Files:** `index.html`

Google has ignored the `meta keywords` tag since 2009. Its presence signals outdated SEO practice to technical visitors.

**Remove this line from `index.html`:**
```html
<meta name="keywords" content="quantum computing, quantum consulting, ...">
```

**Status:** `[ ]`

---

### Step 1.6 — Add Newsletter Input Label (Accessibility)
**Impact:** Medium (accessibility) · **Effort:** 10 minutes · **Files:** `index.html`, `blogs/blogs.html`

The newsletter email input has no `<label>`. Screen readers cannot identify what the field is for. The placeholder disappears when typing begins.

**Replace the newsletter input in both files:**
```html
<!-- Before -->
<input type="email" name="email" placeholder="your@email.com" required class="newsletter-input">

<!-- After -->
<label for="newsletter-email" style="position: absolute; width: 1px; height: 1px;
  overflow: hidden; clip: rect(0,0,0,0);">Email address</label>
<input id="newsletter-email" type="email" name="email"
  placeholder="your@email.com" required class="newsletter-input">
```

**Status:** `[ ]`

---

## PHASE 2 — SEO & Discoverability
> These make the site findable and shareable. Critical for B2B.

---

### Step 2.1 — Add Open Graph Meta Tags
**Impact:** High · **Effort:** 1 hour · **Files:** All HTML files + create one image

Every time someone shares `quantumbeads.com` on LinkedIn, Twitter/X, or WhatsApp, there is currently NO preview image, no custom title, no description card. This is a huge missed opportunity — LinkedIn is your primary channel.

**Step A:** Create a 1200×630px branded image (`webimages/og-image.png`).
- Dark navy background (#0a0a1a)
- QuantumBeads logo centred
- Tagline beneath: "Quantum Computing Consultancy & Research"
- Can be made in Canva, Figma, or any design tool

**Step B:** Add to the `<head>` of every page:

```html
<!-- Open Graph (LinkedIn, Facebook, WhatsApp) -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="QuantumBeads">
<meta property="og:title" content="QuantumBeads | Quantum Computing Consultancy & Research">
<meta property="og:description" content="We help organisations understand and adopt quantum computing through expert consulting, workshops, and active PhD-level research. Honest. Jargon-free. Research-backed.">
<meta property="og:image" content="https://quantumbeads.com/webimages/og-image.png">
<meta property="og:url" content="https://quantumbeads.com/">

<!-- Twitter / X Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="QuantumBeads | Quantum Computing Consultancy & Research">
<meta name="twitter:description" content="Consulting, workshops, and research that makes quantum computing accessible and actionable for organisations.">
<meta name="twitter:image" content="https://quantumbeads.com/webimages/og-image.png">
```

**Customise the `og:url` and `og:title` per page:**
- Insights page: `og:url = https://quantumbeads.com/blogs/blogs.html`
- Events page: `og:url = https://quantumbeads.com/events/events.html`
- etc.

**Status:** `[ ]`

---

### Step 2.2 — Create sitemap.xml
**Impact:** Medium · **Effort:** 20 minutes · **Files:** Create `sitemap.xml` in root

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://quantumbeads.com/</loc>
    <priority>1.0</priority>
    <changefreq>monthly</changefreq>
  </url>
  <url>
    <loc>https://quantumbeads.com/html/about.html</loc>
    <priority>0.8</priority>
    <changefreq>monthly</changefreq>
  </url>
  <url>
    <loc>https://quantumbeads.com/blogs/blogs.html</loc>
    <priority>0.8</priority>
    <changefreq>weekly</changefreq>
  </url>
  <url>
    <loc>https://quantumbeads.com/events/events.html</loc>
    <priority>0.7</priority>
    <changefreq>monthly</changefreq>
  </url>
  <url>
    <loc>https://quantumbeads.com/fatah-jamro.html</loc>
    <priority>0.7</priority>
    <changefreq>monthly</changefreq>
  </url>
  <url>
    <loc>https://quantumbeads.com/lalarukh.html</loc>
    <priority>0.7</priority>
    <changefreq>monthly</changefreq>
  </url>
  <url>
    <loc>https://quantumbeads.com/blogs/practical-realization-qubit.html</loc>
    <priority>0.6</priority>
    <changefreq>yearly</changefreq>
  </url>
</urlset>
```

**Status:** `[ ]`

---

### Step 2.3 — Create robots.txt
**Impact:** Low · **Effort:** 5 minutes · **Files:** Create `robots.txt` in root

```
User-agent: *
Allow: /
Sitemap: https://quantumbeads.com/sitemap.xml
```

**Status:** `[ ]`

---

### Step 2.4 — Add Schema.org Structured Data
**Impact:** High (rich search results) · **Effort:** 30 minutes · **Files:** `index.html`, `fatah-jamro.html`, `lalarukh.html`

Schema.org markup helps Google understand your content and can generate rich results (knowledge panels, breadcrumbs, etc.).

**Add to `index.html` inside `<head>`:**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "QuantumBeads",
  "url": "https://quantumbeads.com",
  "logo": "https://quantumbeads.com/webimages/logo-quantubeads-new-white1.svg",
  "description": "Quantum computing consultancy and research helping organisations navigate the quantum transition through consulting, workshops, and applied research.",
  "email": "contact@quantumbeads.com",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Galway",
    "addressCountry": "IE"
  },
  "sameAs": [
    "https://www.linkedin.com/company/QuantumBeads"
  ],
  "founders": [
    {
      "@type": "Person",
      "name": "Abdul Fatah Jamro",
      "jobTitle": "Co-Founder & CTO",
      "url": "https://quantumbeads.com/fatah-jamro.html"
    },
    {
      "@type": "Person",
      "name": "Lala Rukh",
      "jobTitle": "Co-Founder & CEO",
      "url": "https://quantumbeads.com/lalarukh.html"
    }
  ]
}
</script>
```

**Add Person schema to `fatah-jamro.html`:**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Abdul Fatah Jamro",
  "jobTitle": "Co-Founder & CTO",
  "worksFor": { "@type": "Organization", "name": "QuantumBeads" },
  "url": "https://quantumbeads.com/fatah-jamro.html",
  "sameAs": ["https://www.linkedin.com/in/fatahjamro/"]
}
</script>
```

**Add Person schema to `lalarukh.html`:**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Lala Rukh",
  "jobTitle": "Co-Founder & CEO",
  "worksFor": { "@type": "Organization", "name": "QuantumBeads" },
  "url": "https://quantumbeads.com/lalarukh.html",
  "sameAs": ["https://www.linkedin.com/in/lalarukhfatah/"]
}
</script>
```

**Status:** `[ ]`

---

### Step 2.5 — Add Apple Touch Icon & Web Manifest
**Impact:** Low · **Effort:** 20 minutes · **Files:** `index.html`, create `manifest.json`

Allows the site to install cleanly as a home screen shortcut on mobile devices.

**Create `manifest.json` in root:**
```json
{
  "name": "QuantumBeads",
  "short_name": "QB",
  "description": "Quantum Computing Consultancy & Research",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#0a0a1a",
  "theme_color": "#00d4ff",
  "icons": [
    {
      "src": "/webimages/logo-favicon-quantumbeadsnew1.ico",
      "sizes": "32x32",
      "type": "image/x-icon"
    }
  ]
}
```

**Add to `<head>` of `index.html`:**
```html
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#00d4ff">
```

**Status:** `[ ]`

---

## PHASE 3 — Conversion Improvements
> These directly affect whether visitors become clients.

---

### Step 3.1 — Add Social Proof Stats to Hero
**Impact:** High · **Effort:** 30 minutes · **Files:** `index.html`

You trained 200+ participants at the Winter School. You have two published founders. You have IEEE publications. None of this appears above the fold. Add a simple stat bar beneath the CTA buttons.

**Add this block after the CTA buttons in the hero section:**
```html
<div style="display: flex; gap: 2.5rem; justify-content: center; flex-wrap: wrap;
  margin-top: 2.5rem; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.08);">
  <div style="text-align: center;">
    <div style="font-size: 1.6rem; font-weight: 700; color: var(--accent-blue);">200+</div>
    <div style="font-size: 0.8rem; color: var(--text-secondary); letter-spacing: 0.05em;">Professionals Trained</div>
  </div>
  <div style="text-align: center;">
    <div style="font-size: 1.6rem; font-weight: 700; color: var(--accent-blue);">2</div>
    <div style="font-size: 0.8rem; color: var(--text-secondary); letter-spacing: 0.05em;">Countries Reached</div>
  </div>
  <div style="text-align: center;">
    <div style="font-size: 1.6rem; font-weight: 700; color: var(--accent-blue);">IEEE</div>
    <div style="font-size: 0.8rem; color: var(--text-secondary); letter-spacing: 0.05em;">Published Research</div>
  </div>
  <div style="text-align: center;">
    <div style="font-size: 1.6rem; font-weight: 700; color: var(--accent-blue);">2</div>
    <div style="font-size: 0.8rem; color: var(--text-secondary); letter-spacing: 0.05em;">PhD Researchers</div>
  </div>
</div>
```

**Status:** `[ ]`

---

### Step 3.2 — Add a Credibility Bar (Publication Logos)
**Impact:** High · **Effort:** 1 hour · **Files:** `index.html`

Add a thin strip below the hero showing where you have been published/featured. IonQ, Quantinuum, and every premium B2B company has this. It anchors credibility instantly.

**Add this section immediately after the hero `</section>` and before the services section:**
```html
<section style="padding: 1.5rem 2rem; border-top: 1px solid var(--border-color);
  border-bottom: 1px solid var(--border-color); background: rgba(26,26,62,0.3);">
  <div style="max-width: 900px; margin: 0 auto; display: flex; align-items: center;
    justify-content: center; gap: 2rem; flex-wrap: wrap;">
    <span style="font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.12em;
      color: var(--text-secondary); white-space: nowrap;">As seen in</span>
    <span style="font-size: 0.9rem; font-weight: 600; color: var(--text-secondary);
      opacity: 0.7;">Engineers Ireland</span>
    <span style="color: var(--border-color);">·</span>
    <span style="font-size: 0.9rem; font-weight: 600; color: var(--text-secondary);
      opacity: 0.7;">IEEE QCNC 2024</span>
    <span style="color: var(--border-color);">·</span>
    <span style="font-size: 0.9rem; font-weight: 600; color: var(--text-secondary);
      opacity: 0.7;">World Energy Council</span>
    <span style="color: var(--border-color);">·</span>
    <span style="font-size: 0.9rem; font-weight: 600; color: var(--text-secondary);
      opacity: 0.7;">Lindau Nobel Laureate Meeting</span>
  </div>
</section>
```

**Status:** `[ ]`

---

### Step 3.3 — Upgrade the Hero CTA Buttons
**Impact:** High · **Effort:** 15 minutes · **Files:** `index.html`

"Learn More" goes to the About page — a confusing journey for a first-time visitor. Upgrade both CTAs to be action-oriented.

**Replace current CTA buttons:**
```html
<!-- Before -->
<a href="html/about.html" class="btn btn-primary">Learn More</a>
<a href="#services" class="btn btn-secondary">Our Services</a>

<!-- After -->
<a href="mailto:contact@quantumbeads.com?subject=Discovery%20Call%20Request"
  class="btn btn-primary">Book a Discovery Call</a>
<a href="#services" class="btn btn-secondary">See What We Offer</a>
```

> **Future upgrade:** Replace the `mailto:` link with a Calendly embed URL once you set one up at calendly.com (free plan available).

**Status:** `[ ]`

---

### Step 3.4 — Improve the Contact Section
**Impact:** High · **Effort:** 30 minutes · **Files:** `index.html`

The current contact section shows only an email address. Most enterprise visitors will not cold-email — they need a structured path. Add three clear options.

**Replace the contact section content with:**
```html
<section class="contact">
  <h2>Let's Talk Quantum</h2>
  <p>Considering quantum computing for your organisation? Want to upskill your team?
    Exploring a research collaboration? Choose how you'd like to connect.</p>

  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1.5rem; margin-top: 2rem; max-width: 800px; margin-left: auto; margin-right: auto;">

    <div style="padding: 1.5rem; background: rgba(0,212,255,0.05);
      border: 1px solid var(--accent-blue); border-radius: 10px; text-align: center;">
      <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">📅</div>
      <h4 style="color: var(--accent-blue); margin-bottom: 0.5rem;">Book a Call</h4>
      <p style="color: var(--text-secondary); font-size: 0.88rem; margin-bottom: 1rem;">
        Free 30-minute discovery call to discuss your needs.</p>
      <a href="mailto:contact@quantumbeads.com?subject=Discovery%20Call%20Request"
        style="color: var(--accent-blue); text-decoration: none; font-weight: 600;
        font-size: 0.9rem;">Request a Call →</a>
    </div>

    <div style="padding: 1.5rem; background: rgba(124,58,237,0.05);
      border: 1px solid var(--accent-purple); border-radius: 10px; text-align: center;">
      <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">✉️</div>
      <h4 style="color: var(--accent-purple); margin-bottom: 0.5rem;">Send an Email</h4>
      <p style="color: var(--text-secondary); font-size: 0.88rem; margin-bottom: 1rem;">
        Write to us directly with your question or project brief.</p>
      <a href="mailto:contact@quantumbeads.com"
        style="color: var(--accent-purple); text-decoration: none; font-weight: 600;
        font-size: 0.9rem;">contact@quantumbeads.com →</a>
    </div>

    <div style="padding: 1.5rem; background: rgba(255,0,153,0.05);
      border: 1px solid var(--accent-pink); border-radius: 10px; text-align: center;">
      <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">💼</div>
      <h4 style="color: var(--accent-pink); margin-bottom: 0.5rem;">LinkedIn</h4>
      <p style="color: var(--text-secondary); font-size: 0.88rem; margin-bottom: 1rem;">
        Follow us for weekly quantum insights and updates.</p>
      <a href="https://www.linkedin.com/company/QuantumBeads" target="_blank"
        rel="noopener noreferrer"
        style="color: var(--accent-pink); text-decoration: none; font-weight: 600;
        font-size: 0.9rem;">Follow QuantumBeads →</a>
    </div>

  </div>
</section>
```

**Status:** `[ ]`

---

### Step 3.5 — Add a Testimonial (When Available)
**Impact:** Very High · **Effort:** 30 minutes (when you have content)

This is the single most powerful conversion element missing from the site. One genuine quote from a workshop participant or consulting client is worth more than three sections of self-description.

**Add this section between the Team section and the Events section on the homepage:**
```html
<section style="padding: 4rem 2rem; text-align: center; max-width: 800px;
  margin: 0 auto;">
  <div style="font-size: 3rem; color: var(--accent-blue); line-height: 1;
    margin-bottom: 1.5rem; opacity: 0.5;">"</div>
  <blockquote style="font-size: 1.2rem; color: var(--text-primary); line-height: 1.8;
    font-style: italic; margin: 0 0 1.5rem;">
    [Testimonial text goes here — reach out to Winter School participants for a quote]
  </blockquote>
  <p style="color: var(--accent-blue); font-weight: 600;">— Name, Role, Organisation</p>
</section>
```

**How to get testimonials:** Email 3–5 Winter School 2024 participants asking for a 1–2 sentence quote about the experience. Most people are happy to provide one when asked directly.

**Status:** `[ ]`

---

## PHASE 4 — Design Upgrades
> Visual changes that elevate the site from "good" to "premium."

---

### Step 4.1 — Replace Emoji Icons with SVG Icons
**Impact:** Very High · **Effort:** 2 hours · **Files:** `index.html`

This is the single biggest visual change you can make. Emoji in service cards immediately signals "student project." SVG icons signal "professional product."

**Recommended icon library:** [Phosphor Icons](https://phosphoricons.com/) — free, clean, available as inline SVG.

**For each service card, replace the emoji `<div>` with an SVG. Example for Quantum Consulting:**

```html
<!-- Before -->
<div class="service-icon">🎯</div>

<!-- After — Consulting icon (target/lightbulb) -->
<div class="service-icon">
  <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 256 256"
    fill="none" stroke="url(#iconGrad)" stroke-width="12" stroke-linecap="round"
    stroke-linejoin="round">
    <defs>
      <linearGradient id="iconGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#00d4ff"/>
        <stop offset="100%" stop-color="#7c3aed"/>
      </linearGradient>
    </defs>
    <!-- Lightbulb / consulting icon -->
    <circle cx="128" cy="96" r="64"/>
    <line x1="128" y1="192" x2="128" y2="224"/>
    <line x1="104" y1="208" x2="152" y2="208"/>
    <line x1="104" y1="192" x2="152" y2="192"/>
  </svg>
</div>
```

**Suggested icon shapes per service:**
| Service | Icon concept | Phosphor name |
|---|---|---|
| Quantum Consulting | Lightbulb or target | `Lightbulb`, `Target` |
| Workshops & Training | Chalkboard or graduation cap | `ChalkboardTeacher` |
| Research Partnerships | Flask or atom | `Flask`, `Atom` |
| Technical Assessment | Clipboard or checklist | `ClipboardText` |

**Alternative (easier):** Use the Phosphor Icons CDN and reference icon components directly:
```html
<script src="https://unpkg.com/@phosphor-icons/web"></script>
<!-- Then use: -->
<i class="ph-bold ph-lightbulb" style="font-size: 2.5rem; color: var(--accent-blue);"></i>
```

**Status:** `[ ]`

---

### Step 4.2 — Add a Visual Break Section (Full-Bleed)
**Impact:** High · **Effort:** 1–2 hours · **Files:** `index.html`, `css/styles.css`

The current homepage has identical dark-card sections from top to bottom. There is no visual rhythm. Adding one full-bleed section with a background image or animated pattern breaks the monotony and makes the site feel 40% more polished.

**Add between the Services section and the Research section:**

**Option A — CSS animated particle/circuit pattern (no images needed):**
```html
<section style="position: relative; padding: 5rem 2rem; overflow: hidden;
  background: radial-gradient(ellipse at center, rgba(124,58,237,0.2) 0%, transparent 70%);
  text-align: center; border-top: 1px solid var(--border-color);
  border-bottom: 1px solid var(--border-color);">

  <!-- Animated circuit lines via CSS -->
  <div style="position: absolute; inset: 0; opacity: 0.06;
    background-image: linear-gradient(var(--accent-blue) 1px, transparent 1px),
    linear-gradient(90deg, var(--accent-blue) 1px, transparent 1px);
    background-size: 40px 40px;"></div>

  <div style="position: relative; z-index: 1; max-width: 700px; margin: 0 auto;">
    <h2 style="font-size: 2rem; margin-bottom: 1rem;">
      Research-backed. Jargon-free. Built for real organisations.
    </h2>
    <p style="color: var(--text-secondary); font-size: 1.1rem; line-height: 1.8;">
      Every workshop we deliver and every strategy we recommend is grounded in active
      PhD-level research — not recycled blog posts or vendor marketing.
    </p>
  </div>
</section>
```

**Option B — Use a royalty-free quantum image from Unsplash:**
1. Go to [unsplash.com](https://unsplash.com) and search "quantum circuit"
2. Download at 1400px width and save to `webimages/quantum-visual.jpg`
3. Optimise with ImageMagick: `convert quantum-visual.jpg -resize 1400x -quality 75 quantum-bg.jpg`

```html
<section style="position: relative; padding: 5rem 2rem; overflow: hidden;
  background-image: url('../webimages/quantum-bg.jpg');
  background-size: cover; background-position: center;">
  <!-- Dark overlay so text is readable -->
  <div style="position: absolute; inset: 0;
    background: rgba(10, 10, 26, 0.85);"></div>
  <div style="position: relative; z-index: 1; text-align: center;
    max-width: 700px; margin: 0 auto;">
    <h2>Research-backed. Jargon-free. Built for real organisations.</h2>
    <p style="color: var(--text-secondary); margin-top: 1rem;">...</p>
  </div>
</section>
```

**Status:** `[ ]`

---

### Step 4.3 — Upgrade the Service Card Icons to Gradient Style
**Impact:** Medium · **Effort:** 1 hour · **Files:** `index.html`

Once emojis are replaced with SVGs (Step 4.1), add a gradient icon container to match the premium quantum aesthetic:

**Update the service card CSS:**
```css
.service-icon {
  width: 56px;
  height: 56px;
  border-radius: 14px;
  background: linear-gradient(135deg, rgba(0,212,255,0.15), rgba(124,58,237,0.15));
  border: 1px solid rgba(0,212,255,0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.25rem;
}
```

This gives each service card a consistent, premium icon box — the same treatment used by Stripe, Linear, and Vercel.

**Status:** `[ ]`

---

### Step 4.4 — Improve Homepage Section Rhythm
**Impact:** Medium · **Effort:** 1 hour · **Files:** `index.html`

Currently every section has the same padding, same background, same card style. Add alternating treatment:

**For the Research section, change the background:**
```css
.research-section {
  background: rgba(124, 58, 237, 0.04);
  border-top: 1px solid var(--border-color);
  border-bottom: 1px solid var(--border-color);
}
```

**For the About/Team section, remove the section-header and move the team intro text left:**
Instead of stacking "About QuantumBeads" heading above two side-by-side columns, restructure to: text left (mission + approach), team cards right (clickable). This reduces the section height and improves information density.

**Status:** `[ ]`

---

### Step 4.5 — Add Hover States to Navigation Links
**Impact:** Low-Medium · **Effort:** 20 minutes · **Files:** `css/styles.css`

The nav links have a bottom-border hover animation. Ensure it is consistent and add a subtle colour transition:

```css
nav a {
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 0.95rem;
  font-weight: 500;
  transition: color 0.2s ease;
  position: relative;
  padding-bottom: 4px;
}

nav a::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--accent-blue), var(--accent-purple));
  transition: width 0.25s ease;
}

nav a:hover {
  color: var(--accent-blue);
}

nav a:hover::after,
nav a.active::after {
  width: 100%;
}
```

**Status:** `[ ]`

---

## PHASE 5 — Code Quality & Maintainability
> Technical debt cleanup. Do these when you have a quiet afternoon.

---

### Step 5.1 — Consolidate index.html Inline Styles
**Impact:** Low (maintainability) · **Effort:** 2–3 hours · **Files:** `index.html`, `css/styles.css`

`index.html` has an 800+ line `<style>` block that duplicates much of `css/styles.css`. This means changing a colour or font requires editing two files. The fix: move the `index.html` `<style>` block contents into `css/styles.css`, then link `index.html` to `css/styles.css` like all other pages.

**Process:**
1. Copy the contents of the `<style>` block from `index.html`
2. Add them to the bottom of `css/styles.css` (they will override sub-page styles only where the class names are homepage-specific)
3. Remove the `<style>` block from `index.html`
4. Add `<link rel="stylesheet" href="css/styles.css">` to the `<head>` of `index.html`

**Status:** `[ ]`

---

### Step 5.2 — Move Inline Event Handlers to script.js
**Impact:** Low (security/maintainability) · **Effort:** 30 minutes · **Files:** `index.html`, `js/script.js`

The founder cards use `onclick="window.location='fatah-jamro.html'"` and `onmouseover` inline. These belong in JavaScript.

**In `script.js`, add:**
```javascript
// Founder card navigation
document.querySelectorAll('.founder-info[data-href]').forEach(card => {
  card.addEventListener('click', function() {
    window.location = this.dataset.href;
  });
  card.addEventListener('mouseover', function() {
    this.style.borderColor = this.dataset.hoverColor || 'var(--accent-blue)';
    this.style.transform = 'translateY(-4px)';
  });
  card.addEventListener('mouseout', function() {
    this.style.borderColor = '';
    this.style.transform = '';
  });
});
```

**In `index.html`, replace the inline handlers:**
```html
<!-- Before -->
<div class="founder-info" onclick="window.location='fatah-jamro.html'"
  onmouseover="this.style.borderColor='var(--accent-blue)'..." ...>

<!-- After -->
<div class="founder-info" data-href="fatah-jamro.html"
  data-hover-color="var(--accent-blue)" style="cursor: pointer;" ...>
```

**Status:** `[ ]`

---

### Step 5.3 — Standardise File Naming
**Impact:** Low · **Effort:** 30 minutes

Current webimages folder has inconsistent naming: `logo-quantubeads-new-white1.svg` (typo), `logo-quantumbeads-new.png`, `logo-quantumbeads-new-white1.svg`, etc.

**Proposed naming convention:**
```
logo-primary.svg          ← main white SVG logo
logo-primary-dark.svg     ← dark version (if needed)
favicon.ico               ← favicon
og-image.png              ← Open Graph image (1200x630)
team-fatahjamro.png       ← founder photo
team-lalarukh.jpeg        ← founder photo
article-qubit-cover.jpg   ← article cover image
```

**Process:** Rename files, then do a find-replace across all HTML files to update paths. Test locally before pushing.

**Status:** `[ ]`

---

## PHASE 6 — Future Features
> Build these when the business needs them.

---

### Step 6.1 — Add a Contact Form
Replace the email address with a working HTML form that sends to contact@quantumbeads.com.

**Options (all free tiers available):**
- [Formspree](https://formspree.io) — paste your email, get a form endpoint. Works with static sites.
- [EmailJS](https://www.emailjs.com) — JavaScript-based, no backend needed.
- [Web3Forms](https://web3forms.com) — free, clean API for static sites.

**Minimum fields:** Name · Email · Organisation · Message · How did you hear about us?

**Status:** `[ ]`

---

### Step 6.2 — Add a Pricing / Engagement Page
**What to include:**
- Workshop tiers (half-day / full-day / multi-day)
- Consulting engagement types (assessment / roadmap / ongoing retainer)
- "Contact for custom pricing" as the CTA (do not publish prices yet — get on a call first)
- A "What to expect" process section: Intro call → Proposal → Delivery → Follow-up

**Status:** `[ ]`

---

### Step 6.3 — Add Case Studies / Impact Stories
Once you have 2–3 completed engagements, add a Case Studies page:

**Structure per case study:**
- Client type (anonymised if needed: "European R&D organisation")
- Challenge they faced
- What QuantumBeads delivered
- Outcome / feedback

Even one case study transforms the perception of the company from "PhD student doing consulting" to "consultancy with proven results."

**Status:** `[ ]`

---

### Step 6.4 — Set Up a Calendly Integration
1. Create a free account at [calendly.com](https://calendly.com)
2. Set up a "Discovery Call" event (30 minutes)
3. Replace the `mailto:` discovery call link in the contact section with the Calendly URL
4. Optionally embed the Calendly widget inline on the Contact section

**Status:** `[ ]`

---

### Step 6.5 — Add Google Analytics or Privacy-Friendly Analytics
Understanding which pages convert and where visitors drop off is essential for improving the site.

**Privacy-friendly options (GDPR-compliant, no cookie banner needed):**
- [Plausible](https://plausible.io) — €9/month, simple, no cookies
- [Fathom](https://usefathom.com) — similar to Plausible
- [Google Analytics 4](https://analytics.google.com) — free but requires cookie consent banner

**Status:** `[ ]`

---

## Priority Summary

| Step | Impact | Effort | Do First? |
|------|--------|--------|-----------|
| 1.1 Security fix (rel="noopener") | High | 15 min | ✅ Yes |
| 1.2 Fix title inconsistency | Medium | 10 min | ✅ Yes |
| 1.3 Fix footer team links | Medium | 10 min | ✅ Yes |
| 1.4 Fix stale events date | High | 20 min | ✅ Yes |
| 2.1 Open Graph meta tags | High | 1 hour | ✅ Yes |
| 2.2 sitemap.xml | Medium | 20 min | ✅ Yes |
| 3.1 Social proof stats | High | 30 min | ✅ Yes |
| 3.2 Credibility bar | High | 1 hour | ✅ Yes |
| 3.3 Upgrade CTAs | High | 15 min | ✅ Yes |
| 4.1 Replace emoji with SVG | Very High | 2 hours | Soon |
| 4.2 Visual break section | High | 2 hours | Soon |
| 3.5 Add testimonial | Very High | 30 min | When available |
| 6.1 Contact form | High | 2 hours | Next month |
| 5.1 Consolidate CSS | Low | 3 hours | Rainy day |

---

## Current Site Rating by Area

| Area | Score | Priority |
|------|-------|----------|
| Design & Visual | 7/10 | Improve Phase 4 |
| User Experience | 6.5/10 | Improve Phase 3 |
| Conversion | 5/10 | **Urgent — Phase 3** |
| Performance | 7.5/10 | Acceptable |
| Accessibility | 5.5/10 | Improve Phase 1 |
| SEO | 6/10 | Improve Phase 2 |
| Security | 6/10 | **Urgent — Phase 1** |
| Code Quality | 6.5/10 | Phase 5 |
| **Overall** | **6.5/10** | |

**Target after Phase 1–3:** 8/10 — looks and feels like a premium early-stage startup.  
**Target after Phase 4–6:** 9/10 — indistinguishable from a funded quantum consultancy.

---

*This document is a living guide. Update the Status checkboxes as you complete each step. Add new steps as the business evolves.*
