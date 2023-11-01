"""
Helper functions for loading the flight data and preparing it for training
"""

from dataclasses import dataclass
from typing import Optional

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder

import pandas as pd
from pandas import DataFrame, DatetimeIndex
from .data_loading import DataLoader

def compute_delay_helper(actual_date_time: DatetimeIndex, sched_date_time: DatetimeIndex) -> int:
    """
    Loop over all flights and determine if they are delayed
    """
    return int(actual_date_time > sched_date_time)


def process_flight_num(flight_num: pd.Series) -> str:
    """
    Find and return flight number for a flight
    """
    flight_num = str(flight_num)
    flight_num = flight_num.split('.', maxsplit=-1)[0]
    for i in flight_num:
        if i.isalpha():
            flight_num = flight_num.replace(i, str(ord(i)))
    return flight_num


def get_part_of_day(date_time: DatetimeIndex) -> str:
    """
    Divide times of day into categories 
    """
    h = date_time.hour
    return (
        "morning"
        if 5 <= h <= 11
        else "afternoon"
        if 12 <= h <= 17
        else "evening"
        if 18 <= h <= 22
        else "night"
    )


def is_weekend(date_time: DatetimeIndex) -> int:
    """
    Determine if a time of week is on the weekend
    """
    dayofweek = date_time.dayofweek
    if dayofweek < 5:
        return 0
    else:
        return 1


def compute_delay(data: DataFrame) -> DataFrame:
    """
    Loop over all flights and determine if they are delayed
    """
    data['delay'] = ''
    data_copy = data.copy()
    for index, row in data_copy.iterrows():
        data_copy.at[index, 'delay'] = compute_delay_helper(
            pd.to_datetime(row['actual_date_time'],
                           format='%Y-%m-%d %H:%M:%S',
                           errors='raise'),
            pd.to_datetime(row['sched_date_time'],
                           format='%Y-%m-%d %H:%M:%S',
                           errors='raise'))
    data = data_copy
    return data


@dataclass
class DataProcessor:
    """
    Preprocesses data after loading.

    Args:

    """

    source: str
    columns: list[str]
    data: Optional[DataFrame] = None

    @classmethod
    def create_preprocessor(cls, source: str, columns: list[str]):
        """
        Construct a class for preprocessing the data 
        """
        return cls(source=source, columns=columns)

    def preprocess(self):
        """
        Load the data, remove the redundant fields and create/keep the salient fields
        """
        # Load data and translate column names
        self.data = DataLoader.load(self.source, self.columns)
        self.data = self.data.build_dataframe()

        # Handle missing values
        self.data.dropna()

        # Compute delay column and leave separate
        self.data = compute_delay(self.data)

        # Process flight numbers, making sure they only contain numbers
        self.data.sched_flight_num = self.data.sched_flight_num.apply(process_flight_num)

        # Compute new features
        self.data = self.add_features()

        # Select useful features
        self.data = self.data[['sched_destination_city_code',
                               'sched_airlinecode',
                               'flight_type',
                               'delay',
                               'part_of_day',
                               'is_weekend',
                               'sched_flight_month']]

        # Encode the categorical data
        self.data = self.encode()

        return self.data

    def encode(self) -> DataFrame:
        """
        Convert categorical values to numerical for the learning model
        """
        transformer = ColumnTransformer(transformers=[
            ('tnf1', OrdinalEncoder(categories=[
                        ['morning', 'afternoon', 'evening', 'night'],
                        ['N', 'I']]),['part_of_day', 'flight_type']),
            ('tnf2', OneHotEncoder(handle_unknown='ignore', sparse_output=False, drop='first'),
             ['sched_destination_city_code', 'sched_airlinecode',
              'is_weekend', 'sched_flight_month'])
        ], remainder='passthrough')

        # Transform data using the transformations defined above
        self.data = pd.DataFrame(transformer.fit_transform(self.data))

        # Add names to the columns so that they can be address later
        self.data.columns = transformer.get_feature_names_out()

        return self.data

    def add_features(self) -> DataFrame:
        """
        Add salient features to DataFrame
        """
        self.data['sched_date_time'] = pd.to_datetime(self.data['sched_date_time'],
                                                      format='%Y-%m-%d %H:%M:%S',
                                                      errors='raise')
        self.data['part_of_day'] = self.data['sched_date_time'].apply(get_part_of_day)
        self.data['is_weekend'] = self.data['sched_date_time'].apply(is_weekend)
        self.data['sched_flight_month'] = self.data['sched_date_time'].dt.month
        return self.data

def split_dataset(data):
    """
    Divide data into training and testing sets
    """
    train_labels = data['remainder__delay'].copy()
    train_labels = train_labels.astype('int')

    train_data = data.drop('remainder__delay', axis=1)
    train_data = train_data.to_numpy()

    return train_data, train_labels


# Instead of dropping features, we will just select the ones we want.
# This will avoid some errors if we try to drop
# something that is not there
def drop_columns(df):
    """
    Remove redundant fields
    """
    actual_drop = ["actual_date_time", "actual_flight_num", "actual_OG_city_code",
                   "actual_destination_city_code", "actual_airline_code", "actual_flight_day",
                   "actual_flight_month", "actual_flight_year", "dayof_week_actual_flight",
                   ]
    features2_drop = ["sched_OG_city_code", "dest_city", "airline", "OG_city"]
    df = df.drop(actual_drop, axis=1)
    df = df.drop(features2_drop, axis=1)
    return df
