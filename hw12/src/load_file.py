"""
Creates thumbnail from pictures at url adress. Url addresses are stored in a text file.
"""

import argparse
import os
import requests
import errno
import functools
import time
from multiprocessing.pool import ThreadPool
from multiprocessing import Lock
from io import BytesIO
from PIL import Image



def get_urls_from_file(name_file):
    """
    Returns list of url's file that needs load
    Structure file:
    "
    url_l
    url_2
    url_3
    ...
    "

    :param name_file: file with urls
    :type name_file: str
    :return: list(str) -- list with url's file
    """
    # проверяем, существуем ли файл
    if not os.path.isfile(str(name_file)):
        raise ValueError(f"File {name_file} does not exists.")

    # открываем файл и построчно записываем  в лист
    urls = []
    with open(name_file, 'r') as fin:
        urls = list(fin)
    # возвращаем
    return urls


def create_path(path):
    """
    Create path if path does not exist

    :param path: path file
    :type path: str
    :return: None
    """
    if not os.path.exists(path):
        split_path = os.path.split(path)
        if split_path[0] != '':
            create_path(split_path[0])

        try:
            os.makedirs(path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise


def create_thumbnail(url_file_enum, save_path, size_thumbnail):
    """
    Creates thumbnail from images.
    Pictures are downloaded from the url address and saved with the name of the sequence number.

    :param url_file_enum: numbered url list
    :type url_file_enum: tuple(int,str)
    :param save_path: image save path
    :type save_path: std
    :param size_thumbnail:size thumbnail
    :type size_thumbnail: tuple(int,int)
    :return: class Load_info
    """
    format_img = 'jpeg'
    save_number = url_file_enum[0]
    url_file = url_file_enum[1]

    info = Load_info(url_file, save_number)

    try:
        resp = requests.get(url_file, stream=True)

        info.load_bytes = resp.content.__sizeof__()
    except Exception as e:
        info.sucsess = False
        info.exception = str(e)
    else:
        try:
            img = Image.open(BytesIO(resp.content))
        except Exception as e:
            info.sucsess = False
            info.exception = str(e)
        else:
            try:
                img.thumbnail(size_thumbnail)

                img = img.convert('RGB')

                name_file = '%05d' % (save_number) + '.' + format_img
                img.save(os.path.join(save_path, name_file), format='jpeg')
            except Exception as e:
                info.sucsess = False
                info.exception = str(e)
            else:
                info.sucsess = True
                info.name_file = name_file
                info.save_path = save_path
                info.size = img.size

    lock = Lock()
    lock.acquire()
    info.end_processing()
    lock.release()
    return info


class Load_info:
    """
    Saves information about the consequences of downloading.
    In case of success=True :url, load_bytes, save_path ,name_file,size
    In case of failure(success=False): url, load_bytes,exception
    """

    def __init__(self, url, number):
        self.url = url
        self.enum = number

        # обязательные
        self.sucsess = True
        self.load_bytes = 0
        # в случае успеха
        self.save_path = ''
        self.name_file = ''
        self.size = (0, 0)
        # в случае не успеха
        self.exception = ''

    def end_processing(self):
        """
        Output information after download

        """
        print(self.enum)
        print(self.url)
        print('Result: ', end='')
        if (self.sucsess):
            print("Succses")
        else:
            print("Fail")
        print("\n\n")

    @staticmethod
    def print_statistic(list_info, time):
        """
        Display statistics after all downloads.

        :param list_info: Load info classes to include in statistics
        :type list_info: list(Load_info)
        :param time: lead time
        :type time: float
        :return:
        """
        print("Count loads file: ", len(list(filter(lambda x: x.sucsess, list_info))))
        print("Load byte: ", functools.reduce(lambda x, y: x + y.load_bytes, list_info, 0), 'bytes')
        print("Load fail: ", len(list(filter(lambda x: not x.sucsess, list_info))))
        print("Time: ", '%.2f' % (time), 'sec')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Load files')
    parser.add_argument('directory', type=str, help='')
    parser.add_argument('--dir', default='.', type=str, help='')
    parser.add_argument('--threads', default=1, type=int, help='')
    parser.add_argument('--size', default='100x100', type=str, help='')

    args = parser.parse_args()
    # парсим размер
    size = tuple(map(lambda x: int(x), args.size.split('x')))

    # создаем путь, если его не существует
    create_path(args.dir)

    # скачиваем юрл из файлв
    images = get_urls_from_file(args.directory)

    # сокращаем аргументы
    part_create_thumbnail = functools.partial(create_thumbnail, save_path=args.dir, size_thumbnail=size)

    # создаем пул
    pool = ThreadPool(args.threads)

    # запускам параллельное вычисление
    time1 = time.time()
    result = list(pool.map(part_create_thumbnail, enumerate(images)))
    time2 = time.time()

    # закрываем потоки
    pool.close()
    pool.join()

    # выводи статистику
    Load_info.print_statistic(result, time2 - time1)
