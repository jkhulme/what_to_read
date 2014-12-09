from flask import Flask, render_template
from random import randint
import urllib
import json
from book import Book

app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

NUM_OF_BOOKS = 100

@app.route("/")
def index():
    book = get_book()
    if book is not None:
        return render_template('index.jade', book=book)
    else:
        return render_template('error.jade')

def get_book():
    books = json.loads(urllib.urlopen("https://riidr.com/api/v1/product/?limit=" + str(NUM_OF_BOOKS) + "&format=json").read()).get("objects", [])
    if len(books) < 1:
        return None
    else:
        idx = randint(0, len(books) - 1)
        return Book(books[idx])

if __name__ == "__main__":
    app.run()
