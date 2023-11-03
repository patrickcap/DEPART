"""
Provides the API endpoint that creates, trains, and stores a specific model.
"""

import uuid

from fastapi import APIRouter

from app.api.resources.model import models
from app.api.resources import Model, ModelStatus
# get train model file
from app.train import train
from app.api.resources.model import ModelParams

# Provides a reference to this endpoint for use by main FastAPI object
create_model_router = APIRouter(prefix='/models')


# Using a POST request to submit model creation information from the user
@create_model_router.post("/train")
async def create_model(data_file: str, params: ModelParams):
    """
    Use the user-specified parameters to create, train, and store a model. Return a model identifier and status.
    """
    # Create unique id for this model, set status to pending and copy model parameters to new completed model object,
    # then add to list
    model_id = uuid.uuid4()
    trained_model = train.train(data_file, params)
    model = Model(id=model_id, status=ModelStatus.COMPLETED, params=params, model=trained_model)
    models[model_id] = model
    return {"message": "New model (" + str(model_id) + ") has status " + str(model.status) + "."}
