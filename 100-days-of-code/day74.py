# ********************************************* Method Overriding ***********************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/74-Day-74-Method-Overriding/.tutorial/Tutorial.md

# Method Overriding is a way to change the method of parent class in child class.
import math
class Shape():
    def __init__(self, len, width):
        self.len = len
        self.width = width
    def area(self):
        print("Area : ", self.len * self.width)
class Circle(Shape):
    def __init__(self):
        print("constructor")
    def area(self, rad):
        print("Area of Child: ", math.pi * rad * rad)
s = Shape(3, 4)
s.area()
c = Circle()
c.area(4)

# here i have over-ride area method.