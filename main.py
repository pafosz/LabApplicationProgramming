import os
from bs4 import BeautifulSoup
import requests
import re
from re import sub
from decimal import Decimal
import io
from datetime import datetime

url = 'https://www.cbr.ru/currency_base/daily/'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
table_wrapper = soup.find('div', class_ = 'table-wrapper')
table = table_wrapper.find('div', class_ = 'table')
data = table.find('table', class_ = 'data')
tr = data.find_all('tr')[14]
td = tr.find_all('td')[4].text
print(td)
# Доллары появились начиная с 1996г
