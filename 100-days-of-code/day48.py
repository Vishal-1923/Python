# ******************************************* Local vs Global Variable *************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/48-Day48-local-vs-global-variables/.tutorial/Tutorial.md

# Varibale: is named  location in memory that stores a value.
# We can assign values to variable via =(assignment operator).
# x = 5

# Local Variable: a variable defined within a function and is only accessible within that funtion.
#                 created when function is called and destroyed when function returns.

# Global Variable: a variable that is defined outside of a function and is accessible from within any function in your code.

x = 4 #global variable
print(x)

def hello():
    y = "local" #local variable
    print(y)
    x = 5 #local variable 
    print(x)
    print("Hello Vishal!")

hello()

# print(y)#gives error as it is a local variable defined in hello function and is not accessible here.

# if u want to change global variable use global keyword
def another():
    global x
    x = 10 #doing this will change the content of global variable.
    print(x)

another()
print(x)

# generally it is recommended not to modify global variable from within function.
