#!/usr/bin/env python3
""" Class to manage all authentication
"""

from flask import request
from typing import List


class Auth:
    """Class to manage API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for the given path."""
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path.endswith('/'):
            path = path[:-1]  # Remove trailing slash
        for excluded_path in excluded_paths:
            if excluded_path.endswith('/'):
                excluded_path = excluded_path[:-1]  # Remove trailing slash
            if path == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Extract authorization header from the request."""
        if request is None or request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None):
        """Get the current user from the request."""
        return None
