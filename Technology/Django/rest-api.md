# API
- API stand for Application Programming Interface.  
- REST APIs are an industry-standard way for web services to send and receive data.  
- They use HTTP request methods to facilitate the request-response cycle and typically transfer data using JSON, and more rarely - HTML, XML and other formats.  

## REST API
- REST stands for Representational State Transfer.  
- It is a standard architecture for building and communicating with web services.  
- It typically mandates resources on the web are represented in a text format (like JSON, HTML, or XML) and can be accessed or modified by a predetermined set of operations.  
- Given that we typically build REST APIs to leverage with HTTP instead of other protocols, these operations correspond to HTTP methods like GET, POST, or PUT.  

## REST Framework
- Django REST Framework (**DRF**).
- It is a package built on top of Django to create web APIs.  
- most remarkable features of Django is its Object Relational Mapper (ORM) which facilitates interaction with the database in a Pythonic way.  
- There are three stages before creating a API through REST framework, Converting a Model’s data to JSON/XML format (Serialization), Rendering this data to the view, Creating a URL for mapping to the viewset.  
- To initialize REST Framework in your project, go to settings.py, and in INSTALLED_APPS add ‘rest_framework’ at the bottom.  

### Serialization
- We can not send Python objects over a network, and hence need a mechanism to translate Django models in other formats like JSON, XML, and vice-versa. This sometimes challenging process, also called serialization.  
- Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.  

#### Viewset
- To render data into frontend, and handle requests from user, we need to create a view. In Django REST Framework, we call these as viewsets.  
- 
