"""
Provides the API endpoint that makes a prediction on a target variable within a given set of data.
"""

import asyncio
import random  # TESTING
import uuid

from fastapi import APIRouter
from api.resources.prediction import PredictionParams, Prediction
from api.resources.prediction import predictions

# Provides a reference to this endpoint for use by main FastAPI object
prediction_router = APIRouter(prefix='/predict')


# Using a POST request to submit prediction information from the user
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

    prediction = Prediction(flight_num=new_prediction.flight_num,
                            delay_probability=delay_prediction, id=uuid.uuid4())
    predictions.append(prediction)
    return {"prediction": prediction}
