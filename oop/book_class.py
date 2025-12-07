class Book:
    def __init__(self, title, author, year):
        # Constructor: initializes attributes
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        # Destructor: prints exactly "Deleting (title of the book)"
        print(f"Deleting ({self.title})")

    def __str__(self):
        # Human-friendly string
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Official representation: recreates the object
        return f"Book('{self.title}', '{self.author}', {self.year})"