# ******************** Function Arguement ***********************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/21-Day-21-Function-Arguments/.tutorial/Tutorial.md

# 4 types of arguements which we can provide to functions:
# 1. default arguements
# 2. keyword arguements
# 3. variable length arguements
# 4. required arguements

# Required Arguements
def average(a, b): #here a and b are required args.
    print("Average is: ", (a+b)/2)

average(4,6)

# Default arguements
def defargavg(a = 9, b = 1):#here a's default value is 9 and b's default value is 1
    print("Average is: ", (a+b)/2)

defargavg()#will continue with default values
defargavg(1, 5)#now it will ignore default values and carry operation with these values
defargavg(6)#b's default value will be considered.
# defargavg(, 8) : will cause error only last value can taken for default.
# but we can do like this
defargavg(b=5) #now it knows whom's default value it needs to consider.

# Keyword arguements
average(b=9, a = 10)# we have to pass it like key = value, thus order of arguements also not matters.


# Variable Length Arguements.
def averageVar(*numbers):
    print(type(numbers))#here numbers is considered as Tuple
    sum = 0
    for i in numbers:
        sum = sum + i
    print("the var avg is: ", sum/len(numbers))

averageVar(4,5,6)

# Keyword Arbitary Arguements ----> ise dictionary pdhne k baad dubara dekhenge.
# it will take arguements as dictionary.
def name(**name):
    print(type(name))
    print("Hello!, ", name["fname"], name["mname"], name["lname"])

name(mname = "Buchaan", lname = "Barnes", fname = "James")

# we can also return values from function
def averageVar(*numbers):
    print(type(numbers))#here numbers is considered as Tuple
    sum = 0
    for i in numbers:
        sum = sum + i
    return( sum/len(numbers))

print("Value is: ", averageVar(4,5,99))