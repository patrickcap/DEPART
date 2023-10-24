import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit

def load_data(data_path):
  df = pd.read_csv(data_path)
  df = df.rename(columns={"Fecha-I":"sched_date_time",
                            "Vlo-I":"sched_flight_num",
                            "Ori-I":"sched_OG_city_code",
                            "Des-I":"sched_destination_city_code",
                            "Emp-I":"sched_airlinecode",
                            "Fecha-O": "actual_date_time",
                            "Vlo-O":"actual_flight_num",
                            "Ori-O":"actual_OG_city_code",
                            "Des-O":"actual_destination_city_code",
                            "Emp-O":"actual_airline_code",
                            "DIA":"actual_flight_day",
                            "MES":"actual_flight_month",
                            "AÑO":"actual_flight_year",
                            "DIANOM":"dayof_week_actual_flight",
                            "TIPOVUELO":"flight_type",
                            "OPERA":"airline",
                            "SIGLAORI":"OG_city",
                            "SIGLADES":"dest_city"
                            })
  return df


def compute_delay_helper(actual_date_time, sched_date_time):

  return int(actual_date_time > sched_date_time)

def compute_delay(df):
  df['delay'] = ''
  df_copy = df.copy()
  for index, row in df.iterrows():
      df_copy.at[index, 'delay'] = compute_delay_helper(pd.to_datetime(row['actual_date_time'],
                                                                format = '%Y-%m-%d %H:%M:%S',
                                                                errors='raise'),
                                                pd.to_datetime(row['sched_date_time'],
                                                                format = '%Y-%m-%d %H:%M:%S',
                                                                errors='raise'))
  df = df_copy
  return df

def drop_columns(df):
  actual_drop = ["actual_date_time","actual_flight_num","actual_OG_city_code",
                    "actual_destination_city_code","actual_airline_code","actual_flight_day",
                    "actual_flight_month","actual_flight_year","dayof_week_actual_flight",
                    ]
  features2_drop = ["sched_OG_city_code","dest_city","airline","OG_city"]
  df=df.drop(actual_drop,axis=1)
  df=df.drop(features2_drop,axis=1)
  return df

def process_flight_num(flight_num):
  flight_num = str(flight_num)
  flight_num = flight_num.split('.')[0]
  for i in flight_num:
    if i.isalpha():
      flight_num = flight_num.replace(i, str(ord(i)))
  # flight_num = int(flight_num)
  return flight_num

def get_part_of_day(date_time):
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

def is_weekend(date_time):
  dayofweek = date_time.dayofweek
  if dayofweek < 5:
    return 0
  else:
    return 1

def process_add_columns(df):
  df.sched_flight_num = df.sched_flight_num.apply(process_flight_num)
  df['sched_date_time'] = pd.to_datetime(df['sched_date_time'],
                                        format = '%Y-%m-%d %H:%M:%S',
                                        errors='raise')
  df['part_of_day'] = df['sched_date_time'].apply(get_part_of_day)
  df['is_weekend'] = df['sched_date_time'].apply(is_weekend)
  df['sched_flight_month'] = df['sched_date_time'].dt.month
  df = df.drop('sched_date_time',axis=1)
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
  return train_data,train_labels,test_data,test_labels