# Books online scraping tool

## What it does
Retrieves books data from books.toscrape.com. Uses that data to populate csv
 files either per category or the whole list, and optionally to download the
  book cover image. 

## How to install
1. Clone the repository on your computer.

`git clone https://github.com/mepto/p2.git`

2. Make sure you use python 3.8.5. Check your python version:

`python --version`

3. Create and activate your virtual environment. The methodology below uses the venv module but you may use your favorite
 virtual environment instead.
* Creation from project root:

`python -m venv <your-virtual-env-name>` 
 
* Activation in Windows:

`<your-virtual-env-name>\Scripts\activate.bat`

* Activation in Linux:

`source <your-virtual-env-name>/bin/activate`

4. Install the dependencies with pip

`pip install -r requirements.txt`

## How to use
1. At project root, to launch the script type

`python main.py`

2. The system will prompt you to choose an export by category (type 1) or an
 export of all books (type 2)
 
3. The system will ask if you wish to download the book covers (type 1) or
 not (type 0).
 
4. Patience... The terminal will indicate when your request is done being
 processed.
 
5. Files are stored in <local_path>/p2/books_online/assets
    * /exports/ for *.csv files
    * /media/ for image files 