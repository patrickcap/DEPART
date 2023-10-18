"""
Specifies the information required by the user to make a prediction on any model.
"""

from pydantic import BaseModel

# List to store PredictionParams objects
predictions = []

class PredictionParams(BaseModel):
    """
    Defines the parameters required to make a predicition using any model that can be created by the user.
    """
    flight_num: str
    year_num: int
    month_num: int
    day_num: int
    hour_num: int
    minute_num: int
