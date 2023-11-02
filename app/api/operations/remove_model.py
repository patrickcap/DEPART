"""
Provides the API endpoint that deletes a given model from the model store.
"""

import uuid

from fastapi import APIRouter

from api.resources.model import models

# Provides a reference to this endpoint for use by main FastAPI object
remove_model_router = APIRouter(prefix='/models/{model_id}')

# Using a DELETE request to remove a model resource
@remove_model_router.delete("", status_code=200)
async def remove_model(model_id: uuid.UUID):
    """
    Delete the model specified by the given identifier from the model store.
    """
    # Find model in database
    try:
            models.pop(model_id)
            return {"message" : "Model "+str(model_id)+ " is deleted from the storage"}
    except:
            return {"message": "No model found with that ID."}
