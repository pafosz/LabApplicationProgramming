import re
import csv
import datetime

def replace_date_format(filename: str):
    with open(filename, 'r') as file:
        content = file.read()
   
    updated_content = re.sub(r'(\d{2})\.(\d{2})\.(\d{4})', r'\3-\2-\1', content)

    with open(filename, 'w') as file:
        file.write(updated_content)

def read_data(file_path: str) -> list:
    data = []
    with open(file_path, 'r', encoding="utf-8") as file:
        for line in csv.reader(file):
            data.append(line)
    return data    

def growth(today: str, next_day: str) -> int:   
    current_day = datetime.datetime.strptime(today, '%Y-%m-%d').date()
    following_day = datetime.datetime.strptime(next_day, '%Y-%m-%d').date()
    return (following_day - current_day).days