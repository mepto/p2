#! /usr/bin/python
# coding: utf-8

import requests

from bs4 import BeautifulSoup


class Page:
    """
    Create new instance for parsed page data
    """

    def __init__(self, url):
        page = requests.get(url)
        self.page_content = BeautifulSoup(page.content, 'html.parser')

    def scrape(self):
        return self.page_content
