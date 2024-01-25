from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def no_of_wheels(self):
        """Abstract method to be implemented by child classes.
        
        Returns:
            int: Number of wheels for the specific vehicle.
        """
        pass
    
    def name_of_Vehicle(self):
        """Prints the default vehicle name."""
        print("The Faraz Car")

class Bus(Vehicle):
    def no_of_wheels(self):
        """Implements the abstract method from the parent class.
        
        Returns:
            int: Number of wheels for a bus (in this case, 8).
        """
        return 8

class Car(Vehicle):
    def no_of_wheels(self):
        """Implements the abstract method from the parent class.
        
        Returns:
            int: Number of wheels for a car (in this case, 4).
        """
        return 4

# Creating an instance of the Car class
car = Car()

# Calling the name_of_Vehicle method to print the default vehicle name
car.name_of_Vehicle()

# Calling the no_of_wheels method to get the number of wheels for the car
print(car.no_of_wheels())

# Creating an instance of the Bus class
bus = Bus()

# Calling the no_of_wheels method to get the number of wheels for the bus
print(bus.no_of_wheels())
