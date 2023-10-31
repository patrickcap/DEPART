"""
Provides the API endpoint that creates, trains, and stores a specific model.
"""

import uuid

from fastapi import APIRouter

from api.resources.model import models
#get train model file
from train import train
import shutil

# Provides a reference to this endpoint for use by main FastAPI object
create_model_router = APIRouter(prefix='/models')

# Using a POST request to submit model creation information from the user
@create_model_router.post("/training")
async def create_model(data_file:str):
    """
    Use the user-specified parameters to create, train, and store a model. Return a model identifier and status.
    """
    # Create unique id for this model, set status to pending and copy model parameters to new completed model object, then add to list
    model_id = uuid.uuid4()
    model = train(data_file, model_id)
    models[model_id]=model 
    return {"message": "New model (" + str(model_id) + ") has status Complete."}