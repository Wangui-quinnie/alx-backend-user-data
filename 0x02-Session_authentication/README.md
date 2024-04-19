Back-end Authentication

Background Context
In this project, you will implement a Session Authentication. You are not allowed to install any other module.

In the industry, you should not implement your own Session authentication system and use a module or framework that doing it for you (like in Python-Flask: Flask-HTTPAuth). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

Authentication is the process of verifying the identity of a user or entity attempting to access a system, application, or resource. It ensures that the user is who they claim to be before granting them access. Authentication mechanisms typically involve presenting credentials, such as usernames and passwords, tokens, biometric data, or other forms of identification.

Session authentication is a type of authentication that occurs during a user's session with a web application or service. Once a user successfully authenticates, a session is established, allowing the user to access restricted resources or perform actions within the application without needing to re-authenticate for each request. Session authentication typically involves the use of session tokens or cookies to maintain the user's authenticated state.

Cookies are small pieces of data stored on the client's browser by websites they visit. They are used to store information about the user's interactions with the website, such as login credentials, preferences, shopping cart contents, and more. Cookies are sent by the server to the client's browser in the HTTP response headers and are subsequently included in subsequent HTTP requests to the same website.

To send cookies from the server to the client, the server includes one or more Set-Cookie headers in the HTTP response. Each Set-Cookie header contains the name and value of the cookie, along with optional attributes such as expiration time, domain, path, and secure/HTTP-only flags.

To parse cookies sent by the client to the server, the server reads the Cookie header included in the HTTP request. The Cookie header contains one or more cookies, each represented as a key-value pair separated by semicolons. The server can then parse the Cookie header to extract individual cookies and their values for further processing. Many web frameworks and libraries provide built-in functionality for parsing cookies and managing session authentication.








