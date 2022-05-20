# Rest API Questions

- What is the concept of statelessness in REST?
&emsp;<details>
  The REST architecture is designed in such a way that the client state is not maintained on the server. This is known as statelessness. The context is provided by the client to the server using which the server processes the client’s request. The session on the server is identified by the session identifier sent by the client.

- What are the HTTP Methods?
&emsp;<details>
  - GET: This is used for fetching details from the server and is basically a read-only operation.
  - POST: This method is used for the creation of new resources on the server.
  - PUT: This method is used to update the old/existing resource on the server or to replace the resource.
  - DELETE: This method is used to delete the resource on the server.
  - PATCH: This is used for modifying the resource on the server.
  - OPTIONS: This fetches the list of supported options of resources present on the server.

- Can you tell the disadvantages of RESTful web services?
&emsp;<details>
  - As the services follow the idea of statelessness, it is not possible to maintain sessions. (Session simulation responsibility lies on the client-side to pass the session id)
  - REST does not impose security restrictions inherently. It inherits the security measures of the protocols implementing it. Hence, care must be chosen to implement security measures like integrating SSL/TLS based authentications, etc.

- What are the best practices to develop RESTful web services?
&emsp;<details>
  RESTful web services use REST API as means of implementation using the HTTP protocol. REST API is nothing but an application programming interface that follows REST architectural constraints such as statelessness, cacheability, maintainability, and scalability. It has become very popular among the developer community due to its simplicity. Hence, it is very important to develop safe and secure REST APIs that follow good conventions. Below are some best practices for developing REST APIs:

Since REST supports multiple data formats, it is however good practice to develop REST APIs that accept and responds with JSON data format whenever possible. This is because a majority of the client and server technologies have inbuilt support to read and parse JSON objects with ease, thereby making JSON the standard object notation.
To ensure that the application responds using JSON data format, the response header should have Content-Type set to as application/JSON, this is because certain HTTP clients look at the value of this response header to parse the objects appropriately.
To ensure that the request sends the data in JSON format, again the Content-Type must be set to application/JSON on the request header.
While naming the resource endpoints, ensure to use plural nouns and not verbs. The API endpoints should be clear, brief, easy to understand, and informative. Using verbs in the resource name doesn’t contribute much information because an HTTP request already has what the request is doing in its HTTP method/verb. An appropriate HTTP verb should be used to represent the task of the API endpoint.
Below are the most commonly used HTTP methods to define the verb:
GET - indicates get/retrieve the resource data
POST - indicates create new resource data
PUT - indicates update the existing resource data
DELETE - indicates remove the resource data
To represent the hierarchy of resources, use the nesting in the naming convention of the endpoints. In case, you want to retrieve data of one object residing in another object, the endpoint should reflect this to communicate what is happening. For example, to get the address of an author, we can use the GET method for the URI /authors/:id/address'
Please ensure there are no more than 2 or 3 levels of nesting as the name of the URI can become too long and unwieldy.
Error Handling should be done gracefully by returning appropriate error codes the application has encountered. REST has defined standard HTTP Status codes that can be sent along with the response based on the scenario.
Error codes should also be accompanied by appropriate error messages that can help the developers to take corrective actions. However, the message should not be too elaborate as well which can help the hacker to hack your application.
Common status codes are:
400 - Bad Request – client-side error - failed input validation.
401 - Unauthorized – The user is not authenticated and hence does not have authority to access the resource.
403 - Forbidden – User is authenticated but is not authorized to access the resource.
404 - Not Found – The resource is not found.
500 - Internal server error – This is a very generic server-side error that is thrown when the server goes down. This shouldn’t be returned by the programmer explicitly.
502 - Bad Gateway – Server did not receive a valid response from the upstream server.
503 - Service Unavailable – Some unexpected things happened on the server such as system failure, overload, etc.
While retrieving huge resource data, it is advisable to include filtering and pagination of the resources. This is because returning huge data all at once can slow down the system and reduce the application performance. Hence, filter some items reduces the data to some extent. Pagination of data is done to ensure only some results are sent at a time. Doing this can increase the server performance and reduce the burden of the server resources.
Good security practices are a must while developing REST APIs. The client-server communication must be private due to the nature of data sensitivity. Hence, incorporating SSL/TLS becomes the most important step while developing APIs as they facilitate establishing secure communication. SSL certificates are easier to get and load on the server.
Apart from the secure channels, we need to ensure that not everyone should be able to access the resource. For example, normal users should not access the data of admins or another user. Hence, role-based access controls should be in place to make sure only the right set of users can access the right set of data.
Since REST supports the feature of caching, we can use this feature to cache the data in order to improve the application performance. Caching is done to avoid querying the database for a request repeated times. Caching makes data retrieval fast. However, care must be taken to ensure that the cache has updated data and not outdated ones. Frequent cache update measures need to be incorporated. There are many cache providers like Redis that can assist in caching.
API Versioning: Versioning needs to be done in case we are planning to make any changes with the existing endpoints. We do not want to break communication between our application and the apps that consume our application while we are working on the API release. The transition has to be seamless. Semantic versioning can be followed. For example, 3.0.1 represents 3rd major version with the first patch. Usually, in the API endpoints, we define /v1,/v2, etc at the beginning of the API path.
