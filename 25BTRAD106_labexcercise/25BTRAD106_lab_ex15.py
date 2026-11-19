# Lab 15: Library management system

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def issue_book(self, book_id):
        for b in self.books:
            if b.book_id == book_id:
                if b.available:
                    b.available = False
                    print(b.title, "issued.")
                else:
                    print(b.title, "is already issued.")
                return
        print("Book not found.")

    def return_book(self, book_id):
        for b in self.books:
            if b.book_id == book_id:
                if not b.available:
                    b.available = True
                    print(b.title, "returned.")
                else:
                    print(b.title, "was not issued.")
                return
        print("Book not found.")

    def display_books(self):
        for b in self.books:
            status = "Available" if b.available else "Issued"
            print(b.book_id, "|", b.title, "|", b.author, "|", status)

# Inheritance: a special kind of book
class ReferenceBook(Book):
    def __init__(self, book_id, title, author):
        super().__init__(book_id, title, author)
        self.available = False    # reference books cannot be issued

# Simulation
lib = Library()
lib.add_book(Book(1, "Python Basics", "A. Kumar"))
lib.add_book(Book(2, "Data Structures", "R. Sharma"))
lib.add_book(ReferenceBook(3, "Encyclopedia", "Various"))

lib.display_books()
print()
lib.issue_book(1)
lib.issue_book(1)      # already issued
lib.return_book(1)
lib.return_book(2)     # not issued
lib.issue_book(9)      # not found
print()
lib.display_books()
