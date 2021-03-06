#! /usr/bin/python
# coding: utf-8

SCRAPE_URL = 'http://books.toscrape.com/'
FIELDNAMES = ['product_page_url', 'universal_product_code', 'title',
              'price_including_tax', 'price_excluding_tax',
              'quantity_available', 'product_description', 'category',
              'review_rating', 'image_url']
NO_URL_ERROR = 'No page was given for analysis.'
PATIENCE_MESSAGE = 'This may take a few minutes... Please wait.'