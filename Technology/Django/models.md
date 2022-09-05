# Models

-  To work on database without source code we can you terminal shell intrative utility by using command `python manage.py shell`.
-  **Model Fields :**
   -  Fields argument `verbose_name = 'any_name'` is the name visible in admin panel but in the database original field name is considered.
-  **QuerySet :**
   -  Queryset is a lit of objects in a given model.
   -  It allows to read data from database, filter it and order it.
   -  Example : `model_name.objects.all()`
   -  Useful link to read more about query set https://www.programink.com/django-tutorial/django-queryset.html
-  **Models deployment or migrations commands :**
   -  `python manage.py makemigrations`
      -  This validates the changes in model classes and throw error if any like if any default attribute for a field not defined eg max_length
      -  It basically creates a migration file in \<applincation>/migration/0001_initial.py
   -  `python manage.py migrate`
      -  This apply changes to the database and update database.
   -  `python manage.py test`
   -  `python manage.py squashmigrations <application_name> <migration_file_inital>`
      - Example : `python manage.py squashmigrations ibupdate_app 0004`
      - It will mirge all files 0001_initial.py, 0002_initial.py, 0003_initial.py and 0004_initial.py into one file keeping only also which later we can delete manually.
-  **`bulk_create()`**
   -  This is used to insert multiple record into model in a single operation.
   -  Example `Product.objects.bulk_create([Product(name='Mobile1',price=15), Product(name='Mobile2',price=20),])`
-  **dumpdata**
   -  It is used to take backup of django model database.
   -  Command `python manage.py dumpdata`

-  **Debug :**
   -  To check the actual sql generated from ORM we can use expression `<model_name>.objects.all().query`
