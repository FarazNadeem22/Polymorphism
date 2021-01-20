class Duck:
    def talk(self):
        print("Quack quack....")


class Dog:
    def talk(self):
        print("Woof woof....")


class Cat:
    def talk(self):
        print("Meow Meow....")


class Goat:
    def talk(self):
        print("Mayaah Mayaah....")

def f1(object):
    object.talk()


lst = [Duck(),Dog(),Cat(),Goat()]

for object in lst:
    f1(object)