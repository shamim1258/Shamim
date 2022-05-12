# Installation

### Django installation steps

1. Install python3.
2. Install pip pythan libraries management module.
3. Install virtual environment.  
4. Install django

### Django Project steps

1. Creating Project  
```django-admin startproject projectName```
2. Run new created project
```cd projectName```  
```Python manage.py runserver```  
3. Creating new application.  
```python manage.py startapp projectApp```  
4. Add the app name in settings.py under section INSTALLED_APPS.
5. To render the app using urls we need to include the app in our main project so that urls redirected to that app can be rendered.  
  1. Move to projectName-> projectName -> urls.py and add below code in the header.
  ```from django.urls import include```  
  2. Now in the list of URL patterns, you need to specify app name for including your app urls.  
  ```from django.contrib import admin```  
  ```from django.urls import path, include```  
  ```urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include("projectApp.urls")),
  ]```  
