from book_class import Book
import gc

b = Book("1984", "George Orwell", 1949)
print(b)
print(repr(b))
del b
gc.collect()