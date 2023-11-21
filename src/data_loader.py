import urllib.request
import os
import pandas as pd

from pathlib import Path
from sklearn.preprocessing import LabelEncoder

import warnings
warnings.filterwarnings('ignore')

class DataLoader:

    """
    This script is used to load and clean the data. It performs the following steps:
    1. Downloads the data if it does not exist in the directory.
    2. Removes duplicate entries in 2019 and all rows with SimStartDate after 2019-01-01 and event_type == 'thunderstorm'.
    3. Applies ordinal encoding to 'poly_ewkt', 'event_type' columns.
    4. Converts date columns to year, month, day, and hour.
    5. Drops the 'point_ewkt' column because it's duplicate information from lat and long.
    """
    @staticmethod
    def load_and_clean_data():
        path = Path()

        # Dictionary of file names and download links
        files = {'./data/outage_data.parquet':'https://storage.googleapis.com/aipi_datasets/outage_data.parquet'}

        # Download each file
        for key,value in files.items():
            filename = path/key
            url = value
            # If the file does not already exist in the directory, download it
            if not os.path.exists(filename):
                urllib.request.urlretrieve(url,filename)

        df = pd.read_parquet(path='./data/outage_data.parquet', engine='pyarrow')

        # Remove duplicate entries in 2019
        # Remove all rows with SimStartDate after 2019-01-01 and event_type == 'thunderstorm'
        df = df.loc[~((df['SimStartDate'] > '2019-01-01') & (df['event_type'] == 'thunderstorm'))]

        # Apply label encoding to 'poly_ewkt', 'point_ewkt', 'event_type' columns
        non_numerical_columns = ['poly_ewkt', 'event_type']
        enconder = LabelEncoder()
        for col in non_numerical_columns:
            df[col] = enconder.fit_transform(df[col])

        # df = DataLoader._convert_date_columns(df)

        df.drop(columns = ['point_ewkt'], inplace = True)

        return df

    # @staticmethod
    # def _convert_date_columns(df):
    #     datetime_features = list(df.select_dtypes(include = "datetime64[ns, UTC]").columns)
    #     for i in datetime_features:
    #         df[i+"_year"] = df[i].dt.year
    #         df[i+"_month"] = df[i].dt.month
    #         df[i+"_day"] = df[i].dt.day
    #         df[i+"_hour"] = df[i].dt.hour
            
    #     df.drop(columns = datetime_features, inplace = True)

    #     return df
