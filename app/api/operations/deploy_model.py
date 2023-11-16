"""
Provides the API endpoint that deploys a specific model.
"""

import uuid

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security.api_key import APIKey
from app.api.resources import Model, ModelStatus
from app.api.resources.model import models
from app.api.auth import get_api_key
CURRENT_MODEL = []

# Provides a reference to this endpoint for use by main FastAPI object
deploy_model_router = APIRouter(prefix='/deploy')


# Using a PUT request to modify the state of a model
@deploy_model_router.put("",status_code=200)
async def deploy_model(model_id: uuid.UUID, api_key: APIKey = Depends(get_api_key)) -> JSONResponse:
    """
    If the user provides a valid API key and their specified model has a status of 'completed',
    deploy that model. Return a success message if the model is deployed or an
    appropriate error message otherwise.
    """
    # Find model
    try:
        request_model = models[model_id]
    except:
        return JSONResponse(contect="No model found with that ID."
                            , status_code = 204)

    # Check status of model
    # If status is 'completed', deploy the specified model
    if request_model.status == ModelStatus.COMPLETED:
        CURRENT_MODEL.clear()
        CURRENT_MODEL.append(request_model)
        return JSONResponse(contect= "Model deployed successfully"
                            , status_code = 200)
    # Otherwise, return an appropriate error
    if request_model.status == ModelStatus.FAILED:
        return JSONResponse(contect = "The request model is a failed model."
                            , status_code = 203)
    else:
        return JSONResponse(contect = "The request model is not ready yet."
                            , status_code = 203)


    