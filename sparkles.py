import os


def collect_code_files(directory, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(directory):
            # # Пропускаем папки migrations
            # if 'migrations' in root:
            #     continue

            for file in files:
                # Пропускаем __init__.py
                # if file == '__init__.py':
                #     continue

                if file.endswith('.txt'):
                    # if file.endswith('.txt') or file.endswith('.html'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(f'--- Содержимое файла: {file_path} ---\n')
                        outfile.write(infile.read())
                        outfile.write('\n\n')


if __name__ == "__main__":
    project_directory = '/Users/alinakonuhova/PycharmProjects/Lessons '
    output_txt_file = 'combined_output.txt'
    collect_code_files(project_directory, output_txt_file)
