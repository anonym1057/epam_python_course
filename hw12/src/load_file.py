import argparse
import os
import requests
import errno
import functools
import time
from io import BytesIO
from PIL import Image

"""
1. распарсить аргументы
arguments format
"файл__со_списком_юрл 
--директория_для_сохранения 
--количество_потоков 
--размер_изобвражения "

"""


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
    :return:
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


def load_file_from_url_and_save(url_file, save_number, save_path,size_thumbnail, list_info):
    format_img = 'jpeg'

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
                img.save(os.path.join(save_path, name_file),format='jpeg')
            except Exception as e:
                info.sucsess = False
                info.exception = str(e)
            else:
                info.sucsess = True
                info.name_file = name_file
                info.save_path = save_path
                info.size = img.size
    # img = Image.open(BytesIO(resp.content))

    # img.save(os.path.join(save_path, '%05d' % (save_number) + '.' + format_img))
    info.end_processing()
    list_info.append(info)


class Load_info:
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
        #print('------------------------------------------')
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
        print("Count loads file: ", len(list(filter(lambda x: x.sucsess, list_info))))
        print("Load byte: ", functools.reduce(lambda x, y: x + y.load_bytes, list_info, 0), 'bytes')
        print("Load fail: ", len(list(filter(lambda x: not x.sucsess, list_info))))
        print("Time: ", '%.2f'%(time),'sec')


if __name__ == '__main__':
    print("Hello")
    parser = argparse.ArgumentParser(description='Load files')
    parser.add_argument('directory', type=str, help='')
    parser.add_argument('--dir', default='.', type=str, help='')
    parser.add_argument('--threads', default=1, type=int, help='')
    parser.add_argument('--size', default='100x100', type=str, help='')

    args = parser.parse_args()

    # создаем путь, если его не существуе
    create_path(args.dir)

    # скачиваем из файлв юрл
    urls = get_urls_from_file(args.directory)
    size=tuple(map(lambda x: int(x),args.size.split('x')))

    list_info = []

    # скачиваем  и сохраняем в заданную директорию с заданным именем

    time1=time.time()
    for i, url in enumerate(urls):
        load_file_from_url_and_save(url, i, args.dir,size, list_info)

    #выводи статистику
    time2=time.time()
    Load_info.print_statistic(list_info,time2-time1)