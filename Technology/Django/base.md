# Django

- Django is a Python-based web framework which allows you to quickly create web application.
- Django is a back-end server side web framework.
- Based on MVT (Model View Template) design pattern.
- Open source.
- The main python files are used to link with each other to display our web page are settings.py, view.py, and urls.py.

**Features of Django**
- Admin Interface
- Support multiple database backend
- Templating
- Form Handling
- Internationalization
- A Session, user management, role-based permissions
- Object-relational mapping (ORM)
- Testing Framework
- Fantastic Documentation

**Advantages**
- Django is python framework so it is easy to learn.
- Clear and readable.
- Versitile
- Secure
- Scalable
- Django is a rapid web development framework.
- It is very easy to switch database in Django framework.
- It has built-in admin interface which makes easy to work with it.

**Disadvantages**
- You must know the full structure to work.
- Django module are bulky
- Completely based on django ORM.
- Components are deployed together.
    
**Links**  
[Django File Structure](file-structure.md)  
[Working on Projects](working-on-project.md)  
[Django Models](models.md)  
[Django Model Migration](model-migration.md)
[Django Commands](django-commands.md)
[Django ORM](orm.md)  
[Django Signals](signals.md)  
[Rest API](Api/base.md)  
[Example Code Files](Example/base.md)  
[Example connect.py](Example/connect.md)  
[Django Access Permission Admin Panel](django-admin.md)  
[Middleware](middleware.md)  
[Django Libraries Used](../Python/libraries.md#django-libraries)  
[Django Cache](cache-django.md)  

### MVT

MVT stand for Model View Template.  
MVT is generally very similar to that of MVC which is a Model, View, and Controller. The difference between MVC and MVT here is the Django itself does the work done by the controller part in the MVC architecture. Django does this work of controller by using templates.  
Precisely, the template file is a mixture of HTML part and Django Template Language also known as [DTL](###DTL).  
Although Django follows MVC pattern but maintains it's own conventions. So, control is handled by the framework itself.

- **Model**
  - The model does the linking to the database and each model gets mapped to a single table in the database. These fields and methods are declared under the file models.py
  - With this can perform the DML operations on the data.
  - So after defining our database tables, columns and records; we are going to get the data linked to our application by defining the mapping in settings.py file under the INSTALLED_APPS.
- **View**
  - According to Django, the ‘view’ basically describes the data presented to the user. It does not deal with how the data looks but rather what the data actually is.
  - This is the part where actually we would be mentioning our logic. This coding is done through the python file views.py
  - How do you think that the system is going to understand to display a particular view? This can be done by mapping the views.py in urls.py file.
- **Template**
  - The ‘templates’ on the other hand deal with the presentation of data, thereby, separating the content from its presentation.
  - The Template handles the UI and architecture part of an application.
  - This template helps us to create a dynamic website in an easy manner. The dynamic website deals with dynamic data. Dynamic data deals with a scenario where each user is displayed with their personalized data.
  - The configuration of the template is done in settings.py file under INSTALLED_APPS. So python code would search for the files under the template subdirectory.
  - And after that our usual linking of this file in urls.py and views.py to get a response is mandatory.

**MVT based control flow**
A user requests for a resource to the Django, Django works as a controller and check to the available resource in URL.
If URL maps, a view is called that interact with model and template, it renders a template.
Django responds back to the user and sends a template as a response.

#### DTL
DTL stand for Django Template Language.  
Django template has its own syntax in rendering the data on to the web page.  
- For displaying a dynamic variable, the variable name is written inside the curly braces; denoted by `{{variable_name}}`.


### Django Server side and Client side rendering
check..
