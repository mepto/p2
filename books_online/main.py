#! /usr/bin/python
# coding: utf-8
import csv
from datetime import datetime

from .models.all_categories import AllCategories
from .settings import PATIENCE_MESSAGE
from .utils import get_user_choice


def main():
    """
    Loop over categories to write books data in csv files, optionally
    download book cover image
    """
    scrape_type = get_user_choice('Please choose the type of export: (1) by '
                                  'categories, or (2) all_books.', [1, 2])
    images_download = get_user_choice('Would you like to download the books '
                                      'images files? (1) Yes, (0) No', [0, 1])
    print(PATIENCE_MESSAGE)
    time_start = datetime.now(tz=None)
    AllCategories(scrape_type).get_books(images_download)
    time_stop = datetime.now(tz=None)
    print(f'Export process finished in {time_stop - time_start}.')
