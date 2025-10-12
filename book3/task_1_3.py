from math import pi

class Circle():
    def __init__(self, radius: float) -> None:
        self.radius = radius
    
    def area(self):
        return 2 * pi * (self.radius**2)
    


circle1 = Circle(10)
print(circle1.area())