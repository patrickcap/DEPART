"""
Training the model
"""

from pandas import DataFrame
from xgboost import XGBClassifier
from .data_preprocessing import DataProcessor, split_dataset
from .model_pipeline import XGBModel


def train(file_path: str, params) -> XGBClassifier:
    """
    Remove this docstring on merge
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
    model_instance: XGBClassifier = XGBModel.new_model(params.max_depth,
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

    model_instance: XGBClassifier = model_instance.fit(train_data, train_labels)

    return model_instance
