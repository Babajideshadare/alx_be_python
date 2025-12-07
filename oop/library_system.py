# library_system.py

class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int) -> None:
        super().__init__(title, author)
        self.file_size = file_size  # in KB

    def __str__(self) -> str:
        # Note: no space before KB, and label is "File Size"
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int) -> None:
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self) -> str:
        # Label is "Page Count"
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self) -> None:
        self.books = []

    def add_book(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("Only Book or its subclasses can be added to the Library.")
        self.books.append(book)

    def list_books(self) -> None:
        for book in self.books:
            print(book)  # Uses each class's __str__