# *********************************** Inheritance **************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/61-Day-61-Inheritance-in-Python/.tutorial/01-Inheritance.md

'''
When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods,this is called as inheritance.
'''
class Employee():
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"name of employee with {self.id} id is {self.name}")

    #inheritance
class Programmer(Employee):
    def showLang(self):
        print("The default lang is PYTHON!")

e1 = Employee("vishal", 21)
e1.showDetails()

e2 = Programmer("vi", 201)
e2.showDetails()
e2.showLang()

# There r various type of Inheritance:
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance