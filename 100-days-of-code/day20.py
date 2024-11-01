# *************************** Functions ********************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/20-Day20-Functions/.tutorial/01%20Functions.md

# Functions are used to separate logic from main program

# Function is a block of code that performs a specific task whenever it is called

# 2 types:
# 1. user - defined functions : def likhna pdta hai 
# 2. built - in functions : no need to use def

'''
a = int(input("Enter a no: "))
b = int(input("Enter another no: "))

calc1 = a*b/(a+b)
print(calc1)

c = int(input("Enter a no: "))
d = int(input("Enter another no: "))
calc2 = c*d/(c+d)
print(calc2)
'''

# How many times will we repeat it.
# just make a function and use it

def cal(a, b):
    return a*b/(a+b)

a = int(input("Enter a no: "))
b = int(input("Enter another no: "))
print("Value obtained is: ", cal(a, b))

def calc(a, b):
    pass
# this means ki ye function main baad main likhunga kuch krne ki jrurat ni hai Python ko.
# basically go ahead and process rest code.