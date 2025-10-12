class Person():
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def greet(self) -> None:
        print(f"Hello, my name is {self.name} and I am {self.age} years old")

person1 = Person("Artur", 48)
person2 = Person("Anna", 35)

person1.greet()
person2.greet()