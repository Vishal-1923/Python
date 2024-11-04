# ******************************************** Constructors **********************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/58-Day58-Constructors/.tutorial/Tutorial.md

# providing self while calling is not necessory but it should be there during definition.

'''
class Person:
    name = "Vishal"
    occ = "SDE"
    
    def info(self):
        print(f"{self.name} is {self.occ}")

a = Person()
print(a.name)
a.info()
'''

# instead of doing something like this i can use a constructor
# to create a constructor, we can use __init__ keyword

'''
class Person:
    def __init__(self):
        print("Constructor called!")

# now whenever an object of Person is created, constructor will be called.
a = Person()
b = Person()
c = Person()
'''

# now we can implement name and occ here via constructor
class Person:
    def __init__(self, name, occ):
        self.name = name
        self.occ = occ
        print(f"{self.name} is {self.occ}")
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Vishal", "SDE") #by this Python has set name and occ with given values.
b = Person("Sia", "Doctor") #self is automatically passed. There r 3 params
a.info()
b.info()
# constructors are invoked whenever we create an object.

# Constructor always returns NONE.
# 2 type:
# 1. Parameterized - various param
# 2. Default - only 1 param (self)
