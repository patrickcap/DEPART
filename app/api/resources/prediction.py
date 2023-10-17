from pydantic import BaseModel

predictions = []

class PredictionParams(BaseModel):
    flight_num: str
    year_num: int
    month_num: int
    day_num: int
    hour_num: int
    minute_num: int
