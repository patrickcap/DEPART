from fastapi import FastAPI
from pydantic import BaseModel

class PredictionParams(BaseModel):
    ML_model_id: int
    flight_num: str
    year_num: int
    month_num: int
    day_num: int
    hour_num: int
    minute_num: int