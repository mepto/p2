#! /usr/bin/python
# coding: utf-8
import csv

from .models.all_categories import AllCategories
from .models.book import Book
from .models.category import Category
from .settings import FIELDNAMES, PATIENCE_MESSAGE
from .utils import get_user_choice, get_folder, get_image


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
    categories = AllCategories(scrape_type).get_books_list()
    for category in categories:
        exports_folder = get_folder('exports')
        filename = f"{exports_folder}/{category}.csv"
        # Write csv file(s)
        with open(filename, 'w', encoding="utf-8-sig", newline='') as csv_file:
            print(f"Creating file {category}.csv")
            csv_writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES,
                                        delimiter='|')
            csv_writer.writeheader()
            books = categories[category]
            for book in books:
                csv_writer.writerow(book)
                # Download images
                if images_download == 1:
                    get_image(book)

    print('Export process is done.')
