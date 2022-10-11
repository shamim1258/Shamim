# Caching
-  Django already comes with a cache system where it lets you save the pages but that’s not it, Django does much more than that. It provides you with different levels of cache granularity.
-  Types of cache available in django
   -  **Caching Database :**
      -  Saving cache data in database.
      -  **Setup :**
         -  To create cache table in database `python manage.py createcachetable`.
         -  In settings.py declare CACHE section
^
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': 'cache_data_table',
        }
    }
^
         -  **Advantages :**
            -  Easy to setup
         -  **Disadvantages :**
            -  Compared to other caching methods not much effective.
            -  Require good indexing in tables.
            -  When number of table are much more in database it will require more adjustments.
   -  **Memcached :**
