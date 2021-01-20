from abc import *

class Vehicle(ABC):
    @abstractmethod
    def no_of_wheels(self):
        """This is your abstract method that will be implemented in the child-class see readme.md for more information"""
        pass
    def name_of_Vihicle(self):
        print("The Faraz Car")

class Bus(Vehicle):
    def no_of_wheels(self):
        """Implementing the the abstracrt method from the parent class here"""
        return 8

class Car(Vehicle):
    def no_of_wheels(self):
        """Implementing the the abstracrt method from the parent class here"""
        return 4


car = Car()
car.name_of_Vihicle()
print(car.no_of_wheels())

bus = Bus()
print(bus.no_of_wheels())
