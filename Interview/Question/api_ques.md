# Rest API Questions

- What is the concept of statelessness in REST?
Answer - The REST architecture is designed in such a way that the client state is not maintained on the server. This is known as statelessness. The context is provided by the client to the server using which the server processes the client’s request. The session on the server is identified by the session identifier sent by the client.

- What are the HTTP Methods?
Answer - GET: This is used for fetching details from the server and is basically a read-only operation.
POST: This method is used for the creation of new resources on the server.
PUT: This method is used to update the old/existing resource on the server or to replace the resource.
DELETE: This method is used to delete the resource on the server.
PATCH: This is used for modifying the resource on the server.
OPTIONS: This fetches the list of supported options of resources present on the server.

- Can you tell the disadvantages of RESTful web services?
Answer - As the services follow the idea of statelessness, it is not possible to maintain sessions. (Session simulation responsibility lies on the client-side to pass the session id)
REST does not impose security restrictions inherently. It inherits the security measures of the protocols implementing it. Hence, care must be chosen to implement security measures like integrating SSL/TLS based authentications, etc.
