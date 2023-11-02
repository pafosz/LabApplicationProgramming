import csv
import os

def division_date_and_data(directory_path: str, new_dir_path: str, file_path: str):

    path = os.getcwd() 
    os.chdir(directory_path)    
    
    data = []
    with open(file_path, 'r', encoding="utf-8") as file:
        for line in csv.reader(file):
            data.append(line)
    if not os.path.isdir(new_dir_path):
        os.mkdir(new_dir_path) 
    os.chdir(new_dir_path)

    with open('X.csv', 'w', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(i[0].split('-') for i in data)
    
    with open('Y.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(i[1:] for i in data)

    os.chdir(path)




           

