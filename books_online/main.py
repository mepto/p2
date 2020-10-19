#! /usr/bin/python
# coding: utf-8

from .models import Categories, Product


def main():
    """

    """
    x = Product(
        'http://books.toscrape.com/catalogue/ready-player-one_209/index.html')
    categories = Categories()
    print(categories.get())
