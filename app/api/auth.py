# 

import os

from fastapi import status, Security, HTTPException
from fastapi.security import APIKeyHeader

# API key for private endpoints that require a valid API key
api_key_header = APIKeyHeader(name="X-api-key", auto_error=False)
def get_api_key(api_key_header: str = Security(api_key_header)) -> str:
    if os.environ.get('MY_API_KEY') == api_key_header:
        return api_key_header
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API key"
    )