# Cache Django

-  In django we can cache :
   -  Output of a specific view
   -  Part of template
   -  Entire site
-  Cache is set up in **settings.py**
-  Cache data can be saved in
   -  Database
      -  Need to create one cache table <my_table_name> using command
      -  `python manage.py createcachetable`
^
    CACHES = {
        'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_table_name',
        }
    }
^
   -  File System
^
    CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
        }
    }
^
   -  Local Memory
^
    CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        }
    }

OR

    CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'unix:/tmp/memcached.sock',
        }
    }
^

-  **Caching the Entire Site :**
   -  The simplest way of using cache in Django is to cache the entire site.
   -  
