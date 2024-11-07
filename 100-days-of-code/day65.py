# ******************************* Static Methods ******************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/65-Day-65-Static-Methods/.tutorial/Tutorial.md

# These methods neither belong to class nor to instance.
# ye tb use kia jata hai jb hme class k instance ki jrurat hi na ho

# methods within a class that dont require access to instance(self) or class(cls) attributes.
# are created using @staticmethod decorator
# can be called on class itself as well as on instance.

# Characteristics:
# 1. dont modify class or instance state.
# 2. behave like normal functions but r logically related to class.
# 3. used as UTILITY FUNCTIONS that perform an action related to class but dont need data from instances.

class Maths:
    @staticmethod
    def add(a, b):
        print(a+b)

a = Maths()
a.add(5, 4)
Maths.add(8, 7)

# When to use Static Methods.
# 1. When methods logic is related to class but does not need to access/modify class/instance data.
# 2. when u want to create UTILITY FUNCTIONS that logically belong to class.

# Q there is no need to use self in defining class. As u can see in case of static method we have no self.