#! /usr/bin/python
# coding: utf-8

from urllib.parse import urljoin
import requests

from bs4 import BeautifulSoup

from .settings import SCRAPE_URL


class Categories:
    """
    Create a list of all categories and their href
    """

    all_categories = []

    def __init__(self):
        page = requests.get(SCRAPE_URL)
        self.page_content = BeautifulSoup(page.content, 'html.parser')
        categories_data = self.page_content.select('.side_categories li ul li a')
        for data in categories_data:
            href = urljoin(SCRAPE_URL, data.get('href'))
            category = data.get_text(strip=True)
            self.all_categories.append({'href': href, 'category': category})

    def get(self):
        return self.all_categories


class Product:
    """
    Retrieve data for one book from the page url
    """
    page = ''
    page_content = ''

    def get_item(self, item, pos=0, attr_type='class', attr=''):
        find_item = self.page_content.find_all(item, {attr_type: attr})
        return find_item[pos].text

    def __init__(self, page):
        page = requests.get(page)
        self.page_content = BeautifulSoup(page.content, 'html.parser')
        product = self.page_content.prettify()
        title = self.get_item('h1')
        description = self.get_item('p')
        upc = self.get_item('td')
        price_no_tax = self.get_item('td', pos=2)
        price_tax = self.get_item('td', pos=3)
        nb_reviews = self.get_item('td', pos=6)
        rating = self.page_content.select('.product_main .star-rating')[0][
            'class'][1]
        image = urljoin(SCRAPE_URL, self.page_content.find('div', {
            'id': 'product_gallery'}).find('img')['src'])
        category = self.page_content.find('ul', {'class': 'breadcrumb'}) \
            .find_all('li')[2].select('a')[0].text
        nb_stock = ''
        for char in self.page_content.find('p', {'class': 'availability'}).text:
            if char.isdigit():
                nb_stock += char
        nb_stock = int(nb_stock)
