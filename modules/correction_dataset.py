import pandas as pd
import matplotlib.pyplot as plt
def renames(path: str, colname1: str, colname2: str) -> None:
    df = pd.read_csv(path)

    df.rename(columns={df.columns[0]:  colname1}, inplace=True)
    df.rename(columns={df.columns[1]:  colname2}, inplace=True)

    df.to_csv(path, index=False)

def nan_processing(path: str) -> None:
    df = pd.read_csv(path)

    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    
    df.to_csv(path, index=False)

def median_and_mean(path: str, col_name_data: str, col_name_med: str, col_name_mean: str) -> None:
    df = pd.read_csv(path)

    median_val = df[col_name_data].median()
    mean_val = df[col_name_data].mean()
    df[col_name_med] = df[col_name_data] - median_val #'median_deviation'
    df[col_name_mean] = df[col_name_data] - mean_val #'mean_deviation'

    df.to_csv(path, index=False)



