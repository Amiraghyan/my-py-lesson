#  Աբստրակցիա (Abstraction)
from abc import ABC,abstractmethod
from typing import List

class BaseShape(ABC):
    
    @abstractmethod
    def calculate_area(self) -> float:
        pass
    @abstractmethod
    def get_shape_name(self) -> str:
        pass

class Circle(BaseShape):
    def __init__(self, r: float) -> None:
        self._r = r
    
    def calculate_area(self) -> float:
        return 3.14 * (self._r **2)
    
    def get_shape_name(self) -> str:
        return "Circle"


class Rectangle(BaseShape):
    def __init__(self, h: float, w: float) -> None:
        self._h = h
        self._w = w
    def calculate_area(self) -> float: 
        return self._h * self._w
    def get_shape_name(self) -> str:
        return "Rectangle"
    


# test_BaseShape = BaseShape()
# TypeError: Can't instantiate abstract class BaseShape without an implementation for abstract methods 'calculate_area', 'get_shape_name'

my_circle = Circle(10)
my_rectangle = Rectangle(4,5)

shapes: List[BaseShape] = [my_circle, my_rectangle]


for shape in shapes:
    print(f"{shape.get_shape_name()}  - {shape.calculate_area()}") 