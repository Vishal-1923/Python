# ************************** Instance Variables and Class Varibales ***********************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/66-Day-66-Instance-vs-Class-variables/.tutorial/Tutorial.md

'''
Class Variables:
-> Class variables are defined at the class level and are shared among all instances of the class.
-> They are defined outside of any method and are usually used to store information that is common to all instances of the class.
can store no of instances that had been created.
-> they are accessed using ClassName.
'''
class Example:
    cmpName = "apple"
    no_of_instances = 0
    def __init__(self):
        Example.no_of_instances += 1
        self.no_of_instances += 1#we can do like this too.
    def showInfo(self):
        print(f"No of instances are: {Example.no_of_instances}")
        print(f"No of instances are: {self.cmpName}") #self s krenge to apple india wala change dikhega but class name s access krne p ni dikhega
        # 1 more explaination: kyunki ex1 ka instance variable tha cmpName isiliey ye print hua ex2 ni tha to apple print hua.

ex1 = Example()
ex1.cmpName = "apple india"
ex2 = Example()
ex1.showInfo()
ex2.showInfo()


'''
Instance Variable
-> Instance variables are defined at the instance level and are unique to each instance of the class.
-> They are defined inside the init method and are usually used to store information that is specific to each instance of the class.
-> accessed using self
'''
class Employee():
    def __init__(self, name):
        self.name = name
    
    def showInfo(self):
        print(f"Info is: {self.name}")

ex1 = Employee("Vishal")
ex2 = Employee("Kumar")
ex1.showInfo()
ex2.showInfo()#actually this is converted to below line.
# or
Employee.showInfo(ex1)

'''
 class variables are shared among all instances of a class and are used to store information that is common to all instances. Instance variables are unique to each instance of a class and are used to store information that is specific to each instance.
'''