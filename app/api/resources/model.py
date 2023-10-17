from pydantic import BaseModel
from dataclasses import dataclass
import uuid

# Array to store Model objects
models = []

class ModelParams(BaseModel):
    """Class for the parameters a user must use to define a model."""
    param_x: str
    param_y: str
    param_z: str
    # dataset, target (delay column), optionals with defaults: hyperparameter optimisation, model type (maybe, harder)

@dataclass
class Model:
    """Class for the complete parameters used to define a created model."""
    id: uuid.UUID
    status: str
    params: ModelParams
