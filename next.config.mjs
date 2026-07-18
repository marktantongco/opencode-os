/**
 * next.config.mjs
 * ----------------------------------------------------------------------------
 * - React strict mode (catches effect double-fire bugs in dev — critical for
 *   the 3-Layer Animation Stack where double-mounting a WebGL context would
 *   leak GPU memory).
 * - The existing /api/recommend.ts edge function is auto-detected by Next.js
 *   (no extra config needed). Its `export const config = { runtime: 'edge' }`
 *   is honored as-is.
 * - Static PWA assets live in /public and are served at the root path, so
 *   existing URLs (/index.html, /kb.html, /sw.js, /manifest.json, /icons,
 *   /stacks.json, /mcp-registry.json) keep working.
 */
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  // The legacy/ directory contains archived code from the deprecated master
  // branch (Next.js 16 redesign). It is NOT part of the active build but
  // TypeScript and ESLint would otherwise scan its .tsx/.ts files and fail
  // on missing imports (e.g. '@/components/glass/glass-card' which only
  // existed in the master redesign). These guards prevent that.
  typescript: {
    // tsconfig.json already excludes legacy/ — keep this false so real
    // type errors in app/, components/, api/ still fail the build.
    ignoreBuildErrors: false,
  },
  eslint: {
    // No eslint config in this project; don't let legacy/ files break builds.
    ignoreDuringBuilds: true,
  },
  experimental: {
    // Three.js + GSAP + Framer Motion all benefit from granular chunking.
    optimizePackageImports: ['three', 'gsap', 'framer-motion'],
  },
};

export default nextConfig;
