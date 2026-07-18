import type { Metadata, Viewport } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'opencode OS — Skills Registry & Live Demos',
  description:
    'Knowledge Base PWA for the opencode OS skills ecosystem. 90+ curated skills, MCP server stacks, and live Next.js demos of the 3-Layer Animation Stack (Three.js + GSAP + Framer Motion).',
  applicationName: 'opencode OS',
  authors: [{ name: 'marktantongco' }],
  keywords: ['opencode', 'skills', 'registry', 'threejs', 'gsap', 'framer-motion', 'animation', 'pwa'],
  metadataBase: new URL('https://opencode-accomplishments.vercel.app'),
  openGraph: {
    title: 'opencode OS — Skills Registry & Live Demos',
    description: '90+ curated skills, MCP stacks, and live 3-Layer Animation Stack demo.',
    type: 'website',
    images: ['/og-image.png'],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'opencode OS — Skills Registry & Live Demos',
    description: '90+ curated skills, MCP stacks, and live 3-Layer Animation Stack demo.',
    images: ['/og-image.png'],
  },
  icons: {
    icon: '/icon-192.svg',
    apple: '/icon-192.svg',
  },
  manifest: '/manifest.json',
};

export const viewport: Viewport = {
  themeColor: '#05060A',
  width: 'device-width',
  initialScale: 1,
  viewportFit: 'cover',
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
