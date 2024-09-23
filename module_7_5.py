import os
import time


directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:

        filepath = os.path.join(root, file)

        last_time = os.path.getmtime(filepath)
        formatted_time = time.ctime(last_time)

        filesize = os.path.getsize(filepath)

        parent_dir = os.path.dirname(filepath)

        print(f'Обнаружен файл: {file}')
        print(f'Путь: {filepath}')
        print(f'Размер: {filesize} байт')
        print(f'Время изменения: {formatted_time}')
        print(f'Родительская директория: {parent_dir}\n')

