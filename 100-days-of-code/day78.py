# ******************************************************* Single Inheritance *******************************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/78-Day-78-Single-Inheritance/.tutorial/01-SingleInheritance.md

# Single inheritance is a type of inheritance where a class inherits properties and behaviors from a single parent class. This is the simplest and most common form of inheritance.

# syntax: 
# class ChildClass(ParentClass):
    # class body

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")

class Cat(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
    def make_sound(self):
        print("Meow!")
    def color(self, color):
        print("color is: ", color)




d = Animal("dog", "dog")
d.make_sound()

dg = Dog("dog", "doger")
dg.make_sound()

ct = Cat("vi", "cat")
ct.make_sound()
ct.color("black")