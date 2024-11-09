# ********************************* Class Methods **********************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/69-Day-69-Class-Methods/.tutorial/Tutorial.md

# Class methods are bound to class and not instance of class.
# It operates on whole class rather than its instance.
# defined using @classmethod decorator, followed by function definition.
# The 1st arg of function is always cls which represents class itself.

class Employee():
    company = "apple"
    def show(self):#function is made for instance of class, most of time, method instance k lie bnta hai na ki class k lie.
        print(f"the name is {self.name} and company is {self.company}")
    def changeCompany(any, company): #it is a normal function right now, 1st arg main jo bhi obj aaya hai wo le leta hai.
        any.company = company
    @classmethod
    def changeCmp(cls, company): #1st arg as a class mil rha hai na ki instance
        cls.company = company
e1 = Employee()
e1.name = "Vishal"
e1.company = "appleI"
e1.show()
e1.changeCompany("googlr")
e1.show()
print(Employee.company)
# right now class's company has not been modified
# to modify it, make class method
e1.changeCmp("google")
e1.show()
print(Employee.company)# now it is changed