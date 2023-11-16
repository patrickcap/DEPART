"""
Provides the API endpoint that deletes a given model from the model store.
"""

import random
import uuid

from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from app.api.resources.model import models

# Provides a reference to this endpoint for use by main FastAPI object
remove_model_router = APIRouter(prefix='/models/{model_id}')

# Using a DELETE request to remove a model resource
@remove_model_router.delete("", status_code=204)
async def remove_model(model_id: uuid.UUID) -> JSONResponse:
    """
    Delete the model specified by the given identifier from the model store.
    """
    
    # Throw error 0.5% of the time
    if random.randint(0, 1000) <= 5:
        return JSONResponse(contect = "Unforseen error.", status_code = 500)
    # Search for key in dictionary
    if model_id in models:
        # If found, remove it
        models.pop(model_id)
        return JSONResponse(contect="Model successfully removed."
                            , status_code = 204)
    # If not found, return fail message
    return JSONResponse(contect = "No model found with that ID.",
                        status_code = 404) 
