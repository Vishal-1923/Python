# ******************************************** import ****************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/44-Day44-How-import-works/.tutorial/Tutorial.md

# importing in python is the process of loading code from python module into current script.
# allows us to use the functions and variables defined in module in your current script.
# also any other module may depend on some other module so u have to import both.

# importing
import math

result = math.sqrt(9) #use its function via package name followed by . and function name
print(result)


# we can even import only certain function from any package.
# from keyword
from math import sqrt
result = sqrt(16) #now only sqrt is needed.
print(result)

# importing multiple functions
from math import sqrt, pi
result = sqrt(25) * pi
print(result)

# importing everything : using * wildcard
# this is not recommended as it will import everything each function as well as each variable.
from math import *
result = sqrt(100) * pi
print(result)

# as : renaming package
# benefit: making code more readable.
import math as m
result = m.sqrt(25) * m.pi
print(result)

from math import sqrt as s

# import math vs from math import *
# as we r using any function like this (math.sqrt()) there is no confusion i.e., from where sqrt function is coming but when we do 
# from math import *, we only need to write sqrt() which will lead to confusion. so from math import * not at all recommended.

# dir : print all the functions and variables in package
import math
print(dir(math))

import day44_helper as h
print(h.vish)
print(dir(h))