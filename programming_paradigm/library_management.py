# library_management.py

class Book:
    """
    Represents a book with a title and author, and whether it's checked out.
    """
    def __init__(self, title: str, author: str) -> None:
        self.title = title              # public
        self.author = author            # public
        self._is_checked_out = False    # private state

    def check_out(self) -> bool:
        """
        Mark the book as checked out if available.
        Returns True if successful, False if it was already checked out.
        """
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self) -> bool:
        """
        Mark the book as returned (available).
        Returns True if successful, False if it was not checked out.
        """
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    def is_available(self) -> bool:
        """Return True if the book is available (not checked out)."""
        return not self._is_checked_out

    def __str__(self) -> str:
        """Human-friendly representation, used by print(book)."""
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book objects.
    """
    def __init__(self) -> None:
        self._books: list[Book] = []  # private list of books

    def add_book(self, book: Book) -> None:
        """Add a Book to the collection."""
        self._books.append(book)

    def check_out_book(self, title: str) -> bool:
        """
        Find a book by title and check it out if available.
        Returns True on success, False if not found or already checked out.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                return book.check_out()
        return False

    def return_book(self, title: str) -> bool:
        """
        Find a book by title and return it if it’s currently checked out.
        Returns True on success, False if not found or not checked out.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                return book.return_book()
        return False

    def list_available_books(self) -> list[Book]:
        """Return a list of Book objects that are currently available."""
        return [book for book in self._books if book.is_available()]