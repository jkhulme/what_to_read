class Book(object):

    def __init__(self, book_data):
        self.title = book_data.get("name", "ERR: Missing Title")
        self.authors = self.author_names(book_data.get("authors", ["ERR: Missing Authors"]))
        self.description = book_data.get("description", "ERR: Missing description")
        self.price = book_data.get("price", "ERR: Missing Price")
        self.currency = book_data.get("price_currency", "ERR: Missing Currency")
        self.sample_url = book_data.get("sample_url", "ERR: Missing Sample URL")
        self.uri = book_data.get("resource_uri", "ERR: Missing URI")
        self.image = book_data.get("main_image", "ERR: Missing Image")

    def author_names(self, authors):
        for author in authors:
            print author
