from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def get_salary(self):
        pass

class Manager(Employee):
    def __init__(self, salary) :
        self._salary = salary
    def work(self):
        return "Managing the team"
    def get_salary(self):
        return self._salary

class Developer(Employee):
    def __init__(self, salary) :
        self._salary = salary
    def work(self):
        return "Writing code"
    def get_salary(self):
        return self._salary

manager = Manager(70000)
developer = Developer(60000)

print(manager.work())  #Managing the team
print(manager.get_salary()) # 70000

print(developer.work())  #Writing code
print(developer.get_salary()) # 60000