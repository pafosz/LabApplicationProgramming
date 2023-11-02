import csv
import os
from modules import add_functions as af

def division_date_and_data(directory_path: str, new_dir: str, file_path: str) -> None:

    path = os.getcwd() 
    os.chdir(directory_path)    
    
    data = af.read_data('dataset.csv')
   
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir) 
    os.chdir(new_dir)

    with open('X.csv', 'w', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(i[0].split('-') for i in data)
    
    with open('Y.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(i[1:] for i in data)

    os.chdir(path)

def division_by_year(directory_path: str, new_dir: str, file_path: str) -> None:
    data = af.read_data(file_path)
    path = os.getcwd()
    os.chdir(directory_path)
    year_list = []
    for year in data:
        year_list.append(int(year[0].split("-")[0]))
    year_list = sorted(list(set(year_list)))
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)
    os.chdir(new_dir)
    for year in year_list:
        data_year = []
        for day in data:
            if year == int(day[0].split("-")[0]):
                data_year.append(day)
        a = int("".join(data_year[0][0].split("-")))
        b = int("".join(data_year[len(data_year) - 1][0].split("-")))
        with open(f'{a}_{b}.csv', 'w', encoding="utf-8", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data_year)
    os.chdir(path)     
                       

# def division_by_week(directory_path: str, new_dir: str, file_path: str) -> None:
#     data = af.read_data(file_path)
#     path = os.getcwd()
#     os.chdir(directory_path)
