# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.
import os
import argparse
from collections import namedtuple
import logging

'''
Я не понял, что в задании подразумевается под флагом каталога
'''

logging.basicConfig(filename='file_info.txt', filemode='w', encoding='utf-8',
                    format='{levelname} - {asctime} в строке {lineno} '
                           'функция "{funcName}()" : {msg}', style='{', level=logging.INFO)

file_path = 'C:/pythonHomeWork/my_files'


def file_info(file_path):
    logging.info('Передали в функцию путь до директории')
    my_file_info = []
    MyFile = namedtuple('MyFile', ['name', 'extension', 'parent'])
    os.chdir(file_path)
    list_files = []
    for dir_path, dir_name, file_name in os.walk(file_path):
        list_files.append(file_name)
        list_files.append(dir_name)
    logging.info('Обошли файлы в директории')
    for list_el in list_files:
        for el in list_el:
            if len(el) > 0:
                el = el.split('.')
                if el[-1] not in ['txt', 'exe', 'jpg', 'JPG', 'MP3', 'mp3', 'png', 'PNG', 'AVI', 'avi', 'mp4']:
                    my_file_info.append(
                        MyFile(el[0], 'Каталог, либо неизвестный формат файла', file_path.split('/')[-1]))
                else:
                    my_file_info.append(MyFile(el[0], el[-1], file_path.split('/')[-1]))
    logging.info(f'Собрали информацию в именованный список и записали в текстовый документ')
    for el in my_file_info:
        with open('C:/pythonHomeWork/file_info.txt', 'a', encoding='utf-8') as f:
            f.write(f'Имя файла: {el[0]}, Расширение файла: {el[1]}, Корневая папка: {el[2]}\n')
    return my_file_info


parser = argparse.ArgumentParser(description="Принимаем путь до директории")
parser.add_argument('-file_path', type=str, default='C:/pythonHomeWork/my_files')
args = parser.parse_args()
print(file_info(f'{args.file_path}'))
