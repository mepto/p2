#! /usr/bin/python
# coding: utf-8
import os

import requests


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


# def check_images(user_choice):
#     """
#     Check if user choice for download exists
#     :return: boolean or raise exception
#     """
#     if int(user_choice) == 1:
#         return True
#     elif int(user_choice) == 0:
#         return False
#     else:
#         raise Exception('Invalid choice. Only "Yes (1)" or "No (0)" are '
#                         'valid options.')


def get_image(book):
    """
    Download image file in assets/media folder
    """
    download_folder = get_folder('media')
    filepath, extension = os.path.splitext(book.image)
    image = requests.get(book.image, allow_redirects=True)
    with open(f"{download_folder}/{book.upc}{extension}", 'wb') as file:
        file.write(image.content)
