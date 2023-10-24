#import soupport file
from .data_processing import *
from .model_setting import *
#import pipeline related lib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.pipeline import Pipeline
import pickle


def train_model(file_path,filename):
    df = process_add_columns(drop_columns(compute_delay(load_data(file_path))))

    #split test and train data set
    train_data,train_labels,test_data,test_labels = split_dataset(df)

    #transformer
    transformer = ColumnTransformer(transformers=[
        ('tnf1',OrdinalEncoder(categories=[['morning','afternoon','evening','night'],['N','I']]),['part_of_day','flight_type']),
        ('tnf2',OneHotEncoder(handle_unknown='ignore',sparse=False,drop='first'),['sched_destination_city_code','sched_airlinecode','is_weekend','sched_flight_month'])
    ],remainder='passthrough')

    #pipeline
    #please add new model in model_setting.py and just change the model fucntion in pipeline
    Grid_pipeline = Pipeline([
        ('transformer', transformer),
        ('XB_boosting', GridXGB)
        ])
    # Train it and print the best parameters (3 pts)
    Grid_pipeline.fit(train_data, train_labels)
    XGB = Grid_pipeline['XB_boosting'].best_estimator_
    #shows performance
    pipeline = Pipeline([
        ('transformer', transformer),
        ('XB_boosting', XGB)
        ])
    
    pickle.dump(pipeline, open(filename, 'wb'))