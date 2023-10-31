# import support file
from .model import *
# import pipeline related lib
from .data_preprocessing import DataProcessor, split_dataset
from .model import XGBModel
from sklearn.pipeline import Pipeline
import pickle


def train(file_path, filename):
    # Clean up
    preprocessor = DataProcessor.create_preprocessor(file_path, ['sched_destination_city_code',
                                                                 'sched_airlinecode',
                                                                 'flight_type', 'sched_flight_hour',
                                                                 'sched_flight_minute',
                                                                 'sched_flight_dayofweek'])
    data = preprocessor.preprocess()

    # Split test and train data set
    train_data, train_labels = split_dataset(data)

    # pipeline
    # please add new model in model.py and just change the model function in pipeline
    model_instance = XGBModel.new_model(max_depth=3,
                               learning_rate=0.1,
                               n_estimators=5,
                               objective='binary:logistic',
                               booster='gbtree',
                               n_jobs=2,
                               gamma=0.001,
                               subsample=0.632,
                               colsample_bytree=1,
                               colsample_bylevel=1,
                               colsample_bynode=1,
                               reg_alpha=1,
                               reg_lambda=0,
                               scale_pos_weight=1,
                               base_score=0.5,
                               random_state=20212004,
                               missing=1,
                               use_label_encoder=False)

    model_instance = model_instance.fit(train_data, train_labels)

    test_data = [train_data[0]]

    prediction_proba = model_instance.predict_proba(test_data)
    prediction = model_instance.predict(test_data)

    print('True label: ', train_labels[0])
    print('Predicted probabilities: ', prediction_proba)
    print('Final prediction: ', prediction)
    #Model(filename,ModelStatus.COMPLETED,model_instance)
    return model_instance
    # pickle.dump(pipeline, open(filename, 'wb'))
