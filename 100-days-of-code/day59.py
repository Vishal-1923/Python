# *************************************** decorators **********************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/59-Day-59-Decorators-in-Python/.tutorial/Tutorial.md

# it takes a function modifies it and returns back the function.

def hello():
    print("Helloo World!")

hello()

# wrtie now what will happen is, Helloo World! will be printed.

# but lets suppose u want that this func. should greed before and after doing its work.
# then how will u do it.
# u'll say we'll modify the function itself but lets say there r n no of such functions. then what will u do?
# Will u modify ech and every function??

# No! we will use decorators.

# def greet(fx):
#     def mfx():
#         print("Good Morning!")
#         fx()
#         print("Thanks for using this function!")
#     return mfx

# either do this

# @greet
# def hello():
#     print("Hello World!")

# hello()

# or do this

'''
def hello():
    print("Hello World!")

greet(hello)()
'''

# What if i want to decorate a function which has some parameters??
# we'll use args and kwargs

def greet(fx):
    def mfx(*args, **kwargs): #args : jitne bhi args hai unhe lene ka trika hai as a tuple || kwargs: un args ko as a dictionary lene ka trika hai (key-value) pair.
        print("Hello World!")
        fx(*args, **kwargs)
        print("Bye!")
    return mfx

@greet
def hello(a, b):
    print("HI", a+b)

hello(3, 5)
