class Temperature():
    def __init__(self, degrees) -> None:
        self.degrees = degrees
    
    def __ge__(self, other):
        if isinstance(other,Temperature):
            return self.degrees >= other.degrees
        return NotImplemented
        
    def __lt__(self,other):
        return self.degrees < other.degrees

    def __eq__(self, other):
        return self.degrees == other.degrees
    
temp1 = Temperature(30)
temp2 = Temperature(25)

print(temp1 >= temp2)
print(temp1 < temp2)
print(temp1 == temp2)
print(temp1 == Temperature(30))