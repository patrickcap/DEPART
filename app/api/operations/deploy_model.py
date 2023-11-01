"""
Provides the API endpoint that deploys a specific model.
"""

import uuid

from fastapi import APIRouter, Depends
from fastapi.security.api_key import APIKey
from api.resources import Model, ModelStatus
from api.resources.model import models
from api.auth import get_api_key
CURRENT_MODEL = []
# Provides a reference to this endpoint for use by main FastAPI object
deploy_model_router = APIRouter(prefix='/deploy')

# Using a PUT request to modify the state of a model
@deploy_model_router.put("")
async def deploy_model(model_id: uuid.UUID, api_key: APIKey = Depends(get_api_key)):
    """
    If the user provides a valid API key and their specified model has a status of 'completed', deploy that model. Return a success message if the model is deployed or an appropriate error message otherwise.
    """
    # Find model
    try:
        request_model = models[model_id]
    except:
        return {"message": "No model found with that ID."}

    # Check status of model
    # If status is 'completed', deploy the specified model
    if request_model.status == ModelStatus.COMPLETED:
        CURRENT_MODEL.append(request_model)  
        return {"message": "Model deployed successfully"}
    # Otherwise, return an appropriate error
    if request_model.status == ModelStatus.FAILED:
        return {"message": "The reuqest model is a failed model."}
    else:
        return {"message": "The request model is not ready yet."}

    #return {"message": "Valid key for private endpoint " + str(api_key)}