#! /usr/bin/python
# coding: utf-8
import csv

from .models import Book, Categories, Category
from .settings import FIELDNAMES
from .utils import get_user_choice, get_folder, check_images, get_image


def main():
    """
    Create instances of classes
    """
    scrape_type = get_user_choice('Please choose the type of export: (1) by '
                                  'categories, or (2) all_books.')
    images_download = get_user_choice('Would you like to download the books '
                                      'images files? (1) Yes, (0) No')
    download = check_images(images_download)
    categories = Categories(scrape_type).data()
    for category in categories:
        exports_folder = get_folder('exports')
        category_name = category['category']
        filename = f"{exports_folder}/{category_name}.csv"

        with open(filename, 'w', encoding="utf-8-sig", newline='') as csvfile:
            print(f"Creating file {category_name}.csv")
            csv_writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES,
                                        delimiter='|')
            csv_writer.writeheader()
            category_products = Category(category['href']).data()
            for product in category_products:
                book = Book(product)
                csv_writer.writerow(book.data())
                if download:
                    get_image(book)

    print('Export process is done.')
