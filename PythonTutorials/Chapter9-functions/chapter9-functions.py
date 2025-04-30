# FUNCTIONS
# they r re-usable block of code
# when we call it, it runs the block of code present inside the function

# def -> defining the function.
def hello():
    print("hello world!")
# right now it only defined and not called.

hello()

# Naming Convention:
# 1. all lower case
# 2. multiple words, seperate them out with _ [hello_world] is hello world is my function name.

# function need to receive data, we can use placeholder for that data, those placeholder r called "Paramaters"

# function receiving couple of parameters.
def sum(num1, num2):
    print(num1 + num2)

sum(5, 2)

# arguement is the actual data when function is called.
# Functions r re-usable
sum(1, 2)
sum(10, 20)
sum(30, 40)

# function returning...
def sum(num1, num2):
    # check if recieved arg is integer or they r something else.
    if type(num1) == int and type(num2) == int:
        return num1 + num2
    else:
        print("Please provide correct nos....")
        return
        

val1 = sum(100, -100)
print(val1)

val2 = sum("ui", 98)
print(val2)

# None is neither true nor false, its just none.

# if in any case, any of the parameter is not passed, then python will give error but we can save ourselves via setting default args.
def def_arg_sum(num1 = 0, num2 = 0):
    if type(num1) == int and type(num2) == int:
        return num1 + num2
    else:
        print("Please provide correct nos....")
        return 0

val = def_arg_sum()
print(val)

# Variable args function...
def multiple_args(*args): #* is imp, args can be any word. it will make data inside function a tuple. But right now they dont have names as earlier.
    # can work this data as tuple
    print(args)
    print(type(args))
    
multiple_args()
multiple_args(1)
multiple_args(2, 3)
multiple_args("fg", 4, 5)


# kwargs - keyword arguements.
def multiple_named_args(**kwargs): # ** is imp
    # can work this data as dictionary
    print(kwargs)
    print(type(kwargs))
    
multiple_named_args()
multiple_named_args(first = 1)
multiple_named_args(first = 2, second = '3')
multiple_named_args(first = "fg", second = 4, third = 5)

# right order of args:
# def func(normal, *args, default=5, **kwargs):
