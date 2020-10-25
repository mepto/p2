#! /usr/bin/python
# coding: utf-8

from urllib.parse import urljoin
import requests

from bs4 import BeautifulSoup

from .settings import SCRAPE_URL


class Page:
    """
    Create new instance for parsed page data
    """

    def __init__(self, url):
        page = requests.get(url)
        self.page_content = BeautifulSoup(page.content, 'html.parser')

    def scrape(self):
        return self.page_content


class Categories:
    """
    Create a list of all categories and their href
    """

    all_categories = []

    def __init__(self):
        page = Page(SCRAPE_URL).scrape()
        categories_data = page.select('.side_categories li ul li a')
        for item in categories_data:
            href = urljoin(SCRAPE_URL, item.get('href'))
            category = item.get_text(strip=True)
            self.all_categories.append({'href': href, 'category': category})

    def data(self):
        return self.all_categories


class Category:
    """
    Create a list of all books listed in a category
    """
    total_pages = 1

    def __init__(self, url):
        self.category_products = []
        page = Page(url).scrape()
        if page:
            ...

    def data(self):
        return self.category_products


class Book:
    """
    Retrieve data for one book from the page url
    """
    page_content = ''

    def get_item(self, item, pos=0, attr_type='class', attr=''):
        try:
            find_item = self.page.find_all(item, {attr_type: attr})
            return find_item[pos].text
        except IndexError:
            return 'N/A'

    def __init__(self, url=''):
        self.url = url
        if self.url:
            self.page = Page(self.url).scrape()
            self.title = self.get_item('h1')
            self.description = self.get_item('p')
            self.upc = self.get_item('td')
            self.price_no_tax = self.get_item('td', pos=2)
            self.price_tax = self.get_item('td', pos=3)
            self.nb_reviews = self.get_item('td', pos=6)
            self.rating = self.page.select('.product_main .star-rating')[0][
                'class'][1]
            self.image = urljoin(SCRAPE_URL, self.page.find('div', {
                'id': 'product_gallery'}).find('img')['src'])
            self.category = self.page.find('ul', {'class': 'breadcrumb'}) \
                .find_all('li')[2].select('a')[0].text
            # Get stock
            self.stock = ''
            for char in self.page.find('p', {'class': 'availability'}).text:
                if char.isdigit():
                    self.stock += char
            self.stock = int(self.stock)
        else:
            raise Exception('No page was given for analysis')

    def data(self):
        return {'product_page_url': self.url,
                'universal_product_code': self.upc, 'title': self.title,
                'price_including_tax': self.price_tax,
                'price_excluding_tax': self.price_no_tax,
                'quantity_available': self.stock,
                'product_description': self.description,
                'category': self.category, 'review_rating': self.rating,
                'image_url': self.image}
