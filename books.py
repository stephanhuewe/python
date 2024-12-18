class Book:
    def __init__(self, author, title, year, book_id):
        self.author = author
        self.title = title
        self.year = year
        self.book_id = book_id

    def __str__(self):
        return 'Book({}, {}, {})'.format(self.author, self.title, self.book_id)

    def __repr__(self):

        return 'Book({}, {}, {})'.format(self.author, self.title, self.book_id)

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.book_id == other.book_id
        
foo = Book("William Shakespeare","Macbeth",1606,12345);
print(foo.title)
