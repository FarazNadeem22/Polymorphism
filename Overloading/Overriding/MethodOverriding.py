class Parent:
    def property(self):
        print("Gold, land, cash, power")
    def date(self):
        print("Olivia wilde")

class Child(Parent):
"""Child class inherits from Parent class """
    def date(self):
    """Here we are overriding the parent class date method"""
        #super().date()
        print("Kartina Kaif")

# creating a child object 
c= Child()

#calling property method which is inherited from the parent-class
c.property()

#Here we are calling the overridden date method from child-class.
c.date()
