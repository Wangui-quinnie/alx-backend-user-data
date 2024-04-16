#!/usr/bin/env python3
""" Class to manage all authentication
"""

from flask import request


class Auth:
    """Class to manage API authentication."""

    def require_auth(self, path: str, excluded_paths: list) -> bool:
        """Check if authentication is required for the given path."""
        return False

    def authorization_header(self, request=None) -> str:
        """Extract authorization header from the request."""
        return None

    def current_user(self, request=None):
        """Get the current user from the request."""
        return None
