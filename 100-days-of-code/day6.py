# ********************* Variables and Data types ****************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/06-Day6-Variables-and-Data-Types/.tutorial/Tutorial.md

# Variable is just like a container. This container is inside the memory.

a = 1
print(a)
# this simply means store 1 in memory and put its address in a.

b = "harry"
print(b)

# hm string k case main "" isiliey lgate hai becoz of the following
# harry = 9
# b = harry
# print(b) -> what should it print???
# "" ye pta chal gya ki ye ek value hai na ki variable.


a = 1
print(type(a))
b = "harry"
print(type(b))
c = True
print(type(c))
d = None
print(type(d))

# There r some built-in datatypes in Python:
# 1. Numeric Data: int, float, complex
a=9
print(type(a))

b= 9.9999
print(b, type(b))

c=complex(24, 5)
print(c, type(c))

# 2. Text data: string
# 3. Boolean data
# 4. Sequenced Data: list, tuple
# List: ordered collection of data with ele seperated by , and enclosed within []
#       mutable and can be manipulated/modified after creation.

list1 = [1, 3, [5,6], 90, 4.5, "bisha"]
print(list1)

# Tuple: ordered collection of data with ele seperated by , and enclosed by ()
#       immutable and can't be modified after creation

tuple1 = (1, 3, (5,6), 99, 3.3, "jio")
print(tuple1)

# 5. Mapped data : Dictionary
# unordered collection of data containing a key/value pair, enclosed in {}
dict = {"vishal:5", "ap:24"}
print(dict, type(dict))

# EVERYTHING IS AN OBJECT IN PYTHON :)
# be it int/bool/anything....print(tuple1)