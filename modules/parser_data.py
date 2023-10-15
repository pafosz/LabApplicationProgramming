from bs4 import BeautifulSoup
import requests

def parser(path_for_read: str, ) -> list:
    
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
                html_text = requests.get(line, headers=headers)
                result = html_text.text
          
                soup = BeautifulSoup(result, 'lxml')
                try:
                     date = soup.find('button', class_ = 'datepicker-filter_button').text               
                     course = soup.find('td', string = 'USD').find_next().find_next().find_next().text.replace(',', '.')
                except:               
                     pass
                data.append(f'{date}, {course}')
                count += 1
                if count % 100 == 0:
                     print(f'Загружено {count} дней')
     return data         
 
def upload_csv(parser_data: list, path_for_read: str, path_for_upload: str) -> None:
    # path = 'datasets/dataset.csv'
    parser_data = parser(path_for_read)
    with open(path_for_upload, 'a') as file:
         for line in parser_data:
              file.write(f'{line}\n')