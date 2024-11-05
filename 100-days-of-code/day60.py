# ********************************** getters - setters ************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/60-Day-60-Getters-and-Setters/.tutorial/Tutorial.md

# Getters: used to access the values of an object's properties.
# are typically defined via @property decorator.

class MyClass:
    def __init__(self, value): #constructor
        self.value = value
    def show(self):
        print(f"Value is {self.value}")

    # getter
    @property
    def tenTimesValue(self):
        return 10*self.value

    #setter
    @tenTimesValue.setter
    def tenTimesValue(self, val):
        self.value = val/10
        print(self.value)

obj = MyClass(10)
print(obj.tenTimesValue)
obj.tenTimesValue = 100
obj.show()

# getters and setters r usefull for encapsulation and data validation.