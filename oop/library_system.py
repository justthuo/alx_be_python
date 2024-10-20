# Create instances of each type of book
classic_book = Book("Pride and Prejudice", "Jane Austen")
digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

# Add books to the library
my_library.add_book(classic_book)
my_library.add_book(digital_novel)
my_library.add_book(paper_novel)

# List all books in the library
my_library.list_books()

# library_system.py

class Book:
    """Base class for all books."""
    
    def __init__(self, title: str, author: str):
        """Initialize a Book instance with title and author."""
        self.title = title
        self.author = author

    def __str__(self) -> str:
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Class representing an electronic book."""
    
    def __init__(self, title: str, author: str, file_size: int):
        """Initialize an EBook instance with title, author, and file size."""
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size

    def __str__(self) -> str:
        """Return a string representation of the ebook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Class representing a printed book."""
    
    def __init__(self, title: str, author: str, page_count: int):
        """Initialize a PrintBook instance with title, author, and page count."""
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count

    def __str__(self) -> str:
        """Return a string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class representing a library that manages a collection of books."""
    
    def __init__(self):
        """Initialize the library with an empty book collection."""
        self.books = []

    def add_book(self, book: Book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)

            # main.py

from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()