# Books online scraping tool

## What it does
Retrieves books data from books.toscrape.com. Uses that data to populate csv
 files either per category or the whole list, and optionally to download the
  book cover image. 

## How to install
* Clone the repository on your computer.

`git clone https://github.com/mepto/p2.git`

* Create and activate your virtual environment with your favorite tool. Make
 sure you use python 3.8.5.
* Install the dependencies with pip

`pip install -r requirements.txt`

## How to use
1. At project root, to launch the script type

`python books_online.py`

2. The system will prompt you to choose an export by category (type 1) or an
 export of all books (type 2)
 
3. The system will ask if you wish to download the book covers (type 1) or
 not (type 0).
 
4. Patience... The terminal will indicate when your request is done being
 processed.
 
5. Files are stored in <local_path>/p2/books_online/assets
    * /exports/ for *.csv files
    * /media/ for image files 