#!/usr/bin/env python3
"""
Basic authentication setup
"""


from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Class to manage Basic authentication."""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extract the Base64 part of the Authorization header for
        Basic Authentication."""
        if (authorization_header is None or
                not isinstance(authorization_header, str)):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        base64_part = authorization_header[6:]
        return base64_part
