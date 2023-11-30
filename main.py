from modules import loading_links
from modules import parser_data as pd
from modules import add_functions as af
from modules import division_data as dd
from modules import data_iterator as di


# !autopep8 --in-place --aggressive --aggressive uglycodesample.py  

def main():
    # loading_links.writes_list_file('datasets/url_list.txt', 1993)
    # parser_data.upload_csv('datasets/url_list.txt', 'datasets/dataset.csv')   
    #af.replace_date_format('datasets/dataset.csv')
    # dd.division_date_and_data('datasets', 'date_and_data', 'dataset.csv')
    # dd.division_by_year('datasets', 'data_by_year', 'dataset.csv')
    # dd.division_by_week('datasets', 'data_by_week', 'dataset.csv')       

    it = di.DataIterator()
    print(next(it))
    


if __name__ == "__main__":
   main()