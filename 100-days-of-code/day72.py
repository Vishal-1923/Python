# ******************************************************* super keyword **************************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/72-Day-72-super-Keyword/.tutorial/Tutorial.md

# super is used when we want to call parent class's functions from child class.

class ParentClass():
    def parentMethod(self):
        print("this is parent method")

class ChildClass(ParentClass):
    def parentMethod(self):
        print("Vishal")
        super().parentMethod() #parent class main jao aur us method ko call kr do 
    def childMethod(self):
        print("This is child method")
        # now i want to call parent method, it distinguishes child class's parentmethod from parent class's parentmethod.
        super().parentMethod()
child = ChildClass()
child.childMethod()
child.parentMethod() #if parentmethod is not in child class then it will directly call parentmethod of parent.

# -------------------------------------------------------------------------------------------------------------------------------
class Parent():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Hi", self.name, self.age)

class Child(Parent):
    def __init__(self, name, age, lang):
        super().__init__(name, age)
        self.lang = lang
        print("Hi1", self.name, self.age, self.lang)
        
p = Parent("vishal", 22)
c = Child("Kumar", 20, "python")
