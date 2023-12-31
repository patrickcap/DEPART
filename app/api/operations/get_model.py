"""
Provides the API endpoint that finds a model, returns its status, and exports it if desired.
"""

import uuid
import pickle
from fastapi import APIRouter

from app.api.resources.model import models

# Provides a reference to this endpoint for use by main FastAPI object
check_model_router = APIRouter(prefix='/models')


# Using a GET request to fetch model information for the user
@check_model_router.get("/{model_id}", status_code=200)
async def check_model(model_id: uuid.UUID, export: bool = False):
    """
    Use the user-specified model ID to find the model in the store and export the 
    model if required. Return the status of the model.
    """
    # Find model in database
    try:
        get_model = models[model_id]
        if export is True:
            file_name = str(model_id) + ".pkl"
            pickle.dump(get_model, open(file_name, 'wb'))
            return {"Model have saved successfully in file " + file_name}
        else:
            return {"Model status": get_model.status.value}
    except:
        return {"message": "No model found with that ID."}
