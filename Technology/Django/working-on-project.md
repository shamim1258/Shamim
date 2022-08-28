# Working on Project

### Django installation steps

1. Install python3.
2. Install pip pythan libraries management module.
3. Install virtual environment.  
4. Install django

### Django Project steps

1. Creating Project.  
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

## Command Line Utility

- **runserver**
  - This command is used to run the server for our web application.
  - Syntax `python manage.py runserver`
- **Makemigrations**
  - this is done to apply new migrations that have been carried out due to the changes in the database.
  - `python manage.py makemigrations`
- **Migration**
  - This is used for applying the changes done to our models into the database. That is if we make any changes to our database then we use migrate command. This is used the first time we create a database.
  - `python manage.py migrate`
-  **Database Interactive Shell :**
   -  `python manage.py migrate shell`
      -  `from <appname>.model import <model_class_name>`


## Sample File

### manage.py
    import os
    import sys
    
    def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aws_tools.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    if __name__ == '__main__':
        main()

### settings.py
    from pathlib import Path
    from os.path import abspath, basename, dirname, join, normpath
    import os
    
    BASE_DIR = Path(__file__).resolve().parent.parent

    \# Quick-start development settings - unsuitable for production
    \# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

    \# SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'copy key here'

    \# SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = ['*']

    # Application definition

    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'coulance_access',
    'home',
    'shp',
    'account_sync',
    'account_update',
    'cancel_order',
    'contact_sync',
    'ib_update',
    'interfacelogshome',
    ]

    MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'aws_tools.urls'

    TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
    ]

    WSGI_APPLICATION = 'aws_tools.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/3.1/ref/settings/#databases

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    }
    \# DATABASES = {
    \#     'default': {
    \#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
    \#         'NAME': 'iotd',
    \#         'USER': '',
    \#         'PASSWORD': '',
    \#         'HOST': 'localhost',
    \#         'PORT': '5432',
    \#     }
    \# }

    \# Password validation
    \# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    ]

    \# Internationalization
    \# https://docs.djangoproject.com/en/3.1/topics/i18n/

    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True

    USE_TZ = True


    \# Static files (CSS, JavaScript, Images)
    \# https://docs.djangoproject.com/en/3.1/howto/static-files/

    \# working code
    \#STATIC_URL = join('/code', '/static/')  
    \#STATIC_ROOT = BASE_DIR / 'staticfiles' 

    PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATIC_URL = '/static/'

    DJANGO_ROOT = dirname(dirname(abspath(__file__)))
    SITE_ROOT = dirname(DJANGO_ROOT)
    \# Template directory setting
    TEMPLATE_DIRS = (
        normpath(join('/code', 'templates')),
     )

    LOGIN_REDIRECT_URL = '/'
    LOGOUT_REDIRECT_URL  = '/'
    
### urls.py
    from django.contrib import admin
    from django.urls import path,include

    urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include("home.urls")),
    path('home/', include("home.urls")),
    path('shp/', include("shp.urls")),
    ]  
    
    from django.urls import path
    from . import views

    urlpatterns = [
      path('',views.cancel_order),
      path('cancel_order',views.cancel_order,),
    ]

### apps.py
    from django.apps import AppConfig

    class CancelOrderConfig(AppConfig):
      default_auto_field = 'django.db.models.BigAutoField'
      name = 'cancel_order'  
      
### forms.py
    from django import forms
    from django.forms import ModelForm
    \#from django.forms import ModelForm,CheckboxSelectMultiple
    from . import models

    class NameForm(ModelForm):
      class Meta:
        model = models.cancelorder
        fields = '__all__'
        exclude = ('Username',)

### models.py
    from django.db import models

    class cancelorder(models.Model):
      Username = models.CharField(max_length=8, default='')
      Order_Number = models.CharField(max_length=20, default='')
      \#Order_Status = models.CharField(max_length=20,default='')

### views.py
    from django.shortcuts import render
    from django.http import HttpResponse
    from .forms import NameForm
    from .cancel_order import get_order, cancel_order_fun
    from django.contrib.auth.decorators import login_required

    @login_required
    def cancel_order(request):
      if request.method == 'GET':
          form = NameForm()
          template_name = 'cancel_order/get_order.html'
          return render(request, template_name, {'form': form})
      else:
          form = NameForm(request.POST)
          if request.POST.get("get_order"):
              form = NameForm(request.POST)
              if form.is_valid():
                  order_num_var = request.POST["Order_Number"]
                  get_order_var = get_order(order_num_var)
                  orderid = str(get_order_var[1][0])
                  error_flg = get_order_var[0]
                  if error_flg is not True:
                      error_flg = False
                      process = "get"
                      return render(request, 'cancel_order/cancel_order.html',
                                    context={'form': form, 'errorflag': error_flg, 'order_msg': orderid})
                  else:
                      error_flg = True
                      msg = get_order_var
                      return render(request, 'cancel_order/get_order.html',context={'form': form, 'errorflag': error_flg, 'error_msg': msg[1]})
              else:
                  return HttpResponse(form.errors)
          else:
              get_order_num = request.POST.getlist('Order')[1]
              cancel_order_var = cancel_order_fun(get_order_id)
              if cancel_order_var[1] == 'success':
                  msg = 'Order is successfully cancelled : ' + get_order_num
              else:
                  error_flg = True
                  msg = cancel_order_var[1]
              return render(request, 'cancel_order/get_order.html',
                            context={'form': form, 'errorflag': error_flg, 'success_msg': msg, 'error_msg': msg})
