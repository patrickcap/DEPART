"""
Provides helper methods for validating the user's access to private endpoints in the API.
"""

import os

from fastapi import status, Security, HTTPException # pylint: 
from fastapi.security import APIKeyHeader

# API key for private endpoints that require a valid API key
api_key_header = APIKeyHeader(name="X-api-key", auto_error=False)
def get_api_key(api_key_header_check: str = Security(api_key_header)) -> str:
    """
    Compare the API key provided by the user with that specified as an environment variable.
    Return the key if it is the same, otherwise return an unauthorised error message.
    """
    if os.environ.get('MY_API_KEY') == api_key_header_check:
        return api_key_header_check
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API key"
    )
