import pandas as pd

def filter_by_mean_deviation(data_frame: pd.DataFrame, deviation_value: float) -> pd.DataFrame:
    mean_val = data_frame['data'].mean()
    filtered_df = data_frame[abs(data_frame['data'] - mean_val) >= deviation_value]

    return filtered_df

def filter_by_date(data_frame: pd.DataFrame, start_date: object, end_date: object) -> pd.DataFrame:
    filtered_df = data_frame[(data_frame['date'] >= start_date) & (data_frame['date'] <= end_date)]
    
    return filtered_df

def group_by_month(data_frame: pd.DataFrame) -> pd.DataFrame:
    data_frame['date'] = pd.to_datetime(data_frame['date'])

    monthly_mean = data_frame.set_index('date').resample('M')['data'].mean()
    return monthly_mean