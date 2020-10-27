#! /usr/bin/python
# coding: utf-8
from urllib.parse import urljoin

from books_online.models.page import Page
from books_online.settings import SCRAPE_URL, NO_URL_ERROR


class AllCategories:
    """
    Create a list of all categories and their href
    """

    all_categories = []

    def __init__(self, option):
        page = Page(SCRAPE_URL).scrape()
        if page:
            if option == 1:  # 'categories':
                categories_data = page.select('.side_categories li ul li a')
            elif option == 2:  # 'all_books':
                categories_data = page.select('.side_categories > ul > li > a')
            else:
                raise Exception(
                    'Type unknown. Please select "categories" or "all_books".')

            for item in categories_data:
                href = urljoin(SCRAPE_URL, item.get('href'))
                category = item.get_text(strip=True)
                self.all_categories.append({'href': href, 'category': category})
        else:
            raise Exception(NO_URL_ERROR)

    def data(self):
        return self.all_categories
