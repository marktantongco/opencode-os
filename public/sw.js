// Service Worker for opencode OS — AI Agent Skills
// Cache version — bump on deploy to invalidate old caches
const CACHE_NAME = 'opencode-os-v23';

// Precache: core app shell
const PRECACHE_URLS = [
  '/index.html',
  '/manifest.json'
];

// Cache-first domains (fonts, CDN assets)
const CACHE_FIRST_PATTERNS = [
  /fonts\.googleapis\.com/,
  /fonts\.gstatic\.com/,
  /cdnjs\.cloudflare\.com\/ajax\/libs\/gsap\//
];

// Network-first domains (HTML)
const NETWORK_FIRST_PATTERNS = [
  /\/index\.html$/,
  /\/$/
];

// Install: precache core assets, skip waiting
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(PRECACHE_URLS);
    }).then(() => {
      return self.skipWaiting();
    })
  );
});

// Activate: claim clients, clean old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames
          .filter((name) => name !== CACHE_NAME)
          .map((name) => caches.delete(name))
      );
    }).then(() => {
      return self.clients.claim();
    })
  );
});

// Fetch: routing strategy
self.addEventListener('fetch', (event) => {
  const { request } = event;
  const url = new URL(request.url);

  // Only handle GET requests
  if (request.method !== 'GET') return;

  // Skip non-http(s) requests
  if (!url.protocol.startsWith('http')) return;

  // Strategy selection based on URL patterns
  if (CACHE_FIRST_PATTERNS.some((pattern) => pattern.test(url.href))) {
    // Cache-first for fonts and CDN assets
    event.respondWith(cacheFirst(request));
  } else if (NETWORK_FIRST_PATTERNS.some((pattern) => pattern.test(url.href))) {
    // Network-first for HTML
    event.respondWith(networkFirst(request));
  } else if (url.origin === self.location.origin) {
    // Same-origin: network-first for HTML, cache-first for other assets
    if (request.headers.get('accept')?.includes('text/html')) {
      event.respondWith(networkFirst(request));
    } else {
      event.respondWith(cacheFirst(request));
    }
  } else {
    // Cross-origin non-matched: network with cache fallback
    event.respondWith(networkWithCacheFallback(request));
  }
});

// Cache-first strategy: serve from cache, update in background
async function cacheFirst(request) {
  const cached = await caches.match(request);
  if (cached) {
    // Update cache in background (stale-while-revalidate)
    fetchAndCache(request);
    return cached;
  }
  return fetchAndCache(request);
}

// Network-first strategy: try network, fall back to cache
async function networkFirst(request) {
  try {
    const response = await fetch(request);
    if (response.ok) {
      const cache = await caches.open(CACHE_NAME);
      cache.put(request, response.clone());
    }
    return response;
  } catch (error) {
    const cached = await caches.match(request);
    if (cached) return cached;
    // Offline fallback: serve cached index.html for navigation requests
    if (request.mode === 'navigate') {
      const fallback = await caches.match('/index.html');
      if (fallback) return fallback;
    }
    return new Response('Offline', { status: 503, statusText: 'Service Unavailable' });
  }
}

// Network with cache fallback
async function networkWithCacheFallback(request) {
  try {
    const response = await fetch(request);
    if (response.ok) {
      const cache = await caches.open(CACHE_NAME);
      cache.put(request, response.clone());
    }
    return response;
  } catch (error) {
    const cached = await caches.match(request);
    return cached || new Response('Offline', { status: 503, statusText: 'Service Unavailable' });
  }
}

// Fetch and cache helper
async function fetchAndCache(request) {
  const response = await fetch(request);
  if (response.ok) {
    const cache = await caches.open(CACHE_NAME);
    cache.put(request, response.clone());
  }
  return response;
}
