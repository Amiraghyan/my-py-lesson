from math import pi


class Circle:
    """Represents a circle with a given radius."""

    def __init__(self, radius: float) -> None:
        """Initializes a new Circle object."""
        self.radius = radius

    def area(self) -> float:
        """
        Calculates the area of the circle.
        The formula for the area is: π * r².
        """
        # The original formula was incorrect. This is the correct formula for area.
        return pi * (self.radius**2)


# Define the radius for our circle.
radius_value = 10


circle_one = Circle(radius_value)

# Calculate and print the area.
circle_area = circle_one.area()
print(f"The area of a circle with radius {radius_value} is: {circle_area}")
