"""
Similar files finder entrypoint

"""

import os
import hashlib
from collections import Counter


def get_all_path_file(directory, paths_file):
    """
    Returns all file pathes contains in this directory

    :param directory: directory
    :type directory: str
    :param paths_file: list append file pathes
    :type paths_file: list(str)
    :return: None
    """
    for folder, subfilder, files in os.walk(directory):
        paths_file += (list(map(lambda x: os.path.join(folder, x), files)))


def get_hash_files(fnamelst):
    """
    Returs list with hashes of file pathes

    :param fnamelst: list of file pathes
    :type fnamelst: list(str)
    :return: list(hex) -- List with hashes of file pathes
    """
    return [hashlib.md5(open(fname, 'rb').read()).digest() for fname in fnamelst]


def work(directory):
    """
    Function finds similar files in directory and in all subdirectories. Returns list that containts lists with similar files
    :param directory: directory with files
    :return: list(list(str)) -- list of list of similar_files
    """
    # проверяем, валидна ли директория
    if not os.path.exists(directory):
        print("Directory does not exists")
        return []

    # сгенерируем список путей в листе
    path_files = []
    get_all_path_file(directory, path_files)

    # сгенерируем для всех файлов хэш
    hash_files = get_hash_files(path_files)
    # посчитываем
    counter_hash = Counter(hash_files)

    dict_name_files = dict()

    # пишем в дикт названия файлов с повторяющимся хэшом
    for name_file, hash_file in zip(path_files, hash_files):
        if counter_hash[hash_file] > 1:
            if (hash_file not in dict_name_files):
                dict_name_files[hash_file] = [name_file]
            else:
                dict_name_files[hash_file].append(name_file)

    # возвращаем значения
    return list(dict_name_files.values())
