/**
 * app/page.tsx — root landing page.
 *
 * Renders a minimal index that points to:
 *   - /demo            → live 3-Layer Animation Stack (Three.js + GSAP + Framer Motion)
 *   - /index.html      → the static PWA (Knowledge Base + skill catalog)
 *   - GitHub Pages mirror, GitHub repo, 21st.dev component search
 *
 * The static PWA files (index.html, kb.html, sw.js, manifest.json, icons,
 * stacks.json, mcp-registry.json, og-image.png, rss.xml, sitemap.xml,
 * robots.txt) live in /public and are served at the root path, so existing
 * URLs and service-worker caches keep working.
 *
 * 'use client' is required because DemoCard uses onMouseEnter/onMouseLeave
 * for hover effects. Route metadata for / is inherited from app/layout.tsx.
 */

'use client';

import Link from 'next/link';

export default function Home() {
  return (
    <main
      style={{
        minHeight: '100vh',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '2rem',
        gap: '1.5rem',
        background:
          'radial-gradient(1200px 600px at 50% -10%, rgba(80,120,255,0.18), transparent 60%), #05060a',
      }}
    >
      <div style={{ textAlign: 'center', maxWidth: 720 }}>
        <p
          style={{
            margin: 0,
            fontSize: '0.75rem',
            letterSpacing: '0.3em',
            textTransform: 'uppercase',
            color: '#8ab4ff',
          }}
        >
          opencode OS
        </p>
        <h1
          style={{
            margin: '0.5rem 0 1rem',
            fontSize: 'clamp(2rem, 5vw, 3.25rem)',
            lineHeight: 1.05,
            fontWeight: 800,
            background:
              'linear-gradient(120deg, #f8f9fc 0%, #8ab4ff 60%, #c084fc 100%)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent',
            backgroundClip: 'text',
          }}
        >
          Skills registry &amp; live demos
        </h1>
        <p style={{ margin: 0, color: '#9198ad', fontSize: '1.05rem', lineHeight: 1.5 }}>
          90+ curated agent skills, MCP server stacks, and reference
          implementations. This Next.js route hosts the live demos; the
          full PWA knowledge base lives at{' '}
          <Link href="/index.html">/index.html</Link>.
        </p>
      </div>

      <div
        style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))',
          gap: '1rem',
          width: '100%',
          maxWidth: 880,
        }}
      >
        <DemoCard
          href="/demo"
          title="3-Layer Animation Stack"
          subtitle="Three.js · GSAP · Framer Motion"
          description="Live reference implementation of strict separation: Three.js owns scene & objects, GSAP owns camera + scroll, Framer Motion owns UI overlays. Lazy-loaded with next/dynamic (ssr:false)."
          accent="#8B5CF6"
        />
        <DemoCard
          href="/index.html"
          title="Knowledge Base PWA"
          subtitle="90+ skills · 6 zones · installable"
          description="The full static PWA — skill catalog with install commands, MCP server stacks, doctrine tree, hero zone-gating, My Stack pin, command palette search."
          accent="#06B6D4"
        />
        <DemoCard
          href="https://github.com/marktantongco/opencode-accomplishments"
          title="GitHub repo"
          subtitle="source · AGENTS.md · skills/"
          description="Canonical source. AGENTS.md includes System Master Prompt v4 doctrine. skills/animation-3d-layered-architect/SKILL.md documents the 3-layer pattern; skills/parallel-deep-research-orchestrator/SKILL.md documents the fan-out/fan-in research pipeline."
          accent="#10B981"
        />
      </div>

      <p
        style={{
          marginTop: '1rem',
          fontSize: '0.8rem',
          color: '#5b6178',
          textAlign: 'center',
        }}
      >
        v26.0.0 · Next.js 15 App Router · React 19 · TypeScript 5.7
      </p>
    </main>
  );
}

function DemoCard({
  href,
  title,
  subtitle,
  description,
  accent,
}: {
  href: string;
  title: string;
  subtitle: string;
  description: string;
  accent: string;
}) {
  const isExternal = href.startsWith('http');
  return (
    <a
      href={href}
      target={isExternal ? '_blank' : undefined}
      rel={isExternal ? 'noopener noreferrer' : undefined}
      style={{
        display: 'block',
        padding: '1.25rem',
        borderRadius: 14,
        background: 'rgba(255,255,255,0.04)',
        border: '1px solid rgba(255,255,255,0.08)',
        textDecoration: 'none',
        color: 'inherit',
        transition: 'background 200ms, border-color 200ms, transform 200ms',
      }}
      onMouseEnter={(e) => {
        e.currentTarget.style.background = 'rgba(255,255,255,0.07)';
        e.currentTarget.style.borderColor = accent;
        e.currentTarget.style.transform = 'translateY(-2px)';
      }}
      onMouseLeave={(e) => {
        e.currentTarget.style.background = 'rgba(255,255,255,0.04)';
        e.currentTarget.style.borderColor = 'rgba(255,255,255,0.08)';
        e.currentTarget.style.transform = 'translateY(0)';
      }}
    >
      <div
        style={{
          display: 'flex',
          alignItems: 'baseline',
          gap: '0.5rem',
          marginBottom: '0.5rem',
        }}
      >
        <h2 style={{ margin: 0, fontSize: '1.1rem', fontWeight: 700, color: accent }}>
          {title}
        </h2>
      </div>
      <p
        style={{
          margin: '0 0 0.75rem',
          fontSize: '0.75rem',
          letterSpacing: '0.08em',
          textTransform: 'uppercase',
          color: '#5b6178',
        }}
      >
        {subtitle}
      </p>
      <p style={{ margin: 0, fontSize: '0.875rem', color: '#9198ad', lineHeight: 1.5 }}>
        {description}
      </p>
    </a>
  );
}
