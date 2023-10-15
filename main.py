from modules import loading_links
from modules import parser_data


def main():
    loading_links.writes_list_file('datasest/url_list.txt', 2022)
    parser_data.upload_csv('datasest/url_list.txt', 'datasets/datasetcsv')

if __name__ == "__main__":
   main()