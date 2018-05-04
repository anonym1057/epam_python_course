"""
Similar files finder entrypoint

"""

import os
import hashlib
from collections import Counter


def get_all_path_file(directory):
    """
    Returns all file pathes contains in this directory

    :param directory: directory
    :type directory: str
    :return: list -- name file with path
    """
    paths_file=[]
    for folder, subfilder, files in os.walk(directory):
        paths_file += (list(map(lambda x: os.path.join(folder, x), files)))
    return paths_file


def get_hash_files(fnamelst):
    """
    Returs list with hashes of file pathes

    :param fnamelst: list of file pathes
    :type fnamelst: list(str)
    :return: list(hex) -- List with hashes of file pathes
    """

    hash_list=[]
    for fname in fnamelst:
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        hash_list.append(hash_md5.hexdigest())
    return hash_list
    #return [hashlib.md5(open(fname, 'rb').read()).digest() for fname in fnamelst]


def work(directory):
    """
    Function finds similar files in directory and in all subdirectories. Returns list that containts lists with similar files
    :param directory: directory with files
    :return: list(list(str)) -- list of list of similar_files
    """
    # проверяем, валидна ли директория
    if not os.path.exists(str(directory)):
        print(f"Directory {directory} does not exists")
        return []

    # сгенерируем список путей в листе
    path_files = get_all_path_file(directory)

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
