# API
- API stand for Application Programming Interface.  
- REST APIs are an industry-standard way for web services to send and receive data.  
- They use HTTP request methods to facilitate the request-response cycle and typically transfer data using JSON, and more rarely - HTML, XML and other formats.  

## REST API
- REST stands for Representational State Transfer.  
- It is a standard architecture for building and communicating with web services.  
- It typically mandates resources on the web are represented in a text format (like JSON, HTML, or XML) and can be accessed or modified by a predetermined set of operations.  
- Given that we typically build REST APIs to leverage with HTTP instead of other protocols, these operations correspond to HTTP methods like GET, POST, or PUT.  
- **Setup**
  - Installation : ```pip install djangorestframework```

### Advantages
- Designed for high performance, portability, reliability, and scalability.
- Client-server separation allows each to individually operate and scale.
- Easy to test and adapt to various environments.
- Supports various data transfer technologies including JSON, XML, YAML, images, and more.
- Uses less bandwidth than other methods, such as SOAP.

### Disadvantages
- Doesn’t enforce security practices.
- HTTP method limits you to synchronous requests.
- Due to statelessness, you might be unable to maintain state (e.g. in sessions).

### Response Status Code
```from rest_framework import status```
- 200: Successful request
- 201: Entity or entities created from successful request
- 400: Bad request. Invalid client request.
- 401: Unauthorized. User isn’t authorized to access a resource and may be unauthenticated
- 403: Forbidden. User isn’t authorized to access a resource, user is authenticated
- 404: Not found. Resource not found
- 500: Internal server error. Generic server error
- 502: Bad gateway. Response from upstream server is not valid
- 503: Service unavailable. Result of server-side issue, including overload or system failure

## REST Framework
- Django REST Framework (**DRF**).
- It is a package built on top of Django to create web APIs.  
- most remarkable features of Django is its Object Relational Mapper (ORM) which facilitates interaction with the database in a Pythonic way.  
- There are three stages before creating a API through REST framework, Converting a Model’s data to JSON/XML format (Serialization), Rendering this data to the view, Creating a URL for mapping to the viewset.  
- To initialize REST Framework in your project, go to settings.py, and in INSTALLED_APPS add ‘rest_framework’ at the bottom.  
- Can be done using class based or function based.  

      from django.shortcuts import render
      from django.http import HttpResponse
      from rest_framework.decorators import api_view
      from rest_framework.response import Response
      from talk.models import Post
      from talk.serializers import PostSerializer
      from talk.forms import PostForm

      def home(request):
        tmpl_vars = {'form': PostForm()}
        return render(request, 'talk/index.html', tmpl_vars)


      @api_view(['GET'])
      def post_collection(request):
        if request.method == 'GET':
          posts = Post.objects.all()
          serializer = PostSerializer(posts, many=True)
          return Response(serializer.data)

      @api_view(['GET'])
      def post_element(request, pk):
        try:
          post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
          return HttpResponse(status=404)

      if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

### Serialization
- We can not send Python objects over a network, and hence need a mechanism to translate Django models in other formats like JSON, XML, and vice-versa. This sometimes challenging process, also called serialization.  
- Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.  
- For serialization create file : ```serializers.py```  


      from rest_framework import serializers
      from talk.models import Post
    class PostSerializer(serializers.ModelSerializer):
      class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'created', 'updated')  

#### Viewset
- To render data into frontend, and handle requests from user, we need to create a view. In Django REST Framework, we call these as viewsets.  
- 
