# ******************************* access specifiers *********************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/tree/main/62-Day-62-Access-Specifiers/.tutorial

# There is no such thing as public, private, protected in Python.But still we talk about them.How?
# Access Specifiers / Access Modifiers in python are used to limit the access of class variable and class methods outside of class while implementing the concept of inheritance.

# By default variables of a class are PUBLIC.
# but we can make them as PRIVATE too
# Public: bahar s access kr skte hai
# PRIVATE: bahar s access ni kr skte 
# PROTECTED: class k andr s kr skte hai aur sub class (child class) s

# PUBLIC:
# Any instance variable in class followed by self (self.name) are publically accessed

class Student:
    # constructor
    def __init__(self, age, name):
        self.age = age
        self.name = name
obj = Student(30, "vishal")
print(obj.name, "->", obj.age)


# PRIVATE:
# only accessible inside and not from outside of class 
'''
In Python, there is no strict concept of "private" access modifiers like in some other programming languages. 
However, a convention has been established to indicate that a variable or method should be considered private by prefixing its name with a double underscore (__). 
This is known as a "weak internal use indicator" and it is a convention only, not a strict rule. 
Code outside the class can still access these "private" variables and methods, but it is generally understood that they should not be accessed or modified.
'''
class Student:
    # constructor
    def __init__(self, age, name):
        self.__age = age
        self.name = name
obj = Student(30, "vishal")
# print(obj.name, "->", obj.age)#error in accessing age.
# but we can still access it. 
print(obj._Student__age) #like this we can access it.

# yaha Python n dekha ki __ hai to usne mangling kr di simple.
# This is called Name Mangling in Python
# Name Mangling
# they r used to protect class - private and super-class private attributes from being accidently overwritten by subclasses.
# Name of class private attributes are transformed by addition of a single leading underscore.
# Name of super class private attributes are transformed by addition of a double leading underscore.
# So basically age has been changed to _Student__age and u can access it with this name only but not with age.



# PROTECTED
'''
 In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_). For example, if a class has a method called _my_method, it is indicating that the method should only be accessed by the class itself and its subclasses.
'''
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)
print(obj._funName())
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName()) 
# here name mangling is not done.

# Python kuch enforce ni krta, these r all conventions.