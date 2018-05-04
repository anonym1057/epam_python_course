import os
import hashlib
from collections import Counter


def get_all_path_file(directory, paths_file):
    for folder, subfilder, files in os.walk(directory):
        paths_file += (list(map(lambda x: os.path.join(folder, x), files)))


def get_hash_files(fnamelst):
    return [hashlib.md5(open(fname, 'rb').read()).digest() for fname in fnamelst]


def work(directory):
    # проверяем, валидна ли директория
    if not os.path.exists(directory):
        raise ValueError("Directory is not exist")

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
