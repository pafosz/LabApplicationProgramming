import pandas as pd

def filter_by_mean_deviation(data_frame: pd.DataFrame, deviation_value: float) -> pd.DataFrame:
    '''
    Filters by deviation.
            Parameters:                    
                    data_frame (pd.DataFrame): filtering data
                    deviation_value (float): the value of the deviation from the average value of the course
            Return value:
                    pd.DataFrame
    '''
    mean_val = data_frame['data'].mean()
    filtered_df = data_frame[abs(data_frame['data'] - mean_val) >= deviation_value]

    return filtered_df

def filter_by_date(data_frame: pd.DataFrame, start_date: str, end_date: str) -> pd.DataFrame:
    '''
    Filters data by date.
            Parameters:                    
                    data_frame (pd.DataFrame): filtering data
                    start_date (str): the starting date for filtering
                    end_date (str): the end date for filtering
            Return value:
                    pd.DataFrame
    '''
    filtered_df = data_frame[(data_frame['date'] >= start_date) & (data_frame['date'] <= end_date)]
    
    return filtered_df

def group_by_month(data_frame: pd.DataFrame) -> pd.DataFrame:
    '''
    Groups data by month and finds the average value for this period.
            Parameters:                    
                    data_frame (pd.DataFrame): filtering data                    
            Return value:
                    pd.DataFrame
    '''
    data_frame['date'] = pd.to_datetime(data_frame['date'])

    monthly_mean = data_frame.set_index('date').resample('M')['data'].mean()
    return monthly_mean