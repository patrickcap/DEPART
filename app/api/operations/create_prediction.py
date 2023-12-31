"""
Provides the API endpoint that makes a prediction on a target variable within a given set of data.
"""

import pandas as pd
from fastapi import APIRouter
from app.api.resources.prediction import PredictionParams
from app.api.operations.deploy_model import CURRENT_MODEL

# Provides a reference to this endpoint for use by main FastAPI object
from app.train.data_preprocessing import DataProcessor

prediction_router = APIRouter(prefix='/predict')


# Using a POST request to submit prediction information from the user
@prediction_router.post("", status_code=200)
async def create_prediction(prediction_params: PredictionParams):
    """
    Use the user-specified parameters to make a prediction on a model. Return the prediction result.
    """

    # Put data into dataframe for data processing
    user_input_processor = DataProcessor(None, None,
                                         pd.DataFrame(
                                             {'sched_destination_city_code': prediction_params.destination_city_code,
                                              'sched_airlinecode': prediction_params.sched_airlinecode,
                                              'flight_type': prediction_params.flight_type,
                                              'sched_date_time': prediction_params.sched_date_time},
                                             index=[0]))

    # Process the dataframe
    user_input_processor.add_features()
    user_input_processor.data = user_input_processor.data[[
        'sched_destination_city_code', 'sched_airlinecode',
        'flight_type', 'part_of_day', 'is_weekend', 'sched_flight_month']]

    prediction_data = user_input_processor.data

    delay_prediction = CURRENT_MODEL[0].model.predict_proba(prediction_data)

    return {"message": float(delay_prediction[0][1])}
