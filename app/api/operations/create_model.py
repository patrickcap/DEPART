import uuid

from fastapi import APIRouter

from api.resources.model import UserDefinedModelParams, CompleteModelParams, models

create_model_router = APIRouter(prefix='/models')

# Request, predict, and return the delay probability of a particular future flight.
@create_model_router.post("", status_code=200)
async def create_model(new_model: UserDefinedModelParams):
    # Create unique id for this model, set status to pending and copy model parameters to new completed model object, then add to list
    model = CompleteModelParams(id=str(uuid.uuid4()), status="pending", param_x=new_model.param_x, param_y=new_model.param_y, param_z=new_model.param_z)
    models.append(model)
    return {"message": "New model (" + model.id + ") has status " + model.status + "."}