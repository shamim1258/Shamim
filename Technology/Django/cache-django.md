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
   -  This is done by editing the MIDDLEWARE_CLASSES option in the project **settings.py**
^
    MIDDLEWARE_CLASSES += (
        'django.middleware.cache.UpdateCacheMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.cache.FetchFromCacheMiddleware',
    )
^
   -  Note that the order is important here, Update should come before Fetch middleware.
   -  Cache parameter can be set in settings.py
      -  CACHE_MIDDLEWARE_ALIAS – The cache alias to use for storage.
      -  CACHE_MIDDLEWARE_SECONDS – The number of seconds each page should be cached.
-  **Caching a View :**
   -  If you don’t want to cache the entire site you can cache a specific view.
   -  This is done by using the **cache_page decorator** that comes with Django.
^
    from django.views.decorators.cache import cache_page
    
    @cache_page(60 * 15) #Result will be cached for 15 min

    def viewArticles(request, year, month):
        text = "Displaying articles of : %s/%s"%(year, month)
        return HttpResponse(text)
^
   -  Caching a view can also directly be done in the url.py file.
   -  `urlpatterns = patterns('myapp.views', url(r'^articles/(?P<month>\d{2})/(?P<year>\d{4})/', 'viewArticles', name = 'articles'),)`
-  **Caching a Template Fragment :**
   -  You can also cache parts of a template, this is done by using the cache tag.
   -  The cache tag will take 2 parameters − the time you want the block to be cached (in seconds) and the name to be given to the cache fragment.
^
    {% loadx cache %}
    {% extends "main_template.html" %}
    {% block title %}My Hello Page{% endblock %}
    {% cache 500 content %}
    {% block content %}
    Hello World!!!<p>Today is {{today}}</p>
    We are
    
    {% if today.day == 1 %}
        the first day of month.
    {% elif today == 30 %}
        the last day of month.
    {% else %}
        I don't know.
    {%endif%}

    <p>
    {% for day in days_of_week %}
        {{day}}
    </p>
    {% endfor %}
    {% endblock %}
    {% endcache %}
^
