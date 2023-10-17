from fastapi import APIRouter
import uuid

from api.resources.model import models

check_model_router = APIRouter(prefix='/models/{model_id}')

# Check the training status of a model
@check_model_router.get("", status_code=200)
async def check_model(model_id: uuid.UUID, export: bool = False):
    print(export)

    # Find model in database
    for model in models:
        if model_id == model.id:
            # Export the model

            return {"model_status": model.status.name}
    return {"message": "No model found with that ID."}