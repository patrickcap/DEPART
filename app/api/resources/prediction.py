"""
Specifies the information required by the user to make a prediction on any model.
"""

import uuid

from dataclasses import dataclass
from pydantic import BaseModel

# List to store PredictionParams objects
predictions = []

class PredictionParams(BaseModel):
    """
    Defines the parameters required to make a predicition using 
    any model that can be created by the user.
    """
    flight_num: str
    year_num: int
    month_num: int
    day_num: int
    hour_num: int
    minute_num: int

@dataclass
class Prediction:
    """
    Defines the parameters of a returned prediction.
    """
    flight_num: str
    delay_probability: float
    id: uuid.UUID
