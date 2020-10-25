#! /usr/bin/python
# coding: utf-8
import csv

from .models import Book, Categories, Category
from .settings import FIELDNAMES
from .utils import get_user_choice, get_folder


def main():
    """
    Create instances of classes
    """
    scrape_type = get_user_choice('Please choose the type of export: (1) by '
                                  'categories, or (2) all_books.')
    categories = Categories(scrape_type).data()
    for category in categories:
        folder = get_folder('exports')
        category_name = category['category']
        filename = f"{folder}/{category_name}.csv"

        with open(filename, 'w', encoding="utf-8-sig", newline='') as csvfile:
            print(f"Creating file {category_name}.csv")
            csv_writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES,
                                        delimiter='|')
            csv_writer.writeheader()
            category_products = Category(category['href']).data()
            for product in category_products:
                book = Book(product)
                csv_writer.writerow(book.data())

    print('Export process is done.')
