import datetime
import os

from add_functions import read_data

def search(date: datetime, path: str) -> list | None:
    for day in read_data(path):
        if day[0] == str(date):
            return day[1:]
        
def search_by_year(date: datetime) -> list | None:
    dir = 'datasets/data_by_year'
    for filename in os.listdir(dir):
        if (int(filename[0:4]) == date.year):
            data = read_data(f"{dir}/{filename}") 
            for day in data:
                if(day[0]==str(date)):
                    return day[1:]
                
def search_by_week(date: datetime) -> list | None:
    dir = 'datasets/data_by_week'
    for filename in os.listdir(dir):
        left_date = datetime.datetime.strptime(filename[:8], '%Y%m%d').date()
        right_date = datetime.datetime.strptime(filename[9:17], '%Y%m%d').date()
        if(left_date <= date <= right_date):
            for day in read_data(f"{dir}/{left_date}_{right_date}"):
                if(day[0] == str(date)):
                    return day[1:]      
                
def search_by_xy(date: datetime) -> list | None:
    data_by_x = read_data('datasets/date_and_data/X.csv')
    for row, value in enumerate(data_by_x):
        row_date = "-".join(value)
        if row_date == str(date):
            data_by_y = read_data('datasets/date_and_data/Y.csv')
            return data_by_y[row]

def next() -> tuple:
    index = 0
    data = read_data(r"C:\Users\Admin\Desktop\University\2 cours\3 semester\PP\LabAppProg\LabApplicationProgramming\datasets\dataset.csv")
    if index < len(data) - 1:
        index += 1
        return tuple(data[index])
    

    






