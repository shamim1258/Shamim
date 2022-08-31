# Models

## QuerySet
-  Queryset is a lit of objects in a given model.
-  It allows to read data from database, filter it and order it.
-  Example : `model_name.objects.all()`
-  To work on database without source code we can you terminal shell intrative utility by using command `python manage.py shell`
-  Useful link to read more about query set https://www.programink.com/django-tutorial/django-queryset.html
-  **Models deployment or migrations commands :**
   -  `python manage.py makemigrations`
      -  This validates the changes in model classes and throw error if any like if any default attribute for a field not defined eg max_length
      -  It basically creates a migration file in \<applincation>/migration/0001_initial.py
   -  `python manage.py migrate`
      -  This apply changes to the database and update database.
   -  `python manage.py test`
