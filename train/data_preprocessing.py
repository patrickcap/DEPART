from dataclasses import dataclass
from typing import Optional

import pandas
from sklearn.model_selection import StratifiedShuffleSplit
from data_loading import DataLoader
import pandas as pd
from pandas import DataFrame, DatetimeIndex


# from sklearn.model_selection import StratifiedShuffleSplit


def compute_delay_helper(actual_date_time: DatetimeIndex, sched_date_time: DatetimeIndex) -> int:
    return int(actual_date_time > sched_date_time)


def process_flight_num(flight_num: pandas.Series) -> str:
    flight_num = str(flight_num)
    flight_num = flight_num.split('.')[0]
    for i in flight_num:
        if i.isalpha():
            flight_num = flight_num.replace(i, str(ord(i)))
    return flight_num


def get_part_of_day(date_time: DatetimeIndex) -> str:
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
    dayofweek = date_time.dayofweek
    if dayofweek < 5:
        return 0
    else:
        return 1


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
        self.data = self.compute_delay(self.data)

        # Process flight numbers, making sure they only contain numbers
        print(self.data.info())
        print(self.data.sched_flight_num[0])
        print(type(self.data.sched_flight_num))
        self.data.sched_flight_num = self.data.sched_flight_num.apply(process_flight_num)

        # Compute new features
        self.data = self.add_features()

        # Select useful features
        self.data = self.data[['sched_flight_num', 'sched_destination_city_code', 'sched_airlinecode',
                               'flight_type', 'delay', 'sched_flight_hour', 'sched_flight_minute',
                               'sched_flight_dayofweek']]

        return self.data
        # return processed_data, delay

    def compute_delay(self, data: DataFrame) -> DataFrame:
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

    def add_features(self) -> DataFrame:
        self.data['sched_date_time'] = pd.to_datetime(self.data['sched_date_time'],
                                                      format='%Y-%m-%d %H:%M:%S',
                                                      errors='raise')
        self.data['part_of_day'] = self.data['sched_date_time'].apply(get_part_of_day)
        self.data['is_weekend'] = self.data['sched_date_time'].apply(is_weekend)
        self.data['sched_flight_month'] = self.data['sched_date_time'].dt.month
        return self.data


# Instead of dropping features, we will just select the ones we want. This will avoid some errors if we try to drop
# something that is not there
def drop_columns(df):
    actual_drop = ["actual_date_time", "actual_flight_num", "actual_OG_city_code",
                   "actual_destination_city_code", "actual_airline_code", "actual_flight_day",
                   "actual_flight_month", "actual_flight_year", "dayof_week_actual_flight",
                   ]
    features2_drop = ["sched_OG_city_code", "dest_city", "airline", "OG_city"]
    df = df.drop(actual_drop, axis=1)
    df = df.drop(features2_drop, axis=1)
    return df

def split_dataset(df):
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(df, df["delay"]):
        strat_train_set = df.iloc[train_index]
        strat_test_set = df.iloc[test_index]

    train_labels = strat_train_set['delay'].copy()
    train_labels = train_labels.astype('int')
    train_data = strat_train_set.drop('delay', axis=1)

    test_labels = strat_test_set['delay'].copy()
    test_labels = test_labels.astype('int')
    test_data = strat_test_set.drop('delay', axis=1)
    return train_data, train_labels, test_data, test_labels
