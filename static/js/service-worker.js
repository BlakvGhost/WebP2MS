const CACHE_NAME = 'WebP2MS_CACHE';

const urlsToCache = [
  '/',
  '/static/css/master.css',
  '/static/css/mobile.css',
  '/static/plugins/custom/datatables/datatables.bundle.css',
  '/static/css/style.bundle.css',
  '/static/plugins/global/plugins.bundle.css',
  '/static/vendor/vue/axios.min.js',
  '/static/vendor/vue/vue.global.js',
  '/static/js/app.js',
  '/static/plugins/custom/datatables/datatables.bundle.js',
  '/static/js/table.js',
  '/static/js/add.js',
  '/static/js/signin-methods.js',
  '/static/js/profile-details.js',
  '/static/img/logo.svg',
];

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('activate', function(event) {
  event.waitUntil(
    caches.keys().then(function(cacheNames) {
      return Promise.all(
        cacheNames.filter(function(cacheName) {
          return cacheName.startsWith(CACHE_NAME) && cacheName !== CACHE_NAME;
        }).map(function(cacheName) {
          return caches.delete(cacheName);
        })
      );
    })
  );
});

self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request)
      .then(function(response) {
        return response || fetch(event.request);
      })
      .catch(function() {
        return caches.match('/offline.html');
      })
  );
});
