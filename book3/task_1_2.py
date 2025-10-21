class Book:
    """Represents a book with a title and an author."""

    def __init__(self, title: str, author: str) -> None:
        """Initializes a new Book object."""
        self.title = title
        self.author = author

    def description(self) -> dict:
        """Returns the book's details as a dictionary."""
        return {"title": self.title, "author": self.author}


# --- Script Execution ---

# Create instances of the Book class.
book_one = Book("The Jester King", "Hovhannes Tumanyan")
book_two = Book("The Wise Men of Nukin Town", "Avetik Isahakyan")

# --- Displaying the book details ---

# Print the full dictionary returned by the description() method.
print(book_one.description())
print(book_two.description())

# To avoid calling the method multiple times, we can store its result.
book_one_details = book_one.description()
book_two_details = book_two.description()

# Print the title and author from the stored dictionary, separated by " - ".
print(book_one_details["title"], book_one_details["author"], sep=" - ")
print(book_two_details["title"], book_two_details["author"], sep=" - ")
