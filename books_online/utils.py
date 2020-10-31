#! /usr/bin/python
# coding: utf-8
import csv
import os

import requests

from books_online.settings import FIELDNAMES


def get_user_choice(message, choices):
    """
    Loops until user enters proper choice
    :return: user choice (digit)
    """
    user_choice = input(message)
    while not user_choice.isdigit() or int(user_choice) not in choices:
        user_choice = input(f'Incorrect entry "{user_choice}". {message}')

    return int(user_choice)


def get_folder(folder_path):
    """
    Check if assets folder exists and creates it if necessary
    :return: folder path in assets folder
    """
    current_folder = os.path.dirname(os.path.realpath(__file__))
    current_folder = current_folder.replace('\\', '/')

    assets_path = f'{current_folder}/assets'
    if not os.path.exists(assets_path):
        os.mkdir(assets_path)

    folder_path = f'{assets_path}/{folder_path}'
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    return folder_path


def write_files(title, book_list, download):
    exports_folder = get_folder('exports')
    filename = f"{exports_folder}/{title}.csv"
    download_text = 'and downloading images' if download else ''
    with open(filename, 'w', encoding="utf-8-sig", newline='') as csv_file:
        print(f"Creating file {title}.csv {download_text}")
        csv_writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES,
                                    delimiter='|')
        csv_writer.writeheader()
        for book in book_list:
            csv_writer.writerow(book)
            if download:
                get_image(book)


def get_image(book):
    """
    Download image file in assets/media folder
    """
    download_folder = get_folder('media')
    filepath, extension = os.path.splitext(book['image_url'])
    image = requests.get(book['image_url'], allow_redirects=True)
    with open(f"{download_folder}/{book['universal_product_code']}{extension}",
              'wb') as file:
        file.write(image.content)
