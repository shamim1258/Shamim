# Rest API Authentication example

This example shows the REST API Authentication.

## Basic Authentication

-  This authenticate user with : Username and Password.
-  **Setup :**
   -  In settings.py
^
    REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication'
      ]
    }

-  In the views.py class based views function import `IsAuthenticated`.  
			`from rest_framework.permissions import IsAuthenticated`  
			`permission_classes = [IsAuthenticated]`
-  **Testing :**
   -  Using Postman to test this.
   -  Fail Scenario : 
      -  Cick on send button for GET request without any changes.
      -  Error : Authentication credentials were not provided.
   -  Success Scenario :
      -  Add below in the Header Section.
         -  Key - Authorization
         -  Value - Basic Username:Password
      -  If getting incorrect credentials error, decode the Username:Password with Base64 encode paste in Value.

## Token Authentication

-  When user first login with Username and Password in Database generate new Token and same provide in response.
-  Till the time token is valid user can access without being asked for usernama and password.
-  Once the token is invalidated access is denied and asked to login again with username and password this will again create new token.

**Example :**
-  To separate user account access activities will create user_app for - login, logout, registration/signup.
-  Create a folder - api and create these files in it - urls, views, serializers.
-  This authentication first reqire user to register if needed can be avoided than login with username and password which will generate token and send this token in request response.

-  **Setup :**
   -  In settings.py
^
    REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication'
      ]
    }

   -  In settings.py add in INSTALLED_APPS section `rest_framework.authtoken`.
   -  Migrate the token tables to db `python manage.py migrate`.

-  Generating token with login
   -  In urls.py use obtain_auth_token it will auto return the token for given credentials.
   -  `from rest_framework.authtoken.views import obtain_auth_token`
   -  `path('login/',obtain_auth_token,name='login'),`

-  For user registration/signup.
   -  Create a serializers.py in api folder which will have the fields required for user registration/signup.
^
    from django.contrib.auth.models import User
    from rest_framework import serializers
    import traceback
    class ResigtrationSerializer(serializers.ModelSerializer):
      try :
        password2 = serializers.CharField(style={'input_type': 'password'}, write_only = True)
        class Meta:
            model = User
            fields = ['username','email','password','password2']
            extra_kwargs = {
                'password' : {'write_only' : True}
            }
      except Exception as e:
        print("MyTraceBack_Class::", traceback.print_exc())
      def save(self):
        try:
            password = self.validated_data['password']
            password2 = self.validated_data['password2']

            if password != password2:
                raise serializers.ValidationError({'error': 'password not match'})
                # return {'error': 'password not match'}

            if User.objects.filter(email=self.validated_data['email']).exists():
                raise serializers.ValidationError({'error': 'email already exists'})
                # return {'error': 'password not match'}
            account = User(email=self.validated_data['email'],username=self.validated_data['username'])
            account.set_password(password)
            account.save()
            return account
        except Exception as e:
            print("MyTraceBack::",traceback.print_exc())  


   -  Create a function in views corresponds to serializers to urls to views function to handle the registration/signup.
^
    from rest_framework.decorators import api_view
    from rest_framework.response import Response
    from rest_framework.authtoken.models import Token
    from rest_framework import status
    from user_app.api.serializers import ResigtrationSerializer
    from user_app import models
    import traceback

    @api_view(['POST',])
    def logout_view(request):
      if request.method == 'POST' :
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

    @api_view(['POST',])
    def registration_view(request):
     try:
       if request.method == 'POST':
         serializer = ResigtrationSerializer(data=request.data)
           data = {}
           if serializer.is_valid():
                account = serializer.save()
                data['response'] = 'Registration Success'
                data['username'] = account.username
                data['email'] = account.email
                token = Token.objects.get(user=account).key
                data['token'] = token
            else:
                data = serializer.error
            return Response(data)
     except Exception as e:
        print("MyTraceBack_Views::", traceback.print_exc())

	
   
