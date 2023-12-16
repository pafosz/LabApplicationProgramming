import pandas as pd
import matplotlib.pyplot as plt

def plot_graph_all_period(data_frame: pd.DataFrame) -> None:
    '''
    Plots the course change for all time.
            Parameters:                    
                    data_frame (pd.DataFrame): filtering data                   
            Return value:
                    None
    '''
    data_frame['date'] = pd.to_datetime(data_frame['date'])

    plt.figure(figsize=(10, 6))
    plt.plot(data_frame['date'], data_frame['data'])
    plt.title('Изменение курса доллара')
    plt.xlabel('Дата')
    plt.ylabel('Курс')
    plt.show()

def plot_graph_by_month(data_frame: pd.DataFrame, month: str) -> None:
    '''
    Plots a graph with monthly values, median and mean.
            Parameters:                    
                    data_frame (pd.DataFrame): filtering data  
                    month (str): a month for filtering                 
            Return value:
                    None
    '''
    data_frame['date'] = pd.to_datetime(data_frame['date'])
    data_frame['month'] = data_frame['date'].dt.month

    filtered_df = data_frame[data_frame['month'] == month]
    plt.figure(figsize=(10,6))
    plt.plot(filtered_df['date'], filtered_df['data'])
    plt.axhline(y=filtered_df['data'].median(), color='r', linestyle='--', label='Медиана')
    plt.axhline(y=filtered_df['data'].mean(), color='g', linestyle='--', label='Среднее значение')

    plt.title('Изменение курса доллара за месяц')
    plt.xlabel('Дата')
    plt.ylabel('Курс')
    plt.legend()
    plt.show()