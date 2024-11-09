# ****************************************** Classes and Objects ***************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/tree/main/57-Day57-Classes-and-Objects/.tutorial

# Class is a blueprint/template for creating objects, providing initial values for state(member variables/attributes) and implementation of behaviour(member functions or methods).
# these user defined objects are created using class keywords.

class Person:
    name = "Vishal"
    occupation = "SDE"
    networth = 10
    def info(self):#self is a keyword: reference to current instance of class, used to access variables that belongs to class.It must be provided as extra parameter inside method defn.
        print(f"{self.name} is {self.occupation}")
# wo object jiske lie ye method call kia jaa rha hai <--- self
# to create a person object
a = Person()
print(a.name, "->", a.occupation, "->", a.networth)
a.info()
a.name = "Kumar"
a.occupation = "CA"
print(a.name, "->", a.occupation, "->", a.networth)
a.info()