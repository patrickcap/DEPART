"""
Specifies the information required by the user to create any
model and the information that defines a completed model.
"""
import uuid
from dataclasses import dataclass
from pydantic import BaseModel

# List to store Model objects
models = []

class ModelParams(BaseModel):
    """
    Defines the parameters a user must specify to create a model.
    """
    param_x: str
    param_y: str
    param_z: str
    # dataset, target (delay column), optionals with defaults:
    # hyperparameter optimisation, model type (maybe, harder)

@dataclass
class Model:
    """
    Defines the parameters of a created model.
    """
    id: uuid.UUID
    status: str
    # model: None | (something else, sklearn object, ...)
    params: ModelParams
