# ************************** lambda functions ********************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/52-Day52-Lambda-Functions/.tutorial/Tutorial.md

# small anonymous functions without any name

# defining a lambda function
# lambda arguments: expression

# used where a smaller function is required for a short period of time
# commonly used as arguments to a higher - order funtions such as map, filter and reduce.

# normal function to double the input
def double(x):
    return x*2

# lambda function to double the input.
doubl = lambda x: x*2
print(doubl(4))

# lambda function with multiple args:
avg = lambda x,y: (x+y)/2
print(avg(9, 7))


# lambda function is used only when u want to write 1 liner functions
# we dont want to compress large functions in lambda functions.

# Actual usecase: when we want to pass function as an argument to another function.
def appl(fx, val):
    return 6+fx(val)

print(appl(double, 3))

# print statement in lambda
lf = lambda x, y: print(f"{x} * {y} = {x*y}")
lf(3,4)