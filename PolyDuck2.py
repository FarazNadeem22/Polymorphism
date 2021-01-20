class Duck:
    def talk(self):
        print("Quack quack....")


class Dog:
    def bark(self):
        print("Woof woof....")


class Cat:
    def Meow(self):
        print("Meow Meow....")


class Goat:
    def talk(self):
        print("Mayaah Mayaah....")

def f1(object):
    if hasattr(object, 'talk'):
        object.talk()    
    elif hasattr(object,'bark'):
        object.bark()
    else:
        print("Attribute Not Found")

lst = [Duck(),Dog(),Cat(),Goat()]

for object in lst:
    f1(object)
