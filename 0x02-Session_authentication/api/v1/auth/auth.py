#!/usr/bin/env python3
""" Class to manage all authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Class to manage API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for the given path."""
        if not path or not excluded_paths:
            return True

        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if path.startswith(excluded_path[:-1]):
                    return False
            elif path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Extract authorization header from the request."""
        if request is None or request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current user from the request."""
        return None
