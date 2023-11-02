import re

def replace_date_format(filename: str):
    # Открываем файл на чтение
    with open(filename, 'r') as file:
        content = file.read()

    # Используем регулярное выражение для поиска дат в формате "dd.mm.yyyy"
    # и заменяем их на формат "yyyy-mm-dd"
    updated_content = re.sub(r'(\d{2})\.(\d{2})\.(\d{4})', r'\3-\2-\1', content)

    # Открываем файл на запись и записываем обновленное содержимое
    with open(filename, 'w') as file:
        file.write(updated_content)