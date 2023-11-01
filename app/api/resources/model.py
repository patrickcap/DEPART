"""
Specifies the information required by the user to create any
model and the information that defines a completed model.
"""
import uuid
from dataclasses import dataclass
from train import XGBModel
from .enumerations import ModelStatus

# List to store Model objects
models = {}


@dataclass
class ModelParams:
    """
    Defines the parameters a user must specify to create a model.
    """
    max_depth: int = 3
    learning_rate: float = 0.1
    n_estimators: int = 5
    objective: str = 'binary:logistic'
    booster: str = 'gbtree'
    n_jobs: int = 2
    gamma: float = 0.001
    subsample: float = 0.632
    colsample_bytree: int = 1
    colsample_bylevel: int = 1
    colsample_bynode: int = 1
    reg_alpha: int = 1
    reg_lambda: int = 0
    scale_pos_weight: int = 1
    base_score: float = 0.5
    random_state: int = 20212004
    missing: int = 1
    use_label_encoder: bool = False
    # dataset, target (delay column), optionals with defaults:
    # hyperparameter optimisation, model type (maybe, harder)

@dataclass
class Model:
    """
    Defines the parameters of a created model.
    """
    id: uuid.UUID
    status: ModelStatus
    model: XGBModel
    params: ModelParams
