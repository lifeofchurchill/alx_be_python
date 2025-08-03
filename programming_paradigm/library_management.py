class Book :
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.__is_checked_out = available 

class library :
    def __init__(self, Book):
        self.__Books = Book


def add_book(self) :
    details = f"{self.title} {self.author}"
    return details
