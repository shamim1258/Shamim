# REST API
-  REST stands for Representational State Transfer.   
-  API stand for Application Programming Interface.
-  REST APIs are industry-standard way for web services to send and receive data.  
-  They use HTTP request methods to facilitate the request-response cycle and typically transfer data using JSON, and more rarely - HTML, XML and other formats.  
-  REST APIs leverage with HTTP protocols instead of other protocols, these operations correspond to HTTP methods like GET, POST or PUT.  
-  **URI :** Universal Resource Identifier used to identifying where a specific resource can be found, such as a page or a document.
-  **Idempotent :** An operation is idempotent if it produces same result when called multiple times.
-  **JSON :** stands for JavaScript Object Notation.
-  **HTTP METHODS :**
   -  **GET :**
      -  This is used to get the resource from target.
      -  The URI contains the Id or any identification key in the request.  
      -  It is idempotent.
   -  **POST :**
      -  This is used to create resources without knowing the URI for the new resource.  
      -  POST is not idempotent. So sending the same POST requests multiple times can result in the creation of multiple resources.
      -  POST does not necessarily need to create resources. It can also be used to perform a generic action (e.g. starting a batch job, importing data or process something).
      -  Example `POST /questions`
   -  **PUT :**
      -  Use PUT when we want to modify a singular resource that is already a part of resources collection.
      -  PUT replaces the resource in its entirety meaning it does not update a one or few fields but replaces the entire object. Also the request contains the all the elements.
      -  PUT is idempotent. So if we retry a request multiple times, that should be equivalent to a single request invocation.
      -  The main difference between POST and PUT is a different meaning of the request URI.
      -  Example `PUT /questions/{question-id}`
   -  **PATCH :**
      -  PATCH is used to apply partial modifications to a resource.  
      -  Unlike PUT, PATCH request have only entity which need to be updated.
      -  POST is not idempotent. So sending the same POST requests multiple times can result in the creation of multiple resources. A simple example here is the addition of an item to an existing list resource, like adding a product to a shopping cart. Multiple (partial) update requests might add the product multiple times to the shopping cart.

**Links :**  
- [Example](example_1.md)  
- [Example Authentication](example_2.md)  
- [Example ViewSet Router](example_3.md)  

## Django Rest Framework DRF
- Django REST Framework (DRF) has its own flavor of views that inherit from Django's `View` class.
- The essential component of DRF views is the `APIView` class, which subclasses Django's View class.
- APIView class is a base for all the views that you might choose to use in your DRF application which includes :
  -  **Function-based views :**
     -  Functions are created to handle the api request which uses decorator `@api_view(['GET','POST'])` from `from rest_framework.decorators import api_view`.
     -  The @api_view decorator ensures that the view receives an instance of the django rest framework Request object (instead of the standard Django HttpRequest object) and returns an instance of the django rest framework’s Response object (instead of the standard Django HttpResponse object).
     -  Use Cases
        -  For highly customized view logic.
  -  **Class-based views :**
     -  The APIView class subclasses the django View class and is the base of all views in django rest framework.
     -  Whenever you want to create a class based view you have to subclass the APIView.
     -  APIView some standard generic view functionality but makes no assumptions on what you want to do with your view. You still have to precisely define your logic which means that it is not that different from the function based view. 
     -  Use Cases
        -  Achieve a typical behaviour without much code.
  - Mixins
  - Generic view classes
  - Viewsets
- When a request hits a view, the view first initializes a Request object, which is a DRF-enhanced HttpRequest from Django.
- When compared to Django's HttpRequest, it has the following advantages:
  - Content is automatically parsed according to the Content-Type header and is available as request.data.
  - It supports PUT and PATCH methods (including file uploads). (Django only supports GET and POST methods.)
  - By temporarily overriding the method on a request, it checks permissions against other HTTP methods.
- It is a package built on top of Django to create web APIs.  
- Most remarkable features of Django is its Object Relational Mapper (ORM) which facilitates interaction with the database in a Pythonic way.  
- There are three stages before creating a API through REST framework, Converting a Model’s data to JSON/XML format (Serialization), Rendering this data to the view, Creating a URL for mapping to the viewset.  
- To initialize REST Framework in your project, go to settings.py, and in INSTALLED_APPS add `rest_framework`.
- There are two ways to directly implement APIView: With a function or with a class. If you're writing a view in the form of a function, you'll need to use the @api_view decorator.
- @api_view is a decorator that converts a function-based view into an APIView subclass (thus providing the Response and Request classes). It takes a list of allowed methods for the view as an argument.
- Can be done using class based or function based.  
  - **Function Based**
    - Uses decorator `@api_view` for request and response.
    - If you want to override the default settings for your function-based view, you can use policy decorators. You can use one or multiple of the following:
      - @renderer_classes
      - @parser_classes
      - @authentication_classes
      - @throttle_classes
      - @permission_classes
    - Those decorators correspond to APIView subclasses. Because the @api_view decorator checks if any of the following decorators are used, they need to be added below the api_view decorator.
    - If we use the same example that we did for the policy attributes, we can implement the decorators like so to achieve the same results:  
^
    from rest_framework.decorators import api_view, permission_classes, renderer_classes
    from rest_framework.permissions import IsAuthenticated
    from rest_framework.renderers import JSONRenderer
    from rest_framework.response import Response

    @api_view(['GET'])
    @permission_classes([IsAuthenticated])  # policy decorator
    @renderer_classes([JSONRenderer])       # policy decorator
    def items_not_done(request):
      user_count = Item.objects.filter(done=False).count()
      content = {'not_done': user_count}
    return Response(content)

  - **Class Based**
    - Uses `APIVIEW`

-  **Setup**
   -  Installation : `pip install djangorestframework`
   -  In settings.py add `rest_framework` under INSTALLED_APPS section.
   -  If you're intending to use the browsable API you'll probably also want to add REST framework's login and logout views. Add the following to your root urls.py file.
^
    urlpatterns = [
      ...
      path('api-auth/', include('rest_framework.urls'))
    ]  
^
  -  Any global settings for a REST framework API are kept in a single configuration dictionary named REST_FRAMEWORK. Start off by adding the following to your settings.py module:
^
    REST_FRAMEWORK = {
      # Use Django's standard `django.contrib.auth` permissions,
      # or allow read-only access for unauthenticated users.
      'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
      ]
    }
^

-  **Advantages :**
   - Designed for high performance, portability, reliability, and scalability.
   - Client-server separation allows each to individually operate and scale.
   - Easy to test and adapt to various environments.
   - Supports various data transfer technologies including JSON, XML, YAML, images, and more.
   - Uses less bandwidth than other methods, such as SOAP.

-  **Disadvantages :**
   - Doesn’t enforce security practices.
   - HTTP method limits you to synchronous requests.
   - Due to statelessness, you might be unable to maintain state (e.g. in sessions).

-  **Response Status Code**
   -  ```from rest_framework import status```
   - 200: Successful request
   - 201: Entity or entities created from successful request
   - 400: Bad request. Invalid client request.
   - 401: Unauthorized. User isn’t authorized to access a resource and may be unauthenticated
   - 403: Forbidden. User isn’t authorized to access a resource, user is authenticated
   - 404: Not found. Resource not found
   - 500: Internal server error. Generic server error
   - 502: Bad gateway. Response from upstream server is not valid
   - 503: Service unavailable. Result of server-side issue, including overload or system failure

### Serialization
- We can not send Python objects over a network, and hence need a mechanism to translate Django models in other formats like JSON, XML, and vice-versa. This sometimes challenging process, also called serialization.  
  - GET request : convert from model object to JSON.  
^
      if request.method == 'GET':
        transformer = Transformer.objects.all()
        serializer = TransformerSerializer(transformer, many=True)
        return JsonResponse(serializer.data, safe=False)  
        
  - POST request : convert from JSON to model object can alse called de-serialization.  
^
     elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TransformerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)  
        
- Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data. - Serializer classes -
  - Serializer
  - ModelSerializer 
- For serialization create file : `serializers.py`  
^
    from rest_framework import serializers
    from talk.models import Post
    class PostSerializer(serializers.ModelSerializer):
      class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'created', 'updated')  

#### Viewset
- To render data into frontend, and handle requests from user, we need to create a view. In Django REST Framework, we call these as viewsets.  

#### @api_view
- The @api_view is a decorator in the rest_framework.decorators module, and it is the base class for all the Django REST framework views. We can provide the allowed HTTP verbs as the http_methods_names argument (list of strings) in the @api_view decorator.  
`@api_view(http_method_names=['GET'])`
- The @api_view decorator can parse different content types by choosing the appropriate parser.
- When we use the @api_view decorator, it automatically makes use of APIView class and its settings. This way we will be able to use the parsers and renders.
- The @api_view decorator helps the Django REST framework to examine the Content-Type header in the data attribute and identifies the exact parser to parse the request. It also invokes the rest_framework.negotiation.DefaultContentNegotiation class to select the suitable renderer for the request.  

### Mixins
-  Mixins provide bits of common behavior. They cannot be used standalone; they must be paired with GenericAPIView to make a functional view.
-  While the mixin classes provide create/retrieve/update/delete actions, you still need to bind the appropriate actions to the methods.
- The mixin classes can be imported from rest_framework.mixins  
- The mixin classes provide the actions that are used to provide the basic view behavior. Note that the mixin classes provide action methods rather than defining the handler methods, such as .get() and .post(), directly. This allows for more flexible composition of behavior.  
- List of available mixins:  
  - ListModelMixin: provides a .list() method to the view/viewset
  - RetrieveModelMixin: provides a .retrieve() method to the view/viewset
  - CreateModelMixin: provides a .create() method to the view/viewset
  - UpdateModelMixin: provides a .update() method to the view/viewset
  - DestroyModelMixin: provides a .destroy() method to the view/viewset
-  Example
^
    from rest_framework import mixins
    from rest_framework.generics import GenericAPIView

    class CreateList(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):

        serializer_class = ItemSerializer
        queryset = Item.objects.all()

        def get(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs)

        def post(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)
^
## Authentication

**Links :**  
- [Example Authentication](example_2.md)  


-  The `request.user` property will typically be set to an instance of the `contrib.auth` package's User class.
-  The `request.auth` property is used for any additional authentication information, for example, it may be used to represent an authentication **token** that the request was signed with.
-  Note: Don't forget that authentication by itself won't allow or disallow an incoming request, it simply identifies the credentials that the request was made with.
-  The authentication schemes are always defined as a list of classes. REST framework will attempt to authenticate with each class in the list, and will set request.user and request.auth using the return value of the first class that successfully authenticates.If no class authenticates, request.user will be set to an instance of django.contrib.auth.models.AnonymousUser, and request.auth will be set to None.
-  The value of request.user and request.auth for unauthenticated requests can be modified using the UNAUTHENTICATED_USER and UNAUTHENTICATED_TOKEN settings.
-  The default authentication schemes may be set globally.
^
    REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
      ]
    }  
-  You can also set the authentication scheme on a per-view or per-viewset basis, using the APIView class-based views.
^
     from rest_framework.authentication import SessionAuthentication, BasicAuthentication
     from rest_framework.permissions import IsAuthenticated
     from rest_framework.response import Response
     from rest_framework.views import APIView
     
     class ExampleView(APIView):
       authentication_classes = [SessionAuthentication, BasicAuthentication]
       permission_classes = [IsAuthenticated]

      def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)  
-  Or, if you're using the @api_view decorator with function based views.
^
    @api_view(['GET'])
    @authentication_classes([SessionAuthentication, BasicAuthentication])
    @permission_classes([IsAuthenticated])
    def example_view(request, format=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return Response(content)
