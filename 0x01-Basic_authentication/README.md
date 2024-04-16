Back-end Authentication

Background Context
In this project, you will learn what the authentication process means and implement a Basic Authentication on a simple API.

In the industry, you should not implement your own Basic authentication system and use a module or framework that doing it for you (like in Python-Flask: Flask-HTTPAuth). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.


Authentication is the process of verifying the identity of a user or system. It ensures that the entity trying to access a resource is who it claims to be. Authentication mechanisms can involve various methods such as passwords, biometrics, security tokens, or digital certificates.

Base64 is a binary-to-text encoding scheme that converts binary data into ASCII characters. It's commonly used to encode binary data, such as images, into a format that can be transmitted over text-based protocols like HTTP or SMTP.

Encoding a string in Base64 involves converting each group of three bytes of binary data into four ASCII characters. If the input data length is not a multiple of three bytes, padding characters '=' are added at the end. Many programming languages and libraries provide built-in functions or methods to encode data in Base64.

Basic authentication is a simple authentication scheme used by HTTP for authenticating users. It involves sending a username and password with each request. The credentials are combined into a single string of the form "username:password", which is then Base64 encoded and included in the Authorization header of the HTTP request.

To send the Authorization header with Basic authentication, you need to include it in the HTTP request headers. The Authorization header value starts with the word "Basic" followed by a space and the Base64 encoded string of the username and password concatenated with a colon (':'). For example:

Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==
In this example, "QWxhZGRpbjpvcGVuIHNlc2FtZQ==" is the Base64 encoded form of the string "username:password".

