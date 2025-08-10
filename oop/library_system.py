# library_system.py

class Book:
    def __init__(self, title, author):
        """Initialize common book attributes."""
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize EBook attributes and call base class constructor."""
        super().__init__(title, author)
        self.file_size = file_size  # in KB

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize PrintBook attributes and call base class constructor."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize an empty library."""
        self.books = []

    def add_book(self, book):
        """Add a Book (or subclass) instance to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only Book, EBook, or PrintBook instances can be added to the library.")

    def list_books(self):
        """List all books in the library."""
        for book in self.books:
            print(book)
