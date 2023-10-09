import os
from bs4 import BeautifulSoup
import requests
import re
from re import sub
from decimal import Decimal
import io
from datetime import datetime

url = range('https://www.cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To={day}.{month}.{year}')
# html_text = requests.get(url).text
# soup = BeautifulSoup(html_text, 'lxml')

# block_usd = soup.find('table', class_ = 'data').find_all('tr')[14]
# course = block_usd.find_all('td')[4].text

# date = soup.find('button', class_ = 'datepicker-filter_button').text
# #print(date)
days = range(1, 31)
for day in days:
    print(day+1)
now_year =  datetime.now().year
manth = datetime.now().month
years = range(1996, now_year)
for year in years:
    print(year+1)

     


# Доллары появились начиная с 1996г
