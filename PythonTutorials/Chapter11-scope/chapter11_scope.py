# There r diff types of scope:
# 1. Global Scope --> available to everyone in the file.
# *********************************************************************
name = "Vishal"

def greeting():
    print(name) #name is available here as it is in "Global Scope"

greeting()

# Never use Global Variable un-necessarily.
# *********************************************************************

# 2. local scope --> available only at that block
# *********************************************************************
def anotherGreet(firstName): #here firstName is in "Local Scope"
    print(firstName)

# as firstName is in Local Scope, we cant access it here... or anywhere except its own block which in this case is function anotherGreet

anotherGreet("Vishal")
# *********************************************************************

# who wins ??? [Global vs Local]
# *********************************************************************
name = "Vishal"

def greeting(name):
    print(name) #Local Scope wins in these cases.....

greeting("VK Kumar")
# *********************************************************************

# local - global does not limit themselves with variables, they apple to functions as well.
# *********************************************************************
def another():
    color = "nylon"
    
    def greeting(name): #now this greeeting is in Local Scope of function another and hence cant be used outside the block of another.
        print(color)
        print(name)
    
    greeting("Vishzzz")

another()

# *********************************************************************


# POLLUTING GLOBAL SCOPE

# always put things in global scope if and only if its required.
# if not, put it in Local Scope, as it creates confusion when working with other devlopers and may cause errors.

# modifying global value 
count = 1

def show():
    #count = 2 #creating a new variable - local scope

    #count += 1 #error as there was no count previously defined inside local scope and hence it is trying modifying global variable, but thats not correct.

    # global count += 1 #this is also not the correct way, we cant do this in 1 line as 
    # global count is a decleration and not an expression or statement which can be combined with operations like +=.
    # we first declare or tell python that i am refering to global count
    # and then modifying it.

    global count #this is the correct way.
    count += 1

    print(count)
    
    # this also works for nested functions too, but the keyword there we use is "nonlocal"
    
    color = "green"
    def nested_show():
        #print(color) #will give error as python parses entire function at once and it sees color as nonlocal and u r using it before its decleration thus error.
        nonlocal color
        color = "orange"
        print(color)
    nested_show()
    print(color)

show()

print(count)