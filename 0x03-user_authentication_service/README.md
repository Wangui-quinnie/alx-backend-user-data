Back-end Authentication Service

To declare API routes in a Flask app, you can use the Flask framework's @app.route() decorator. Here's a basic example:

from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a route for your API
@app.route('/api/resource', methods=['GET'])
def get_resource():
    # Your logic to fetch the resource
    resource = {'name': 'example', 'value': 100}
    return jsonify(resource)

if __name__ == '__main__':
    app.run(debug=True)
To get and set cookies in Flask, you can use the request.cookies to retrieve cookies from the client, and make_response and set_cookie to set cookies in the response. Here's how you can do it:

from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    # Retrieve cookie
    user_id = request.cookies.get('user_id')
    return f'User ID: {user_id}'

@app.route('/setcookie')
def setcookie():
    resp = make_response('Cookie Set')
    resp.set_cookie('user_id', '123')
    return resp

if __name__ == '__main__':
    app.run(debug=True)
To retrieve request form data in Flask, you can use request.form for form data submitted via POST requests. Here's an example:

from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Your login logic here
    return f'Username: {username}, Password: {password}'

if __name__ == '__main__':
    app.run(debug=True)
To return various HTTP status codes in Flask, you can use the abort() function from flask module along with specifying the status code in the response. Here's an example:

from flask import Flask, abort

app = Flask(__name__)

@app.route('/api/resource/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    if resource_id not in [1, 2, 3]:
        abort(404)  # Resource not found
    # Your logic to fetch the resource
    resource = {'id': resource_id, 'name': 'example'}
    return resource, 200  # Returning status code along with the resource

if __name__ == '__main__':
    app.run(debug=True)

