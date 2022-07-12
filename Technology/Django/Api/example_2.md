# Rest API Authentication example

This example shows the REST API Authentication.

## Basic Authentication

-  This authenticate user with : Username and Password.
-  **Setup :**
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
