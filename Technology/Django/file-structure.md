# Django Project File Structure

- ProjectName
  - [Project Name](###project-folder)
    \- [\_\_init__.py](###__init__)
    \- settings
    \- urls.py
    \- wsgi.py
  - apps
    \- \_\_init__.py(###__init__)
  - configs
    \- README
  - [manage.py](###manage.py)
  - README
  - static
    - README
  - tempaltes
    - base.html
    - core
      - login.html
    - README

#### manage.py
This file is used to interact with your project via the command line.

#### Project Folder
This folder contains all the packages of your project. Initially, it contains four files -
  - \_init_.py
  It is a python package. We usually use this to execute package initialization code.
  - settings.py
  it contains all the website settings.
  - urls.py
  In this file, we store all links of the project and functions to call.
  - wsgi.py
  This file is used in deploying the project in WSGI. It is used to help your Django application communicate with the webserver.
  
