import os


def get_file_info(directory, output_file):
    with open(output_file, 'w', encoding='utf-8') as out_file:
        out_file.write(
            f"{'№':<3} {'Название':<30} {'Описание':<50} {'Количество строк':<20} {'Размер файла в КБ':<20}\n")
        out_file.write("=" * 120 + "\n")

        for idx, filename in enumerate(os.listdir(directory), start=1):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                try:
                    # Получаем количество строк в файле
                    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
                        line_count = sum(1 for line in file)
                except UnicodeDecodeError:
                    # Если возникает ошибка, пробуем другую кодировку
                    with open(file_path, 'r', encoding='latin1', errors='replace') as file:
                        line_count = sum(1 for line in file)

                # Получаем размер файла в КБ
                file_size = os.path.getsize(file_path) / 1024

                out_file.write(f"{idx:<3} {filename:<30} {'':<50} {line_count:<20} {file_size:<20.2f}\n")


# Укажите путь к директории и файл для сохранения результата
directory_path = '/Users/alinakonuhova/PycharmProjects/KorShop/templates/inc'
output_file_path = 'inc.txt'
get_file_info(directory_path, output_file_path)
