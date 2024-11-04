# ******************************** map, filter, reduce *********************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/53-Day53-Map-Filter-and-Reduce/.tutorial/Tutorial.md

# map, filter, reduce functions are built-in functions that allow u to apply a function to sequence of ele and return a new sequence.
# These functions are known as higher order functions as they take other function as an argument.
def cube(x):
    return x*x*x

print(cube(2))

l = [1,2, 3, 4,5]
# i want to have a list which contains all the ele having their cube.
# 1. for loop and apply cube function to each ele.
newl = []
for i in l:
    newl.append(cube(i))
print(newl)

# 2. using map
newl = list(map(cube, l)) #map will return a map object which can be converted to list.
print(newl)
newl = list(map(lambda x: x*x*x, l)) #lambda function.
print(newl) #map object is returned for efficiency purposes.

# filter
# it filters sequence of elements based on a predicate (a function which returns T/F) and returns a new sequence containing only those ele which follows the predicate.
# filter(predicate, iterable)
def filter_function(a):
    return a>4

newnewl = list(filter(filter_function, l))#returns filter object.
print(newnewl)

# reduce
# higher order funtion
# applies to a sequence but return a single value.
# part of functools module in python.
# reduce(predicate, iterable)

# 1,2,3,4,5 : function will be applied to 1,2 then function will be applied to result of 1,2 and 3 and so on.
from functools import reduce
numbers = [1,2,3,4,5]
sum = reduce(lambda x,y: x+y, numbers)
print(sum)