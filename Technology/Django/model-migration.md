# Model Migrations

-  Migration in django refers to models file of all the apps mentioned in the settings.py INSTALLED_APPS section, moving these models changes to the database.
-  We use 2 commands for this `python manage.py makemigrations` and `python manage.py migrate`.

### Migrations
-  Makemigrations command check all the models.py file mentioned in the settings.py INSTALLED_APPS section and if any change is found in the given app models file than create a file(app/migrations/0001_initial.py) under app/migrations folder which have information about the changes only not all model details just changes for this migration.
-  Using the files we can check what changes are done in the database in a given migration.
-  Syntax `python manage.py makemigrations`
-  This command does not create the sql queries it uses pythonic way of dedecting the changes and creating migration files.

### Migrate
-  Migrate command perform the operation of making changes in the database by reading the migration files.
-  Syntax `python manage.py migrate`.
-  `migrate --fake`

### Scenario
-  If multiple user have made changes to same models file but in different fields not the same field. How to handle this.
   -  Solution 1 :
      -  Make sure that both developer communicate so when one change gets committed to the main branch the other developer can pull those changes into their branch and re-create their migration files.
