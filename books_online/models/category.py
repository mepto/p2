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
        page = Page(url).scrape()

        # Find max items per page
        main_page = Page(SCRAPE_URL).scrape()
        products_per_page = int(
            main_page.select('form.form-horizontal strong')[2].text)

        if page:
            self.get_page_products(url)
            total_results = int(
                page.select('form.form-horizontal strong')[0].text)
            # Determine if and scrape when there is more than 1 result page
            if total_results > products_per_page:
                extra_pages = trunc(total_results / products_per_page)
                base_url = url[:url.rfind('/')]
                for result_page in range(2, extra_pages + 2):
                    extra_page_url = f'{base_url}/page-{result_page}.html'
                    self.get_page_products(extra_page_url)
        else:
            raise Exception(NO_URL_ERROR)

    def get_page_products(self, url):
        """
        Get list of books href on result page
        """
        current_page = Page(url).scrape()
        links = current_page.select('section ol li article.product_pod h3 a')
        for link in links:
            stripped_link = link.get('href').strip('../')
            self.category_products.append(SCRAPE_URL + 'catalogue/' +
                                          stripped_link)

    def data(self):
        return self.category_products
