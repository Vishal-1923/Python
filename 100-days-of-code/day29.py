# ************************** Docstring and PEP8 ***********************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/tree/main/29-Day29-Docstrings/.tutorial

# Python docstrings are string literals that appear right after the definition of function, method, class or module.

def square(n):
    '''Takes in a number n, returns the squeare of n'''
    print(n**2)
square(5)
print(square.__doc__) #printing docstring using this.
# here doc is an attribute 
#docstrings are not ignored via Python as in case of comments.
# docstrings are written just before the function body.
# chaging docstring can change the output of the program but changing commments cant.

def square(n):
    print(n)
    '''Takes in a number n, returns the squeare of n'''
    print(n**2)
square(5)
print(square.__doc__) #now there is no docstring. becoz only place they can exist is just before function body.
# basically it will print none.

# PEP8 - Python Enhancement Proposal
# a doc which provides guidelines and best practices to write a python code.
# main focus of it is to improve readability and consistency of Python program.

# PEP is a doc that describes new features proposed for Python and doc aspect of Python like design and style for community.

# Zen of Python
# when we import this -> Python imports Zen of Python 
# This is basically a poem written by Tim Peters
# This will more sense when u r at intermediate stage.

# import this
