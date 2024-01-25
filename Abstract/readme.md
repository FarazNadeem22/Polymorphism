# README.md

## Vehicle Abstraction

This Python code defines a simple abstraction for vehicles using abstract classes. The main purpose is to demonstrate the concept of abstraction in object-oriented programming.

### Code Structure

The code consists of two classes:

1. **Vehicle (Abstract Base Class - ABC):**
   - Contains an abstract method `no_of_wheels()`, which should be implemented by its child classes.
   - Provides a concrete method `name_of_Vehicle()` that prints a default vehicle name.

2. **Bus and Car (Concrete Classes):**
   - Inherit from the `Vehicle` class.
   - Implement the abstract method `no_of_wheels()` by specifying the number of wheels for each type of vehicle.

### How to Use

1. **Creating Instances:**
   - Instantiate objects of the `Car` or `Bus` class.

```python
car = Car()
bus = Bus()
```

Accessing Methods:
Call the name_of_Vehicle() method to print the default vehicle name.
Call the no_of_wheels() method to get the number of wheels for the specific vehicle.


```python
car.name_of_Vehicle()
print(car.no_of_wheels())
bus.name_of_Vehicle()
print(bus.no_of_wheels())


Example Output
The Faraz Car
4
8


Faraz 
Creator of Vehicle Abstraction Code
