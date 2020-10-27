#! /usr/bin/python
# coding: utf-8

from math import trunc

from books_online.models.page import Page
from books_online.settings import SCRAPE_URL, NO_URL_ERROR


class Category:
    """
    Create a list of all books listed in a category
    """
    total_pages = 1

    def __init__(self, url=''):
        self.category_products = []
        products_per_page = 20

        page = Page(url).scrape()

        if page:
            self.get_page_products(url)
            total_results = int(
                page.select('form.form-horizontal strong')[0].text)
            if total_results > products_per_page:
                extra_pages = trunc(total_results / products_per_page)
                base_url = url[:url.rfind('/')]
                for result_page in range(2, extra_pages + 2):
                    extra_page_url = f'{base_url}/page-{result_page}.html'
                    self.get_page_products(extra_page_url)
        else:
            raise Exception(NO_URL_ERROR)

    def get_page_products(self, url):
        current_page = Page(url).scrape()
        links = current_page.select('section ol li article.product_pod h3 a')
        for link in links:
            stripped_link = link.get('href').strip('../')
            self.category_products.append(SCRAPE_URL + 'catalogue/' +
                                          stripped_link)

    def data(self):
        return self.category_products
