# ****************************************** class methods as alternate constructors ***********************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/70-Day-70-Class-methods-as-alternative-constructors/.tutorial/Tutorial.md

# Sometimes we have data in certain format, and if we pass constructor this data in wrong format then it may give error. Thus we have to parse data and then we pass that parsed data to contructor. 
# This can be solved via using class methods as alternative constructor.

class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, nameData):
        return cls(nameData.split("-")[0], nameData.split("-")[1])

e1 = Employee("Vishal", 12000)
print(e1.name)
print(e1.salary)

# suppose we have data in format of name-salary then how will u pass it to constructor

nameData = "John-15000"
e2 = Employee(nameData.split("-")[0], nameData.split("-")[1])
print(e2.name)
print(e2.salary)

# but this is not advisable as suppose we have to make multiple instances then if we have to do so much then it will make code ugly.
# and code repetition will be there.
# so yaha diff format main data hai to use handle kaise krein??
nameData = "Kumar-105000"
e3 = Employee.fromStr(nameData)
print(e3.name)
print(e3.salary)
