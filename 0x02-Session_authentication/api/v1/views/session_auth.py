#!/usr/bin/env python3
"""Session authentication views."""


from flask import Flask, jsonify, request, abort
from api.v1.views import app_views
from models.user import User
from api.v1.app import auth


@app_views.route('/auth_session/login', methods=['POST', 'GET'],
                 strict_slashes=False)
def session_login():
    """Handle user login using session authentication."""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email:
            return jsonify({"error": "email missing"}), 400
        if not password:
            return jsonify({"error": "password missing"}), 400

        user = User.search({'email': email})
        if not user:
            return jsonify({"error": "no user found for this email"}), 404

        if not user[0].is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401

        session_id = auth.create_session(user[0].id)
        response = jsonify(user[0].to_json())
        response.set_cookie(auth.session_name, session_id)
        return response, 200

    return jsonify({"error": "Method Not Allowed"}), 405


@app_views.route('/auth_session/logout', methods=['DELETE', 'GET'],
                 strict_slashes=False)
def logout():
    """Logs out a user by deleting the session"""
    if request.method == 'DELETE':
        if not auth.destroy_session(request):
            abort(404)
        return jsonify({}), 200
    return jsonify({}), 405
