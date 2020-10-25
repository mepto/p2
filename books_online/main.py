#! /usr/bin/python
# coding: utf-8

from .models import Book, Categories, Category
from .utils import get_user_choice


def main():
    """
    Create instances of classes
    """
    scrape_type = get_user_choice('Please choose the type of export: (1) by '
                                  'categories, or (2) all_books.')
    categories = Categories(scrape_type).data()
    for category in categories:
        category_products = Category(category['href']).data()
        for product in category_products:
            book = Book(product)
            print(book.data())
