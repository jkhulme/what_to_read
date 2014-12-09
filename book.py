class Book(object):

    def __init__(self, book_data):
        print book_data.keys()
        self.id = book_data.get("id", "ERR: Missing id")
        self.title = book_data.get("name", "ERR: Missing Title")
        self.authors = self.author_names(book_data.get("authors", [{}]))
        self.description = book_data.get("description", "ERR: Missing description")
        self.price = book_data.get("price", "ERR: Missing Price")
        self.currency = book_data.get("price_currency", "ERR: Missing Currency")
        self.sample_url = book_data.get("sample_url", "ERR: Missing Sample URL")
        self.uri = book_data.get("resource_uri", "ERR: Missing URI")
        self.image = self.get_image_url(book_data.get("main_image", [{}]))

    def author_names(self, authors):
        author_names = []
        for author in authors:
            author_names.append(author.get("name", "Author Missing"))
        return author_names

    def get_image_url(self, image):
        return image.get("image", {}).get("640x640", "ERR:Missing image")
