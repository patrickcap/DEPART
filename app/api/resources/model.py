from pydantic import BaseModel
from dataclasses import dataclass

# Array to store Model objects
models = []

class UserDefinedModelParams(BaseModel):
    """Class for the parameters a user must use to define a model."""
    param_x: str
    param_y: str
    param_z: str

@dataclass
class CompleteModelParams:
    """Class for the complete parameters used to define a created model."""
    id: str
    status: str
    param_x: str
    param_y: str
    param_z: str

# @dataclass(kw_only=True)
# class ModelParams(UserDefinedModelParams):
#     """Class for the complete parameters used to define a created model."""
#     id: str
#     status: str