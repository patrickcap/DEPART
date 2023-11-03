"""
Provides the API endpoint that creates, trains, and stores a specific model.
"""

import uuid

from fastapi import APIRouter

from api.resources.model import models, ModelParams, Model, ModelStatus
from train import train
import pickle

# Provides a reference to this endpoint for use by main FastAPI object
create_model_router = APIRouter(prefix='/models')


# Using a POST request to submit model creation information from the user
@create_model_router.post("/train")
async def create_model(data_file: str, params: ModelParams):
    """
    Use the user-specified parameters to create, train, and store a model.
    Return a model identifier and status.
    """
    # Create unique id for this model, set status to pending and
    # copy model parameters to new completed model object,
    # then add to list
    model_id = uuid.uuid4()

    # Instance of Model containing the trained model
    model = Model(id=model_id, status=ModelStatus.PENDING, params=params, model=None)
    trained_model = train.train(data_file, params, model)
    models[model_id] = trained_model

    return {"message": "New model (" + str(model_id) + ") has status " + str(trained_model.status) + "."}


@create_model_router.post("/upload")
async def upload_model(model_file: str):
    """
    Use local exist trained model file by uploading to api
    Return a model identifier and status.
    """
    model_id = uuid.uuid4()
    model = Model(id=model_id, status=ModelStatus.PENDING, params=None, model=None)

    try:
        with open(model_file, "rb") as input_file:
            loaded_file = pickle.load(input_file)
        model.model = loaded_file
        model.status = ModelStatus.COMPLETED
        models[model_id] = model
    except:
        model.status = ModelStatus.FAILED

    return {"message": 
            "Trained model (" + str(model_id) + ") has status " + str(model.status) + "is added into models."}

@create_model_router.get("/all")
async def get_all_models():
    return {str(list(models.keys()))}

