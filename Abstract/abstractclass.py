from abc import *

class Vehicle(ABC):
    @abstractmethod
    def no_of_wheels(self):
        pass
    def name_of_Vihicle(self):
        print("The Faraz Car")

class Bus(Vehicle):
    def no_of_wheels(self):
        return 8

class Car(Vehicle):
    def no_of_wheels(self):
        return 4


car = Car()
car.name_of_Vihicle()
print(car.no_of_wheels())

bus = Bus()
print(bus.no_of_wheels())
