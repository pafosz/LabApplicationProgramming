import pandas as pd
import matplotlib.pyplot as plt
def renames(path: str, colname1: str, colname2: str) -> None:
    '''
    Renames the first two headers.
            Parameters:                    
                    path (str): the path to the source data
                    colname1 (str): name for the first column
                    colname2 (str): name for the second column
            Return value:
                    None
    '''
    df = pd.read_csv(path)

    df.rename(columns={df.columns[0]:  colname1}, inplace=True)
    df.rename(columns={df.columns[1]:  colname2}, inplace=True)

    df.to_csv(path, index=False)

def nan_processing(path: str) -> None:
    '''
    Processes all elements with nan values.
            Parameters:                    
                    path (str): the path to the source data                    
            Return value:
                    None
    '''
    df = pd.read_csv(path)

    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    
    df.to_csv(path, index=False)

def median_and_mean(path: str, col_name_data: str, col_name_med: str, col_name_mean: str) -> None:
    '''
    Сreates new columns with data on deviations from the median and the
      average value of the exchange rate.
            Parameters:                    
                    path (str): the path to the source data
                    col_name_data (str): name of the data column
                    col_name_med  (str): the name of the new column with the deviation value from the median
                    col_name_mean (str): the name of the new column with the deviation value from the mean
            Return value:
                    None
    '''
    df = pd.read_csv(path)

    median_val = df[col_name_data].median()
    mean_val = df[col_name_data].mean()
    df[col_name_med] = df[col_name_data] - median_val #'median_deviation'
    df[col_name_mean] = df[col_name_data] - mean_val #'mean_deviation'

    df.to_csv(path, index=False)



