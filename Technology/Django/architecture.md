# Architecture

Django is based on MVT (Model-View-Template) architecture. MVT is a software design pattern for developing a web application.
MVT Structure has the following three parts – 
1. **Model**  
It is the logical data structure behind the entire application and is represented by a database.
2. **View**  
The View is the user interface — what you see in your browser when you render a website. It is represented by HTML/CSS/Javascript and Jinja files.
3. **Template**  
A template consists of static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted. 

## Project Structure

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
