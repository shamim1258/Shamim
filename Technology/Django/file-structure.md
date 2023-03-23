# Django Project File Structure
 
- ProjectName
  - ProjectName
    - \_\_init__.py
    - settings
    - urls.py
    - wsgi.py
  - apps
    - migrations
    - \_\_init__.py
    - admin.py
    - apps.py
    - models.py
    - tests.py
    - views.py
  - api_app
    -  admin.py
    -  __init__.py
    -  serializers.py
    -  models.py
    -  urls.py
    -  views.py
  - configs
    - README
  - manage.py
  - requirements.txt
  - README
  - static
    - README
  - tempaltes
    - base.html
    - core
      - login.html
    - README
  - Dockerfile

**Notes :**
- **Root Directory :** the directory which contains your manage.py file.
- The name of root directory is the same as the project name you mentioned in django-admin startproject [projectname].
- db.sqlite, which is a database file.
- 

#### manage.py
- This file is used to interact with your project via the [command line utility](##command-line-utility) and for deploying, debugging, or running our web application.
- This file contains code for runserver, or makemigrations or migrations, etc.
- Anyway, we do not need to make any changes to the file.

#### Project Folder
This folder contains all the packages of your project. Initially, it contains four files -
  - **\_init_.py**
    - This file remains empty and is present their only to tell that this particular directory(in this case django_project) is a package.
    - We will not make any changes to this file.
  - **settings.py**
    - it contains all the website settings.
    - This file is present for adding all the applications and the middleware application present.
    - it has information about templates and databases
  - **urls.py**
    - This file handles all the URLs of our web application.
    - This file has the lists of all the endpoints that we will have for our website.
  - **wsgi.py**
    - This file mainly concerns with the WSGI server and is used for deploying our applications on to servers like Apache etc.
    - WSGI, short for Web Server Gateway Interface
    - This can be thought of as a specification that describes how the servers interact with web applications.
    - We will not make any changes to this file also.
  
#### Apps Folder
  - **migrations**
    - This folder is where Django stores migrations, or changes to your database.
  - **\_init_.py**
    Use of this file is same as in Project Folder file.
  - **admin.py**
    - This file is used for registering the models into the Django administration.
    - `admin.site.register(model_name)`
  - **apps.py**
    - This file deals with the application configuration of the apps.
    - The default configuration is sufficient enough in most of the cases and hence we won’t be doing anything here in the beginning.
  - **models.py**
    - This file contains the models of our web applications (usually as classes).
    - Models are basically the blueprints of the database we are using and hence contain the information regarding attributes and the fields etc of the database.
  - **views.py**
    - This is the mail file having all the logic.
    - Views are user interface for what we see when render a web application.
  - **urls.py**
    - Just like the project urls.py file, this file handles all the URLs of our web application.
  - **tests.py**
    - This file contains the code that contains different test cases for the application.
    - It is used to test the working of the application.
    - We won’t be working on this file in the beginning and hence it is going to be empty as of now.
