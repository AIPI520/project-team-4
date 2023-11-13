import urllib.request
from pathlib import Path
import os

def load_and_clean_data():
    path = Path()

    # Dictionary of file names and download links
    files = {'outage_data.parquet':'https://storage.googleapis.com/aipi_datasets/outage_data.parquet'}

    # Download each file
    for key,value in files.items():
        filename = path/key
        url = value
        # If the file does not already exist in the directory, download it
        if not os.path.exists(filename):
            urllib.request.urlretrieve(url,filename)

    df = pd.read_parquet(path='..//outage_data.parquet', engine='pyarrow')

    # Remove duplicate entries in 2019
    # Remove all rows with SimStartDate after 2019-01-01 and event_type == 'thunderstorm'
    df = df.loc[~((df['SimStartDate'] > '2019-01-01') & (df['event_type'] == 'thunderstorm'))]

    # Apply ordinal encoding to 'poly_ewkt', 'point_ewkt', 'event_type' columns
    non_numerical_columns = ['poly_ewkt', 'event_type']
    enconder = OrdinalEncoder()
    enconder.fit(df[non_numerical_columns])
    df[non_numerical_columns] = enconder.transform(df[non_numerical_columns])

    df = convert_date_columns(df)

    return df

def convert_date_columns(df):
    # Convert datetime columns to separate columns for year, month, day, hour, minute, second
    df['SimStartYear'] = df['SimStartDate'].dt.year
    df['SimStartMonth'] = df['SimStartDate'].dt.month
    df['SimStartDay'] = df['SimStartDate'].dt.day
    df['SimStartHour'] = df['SimStartDate'].dt.hour
    df['outage_start_year'] = df['outage_start_time'].dt.year
    df['outage_start_month'] = df['outage_start_time'].dt.month
    df['outage_start_day'] = df['outage_start_time'].dt.day
    df['outage_start_hour'] = df['outage_start_time'].dt.hour
    df['outage_end_year'] = df['outage_end_time'].dt.year
    df['outage_end_month'] = df['outage_end_time'].dt.month
    df['outage_end_day'] = df['outage_end_time'].dt.day
    df['outage_end_hour'] = df['outage_end_time'].dt.hour
    df['weather_start_year'] = df['weather_start_time'].dt.year
    df['weather_start_month'] = df['weather_start_time'].dt.month
    df['weather_start_day'] = df['weather_start_time'].dt.day
    df['weather_start_hour'] = df['weather_start_time'].dt.hour
    df['weather_end_year'] = df['weather_end_time'].dt.year
    df['weather_end_month'] = df['weather_end_time'].dt.month
    df['weather_end_day'] = df['weather_end_time'].dt.day
    df['weather_end_hour'] = df['weather_end_time'].dt.hour
    return df
