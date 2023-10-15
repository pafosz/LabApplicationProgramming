from modules import loading_links
from modules import parser_data


def main():
    loading_links.writes_list_file('datasets/url_list.txt', 2023)
    parser_data.upload_csv('datasets/url_list.txt', 'datasets/dataset.csv')

if __name__ == "__main__":
   main()