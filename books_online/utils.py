#! /usr/bin/python
# coding: utf-8
import os


def get_user_choice(message):
    """
    Loops until user enters proper choice
    :return: user choice (digit)
    """
    user_choice = input(message)
    while not user_choice.isdigit():
        user_choice = input(f'Incorrect entry "{user_choice}". {message}')
    return user_choice


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
