from datetime import datetime 

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

  
def writes_links_list(since_year: int) -> list:
     url_list = []  
     now_year = datetime.now().year 
     now_month = datetime.now().month
     now_day = datetime.now().day 
     
     for year in range(since_year, now_year+1):     
         for month in range(1, 13):          
              if year == now_year and month > now_month and day >= now_day:
                  break
          
              day = 1  

              while day <= days_in_month(month, year):   
               
               if year == since_year and month == 1 and day <= 4:
                   day += 1   
                   continue 

               url = f'https://www.cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To={str(day).zfill(2)}.{str(month).zfill(2)}.{year}'
               url_list.append(url)

               if year == now_year and month == now_month and day >= now_day:
                   break
          
               day += 1
               return url_list

def writes_list_file(path_for_upload: str, since_year: int) -> None:
    url_list = writes_links_list(since_year)
    # path = 'datasets/url_list.txt'
    with open(path_for_upload, 'a') as file:   
         for line in url_list:
             file.write(f'{line}\n') 