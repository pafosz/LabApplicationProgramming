import os
from bs4 import BeautifulSoup
import requests
import re
from re import sub
from decimal import Decimal
import io
from datetime import datetime


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
        if year == now_year and month == now_month and day == now_day:
                 break
        day = 1       
        while day <= days_in_month(month, year):   
            
            url = f'https://www.cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To={str(day).zfill(2)}.{str(month).zfill(2)}.{year}'
            url_list.append(url)

            if year == now_year and month == now_month and day > now_day:
                 break
     
            day += 1

with open('url_list.txt', 'a') as file:
     for line in url_list:
        file.write(f'{line}\n')

# html_text = requests.get(url)
# result = html_text.text
# soup = BeautifulSoup(result, 'lxml')

# print(f'{str(day).zfill(2)}.{str(month).zfill(2)}.{year}')             
            
# block_usd = soup.find('table', class_ = 'data').find_all('tr')[14]
# course = block_usd.find_all('td')[4].text


    

# # for i in range('05.01.1996', '12.10.2023'):
# #     url = f'https://www.cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To={i}'


# url = range('https://www.cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To={day}.{month}.{year}')
# html_text = requests.get(url).text
# soup = BeautifulSoup(html_text, 'lxml')



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



# Доллары появились начиная с 1996г
