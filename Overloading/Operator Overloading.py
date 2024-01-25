class Book:
    def __init__(self, pages):
        """Constructor method to initialize the Book object with the given number of pages.

        Args:
            pages (int): Number of pages in the book.
        """
        self.pages = pages

    def __add__(self, other):
        """Overloaded addition operator to add two Book objects.

        Args:
            other (Book): Another Book object to be added.

        Returns:
            Book: A new Book object with the sum of pages from the two input books.
        """
        new_book = Book(self.pages + other.pages)
        return new_book

    def display(self):
        """Displays the number of pages in the book."""
        print(self.pages)

# Creating instances of the Book class
b1 = Book(100)
b2 = Book(100)
b3 = Book(200)

# Using the overloaded addition operator to add b1 and b2
result_book = b1 + b2
print(result_book)
print("*" * 50)

# Using the overloaded addition operator to add b1, b2, and b3
total_pages = b1 + b2 + b3
print(total_pages.pages)

# Displaying the total number of pages
total_pages.display()
