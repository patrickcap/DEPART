"""
Provides the API endpoint that finds a model, returns its status, and exports it if desired.
"""

import redis
import uuid

from fastapi import APIRouter

from api.resources.model import models

# rd = redis.Redis(host="localhost", port=)

# Provides a reference to this endpoint for use by main FastAPI object
check_model_router = APIRouter(prefix='/models/{model_id}')

# Using a GET request to fetch model information for the user
@check_model_router.get("", status_code=200)
async def check_model(model_id: uuid.UUID, export: bool = False):
    """
    Use the user-specified model ID to find the model in the store and export the 
    model if required. Return the status of the model.
    """
    print(export)

    # Find model in database
    for model in models:
        if model_id == model.id:
            # Export the model

            return {"model_status": model.status.name}
    return {"message": "No model found with that ID."}
