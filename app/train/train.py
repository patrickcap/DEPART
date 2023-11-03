"""
Create an instance of a trained model using data provided
"""
import uuid
from pandas import DataFrame
from xgboost import XGBClassifier
from .data_preprocessing import DataProcessor, split_dataset
from .model_pipeline import XGBModel
from app.api.resources import ModelStatus
from sklearn.pipeline import Pipeline


def train(file_path: str, params, model) -> XGBClassifier:
    """
    Train a machine learning model with the data from the path provided
    """

    preprocessor: DataProcessor = DataProcessor.create_preprocessor(
        file_path, ['sched_destination_city_code',
                    'sched_airlinecode',
                    'flight_type', 'sched_flight_hour',
                    'sched_flight_minute',
                    'sched_flight_dayofweek'])
    data: DataFrame = preprocessor.preprocess()

    # Split test and train data set
    train_data, train_labels = split_dataset(data)

    # pipeline
    # please add new model in model.py and just change the model function in pipeline
    model_pipeline: Pipeline = XGBModel.new_model(params.max_depth,
                                                  params.learning_rate,
                                                  params.n_estimators,
                                                  params.objective,
                                                  params.booster,
                                                  params.n_jobs,
                                                  params.gamma,
                                                  params.subsample,
                                                  params.colsample_bytree,
                                                  params.colsample_bylevel,
                                                  params.colsample_bynode,
                                                  params.reg_alpha,
                                                  params.reg_lambda,
                                                  params.scale_pos_weight,
                                                  params.base_score,
                                                  params.random_state,
                                                  params.missing,
                                                  params.use_label_encoder)
    model.status = ModelStatus.IN_PROGRESS

    try:
        model_pipeline: Pipeline = model_pipeline.fit(train_data, train_labels)
        model.status = ModelStatus.COMPLETED
        model.model = model_pipeline
    except ValueError:
        model.status = ModelStatus.FAILED
        print(f'The model has status {model.status.value}: Something went wrong during training')

    return model
