from abc import ABC, abstractmethod


class Employee(ABC):
    """
    An abstract base class for all employee types.

    It defines a contract that all subclasses must follow by implementing
    the `work` and `get_salary` methods.
    """

    @abstractmethod
    def work(self) -> str:
        """An abstract method to describe the employee's work."""
        pass

    @abstractmethod
    def get_salary(self) -> float:
        """An abstract method to retrieve the employee's salary."""
        pass


class Manager(Employee):
    """A concrete implementation of an Employee who manages a team."""

    def __init__(self, salary: float):
        """Initializes the Manager with a salary."""
        # A simple check to ensure the salary is a valid number.
        if salary < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = salary

    def work(self) -> str:
        """Implements the work method for a Manager."""
        return "Managing the team"

    def get_salary(self) -> float:
        """Implements the get_salary method for a Manager."""
        return self._salary


class Developer(Employee):
    """A concrete implementation of an Employee who writes code."""

    def __init__(self, salary: float):
        """Initializes the Developer with a salary."""
        if salary < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = salary

    def work(self) -> str:
        """Implements the work method for a Developer."""
        return "Writing code"

    def get_salary(self) -> float:
        """Implements the get_salary method for a Developer."""
        return self._salary


# 1. Create instances of the concrete classes.
manager = Manager(70000)
developer = Developer(60000)

# 2. Demonstrate that each object works as expected.
print(f"Manager's work: {manager.work()}")
print(f"Manager's salary: {manager.get_salary()}")

print(f"Developer's work: {developer.work()}")
print(f"Developer's salary: {developer.get_salary()}")

# Note: You cannot create an instance of the abstract class itself.
# The following line would cause a TypeError:
# invalid_employee = Employee()
