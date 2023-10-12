import os
from bs4 import BeautifulSoup
import bs4
import requests
import re
from re import sub
from decimal import Decimal
import io
from datetime import datetime 
import random
from time import sleep
import csv

now_year = datetime.now().year 
now_month = datetime.now().month
now_day = datetime.now().day  

def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):

    if month in [4, 6, 9, 11]:        
        return 30
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2 and is_leap_year(year) == True:
            return 29
    elif month == 2 and is_leap_year(year) == False:
            return 28
    else:
        return None

url_list = []    

for year in range(1996, now_year+1):   
    
    for month in range(1, 13):
       
        if year == now_year and month > now_month and day >= now_day:
                 break
       
        day = 1  

        while day <= days_in_month(month, year):   
            
            if year == 1996 and month == 1 and day <= 4:
             day += 1   
             continue 

            url = f'https://www.cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To={str(day).zfill(2)}.{str(month).zfill(2)}.{year}'
            url_list.append(url)

            if year == now_year and month == now_month and day >= now_day:
                 break
     
            day += 1

with open('datasets/url_list.txt', 'a') as file:
     for line in url_list:
        file.write(f'{line}\n') 

headers = {
     "Accept": "*/*", 
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

with open('datasets/url_list.txt') as file:
     
     lines = [line.strip() for line in file.readlines()]
     data = []
     count = 0
     for line in lines:
          html_text = requests.get(line, headers=headers)
          result = html_text.text
          print(count)
          soup = BeautifulSoup(result, 'lxml')
          
          date = soup.find('button', class_ = 'datepicker-filter_button').text
          try:
            course = soup.find('td', string = 'USD').find_next().find_next().find_next().text
          except:
               print(None)
               pass
          data.append(f'{date}, {course}')
          sleep(random.randrange(1, 3))
          count += 1
          if count % 100 == 0:
               print(f'Загружено {count} дней')         
 

with open('datasets/dataset.csv', 'a') as file:
     for line in data:
          file.write(f'{line}\n')


# url = 'https://www.cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To=02.07.2004'
# html_text = requests.get(url, headers=headers)
# result = html_text.text
# soup = BeautifulSoup(result, 'lxml')

# date = soup.find('button', class_ = 'datepicker-filter_button').text
# find_usd = soup.find('td', string = 'USD').text
# course = soup.find('td', string = 'USD').find_next().find_next().find_next().text

# print(f'Страна: {find_usd}, курс: {course}, на {date}') 
     
          
     
    

# course = block_usd.find_all('td')[4].text
# print(course)


# html_text = requests.get(url)
# result = html_text.text
# 
# print(f'{str(day).zfill(2)}.{str(month).zfill(2)}.{year}')             
            

# date = soup.find('button', class_ = 'datepicker-filter_button').text
# #print(date)
# days = range(1, 31)
# for day in days:
#     print(day+1)
# now_year =  datetime.now().year
# manth = datetime.now().month
# years = range(1996, now_year)
# for year in years:
#     print(year+1)
