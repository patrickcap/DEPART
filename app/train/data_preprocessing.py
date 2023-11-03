"""
Helper functions for loading the flight data and preparing it for training
"""

from dataclasses import dataclass
from typing import Optional

from sklearn.model_selection import StratifiedShuffleSplit
import pandas as pd
from pandas import DataFrame, DatetimeIndex
from .data_loading import DataLoader


def compute_delay_helper(actual_date_time: DatetimeIndex, sched_date_time: DatetimeIndex) -> int:
    """
    Loop over all flights and determine if they are delayed
    """
    return int(actual_date_time > sched_date_time)


def get_part_of_day(date_time: DatetimeIndex) -> str:
    """
    Divide times of day into categories
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
    Determine if a time of week is on the weekend
    """
    dayofweek = date_time.dayofweek
    if dayofweek < 5:
        return 0
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
        if 'sched_date_time' in self.data:
            self.data = self.data.drop('sched_date_time', axis=1)
        return self.data


def split_dataset(data):
    """
    Divide data into training and testing sets
    """
    train_labels = data['delay'].copy()
    train_labels = train_labels.astype('int')

    train_data = data.drop('delay', axis=1)
    #train_data = train_data.to_numpy()

    return train_data, train_labels
