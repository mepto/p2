#! /usr/bin/python
# coding: utf-8

"""
:synopsis: Start scraping programme from here
"""

# renommer ce fichier en main.py
from time import process_time

from books_online import main as scrape


# Launch main loop from project root

if __name__ == '__main__':
    t1_start = process_time()
    scrape.main()
    t1_stop = process_time()
    print('elapsed time: ', t1_stop-t1_start)
