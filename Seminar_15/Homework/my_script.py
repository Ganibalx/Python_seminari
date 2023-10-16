import argparse
import logging
import os
from collections import namedtuple


def path_info(path=os.getcwd()):
    format = '{levelname:<5} - {asctime:<20} - {funcName} - {msg}'
    logging.basicConfig(filename='my.log.', style='{', filemode='a', encoding='utf-8', level=logging.NOTSET,
                        format=format)
    logger = logging.getLogger(__name__)
    File = namedtuple('File', ['name', 'flag', 'parent_dir'])
    for dir_path, dir_name, file_name in os.walk(path):
        for file in file_name:
            f = File(file.split('.')[0], *file.split('.')[-1:], os.path.basename(dir_path))
            logger.info(msg=f'Добавлен файл {f}')
        for folder in dir_name:
            f = File(folder, 'dir', os.path.basename(dir_path))
            logger.info(msg=f'Добавлена директория {f}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, help='Введите путь папки')
    args = parser.parse_args()
    path_info(args.path)

