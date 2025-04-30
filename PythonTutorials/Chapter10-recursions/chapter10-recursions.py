# RECURSION
# it happens when a function call itself over and over again.

def add_one(num):
    # base case
    if num >= 9:
        return num + 1
    
    total = num + 1
    print(total)
    
    # add_one(total) #will not return 10
    return add_one(total) #will return 10 

print(add_one(0))

# example
value = True

while value:
    print(value)
    value = False
    # value = 0 #will also work.

# now, value does not have to be true, it needs to just exist i.e., value = "y" will also work
value = "y"

while value:
    print(value)
    value = False
    
    
value = "y"
count = 0

while value:
    count += 1
    print(count)
    
    if count == 5:
        break
    else:
        value = 0
        continue #does using continue means "will while condition be checked or not?" --> Yes it will be checked...