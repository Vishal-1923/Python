# ************************************ dir(), dict() and help() methods ******************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/71-Day-71-dir-dict-and-help-methods/.tutorial/Tutorial.md

# dir() and help() are methods
# __dict__() is an attribute
# these 3 make it esy for us to understand how classes resolve various functions and executes code.

# object introspection : to see what is in the object.
# basically ek anjaan class ya kisi bhi obj. k baare main jankari leni ho to in 3 k help s kr skte hai

# ----------------------------------------------------------------------------------------------------------------------------------
# dir():returns a list  of all attributes and methods (including dunder methods) available for an object.
# usefull tool for discovering what u can do with an object.
x = [1, 2, 3]
print(dir(x))
# infact, we can understand about each and every thing that is given by dir
print(x.__add__) #if object is not there then it will give no attribute error.


# ----------------------------------------------------------------------------------------------------------------------------------
# __dict__: attribute returns a dictionary representation of an object's attributes.
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Vishal", 30)
print(p.__dict__) #basically self kr k jo bhi cheezein maine add kri hai wo dikh jaaega 

# ----------------------------------------------------------------------------------------------------------------------------------
# help(): used to get help documentation for an object, including description of its attributes and methods
# print(help(str))
print(help(Person))