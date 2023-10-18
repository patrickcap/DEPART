"""
Provides the API endpoint that creates, trains, and stores a specific model.
"""

import uuid

from fastapi import APIRouter

from api.resources.model import ModelParams, Model, models
from api.resources.enumerations import ModelStatus

# Provides a reference to this endpoint for use by main FastAPI object
create_model_router = APIRouter(prefix='/models')

# Using a POST request to submit model creation information from the user
@create_model_router.post("", status_code=200)
async def create_model(new_model: ModelParams):
    """
    Use the user-specified parameters to create, train, and store a model. Return a model identifier and status.
    """
    # Create unique id for this model, set status to pending and copy model parameters to new completed model object, then add to list
    model = Model(id=uuid.uuid4(), status=ModelStatus.PENDING, params=new_model)
    models.append(model)
    return {"message": "New model (" + str(model.id) + ") has status " + str(model.status) + "."}