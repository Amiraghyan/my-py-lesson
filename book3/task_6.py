class Animal:
    def speak(self):
        return "Animal Sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"
    
def make_sounds(animals):
    for animal in animals:
        print(animal.speak(), end=" ")

animals = [Dog(), Cat()]
make_sounds(animals)