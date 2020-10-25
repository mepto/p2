#! /usr/bin/python
# coding: utf-8


def get_user_choice(message):
    """
    Loops until user enters proper choice
    :return: user choice (digit)
    """
    user_choice = input(message)
    while not user_choice.isdigit():
        user_choice = input(f'Incorrect entry "{user_choice}". {message}')
    return user_choice
