import uuid

from fastapi import APIRouter

from api.resources.model import models

remove_model_router = APIRouter(prefix='/models/{model_id}')

@remove_model_router.delete("", status_code=200)
async def remove_model(model_id: uuid.UUID):
    """
    Delete the model specified by the given identifier from the model store.
    """
    # Find model in database
    for model in models:
        if model_id == model.id:
            models.remove(model)
            return {"message": "Model successfully removed."}
    return {"message": "No model found with that ID."}