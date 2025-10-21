class MyList:
    """A simple, custom list-like container."""

    def __init__(self) -> None:
        """Initializes an empty list to store the elements."""
        # The underscore `_` prefix suggests this is an "internal" attribute.
        self._list = []

    def __repr__(self) -> str:
        """
        Returns the official string representation of the object.
        This is used when you print the object directly.
        """
        return f"MyList({self._list})"

    def __len__(self) -> int:
        """
        Returns the number of items in the list.
        This allows the built-in len() function to work on MyList objects.
        """
        return len(self._list)

    def __getitem__(self, index: int):
        """
        Gets an item by its index.
        This allows using square bracket notation for access (e.g., my_list[0]).
        """
        return self._list[index]

    def __setitem__(self, index: int, value) -> None:
        """
        Sets an item at a specific index.
        This allows using square bracket notation for assignment (e.g., my_list[0] = 100).
        """
        self._list[index] = value

    def append(self, element) -> None:
        """Adds an element to the end of the list."""
        self._list.append(element)


# Create an instance of our custom list.
my_custom_list = MyList()

# Add some elements to it using our custom append method.
my_custom_list.append(1)
my_custom_list.append(2)

# Use the built-in len() function, which works thanks to our __len__ method.
print(f"Length of the list: {len(my_custom_list)}")

# Access an element using square brackets, thanks to our __getitem__ method.
print(f"Element at index 0: {my_custom_list[0]}")

# Change an element's value, thanks to our __setitem__ method.
print("Changing element at index 0 to 100...")
my_custom_list[0] = 100

# Print the entire object, which looks nice thanks to our __repr__ method.
print(f"The list after modification: {my_custom_list}")
