import asyncio
import random
import uuid

from dataclasses import dataclass
from fastapi import APIRouter
from api.resources.prediction import PredictionParams
from typing import Any

predictions = []

prediction_router = APIRouter(prefix='/predictions')

# Request, predict, and return the delay probability of a particular future flight.
@prediction_router.post("", status_code=200)
async def create_prediction(prediction_params: PredictionParams):
    # Pass prediction_params to the model with id model_id

    ##############################################
    # Simulating the model fetching the prediction
    await asyncio.sleep(2)
    delay_prediction: float = random.random()
    ##############################################

    prediction_id: str = str(uuid.uuid4())
    prediction = {"ML_model_id": prediction_params.ML_model_id,
                    "flight_num": prediction_params.flight_num,
                    "delay_probability": delay_prediction,
                    "id": prediction_id}

    predictions.append(prediction)
    return {"prediction": prediction}