# modules r small code libraries that r based on related features.

import math #this is a built-in module which comes with python.
import sys
import random
# these were importing whole lib

from enum import Enum #will make only Enum available from whole enum library.

# can also create alias
import random as vis

print(math.pi)

print(random.choice("123"))

print(vis.choice("345"))

# we can see whatever options which r there in a module
# via dir()

print(dir(vis))

for item in dir(vis):
    print(item)
    
# via . notation in vs code.

# for detailed info goto python documentation

# lets experiment with my module
import exampleModule

print(exampleModule.capital)
exampleModule.randomfunfact()

# there is a special value that every module has i.e., name value.
print(__name__) #will print main as this is the module which i am runing
print(exampleModule.__name__)


from rps7 import rock_paper_scissors
rock_paper_scissors()

sys.exit() #used to exit the program...



# actually function runs automatially when module is imported becoz python actually runs the file when it is importing that file. this is python way of doing....
