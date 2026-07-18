# MARK ANTHONY TANTONGCO — PORTFOLIO AI SYSTEM PROMPT

**Version:** 2.0  
**Date Generated:** April 2026  
**Purpose:** Complete reconstruction, extension, and AI-assisted enhancement guide  
**Status:** Production-Ready, Copy/Paste Deployment

---

## TABLE OF CONTENTS
1. [BRAND IDENTITY & VOICE](#brand-identity--voice)
2. [VISUAL DESIGN SYSTEM](#visual-design-system)
3. [STRUCTURAL ARCHITECTURE](#structural-architecture)
4. [INTERACTIVE COMPONENTS](#interactive-components)
5. [CONTENT STRUCTURE & MESSAGING](#content-structure--messaging)
6. [TECHNICAL STACK & PERFORMANCE](#technical-stack--performance)
7. [ANIMATION & MOTION DESIGN](#animation--motion-design)
8. [PROJECT & ARC SPECIFICATIONS](#project--arc-specifications)
9. [SEO & METADATA](#seo--metadata)
10. [DEPLOYMENT & MAINTENANCE](#deployment--maintenance)

---

## BRAND IDENTITY & VOICE

### Core Positioning
**Mark Anthony Tantongco** is an **AI Creative Technologist**—a hybrid discipline combining:
- **Prompt Engineering** (AI orchestration & creative direction)
- **Digital Brand Systems** (design tokens, visual identity, scaled production)
- **Generative AI Integration** (WebGPU, Three.js, real-time rendering)
- **Photography AI & ACES Color Science**
- **Full-stack JavaScript** (React, Next.js, creative coding)

### Brand Narrative
Mark builds **"living digital organisms"**—websites, platforms, and experiences that merge:
- **Brutalist aesthetics** (raw, stripped-to-essence design)
- **Hacker/terminal culture** (CLI-inspired, monospace moments)
- **Cinematic web experiences** (WebGPU, Three.js real-time rendering)
- **Data-driven storytelling** (metrics, visual proofs, impact clarity)

He solves problems at the **intersection of AI, code, and human creativity**—not as a pure technologist, nor as a pure designer, but as someone who **orchestrates all three**.

### Tone & Voice
- **Direct.** No fluff. Statements, not questions.
- **Confident.** Strong opinions on design & tech; owns decisions.
- **Accessible.** Explains the "why" without jargon bloat.
- **Filipino-rooted.** Cultural awareness, family values, community-first mindset.
- **Future-facing.** Excited about what's possible *now* with AI, not speculation.

**Word choice patterns:**
- "Built," "orchestrated," "shaped," "engineered," "shipped"
- Avoid: "created," "designed," "developed" (too passive)
- Metric-focused: "$X impact," "Y% improvement," "Z users reached"

---

## VISUAL DESIGN SYSTEM

### Color Palette

#### Dark Mode (Default)
```
--neon:           #ccff00 (Lime green, primary accent)
--cyan:           #00ffff (Cyan, secondary accent)
--accent:         #ccff00 (Lime, primary CTA/focus)
--accent-dim:     rgba(204,255,0,.08) (8% opacity, backgrounds)
--accent-mid:     rgba(204,255,0,.38) (38% opacity, borders/dividers)

--bg:             #0a0a0a (Pure black base)
--bg2:            #0f0f0f (Dark gray, cards/sections)
--bg3:            #181818 (Lighter gray, elevated)
--fg:             #efefef (White text)
--fg2:            rgba(239,239,239,.58) (Secondary text, 58% opacity)
--fg3:            rgba(239,239,239,.25) (Tertiary text, 25% opacity)

--border:         rgba(204,255,0,.2) (20% accent opacity)
--bs (border-simple): 1.5px solid rgba(204,255,0,.2)

--card:           #0f0f0f
--nav-bg:         rgba(10,10,10,.92) (Translucent dark)

--danger:         #ff3b30 (iOS red)
--success:        #00e676 (Bright green, confirmation)
```

#### Light Mode Variant
- **Inverted palette:** Light backgrounds (#f5f4ef), dark text (#0d0d0d)
- **Accent adjusted:** --radar-stroke: #5a6e00 (desaturated lime)
- **Preserves** contrast ratios and interactive hierarchy

### Typography

#### Font Stack
```
Bebas Neue       — Logo, heroic headers (sans-serif, all-caps)
DM Sans          — Body text, nav, conversational (sans-serif, humanist)
DM Mono          — Code, technical labels, terminal feel (monospace)
```

**Loaded via Google Fonts:**
```html
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&family=DM+Mono:wght@400;500&display=swap">
```

#### Type Scale & Usage
| Element | Font | Size | Weight | Letter-Spacing | Usage |
|---------|------|------|--------|-----------------|-------|
| Logo / Nav | Bebas Neue | 1.5rem | Regular | 0.12em | Branded identity |
| Section Headers | Bebas Neue | 2.5–4rem | Regular | 0.05em | Hero moments |
| H1 (Hero) | Bebas Neue | 3.5rem | Regular | 0.05em | Page hero |
| H2 / H3 | DM Sans | 2rem / 1.5rem | 500 | 0 | Section headers |
| Body Text | DM Sans | 1rem | 400 | 0 | Paragraphs, descriptions |
| Nav Links | DM Mono | 0.58rem | 400 | 0.18em | Navigation, uppercase |
| Labels / Tags | DM Mono | 0.75rem | 500 | 0.15em | Skills, badges |
| Code / Terminal | DM Mono | 0.875rem | 400 | 0 | Code blocks, CLI |

### Layout & Spacing
- **Max-width container:** 1200px (with 2rem padding on mobile)
- **Grid:** CSS Grid + Flexbox hybrid
- **Section padding:** 4–6rem vertical (responsive 2–4rem mobile)
- **Gap/margin ratios:** 8px, 16px, 24px, 32px, 48px base units
- **Border radius:** Minimal (0–8px), mostly sharp edges (brutalism)
- **Scrollbar:** 2px width, accent color (visible, not hidden)

### Component Patterns

#### Buttons & CTAs
```css
/* Primary (lime accent) */
.btn-primary {
  background: transparent;
  color: var(--accent);
  border: 1.5px solid var(--accent);
  padding: 12px 24px;
  font-family: 'DM Mono';
  font-size: 0.75rem;
  letter-spacing: 0.12em;
  cursor: pointer;
  transition: background .3s, color .3s;
}
.btn-primary:hover {
  background: var(--accent);
  color: var(--bg);
}
```

#### Cards & Containers
- **Background:** var(--card) (#0f0f0f)
- **Border:** 1.5px solid rgba(204,255,0,.2)
- **Padding:** 24–32px
- **Border-radius:** 2–4px (sharp)
- **Shadow:** None (brutalism), OR subtle (8px blur, 2% opacity) on hover

#### Dividers & Separators
- **Accent color:** #ccff00 at 20% opacity
- **Height:** 1–1.5px
- **Width:** Full-width or contained (80%)
- **Margin:** 2rem above/below

---

## STRUCTURAL ARCHITECTURE

### Page Layout
```
┌─────────────────────────────────────┐
│  NAV (fixed, z-index 800)          │
├─────────────────────────────────────┤
│  HERO / IDENTITY (ScrollTrigger)    │
├─────────────────────────────────────┤
│  OVERVIEW / BIO                      │
├─────────────────────────────────────┤
│  SKILLS & RADAR CHART                │
├─────────────────────────────────────┤
│  SERVICES (4 cards, grid)            │
├─────────────────────────────────────┤
│  PROCESS (5-step horizontal timeline)│
├─────────────────────────────────────┤
│  FEATURED PROJECTS (grid, clickable) │
├─────────────────────────────────────┤
│  TIMELINE / ARC (vertical, indexed)  │
├─────────────────────────────────────┤
│  BLOG / WRITING (list)               │
├─────────────────────────────────────┤
│  CONTACT / CTA                       │
└─────────────────────────────────────┘
```

### Navigation Structure
```html
<nav>
  <!-- Logo (left) -->
  <div class="nav-logo">MAT</div>
  
  <!-- Links (center) -->
  <ul class="nav-links">
    <li><a href="#identity">Identity</a></li>
    <li><a href="#overview">About</a></li>
    <li><a href="#skills">Skills</a></li>
    <li><a href="#services">Services</a></li>
    <li><a href="#process">Process</a></li>
    <li><a href="#projects">Work</a></li>
    <li><a href="#arc">Arc</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
  
  <!-- Theme toggle + social (right) -->
  <div class="nav-right">
    <button class="theme-btn"></button>
    <a href="https://github.com/marktantongco">GitHub</a>
  </div>
</nav>
```

### Section IDs (For Scrollspy)
- `#identity` — CLI typewriter intro
- `#overview` — Bio/mission
- `#skills` — Radar chart
- `#services` — Service cards
- `#process` — Process steps
- `#projects` — Project grid
- `#arc` — Timeline
- `#blog` — Blog/writing
- `#contact` — Contact form

---

## INTERACTIVE COMPONENTS

### 1. Cursor System
**Custom cursor replacing native pointer:**

```javascript
// Dual-element cursor: blob (ring) + dot (center)
const cursorBlob = document.getElementById('cursor-blob');
const cursorDot = document.getElementById('cursor-dot');

document.addEventListener('mousemove', (e) => {
  cursorBlob.style.left = e.clientX + 'px';
  cursorBlob.style.top = e.clientY + 'px';
  cursorDot.style.left = e.clientX + 'px';
  cursorDot.style.top = e.clientY + 'px';
});

// Expand on hover
document.addEventListener('mouseover', (e) => {
  if (e.target.matches('button, a, [data-hover]')) {
    cursorBlob.classList.add('hov');
  }
});
```

**Blob styling:**
```css
#cursor-blob {
  width: 40px;
  height: 40px;
  border: 2px solid var(--accent);
  border-radius: 50%;
  pointer-events: none;
  mix-blend-mode: difference;
  z-index: 9999;
}
#cursor-blob.hov {
  width: 64px;
  height: 64px;
  opacity: 0.7;
}
#cursor-dot {
  width: 5px;
  height: 5px;
  background: var(--accent);
  border-radius: 50%;
  z-index: 10000;
}
```

**When to apply `.hov` class:**
- Buttons, links, form fields
- Interactive cards
- Skill pills
- Project cards
- Tab triggers

---

### 2. CLI Typewriter Identity Component
**Progressive text reveal simulating terminal input:**

```javascript
function initTypewriter() {
  const lines = [
    { text: '$ whoami', delay: 0 },
    { text: 'mark-anthony-tantongco', delay: 800, style: 'accent' },
    { text: '$ ls -la ~/skills', delay: 1600 },
    { text: '[prompt-engineering] [design-systems] [webgpu]', delay: 2400, style: 'accent' },
    { text: '$ cat philosophy.txt', delay: 3200 },
    { text: 'Building living digital organisms at the intersection of AI, code, and human creativity.', delay: 4000, style: 'accent' }
  ];
  
  lines.forEach(line => {
    setTimeout(() => {
      typewriterLine(line.text, line.style);
    }, line.delay);
  });
}

function typewriterLine(text, style) {
  const container = document.getElementById('typewriter');
  const lineEl = document.createElement('div');
  lineEl.className = style ? `typewriter-line ${style}` : 'typewriter-line';
  let index = 0;
  
  const type = () => {
    if (index < text.length) {
      lineEl.textContent += text[index];
      index++;
      setTimeout(type, 30); // 30ms per char
    } else {
      lineEl.classList.add('complete');
    }
  };
  
  container.appendChild(lineEl);
  type();
}
```

**Styling:**
```css
#typewriter {
  font-family: 'DM Mono', monospace;
  font-size: 0.95rem;
  line-height: 1.8;
  color: var(--fg2);
  letter-spacing: 0.02em;
}

.typewriter-line {
  margin-bottom: 1rem;
  opacity: 0;
  animation: fadeIn 0.3s ease forwards;
}

.typewriter-line.accent {
  color: var(--accent);
  font-weight: 500;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
```

---

### 3. Live Radar Skills Chart
**Chart.js radar visualization, updates on skill pill hover:**

```javascript
const radarCtx = document.getElementById('skills-radar').getContext('2d');
let radarChart = null;

const skillCategories = {
  'AI/Generative': { data: [85, 78, 92, 88], color: '#ccff00' },
  'Dev/Engineering': { data: [88, 92, 85, 78], color: '#00ffff' },
  'Visual/Brand': { data: [92, 85, 88, 90], color: '#7c3aed' },
  'Strategy': { data: [78, 88, 85, 92], color: '#10b981' }
};

function initRadar() {
  radarChart = new Chart(radarCtx, {
    type: 'radar',
    data: {
      labels: ['Prompt Engineering', 'System Design', 'Visual Direction', 'Product Strategy'],
      datasets: [
        {
          label: 'Mark Anthony Tantongco',
          data: [88, 85, 90, 86],
          borderColor: '#ccff00',
          backgroundColor: 'rgba(204, 255, 0, 0.08)',
          borderWidth: 2,
          pointRadius: 5,
          pointBackgroundColor: '#ccff00',
          pointBorderColor: '#0a0a0a',
          pointBorderWidth: 2,
          pointHoverRadius: 8
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      scales: {
        r: {
          beginAtZero: true,
          max: 100,
          ticks: { color: 'var(--fg3)', font: { family: "'DM Mono'" } },
          grid: { color: 'rgba(204, 255, 0, 0.1)' },
          angleLines: { color: 'rgba(204, 255, 0, 0.1)' }
        }
      },
      plugins: {
        legend: { display: true, labels: { color: 'var(--fg2)', font: { family: "'DM Mono'" } } }
      }
    }
  });
}

// Skill pill hover behavior
document.querySelectorAll('.skill-pill').forEach(pill => {
  pill.addEventListener('mouseenter', () => {
    const category = pill.dataset.category;
    const newData = skillCategories[category].data;
    radarChart.data.datasets[0].data = newData;
    radarChart.data.datasets[0].borderColor = skillCategories[category].color;
    radarChart.data.datasets[0].backgroundColor = 
      skillCategories[category].color.replace(')', ', 0.08)').replace('rgb', 'rgba');
    radarChart.update('none'); // no animation
  });
});
```

---

### 4. Project Card Click & Popup System

**Data structure (JavaScript):**
```javascript
const POP_PROJECTS = [
  {
    color: 'photography',
    title: 'AI Photography Pipeline',
    subtitle: 'End-to-end image processing with ACES color science',
    metrics: [
      { label: '200+', desc: 'Assets processed' },
      { label: '40%', desc: 'Faster workflow' },
      { label: '99.2%', desc: 'Color accuracy' }
    ],
    demo: 'canvas', // Canvas 3D or visual
    code: `
const aces = new ACESFilm({
  exposure: 1.2,
  colorSpace: 'rec709'
});
aces.process(imageData);
    `,
    results: [
      '✓ Reduced post-production time by 40%',
      '✓ Achieved cinema-standard color grading',
      '✓ Integrated into 10+ client workflows'
    ],
    cta: { text: 'View Case Study', url: '#' }
  },
  // ... more projects
];

const POP_ARC = [
  // Timeline/arc entries with same structure
];
```

**Popup DOM structure:**
```html
<div id="popup-overlay" class="popup-overlay">
  <div id="popup-shell" class="popup-shell" data-color="photography">
    <button id="popup-close-btn" class="popup-close">✕</button>
    
    <h2 class="popup-title">AI Photography Pipeline</h2>
    <p class="popup-subtitle">End-to-end image processing with ACES color science</p>
    
    <!-- Tabs -->
    <div class="popup-tabs">
      <button class="popup-tab active" data-tab="overview">Overview</button>
      <button class="popup-tab" data-tab="demo">Demo</button>
      <button class="popup-tab" data-tab="code">Code</button>
      <button class="popup-tab" data-tab="results">Results</button>
    </div>
    
    <!-- Tab Panels -->
    <div id="tab-overview" class="popup-panel active">
      <div class="popup-metrics">
        <div class="popup-metric">
          <div class="popup-metric-n">200+</div>
          <div class="popup-metric-d">Assets processed</div>
        </div>
        <!-- more metrics -->
      </div>
    </div>
    
    <div id="tab-demo" class="popup-panel">
      <div id="popup-demo-wrap" style="width: 100%; height: 300px;"></div>
    </div>
    
    <div id="tab-code" class="popup-panel">
      <pre id="code-content">const aces = ...</pre>
      <button class="popup-code-copy" onclick="copyCode()">Copy Code</button>
    </div>
    
    <div id="tab-results" class="popup-panel">
      <div class="popup-results">
        <div>✓ Reduced post-production time by 40%</div>
      </div>
    </div>
    
    <div class="popup-cta-row">
      <a href="#" class="btn-primary">View Case Study</a>
    </div>
  </div>
</div>
```

**Open/close logic:**
```javascript
function openPopup(projectData, type) {
  const overlay = document.getElementById('popup-overlay');
  const shell = document.getElementById('popup-shell');
  
  // Populate data
  shell.setAttribute('data-color', projectData.color);
  shell.querySelector('.popup-title').textContent = projectData.title;
  // ... populate other fields
  
  // Animate in
  overlay.classList.add('open');
  document.body.style.overflow = 'hidden';
  gsap.fromTo(shell, 
    { y: 50, opacity: 0, scale: 0.96 },
    { y: 0, opacity: 1, scale: 1, duration: 0.4, ease: 'power2.out' }
  );
}

function closePopup() {
  const overlay = document.getElementById('popup-overlay');
  const shell = document.getElementById('popup-shell');
  gsap.to(shell, {
    y: 30, opacity: 0, scale: 0.96, duration: 0.3, ease: 'power2.in',
    onComplete: () => {
      overlay.classList.remove('open');
      document.body.style.overflow = '';
    }
  });
}
```

---

### 5. Timeline / Arc Component
**Vertical scrollable timeline with indexed nodes:**

```html
<div id="arc" class="timeline">
  <div class="tl-item" data-index="0">
    <div class="tl-dot"></div>
    <div class="tl-line"></div>
    <div class="tl-card">
      <h3>Started exploring prompt engineering</h3>
      <span class="tl-date">2023</span>
      <div class="tl-hint">Tap to explore</div>
    </div>
  </div>
  
  <div class="tl-item" data-index="1">
    <div class="tl-dot"></div>
    <div class="tl-line"></div>
    <div class="tl-card">
      <h3>Built first gen AI platform for Pacific Cross</h3>
      <span class="tl-date">2024</span>
    </div>
  </div>
  <!-- more items -->
</div>
```

**Timeline styling:**
```css
.timeline {
  position: relative;
  padding: 4rem 2rem;
}

.tl-item {
  display: grid;
  grid-template-columns: 60px 1fr;
  gap: 2rem;
  margin-bottom: 3rem;
  position: relative;
}

.tl-dot {
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: var(--accent);
  border: 3px solid var(--bg);
  position: relative;
  top: 28px;
  transition: scale 0.3s;
}

.tl-line {
  position: absolute;
  left: 30px;
  top: 50px;
  width: 2px;
  height: calc(100% + 2rem);
  background: var(--border);
}

.tl-card {
  background: var(--card);
  border: var(--bs);
  padding: 1.5rem;
  cursor: pointer;
  transition: all 0.3s;
}

.tl-card:hover {
  border-color: var(--accent);
  background: var(--bg3);
  transform: translateX(8px);
}
```

**Arc data structure:**
```javascript
const POP_ARC = [
  {
    color: 'tl-c0',
    title: 'Explored generative AI foundations',
    subtitle: 'Deep dive into prompt engineering patterns',
    date: '2023',
    // ... rest of structure like projects
  },
  // indexed 0, 1, 2, 3, 4, 5, 6
];
```

---

## CONTENT STRUCTURE & MESSAGING

### Hero Section
```html
<section id="identity" class="hero">
  <div class="hero-content">
    <h1 class="hero-title">Mark Anthony Tantongco</h1>
    <p class="hero-subtitle">AI Creative Technologist</p>
    <div id="typewriter" class="typewriter-container"></div>
    <div class="hero-cta">
      <a href="#services" class="btn-primary">Explore Work</a>
      <a href="#contact" class="btn-secondary">Get in Touch</a>
    </div>
  </div>
</section>
```

### Overview / Bio
**Keep it under 3 sentences. Show proof, not promises.**

Example copy:
> I orchestrate AI, design, and code to build experiences that feel alive. Over the past 18 months, I've shipped production platforms for 50K+ users, engineered prompt systems that reduce iteration time by 60%, and led creative direction on digital brand systems used by 5+ insurance companies in the Philippines. My work lives at the intersection—not pure tech, not pure design, but the amplification that happens when they meet.

### Services (4 Cards)
1. **Prompt Engineering & AI Direction**
   - Orchestrating complex LLM workflows
   - Building mental models for teams
   - Reducing prompt iteration time

2. **Digital Brand Systems**
   - Design tokens & component libraries
   - Scalable visual language
   - Brand-to-code pipeline

3. **WebGPU & Real-Time Rendering**
   - Three.js + custom shaders
   - Performance-first animations
   - GPU-accelerated visuals

4. **Photography AI & ACES Pipeline**
   - Color-accurate image processing
   - Automated asset workflows
   - Production-grade output

### Process (5 Steps)
1. **Discovery** — Understand the problem space, user needs, constraints
2. **Strategy** — Define North Star, KPIs, technical approach
3. **Prototype** — Build high-fidelity prototypes, test hypotheses
4. **Polish** — Refine interactions, performance, accessibility
5. **Deploy** — Ship to production, measure, iterate based on data

### Featured Projects (Grid)
**Show 4–6 highest-impact projects with:**
- Hero image or canvas preview
- Title + subtitle
- 3 key metrics
- "Explore" CTA

**Sort by:**
1. User impact (most users/reach first)
2. Technical novelty (WebGPU, novel AI integration)
3. Business impact (revenue, retention, cost savings)

### Blog / Writing
**Link to or embed recent articles on:**
- Prompt engineering techniques
- Design system thinking
- AI integration patterns
- Creative coding tutorials

---

## TECHNICAL STACK & PERFORMANCE

### Core Libraries
```html
<!-- Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">

<!-- Three.js (3D rendering) -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

<!-- GSAP (animation engine) -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>

<!-- Chart.js (data visualization) -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
```

### Performance Optimizations
- **Lazy loading:** Images via `loading="lazy"`, sections via Intersection Observer
- **Code splitting:** Separate files for heavy components (Three.js, popup logic)
- **CSS optimization:** Minified, no unused styles, critical CSS inline
- **Font subsetting:** Only include required characters
- **WebP images:** With PNG fallback
- **Scroll optimization:** RequestAnimationFrame for smooth 60fps animations
- **Debouncing:** Resize/scroll events (300ms throttle)

### Accessibility (A11y)
- **Color contrast:** All text meets WCAG AA (4.5:1 ratio)
- **Focus states:** Visible outline on all interactive elements
- **Keyboard nav:** Tab through nav, popups, buttons; Escape closes popups
- **ARIA labels:** `aria-label`, `aria-expanded`, `aria-hidden` where needed
- **Alt text:** All images, icons
- **Semantic HTML:** `<nav>`, `<section>`, `<article>`, `<button>` instead of divs

### Mobile Responsiveness
```css
/* Breakpoints */
@media (max-width: 768px) {
  /* Stack grids vertically */
  /* Reduce padding/margins */
  /* Adjust font sizes */
  /* Hide desktop-only elements */
}

@media (max-width: 480px) {
  /* Single-column layout */
  /* Smaller headings */
  /* Full-width cards */
  /* Touch-friendly spacing (48px min tap targets) */
}
```

---

## ANIMATION & MOTION DESIGN

### GSAP ScrollTrigger Patterns

#### Section Entrance (Fade + Slide)
```javascript
ScrollTrigger.create({
  trigger: '#services',
  start: 'top 80%',
  once: true, // Fire only once
  onEnter: () => {
    gsap.fromTo('#services .services-heading',
      { opacity: 0, y: 60, skewY: 2 },
      { opacity: 1, y: 0, skewY: 0, duration: 1, ease: 'expo.out' }
    );
    gsap.fromTo('.service-card',
      { opacity: 0, y: 50, scale: 0.95 },
      { opacity: 1, y: 0, scale: 1, duration: 0.8, stagger: 0.15, delay: 0.25, ease: 'back.out(1.4)' }
    );
  }
});
```

#### Parallax Scroll Effect
```javascript
gsap.to('.parallax-element', {
  y: (i, target) => -window.innerHeight * 0.5,
  scrollTrigger: {
    trigger: target,
    start: 'top bottom',
    end: 'bottom top',
    scrub: 1, // Tied to scrollbar
    markers: false
  }
});
```

#### Hover Interactions
```javascript
// Button expand
gsap.to(button, { 
  duration: 0.3, 
  scale: 1.05, 
  ease: 'back.out(2)', 
  overwrite: 'auto' 
}, 'mouseenter');

// Cursor blob expansion
gsap.to(cursorBlob, {
  width: 64,
  height: 64,
  opacity: 0.7,
  duration: 0.2,
  ease: 'power2.out'
});
```

#### Tab Switch Animation
```javascript
gsap.fromTo('.popup-panel.active > *',
  { opacity: 0, y: 16 },
  { opacity: 1, y: 0, duration: 0.45, stagger: 0.055, ease: 'power2.out', clearProps: 'all' }
);
```

### Easing Functions (Preset)
- `expo.out` — Energetic entrances (snappy, quick decel)
- `power2.out` — Standard UI interactions (smooth)
- `back.out(1.4–2)` — Bouncy hover states
- `elastic.out(1,.6)` — Playful, spring-like
- `power2.in` — Exit animations (smooth accelerate)

### Motion Principles
- **Duration:** 0.2–0.4s for micro-interactions, 0.6–1s for section entrances
- **Stagger:** 0.1–0.15s between child animations (not too fast/slow)
- **Delay:** 0.2–0.4s between section triggers
- **Overwrite:** `'auto'` to prevent animation conflicts
- **ClearProps:** Remove inline styles post-animation (cleaner DOM)

---

## PROJECT & ARC SPECIFICATIONS

### Project Card Data Model
```javascript
{
  color: 'photography', // Used for popup accent color
  title: 'AI Photography Pipeline',
  subtitle: 'End-to-end image processing with ACES color science',
  heroImage: 'https://...',
  
  // Overview tab
  challenge: 'Color accuracy and workflow speed were bottlenecks...',
  solution: 'Built automated ACES-compliant pipeline...',
  
  // Metrics
  metrics: [
    { label: '200+', desc: 'Assets processed' },
    { label: '40%', desc: 'Time savings' },
    { label: '99.2%', desc: 'Color accuracy' }
  ],
  
  // Demo tab
  demo: 'three-js' | 'canvas' | 'html', // Type of demo
  demoCode: 'https://...' | function, // Render function
  
  // Code tab
  code: `
    const aces = new ACESFilm({ exposure: 1.2 });
    aces.process(imageData);
  `,
  
  // Results tab
  results: [
    '✓ Reduced post-production time by 40%',
    '✓ Achieved cinema-standard color grading',
    '✓ Integrated into 10+ client workflows'
  ],
  
  // CTA
  cta: {
    text: 'View Case Study',
    url: 'https://...'
  },
  
  // Metadata
  tags: ['AI', 'Photography', 'ACES Color', 'Automation'],
  year: 2024,
  impact: 8.5 // 1-10 scale for sorting
}
```

### Arc / Timeline Entry Model
```javascript
{
  color: 'tl-c0', // From: tl-c0 (lime) to tl-c5 (green)
  date: '2023',
  title: 'Explored prompt engineering foundations',
  subtitle: 'Built first CLI tool for LLM orchestration',
  
  // Same popup structure as projects
  challenge: '...',
  solution: '...',
  metrics: [...],
  results: [...],
  demo: '...',
  code: '...',
  cta: { text: '...', url: '...' },
  
  index: 0 // 0-6, mapped to tl-c0 through tl-c5
}
```

---

## SEO & METADATA

### HTML Head
```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mark Anthony Tantongco — AI Creative Technologist</title>
<meta name="description" content="AI Creative Technologist. Prompt Engineering. Digital Brand Systems. Building living digital organisms at the frontier of AI and design.">
<meta name="author" content="Mark Anthony Tantongco">
<meta name="keywords" content="AI, prompt engineering, design systems, WebGPU, digital branding, Philippines">

<!-- OG Social -->
<meta property="og:title" content="Mark Anthony Tantongco — AI Creative Technologist">
<meta property="og:description" content="Building living digital organisms at the intersection of AI, code, and human creativity.">
<meta property="og:image" content="https://marktantongco.com/og-image.jpg">
<meta property="og:url" content="https://marktantongco.com">
<meta property="og:type" content="website">

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Mark Anthony Tantongco — AI Creative Technologist">
<meta name="twitter:description" content="Building living digital organisms at the intersection of AI, code, and human creativity.">
<meta name="twitter:image" content="https://marktantongco.com/og-image.jpg">
<meta name="twitter:creator" content="@markytanky">

<!-- Structured Data (JSON-LD) -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Mark Anthony Tantongco",
  "jobTitle": "AI Creative Technologist",
  "url": "https://marktantongco.com",
  "image": "https://marktantongco.com/mark.jpg",
  "sameAs": [
    "https://github.com/marktantongco",
    "https://instagram.com/markytanky",
    "https://linkedin.com/in/marktantongco1"
  ],
  "knowsAbout": [
    "Prompt Engineering",
    "Generative AI",
    "Design Systems",
    "WebGPU",
    "GSAP",
    "React",
    "Next.js"
  ]
}
</script>

<!-- Canonical -->
<link rel="canonical" href="https://marktantongco.com">

<!-- Preconnect -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="dns-prefetch" href="https://cdnjs.cloudflare.com">
```

### SEO Best Practices
- **H1:** One per page, include main keyword
- **Internal links:** Link to projects, blog, case studies
- **Image alt text:** Descriptive, not keyword-stuffed
- **Page speed:** < 2s Largest Contentful Paint (LCP)
- **Mobile-first:** Responsive, touch-friendly
- **Structured data:** Person, SoftwareApplication (for components)
- **Sitemap:** Submit sitemap.xml to Search Console
- **Robot.txt:** Allow crawling, disallow admin paths

---

## DEPLOYMENT & MAINTENANCE

### Build & Hosting
**Recommended stack:**
- **Hosting:** Vercel, Netlify, or Cloudflare Pages (fast, free HTTPS, Git integration)
- **Domain:** marktantongco.com (GoDaddy, Namecheap, Google Domains)
- **Email:** hi@marktantongco.com via Cloudflare Email Routing or Gmail
- **Analytics:** Vercel Analytics or Plausible (privacy-first, no cookies)

### Deployment Checklist
- [ ] Minify CSS & JavaScript
- [ ] Optimize all images (WebP + PNG fallback)
- [ ] Test on Chrome, Safari, Firefox, mobile browsers
- [ ] Validate HTML (W3C validator)
- [ ] Check Lighthouse score (target: 90+ all categories)
- [ ] Test keyboard navigation (Tab, Enter, Escape)
- [ ] Verify all links work (internal + external)
- [ ] Test popups on mobile (touch close, swipe)
- [ ] Check dark/light mode toggle
- [ ] Verify analytics fire correctly

### Content Updates
**Update frequency:**
- **Projects:** Monthly (new case study or featured work)
- **Blog:** Bi-weekly (insights, tutorials, retrospectives)
- **Arc/Timeline:** Quarterly (milestones, learnings)
- **Skills radar:** As needed (new capabilities, depth changes)
- **Bio/headline:** Yearly review and refresh

### Analytics Events to Track
```javascript
// Project view
gtag('event', 'view_project', { project_name: 'AI Photography Pipeline' });

// Popup tab switch
gtag('event', 'popup_tab_switch', { tab: 'demo', project: 'photography' });

// CTA click
gtag('event', 'cta_click', { cta_text: 'View Case Study', project: 'photography' });

// Contact form submit
gtag('event', 'contact_form', { status: 'submitted' });
```

### Maintenance & Monitoring
- **Uptime:** Uptime Robot (monitor for 99.9%+ availability)
- **Errors:** Sentry or LogRocket (capture JS errors in prod)
- **Performance:** Web Vitals dashboard (LCP, FID, CLS)
- **Backups:** Version control (GitHub), automated backups
- **Security:** HTTPS always, no plain text passwords, CSP headers

---

## ADVANCED CUSTOMIZATION GUIDE

### Color Scheme Variants
**To change accent color from lime to another:**
1. Update `--neon`, `--accent`, `--accent-dim`, `--accent-mid` in CSS variables
2. Update Bebas Neue font color in nav/headers
3. Update border color (uses accent at 20% opacity)
4. Re-test contrast ratios (WCAG AA minimum 4.5:1)

Example (blue accent):
```css
--neon: #0099ff;
--cyan: #00d4ff;
--accent: #0099ff;
--accent-dim: rgba(0, 153, 255, 0.08);
--accent-mid: rgba(0, 153, 255, 0.38);
--border: rgba(0, 153, 255, 0.2);
```

### Adding New Project
1. Create data object in `POP_PROJECTS` array
2. Match color to accent (or choose from: `photography`, `brand`, `webgpu`, `seo`)
3. Add project card to `.projects-grid`
4. Wire up click handler (auto-wired if `data-idx` matches array index)
5. Populate all popup tabs (overview, demo, code, results)
6. Test popup on desktop + mobile

### Three.js Canvas Integration
For project demos requiring 3D rendering:

```javascript
function buildPopupDemo(demoType, catDot) {
  const canvas = document.createElement('canvas');
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(75, canvas.width / canvas.height);
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
  
  // Your demo logic here
  const mesh = new THREE.Mesh(
    new THREE.IcosahedronGeometry(2, 4),
    new THREE.MeshPhongMaterial({ color: 0xccff00 })
  );
  scene.add(mesh);
  
  const animate = () => {
    requestAnimationFrame(animate);
    mesh.rotation.x += 0.005;
    mesh.rotation.y += 0.008;
    renderer.render(scene, camera);
  };
  animate();
  
  document.getElementById('popup-demo-wrap').appendChild(canvas);
}
```

---

## QUICK REFERENCE CHECKLISTS

### Before Publishing
- [ ] All links tested and working
- [ ] Images optimized and compressed
- [ ] Typos and grammar checked
- [ ] Lighthouse score 90+
- [ ] Mobile responsive (tested on real devices)
- [ ] Accessibility audit passed
- [ ] Meta tags and OG images set
- [ ] Analytics configured
- [ ] SSL certificate active
- [ ] Form validation working

### Monthly Maintenance
- [ ] Check error logs (Sentry)
- [ ] Review analytics (users, bounce rate, conversions)
- [ ] Update project showcase (remove stale, add new)
- [ ] Test all CTAs and external links
- [ ] Performance check (Lighthouse, Core Web Vitals)
- [ ] Backup database/content

### Quarterly Review
- [ ] Refresh bio/headline if needed
- [ ] Review and update skills radar
- [ ] Add new timeline/arc entry if applicable
- [ ] Audit brand messaging for consistency
- [ ] Plan next 3 months of content/projects

---

## SUPPORT & EXTENSION

### Common Modifications
**Change hero text:**
Update `#identity` section or modify typewriter data

**Reorder projects:**
Change `data-idx` on project cards, reorder `POP_PROJECTS` array

**Add new section:**
Create section, assign unique ID, wire nav link, add ScrollTrigger entrance

**Modify color theme:**
Update CSS variables in `:root` or `[data-theme]`

**Change fonts:**
Replace Google Fonts import, update font-family in CSS

### Resources
- **GSAP Docs:** https://greensock.com/docs/
- **Three.js Docs:** https://threejs.org/docs/
- **Chart.js Docs:** https://www.chartjs.org/docs/
- **CSS Variables:** https://developer.mozilla.org/en-US/docs/Web/CSS/--*
- **Accessibility:** https://www.a11y-101.com/

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 2.0 | April 2026 | Complete system prompt with all components, animations, data models |
| 1.0 | March 2026 | Initial portfolio launch |

---

**End of AI System Prompt**

*This document is living. Update as brand, projects, or technical stack evolve.*
