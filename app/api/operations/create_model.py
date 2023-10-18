import uuid

from fastapi import APIRouter

from api.resources.model import ModelParams, Model, models
from api.resources.enumerations import ModelStatus

create_model_router = APIRouter(prefix='/models')

# Request, predict, and return the delay probability of a particular future flight.
@create_model_router.post("", status_code=200)
async def create_model(new_model: ModelParams):
    """
    Use the user-specified parameters to create, train, and store a machine learning model. Return a model identifier and status.
    """
    # Create unique id for this model, set status to pending and copy model parameters to new completed model object, then add to list
    model = Model(id=uuid.uuid4(), status=ModelStatus.PENDING, params=new_model)
    models.append(model)
    return {"message": "New model (" + str(model.id) + ") has status " + str(model.status) + "."}