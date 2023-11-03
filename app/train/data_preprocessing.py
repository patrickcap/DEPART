"""
Functions for Preprocessing Training and User Input Data.
"""

from dataclasses import dataclass
from typing import Optional

from sklearn.model_selection import StratifiedShuffleSplit

import pandas as pd
from pandas import DataFrame, DatetimeIndex
from .data_loading import DataLoader

def compute_delay_helper(actual_date_time: DatetimeIndex, sched_date_time: DatetimeIndex) -> int:
    """
    Computation for determining delay boolean feature
    """
    return int(actual_date_time > sched_date_time)

def get_part_of_day(date_time: DatetimeIndex) -> str:
    """
    Computation for determing time of day based on the time 
    provided. 
    """
    h = date_time.hour
    return (
        1 if 5 <= h <= 11
        else 2 if 12 <= h <= 17
        else 3 if 18 <= h <= 22
        else 4
    )


def is_weekend(date_time: DatetimeIndex) -> int:
    """
    Computation for determining whether it is the weekend 
    based on the provided date. 
    """
    dayofweek = date_time.dayofweek
    if dayofweek < 5:
        return 0
    else:
        return 1


def compute_delay(data: DataFrame) -> DataFrame:
    """
    Calculating the delay target feature and appending 
    it to the dataframe provided. 
    """

    data['delay'] = ''
    data_copy = data.copy()
    for index, row in data_copy.iterrows():
        data_copy.at[index, 'delay'] = compute_delay_helper(pd.to_datetime(row['actual_date_time'],
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
        return cls(source=source, columns=columns)

    def preprocess(self):
        # Load data and translate column names
        self.data = DataLoader.load(self.source, self.columns)
        self.data = self.data.build_dataframe()

        # Handle missing values
        self.data.dropna()

        # Compute delay column and leave separate
        self.data = compute_delay(self.data)

        # Compute new features
        self.data = self.add_features()

        # Select useful features
        self.data = self.data[['sched_destination_city_code', 'sched_airlinecode',
                               'flight_type', 'delay', 'part_of_day', 'is_weekend',
                                'sched_flight_month']]


        return self.data

    def add_features(self) -> DataFrame:
        self.data['sched_date_time'] = pd.to_datetime(self.data['sched_date_time'],
                                                      format='%Y-%m-%d %H:%M:%S',
                                                      errors='raise')
        self.data['part_of_day'] = self.data['sched_date_time'].apply(get_part_of_day)
        self.data['is_weekend'] = self.data['sched_date_time'].apply(is_weekend)
        self.data['sched_flight_month'] = self.data['sched_date_time'].dt.month
        if 'sched_date_time' in self.data:
            self.data = self.data.drop('sched_date_time',axis=1)
        return self.data


def split_dataset(data):
    train_labels = data['delay'].copy()
    train_labels = train_labels.astype('int')

    train_data = data.drop('delay', axis=1)
    #train_data = train_data.to_numpy()

    return train_data, train_labels

# Instead of dropping features, we just select the ones we want.
# This will avoid some errors if we try to drop something not there
def drop_columns(df):
    actual_drop = ["actual_date_time", "actual_flight_num", "actual_OG_city_code",
                   "actual_destination_city_code", "actual_airline_code", "actual_flight_day",
                   "actual_flight_month", "actual_flight_year", "dayof_week_actual_flight",
                   ]
    features2_drop = ["sched_OG_city_code", "dest_city", "airline", "OG_city"]
    df = df.drop(actual_drop, axis=1)
    df = df.drop(features2_drop, axis=1)
    return df
