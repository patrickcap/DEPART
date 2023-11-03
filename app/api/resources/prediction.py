"""
Specifies the information required by the user to make a prediction on any model.
"""

from dataclasses import dataclass


@dataclass
class PredictionParams:
    """
    Defines the parameters required to make a predicition using any model that can be created by the user.
    """
    destination_city_code: str
    sched_airlinecode: str
    flight_type: str
    sched_date_time: object
