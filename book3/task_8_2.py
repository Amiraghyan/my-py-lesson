class Car:
    count = 0

    def __init__(self, model):
        self._model = model
        Car.count += 1

    @classmethod
    def get_count(cls):
        return cls.count
    
car1 = Car("Mercedes-Benz")
car2 = Car("Honda")

print(Car.get_count())