"""
Provides the API endpoint that deletes a given model from the model store.
"""

import random
import uuid

from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from api.resources.model import models

# Provides a reference to this endpoint for use by main FastAPI object
remove_model_router = APIRouter(prefix='/models/{model_id}')

# Using a DELETE request to remove a model resource
@remove_model_router.delete("", status_code=200)
async def remove_model(model_id: uuid.UUID):
    """
    Delete the model specified by the given identifier from the model store.
    """
    # Throw error 0.5% of the time
    if random.randint(0, 1000) >= 500:
        raise HTTPException(status_code=500, detail="Unforseen error.")

    # Search for key in dictionary
    if model_id in models:
        # If found, remove it
        models.pop(model_id)
        return {"message": "Model successfully removed."}
    # If not found, return fail message
    return {"message": "No model found with that ID."}
