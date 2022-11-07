import os

main_sort_directory = 'D:\\python_lesson_school\\file_sort\\all_files'  # Исходная папка с различными файлами
extensions = {'pictures': ['png', 'jpg'], 'music': ['mp3', 'flac'], 'text': ['pdf', 'txt', 'doc']}
# Ключ - название папки, значение - расширение отсортированных файлов в папке


# Функция проверяет создана ли такая папка, если нет, создает
def create_folders_from_list(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')


# Функция создает папки из списка
def get_subfolder_path(folder_path):
    subfolder_path = [f.path for f in os.scandir(folder_path) if f.is_dir()]
    return subfolder_path


# Список всех путей файлов
def get_file_path(folder_path) -> list:
    file_path = [f.path for f in os.scandir(folder_path) if not f.is_dir()]
    return file_path


# Функция сортирующая файлы по папкам
def sort_files(folder_path, dict_=extensions):
    file_path = get_file_path(folder_path)
    ext_list = list(dict_.items())
    for file_path in file_path:
        extensions = file_path.split('.')[-1]
        file_name = file_path.split('\\')[-1]

        for dict_key_int in range(len(ext_list)):
            if extensions in ext_list[dict_key_int][1]:
                try:
                    print(f'Перемещение {file_name} в папку {ext_list[dict_key_int][0]}')
                    os.rename(file_path, f'{main_sort_directory}\\{ext_list[dict_key_int][0]}\\{file_name}')
                except FileExistsError:
                    print(f'В папке назначения уже есть этот файл')


create_folders_from_list(main_sort_directory, extensions)
sort_files(main_sort_directory)
