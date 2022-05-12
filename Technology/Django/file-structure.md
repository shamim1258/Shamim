# Django Project File Structure


    - ProjectName
     - ProjectName
      - AppName
       - common.py
        - 123.py

- ProjectName
  - ProjectName
    - [__init__.py](#__init__)
    - settings
      - common.py
      - development.py
      - i18n.py
      - __init__.py
      - production.py
    - urls.py
    - wsgi.py
  - apps
    - __init__.py
  - configs
    - README
  - doc
    - MakeFile
    - source
  - manage.py
  - README
  - run
    - media
      - README
    - README
    - static
      - README
  - static
    - README
  - tempaltes
    - base.html
    - core
      - login.html
    - README

- manage.py  
This file is used to interact with your project via the command line.
- project folder
This folder contains all the packages of your project. Initially, it contains four files -
  - \_init_.py
  It is a python package. We usually use this to execute package initialization code.
  - settings.py
  it contains all the website settings.
  - urls.py
  In this file, we store all links of the project and functions to call.
  - wsgi.py
  This file is used in deploying the project in WSGI. It is used to help your Django application communicate with the webserver.
