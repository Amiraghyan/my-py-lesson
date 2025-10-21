class Stack:
    """A simple implementation of a stack data structure."""

    def __init__(self) -> None:
        """Initializes an empty stack."""
        # The double underscore `__` triggers name mangling, making it harder
        # to access this list from outside the class (e.g., stack.__items).
        self.__items = []

    def push(self, item) -> None:
        """Adds an item to the top of the stack."""
        self.__items.append(item)

    def pop(self):
        """
        Removes and returns the top item from the stack.
        Returns None and prints a warning if the stack is empty.
        """
        # Check if the stack is empty before trying to pop an item.
        if not self.is_empty():
            return self.__items.pop()
        else:
            # This prevents the program from crashing with an IndexError.
            print("Warning: Cannot pop from an empty stack.")
            return None

    def is_empty(self) -> bool:
        """Returns True if the stack is empty, False otherwise."""
        # An empty list is "falsy", so `not []` evaluates to True.
        return not self.__items

    def size(self) -> int:
        """Returns the number of items currently in the stack."""
        return len(self.__items)


# Create an instance of our Stack.
my_stack = Stack()

# Add some items to the stack.
print("Pushing 1, 2, and 3 onto the stack...")
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

# Pop items from the stack (Last-In, First-Out).
popped_item = my_stack.pop()
print(f"Popped item: {popped_item}")  # Expected: 3

popped_item = my_stack.pop()
print(f"Popped item: {popped_item}")  # Expected: 2

# Check if the stack is empty.
print(f"Is the stack empty? {my_stack.is_empty()}")  # Expected: False

# Check the current size.
print(f"Current size of the stack: {my_stack.size()}")  # Expected: 1

# This demonstrates name mangling. Trying to access `__items` directly
# from outside the class will result in an AttributeError.
# print(my_stack.__items)
