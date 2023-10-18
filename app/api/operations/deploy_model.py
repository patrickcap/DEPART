import uuid

from fastapi import APIRouter, Depends
from fastapi.security.api_key import APIKey

from api.auth import get_api_key

deploy_model_router = APIRouter(prefix='/deploy')

@deploy_model_router.put("")
async def deploy_model(model_id: uuid.UUID, api_key: APIKey = Depends(get_api_key)):
    """
    If the user provides a valid API key and their specified model has a status of 'completed', deploy that model. Return a success message if the model is deployed or an appropriate error message otherwise.
    """
    # Find model


    # Check status of model


    # If status is 'completed', deploy the specified model


    # Otherwise, return an appropriate error


    return {"message": "Valid key for private endpoint " + str(api_key)}