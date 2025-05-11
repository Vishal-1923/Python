from functools import reduce #required for reduce.


# lambda function is a single expression that returns a value 

lambda num : num * num #thats how u define a lambda... although we r not returning a value but it will return a value

# we cant call it via name as its an anonymous function.

# but we can safely assign lambda to a variable.

squared = lambda num : num * num

# above lambda expression is same as 
# def squared(num): return num * num

print(squared)
print(squared(2))

addTwo = lambda num : num + 2
print(addTwo(1))

# lambda can also except more than 1 param
sum_of_two = lambda a, b: a+b
print(sum_of_two(1, 2))

# #############################################
# when would i use one?
# they r most often used inside another function, basically a quick function, which u dont want later. This makes them very powerfull tool.

# here lambda acts as a function builder.
def funcBuilder(x):
    # return a lambda function
    return lambda num : num + x #closure

# we will use this function to build another function.

addTen = funcBuilder(3) #returns lambda function
print(addTen(10)) #lambda func is called.
# here 3 is x and 10 is num

# ####################################
# What is a higher order function
# Function which takes 1 or more functions as arguements or a function which returns a function as its result.
# so here funcBuilder is also a higher order function...
# so closure is created by a higher order function

# there r pre-defined functions built in python...
# 1. map
# 2. filter
# 2. reduce


# List, Tuple, Dictionary, Set all r diff diff data collections.

numbers = [1, 2, 3, 4, 5, 6, 7]
# 1st arg -> function
# 2nd arg -> data collection
squared_num = map(lambda num : num * num, numbers)
# it will not be essentially a list
print(list(squared_num))

# ########################################
is_odd = filter(lambda num : num % 2 != 0, numbers)
print(list(is_odd))
# lambda was returning true/false so filter actually filtered out those values which were true.

# ########################################
# reduce can be complex function but at its very lowest is a function which adds all (everything together) 

# reduce accepts a fuction with 2 param
# 1. sub-total -> an accumulator
# 2. curr -> curr value/item.

# we can also give a starting num 
total = reduce(lambda acc, curr : acc + curr, numbers, 10)
print(total) #reduce returns an int value.

# we can do that via a simple built-in function sum
# can do that via sum too - give a starting number
print(sum(numbers, 20))


# another example for reduce.
names = ['Dave', 'Gray', 'Python']
total_char = reduce(lambda acc, curr : acc + len(curr), names, 0) #here starting number is necessary as we r originally dealing with char... this error will come - TypeError: can only concatenate str (not "int") to str
# basically reduce things this as string and will think of adding int to it thus we give 0 or starting num.

# phir bhi ise thoda dekh lio dngh s ise....

print(total_char)