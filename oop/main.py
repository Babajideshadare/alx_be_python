from book_class import Book
import gc  # ensures __del__ runs promptly when we delete references

if __name__ == "__main__":
    # Create a Book instance
    b = Book("The Alchemist", "Paulo Coelho", 1988)

    # Use __str__
    print(b)  # expected: The Alchemist by Paulo Coelho, published in 1988

    # Use __repr__
    print(repr(b))  # expected: Book('The Alchemist', 'Paulo Coelho', 1988)

    # Trigger destructor
    del b
    gc.collect()  # ensure the __del__ message prints during this run