# Caching
-  Django already comes with a cache system where it lets you save the pages but that’s not it, Django does much more than that. It provides you with different levels of cache granularity.
-  
-  Types of cache available in django
   -  [Caching Database](#caching-database)
   -  [Filesystem Caching](#filesystem-caching)
   -  [Memcached Caching](#memcached-caching)
   -  [Redis Caching](#redis-caching)

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

# Redis Caching
-  Redis is an open-source data-structure store that can be used as a database, cache, message broker, etc.
-  **Setup :**
   -  Install django-redis library makes it easier to connect your Django application to Redis `pip install django-redis`
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
