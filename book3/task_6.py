class Animal:
    """A base class for all animals."""

    def speak(self) -> str:
        """Returns a generic animal sound."""
        return "Animal Sound"


class Dog(Animal):
    """A subclass representing a dog."""

    def speak(self) -> str:
        """Overrides the base method to return a bark."""
        return "Bark"


class Cat(Animal):
    """A subclass representing a cat."""

    def speak(self) -> str:
        """Overrides the base method to return a meow."""
        return "Meow"


def make_animals_speak(list_of_animals: list) -> None:
    """
    Takes a list of animal objects and prints the sound each one makes.

    :param list_of_animals: A list containing instances of Animal or its subclasses.
    """
    for animal in list_of_animals:
        print(animal.speak(), end=" ")
    # Add a final print() to move the cursor to the next line for clean output.
    print()


# 1. Create a list containing different types of animal objects.
all_animals = [Dog(), Cat()]

# 2. Pass the list to the function and let polymorphism do its work.
print("The animals say:")
make_animals_speak(all_animals)
