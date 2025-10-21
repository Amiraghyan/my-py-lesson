class Person:
    """Represents a person with a name and an age."""

    def __init__(self, name: str, age: int) -> None:
        """Initializes a new Person object."""
        self.name = name
        self.age = age

    def greet(self) -> None:
        """Prints a greeting message using the person's details."""
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# --- Script Execution ---

# Create the first instance (object) of the Person class.
person_one = Person("Artur", 48)

# Create the second instance of the Person class.
person_two = Person("Anna", 35)

# Call the greet() method for each person object to display their info.
person_one.greet()
person_two.greet()
