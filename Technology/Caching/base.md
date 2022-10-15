# Caching
-  Django already comes with a cache system where it lets you save the pages but that’s not it, Django does much more than that. It provides you with different levels of cache granularity.
-  Types of cache available in django
   -  [Caching Database](#caching-database)
   -  [Filesystem Caching](#filesystem-caching)
   -  [Memcached Caching](#memcached-caching)
   -  [Redis Caching](#redis-caching)
-  Django caching level
   -  [Per-site cache](#per-site-cache)
   -  [Per-view cache](#per-view-cache)
   -  [Template fragment cache](#template-fragment-cache)
   -  [Low-level cache API](#low-level-cache-api)
-  Some very cache-friendly content for most sites are
   -  Logos and brand images
   -  Non-rotating images in general (navigation icons, for example)
   -  Style sheets
   -  General Javascript files
   -  Downloadable Content
   -  Media Files

## Caching Database
-  Saving cache data in database.
-  **Advantages :**
   -  Easy to setup
-  **Disadvantages :**
   -  Compared to other caching methods not much effective.
   -  Database caching works best if you’ve got a fast, well-indexed database server.
   -  When number of table are much more in database it will require more adjustments.
   -  The database caching backend uses the same database as specified in your settings file. You can’t use a different database backend for your cache table.
-  **Setup :**
   -  To create cache table in database `python manage.py createcachetable <cache_table_name>`.
   -  In settings.py declare CACHE section
 ^
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': 'cache_data_table',
        }
     }
 ^
 
## Filesystem Caching
-  Saving the cache data in file system.
-  **Advantages :**
   -  Easy to setup
-  **Disadvantages :**
   -  Each cache value will be stored as a separate file whose contents are the cache data saved in a serialized (“pickled”) format, using Python’s pickle module.
   -  Make sure the directory pointed-to by this setting exists and is readable and writable by the system user under which your Web server runs.
-  **Setup :**
   -  In settings.py declare CACHE section
^
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': 'path',
        }
    }
^

## Memcached Caching
-  By far the fastest, most efficient type of cache available to Django.
-  **Advantages :**
   -  Easy to setup
-  **Disadvantages :**
   -  Each cache value will be stored as a separate file whose contents are the cache data saved in a serialized (“pickled”) format, using Python’s pickle module.
   -  Make sure the directory pointed-to by this setting exists and is readable and writable by the system user under which your Web server runs.
-  **Setup :**
^
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
            'LOCATION': '127.0.0.1:9000',
        }
    }
^

## Redis Caching
-  Redis is an open-source data-structure store that can be used as a database, cache, message broker, etc.
-  **Setup :**
   -  Install redis in server or local.
   -  Run the redis-server.
   -  Install `django-redis` library makes it easier to connect your Django application to Redis `pip install django-redis`
   -  Run the redis-cli command line terminal.
      -  To test if working fine run command `ping` and getting response `PONG` than it is working fine.
      -  To select the database `select 1`
      -  To get all cache keys `keys *`
      -  To get any key value `get "key_name"`
   -  In settings.py
^
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': 'redis://127.0.0.1:6379/1',
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            }
        }
    }
^

## Per site cache
-  Easy to implement.
-  This is best suitable for static sites.
-  May not be much effective as it cache entire site.
-  Add two middleware classes to your settings.py file. The order of the middleware is important here. `UpdateCacheMiddleware` must come before `FetchFromCacheMiddleware`
^
    MIDDLEWARE = [
        'django.middleware.cache.UpdateCacheMiddleware',     # NEW
        'django.middleware.common.CommonMiddleware',
        'django.middleware.cache.FetchFromCacheMiddleware',  # NEW
    ]
^
-  In settings.py
    CACHE_MIDDLEWARE_ALIAS = 'default'  # which cache alias to use
    CACHE_MIDDLEWARE_SECONDS = '600'    # number of seconds to cache a page for (TTL)
    CACHE_MIDDLEWARE_KEY_PREFIX = ''    # should be used if the cache is shared across multiple sites that use the same Django instance
    
## Per view cache
-  This caches specific views.
-  You can implement this type of cache with the `cache_page` decorator either on the view function directly or in the path within `URLConf`.
^
    from django.views.decorators.cache import cache_page
    @cache_page(60 * 15)
    def your_view(request):
    ...
^
OR
^
    from django.views.decorators.cache import cache_page
    urlpatterns = [path('object/int:object_id/', cache_page(60 * 15)(your_view)),]
^
-  The cache itself is based on the URL, so requests to, say, object/1 and object/2 will be cached separately.
-  It's worth noting that implementing the cache directly on the view makes it more difficult to disable the cache in certain situations. For example, what if you wanted to allow certain users access to the view without the cache? Enabling the cache via the URLConf provides the opportunity to associate a different URL to the view that doesn't use the cache.

## Template fragment cache
-  If your templates contain parts that change often based on the data you probably want to leave them out of the cache.
-  To cache a list of objects


