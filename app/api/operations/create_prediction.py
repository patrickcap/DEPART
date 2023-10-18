import asyncio
import joblib
import random # TESTING
import uuid

from fastapi import APIRouter
from api.resources.prediction import PredictionParams

from api.resources.prediction import predictions

prediction_router = APIRouter(prefix='/predict')

@prediction_router.post("", status_code=200)
async def create_prediction(new_prediction: PredictionParams):
    """
    Use the user-specified parameters to make a prediction on a model. Return the prediction result.
    """

    # Pass new_prediction to the model with id model_id

    ##############################################
    # Simulating the model fetching the prediction
    await asyncio.sleep(2)
    delay_prediction: float = random.random()
    ##############################################

    lr = joblib.load('randomfs.pkl')

    prediction_id: str = str(uuid.uuid4())
    prediction = {"flight_num": new_prediction.flight_num,
                  "delay_probability": delay_prediction,
                  "id": prediction_id}

    predictions.append(prediction)
    return {"prediction": prediction}