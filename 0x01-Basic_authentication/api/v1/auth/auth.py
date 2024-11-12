#!/usr/bin/env python3

"""
Module of Auth views
"""

from typing import List, TypeVar

from flask import request


class Auth:
    """
    Auth class to manage the API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if the given path requires authentication.
        Args:
            path (str): The path to check.
            excluded_paths (List[str]): A list of paths that do not require authentication.
        Returns:
            bool: True if the path requires authentication, False otherwise.
        """
        if path is None:
            return True
        elif excluded_paths is None or excluded_paths == []:
            return True
        elif path in excluded_paths:
            return False
        else:
            for i in excluded_paths:
                if i.startswith(path):
                    return False
                if path.startswith(i):
                    return False
                if i[-1] == '*' and path.startswith(i[:-1]):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request.
        Args:
            request: The Flask request object.
        Returns:
            str: The authorization header if present, None otherwise.
        """
        if request is None or "Authorization" not in request.headers:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Retrieves the current user based on the request.
        Args:
            request: The Flask request object.
        Returns:
            TypeVar('User'): The current user if authenticated, None otherwise.
        """
        return None
