class Car:
    """
    Represents a car and tracks the total count of all created cars.
    """

    # This is a class attribute
    count = 0

    def __init__(self, model: str):
        """
        Initializes a new Car object and increments the class-level counter.
        """
        self._model = model
        # increment count
        Car.count += 1

    @classmethod
    def get_count(cls) -> int:
        """
        A class method that returns the total number of cars created.
        """
        return cls.count


# Create the first instance of the Car class.
car_one = Car("Mercedes-Benz")
car_two = Car("Honda")

# Get the total count.
total_cars = Car.get_count()

# Print the count result
print(f"Total number of cars created: {total_cars}")
