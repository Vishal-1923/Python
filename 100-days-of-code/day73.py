# ****************************************************** Magic/Dunder Methods ***********************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/73-Day-73-MagicDunder-Methods/.tutorial/Tutorial.md

# special methods which start from __
# hm ise kbhi iske naam s call ni krte but ye ho jate hai call jaise ki __init__ method and __len__ method
# purpose is to do some special work
class Employee():
    name = "vishal"
    def __len__(self):#by calling len(), __len__() will be called. Thus they r called "MAGIC METHOD"
        i = 0
        for c in self.name:
            i += 1
        return i
    def __str__(self):
        return f"This class is named as Vishal"
    def __repr__(self):
        return f"Employee('{self.name}')"
    def __call__(self):
        print("Hey! this is call")
e = Employee()
print(e.name)
print(len(e))
print(e) #if we want to know about an object of class then we can do like this, originally it would print something rubbish(<__main__.Employee object at 0x772b8de5bfa0>). and via using str we can print desired info about class instead of this.

# str: used when u want to print out an object.
# repr: used when u want to get a string representation of an object that can be used to recreate  the object.
# it would fallback to repr if str is not there and if repr is also not there then it would print default info.
# repr: represents obj k us triko ko jisse ise recreate kia ja skta hai 

print(str(e))
print(repr(e)) #hm Employee('vishal') is trike s ise recreate kr skte hai
e()