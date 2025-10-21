class MathOperations:
    """
    A utility class that provides a collection of static math functions.
    It doesn't need to be instantiated to be used.
    """

    @staticmethod
    def add(x: float, y: float) -> float:
        """
        Adds two numbers together.
        """
        return x + y

    @staticmethod
    def multiply(x: float, y: float) -> float:
        """
        Multiplies two numbers.
        """
        return x * y


# Call the static methods directly on the class, without creating an object.
sum_result = MathOperations.add(4, 3)
product_result = MathOperations.multiply(2, 3)

# Print the results in a more descriptive way.
print(f"The result of adding 4 and 3 is: {sum_result}")
print(f"The result of multiplying 2 and 3 is: {product_result}")
