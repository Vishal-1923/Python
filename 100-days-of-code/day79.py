# ************************************************ Multiple Inheritance *******************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/79-Day-79-Multiple-Inheritance/.tutorial/01.Multiple%20inheritance.md

# basically we have multiple parent and through them we r making 1 single child.

class Employee:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance
    def show(self):
        print(f"The name is {self.dance}")

class EmpDancer(Employee, Dancer):#jo yaha pehle class aaya hai usi ka show method call hoga
    def __init__(self, name, dance):
        self.dance = dance
        self.name = name

e = EmpDancer("vishal", "dance")
e.show()

# mro : method resolution order
print(EmpDancer.mro())