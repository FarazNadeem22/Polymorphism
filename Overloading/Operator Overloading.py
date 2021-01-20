class Book:
    def __init__(self, pages):
        self.pages = pages

    # def __add__(self, other):
    #     return self.pages + other.pages

    def __add__(self, other):
        object = Book(self.pages+other.pages)
        return object

    def display(self):
        print(self.pages)
    # def __str__(self):
    #     return self.pages

b1 = Book(100)
b2 = Book(100)
b3 = Book(200)

print(b1+b2)
print("*"*50)
pages = b1+b2+b3
print(pages.pages)
pages.display()
