# Django Project File Structure

- ProjectName
  - ProjectName
    \- \_\_init__.py
    \- settings
    \- urls.py
    \- wsgi.py
  - apps
    \- \_\_init__.py
  - configs
    \- README
  - manage.py
  - README
  - static
    \- README
  - tempaltes
    \- base.html
    \- core
      \- login.html
    \- README

#### manage.py
- This file is used to interact with your project via the [command line utility](##command-line-utility) and for deploying, debugging, or running our web application.
- This file contains code for runserver, or makemigrations or migrations, etc.
- Anyway, we do not need to make any changes to the file.

#### Project Folder
This folder contains all the packages of your project. Initially, it contains four files -
  - \_init_.py
    - This file remains empty and is present their only to tell that this particular directory(in this case django_project) is a package.
    - We will not make any changes to this file.
  - settings.py
    - it contains all the website settings.
    - This file is present for adding all the applications and the middleware application present.
    - it has information about templates and databases
  - urls.py
    - This file handles all the URLs of our web application.
    - This file has the lists of all the endpoints that we will have for our website.
  - wsgi.py
    - This file mainly concerns with the WSGI server and is used for deploying our applications on to servers like Apache etc.
    - WSGI, short for Web Server Gateway Interface
    - This can be thought of as a specification that describes how the servers interact with web applications.
    - We will not make any changes to this file also.
  
### Command Line Utility

- runserver
  - This command is used to run the server for our web application.
  - Syntax ```python manage.py runserver```
- Makemigrations
  - this is done to apply new migrations that have been carried out due to the changes in the database.
  - ```python manage.py makemigrations```
- Migration
  - This is used for applying the changes done to our models into the database. That is if we make any changes to our database then we use migrate command. This is used the first time we create a database.
  - ```python manage.py migrate```
