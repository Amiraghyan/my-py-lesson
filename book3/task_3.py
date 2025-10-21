class Temperature:
    """Represents a temperature value in degrees."""

    def __init__(self, degrees: float) -> None:
        """Initializes a new Temperature object."""
        self.degrees = degrees

    def __ge__(self, other) -> bool:
        """
        Handles the greater than or equal to (>=) comparison.
        It only works if 'other' is also a Temperature object.
        """
        if isinstance(other, Temperature):
            return self.degrees >= other.degrees
        # If we try to compare with a non-Temperature type, we let Python know
        # that this operation is not implemented for that combination.
        return NotImplemented

    def __lt__(self, other) -> bool:
        """
        Handles the less than (<) comparison.
        It only works if 'other' is also a Temperature object.
        """
        if isinstance(other, Temperature):
            return self.degrees < other.degrees
        return NotImplemented

    def __eq__(self, other) -> bool:
        """
        Handles the equality (==) comparison.
        It only works if 'other' is also a Temperature object.
        """
        if isinstance(other, Temperature):
            return self.degrees == other.degrees
        return NotImplemented


# Create two instances (objects) of the Temperature class.
temp_one = Temperature(30)
temp_two = Temperature(25)

# Perform comparisons, which now work because we defined the special methods.
print(f"Is temp_one >= temp_two?  -> {temp_one >= temp_two}")
print(f"Is temp_one < temp_two?   -> {temp_one < temp_two}")
print(f"Is temp_one == temp_two?  -> {temp_one == temp_two}")

# A final check for equality with a new object having the same value.
print(f"Is temp_one == Temperature(30)? -> {temp_one == Temperature(30)}")
