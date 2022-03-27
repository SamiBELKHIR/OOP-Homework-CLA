#Write a Python class named Rectangle constructed by a length and width and a method 
# which will compute the area of a rectangle.
class Rectangle:
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def area(self):
        print('area is ', self.length*self.width)
A=Rectangle(10, 10)
A.area()