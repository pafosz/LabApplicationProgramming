import os
import pandas as pd
from datetime import timedelta

def division_date_and_data(input_data: str, output_data: str) -> None:
    '''
    Divides the original csv file into X.csv (dates) and Y.csv (data) files.
            Parameters:                    
                    input_data (str): source file
                    output_data (str): the folder for recording
            Return value:
                    None
    '''
    output_data = output_data + "/date_and_data"
    path = os.getcwd()
    df = pd.read_csv(input_data)

    df_x = df['Date']
    df_y = df.drop(columns=['Date'])
    os.chdir(output_data)
    df_x.to_csv('X.csv', index=False, encoding="utf-8", date_format='%Y%m%d')
    df_y.to_csv('Y.csv', index=False, encoding="utf-8")
    os.chdir(path)
    


def division_by_year(input_data: str, output_data: str) -> None: 
    '''
    Devides the original csv file into files corresponding to the years.
            Parameters:
                    input_data (str): source file
                    output_data (str): the folder for recording
            Return value:
                    None
    '''   
    output_data = output_data + "/data_by_year"
    path = os.getcwd()    

    df = pd.read_csv(input_data)
    os.chdir(output_data)

    df['Date'] = pd.to_datetime(df['Date'])    
    group_by_year = df.groupby(df['Date'].dt.year)   

    for group in group_by_year:        
        start_date = group[1]['Date'].min().strftime('%Y%m%d')
        end_date = group[1]['Date'].max().strftime('%Y%m%d')

        group[1].to_csv(f'{start_date}_{end_date}.csv', index=False, encoding="utf-8")

    os.chdir(path)

def division_by_week(input_data: str, output_data: str) -> None: 
    '''
    Devides the original csv file into files corresponding to weeks.
            Parameters:
                    input_data (str): source file
                    output_data (str): the folder for recording
            Return value:
                    None
    '''    
    output_data = output_data + "/data_by_week"
    path = os.getcwd()    

    df = pd.read_csv(input_data)
    os.chdir(output_data)

    df['Date'] = pd.to_datetime(df['Date'])

    min_date = df['Date'].min()
    max_date = df['Date'].max()

    start_week = min_date - timedelta(days=min_date.weekday())
    end_week = start_week + timedelta(days=6)

    while start_week <= max_date:
        week_data = df[(df['Date'] >= start_week) & (df['Date'] <= end_week)]

        start_date = week_data['Date'].min().strftime('%Y%m%d')
        end_date = week_data['Date'].max().strftime('%Y%m%d')

        week_data.to_csv(f'{start_date}_{end_date}.csv', index=False, encoding="utf-8")

        start_week += timedelta(days=7)
        end_week += timedelta(days=7)

    os.chdir(path)
     