const CACHE_NAME = "vendas-cache-v1";
const urlsToCache = [
  "/",
  "/static/css/style.css",
  "/static/icons/icon-192x192.png",
  "/static/icons/icon-512x512.png",
  // Adicione aqui outros arquivos estáticos importantes
];

// Instala o service worker e faz o cache dos arquivos
self.addEventListener("install", function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache);
      })
  );
});

// Intercepta requisições e serve do cache
self.addEventListener("fetch", function(event) {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});
