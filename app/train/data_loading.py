"""
Access data to learn and organise it into a DataFrame object
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import pandas as pd
from pandas import DataFrame


def discover_csv_files(source: str) -> str:
    """
    Search for data in specified path location
    """
    csv_folder_path = Path(source)

    # TODO: Add functionality to handle a dir with several .csv files
    if csv_folder_path.is_file() and '.csv' == csv_folder_path.suffix:
        return source

    else:
        raise Exception(
            f'DATA_CONFIG_ERROR: {source} is not a valid directory, file, or could not be read'
        )
    return source


@dataclass
class DataLoader:
    """
    Loads data from files and only the specified columns.

    Args:
        files: filename to read the data from
        columns: list of columns to be read
    """

    files: str
    columns: list[str]
    data: Optional[DataFrame] = None

    @classmethod
    def load(cls, source: str, columns: list[str]) -> 'DataLoader':
        """
        If the data is found in the given path, prepare it for reading
        """
        files = discover_csv_files(source)
        return cls(files=files, columns=columns)

    def translate_columns(self):
        """
        Translate column names from Spanish to English
        """
        column_translation = {"Fecha-I": "sched_date_time",
                              "Vlo-I": "sched_flight_num",
                              "Ori-I": "sched_OG_city_code",
                              "Des-I": "sched_destination_city_code",
                              "Emp-I": "sched_airlinecode",
                              "Fecha-O": "actual_date_time",
                              "Vlo-O": "actual_flight_num",
                              "Ori-O": "actual_OG_city_code",
                              "Des-O": "actual_destination_city_code",
                              "Emp-O": "actual_airline_code",
                              "DIA": "actual_flight_day",
                              "MES": "actual_flight_month",
                              "AÑO": "actual_flight_year",
                              "DIANOM": "dayof_week_actual_flight",
                              "TIPOVUELO": "flight_type",
                              "OPERA": "airline",
                              "SIGLAORI": "OG_city",
                              "SIGLADES": "dest_city"
                              }
        self.data = self.data.rename(columns=column_translation)

    def build_dataframe(self) -> DataFrame:
        """
        Transfer the input CSV data to a DataFrame object
        """
        # This assumes the data is in Spanish
        dtype = {"Fecha-I": object,
                 "Vlo-I": object,
                 "Ori-I": object,
                 "Des-I": object,
                 "Emp-I": object,
                 "Fecha-O": object,
                 "Vlo-O": object,
                 "Ori-O": object,
                 "Des-O": object,
                 "Emp-O": object,
                 "DIA": int,
                 "MES": int,
                 "AÑO": int,
                 "DIANOM": object,
                 "TIPOVUELO": object,
                 "OPERA": object,
                 "SIGLAORI": object,
                 "SIGLADES": object
                 }
        self.data = pd.read_csv(self.files, dtype=dtype)

        self.translate_columns()

        return self.data
