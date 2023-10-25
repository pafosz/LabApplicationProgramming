from bs4 import BeautifulSoup
import requests

def parser(path_for_read: str) -> list:
    
     headers = {
     "Accept": "*/*", 
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
     # path_for_read = 'datasets/url_list.txt'
     with open(path_for_read) as file:
     
           lines = [line.strip() for line in file.readlines()]
           data = []
           count = 0
           for line in lines:
                try:
                    html_text = requests.get(line, headers=headers)
                except:
                    continue
                print(html_text.status_code)
                result = html_text.text

                soup = BeautifulSoup(result, 'lxml')
                try:
                     date = soup.find('button', class_ = 'datepicker-filter_button').text               
                     course = soup.find('td', string = 'USD').find_next().find_next().find_next().text.replace(',', '.')
                     data.append(f'{date}, {course}')                
                except: 
                     data.append(f'{date}, -')                              
                
                count += 1                
                print(f'Загружено {count} дней')
     return data         
 
def upload_csv(path_for_read: str, path_for_upload: str) -> None:
    # path = 'datasets/dataset.csv'
    parser_data = parser(path_for_read)
    with open(path_for_upload, 'a') as file:
         for line in parser_data:
              file.write(f'{line}\n')