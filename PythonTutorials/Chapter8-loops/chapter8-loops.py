# There r 2 types of loops:
# 1. while loop
# 2. for loop

# WHILE LOOP
# -> will execute block of code while the condition is true

value = 1
while value <= 10: #iterated the loop 10 times.
    print(value)
    value += 1

print("")

# BREAK
# we can also exit the loop without trueing the condition, via break...
value = 1
while value <= 10: #iterated the loop 10 times.
    print(value)
    if value == 5:
        print("value reached 5, breaking!!!")
        break
    value += 1
    
# CONTINUE
value = 1
while value <= 10: #iterated the loop 10 times.
    value += 1
    if value == 5:
        print("reached 5, continue!!!")
        continue
    print(value)
else: #will only execute when while completes fully, purely, no break nothing.!!!
    print("value is now equals to " + str(value))
    

# FOR LOOP
# iterates over a sequence, sequence can be contents of a collection data type(list, tuple, dict, set) or even individual char of a string.
names = ["Dave", "Sara", "John"]
for x in names: #x represents each value out of whole.
    print(x)

for c in "Mississippi":
    print(c)

for x in names:
    if x == "Sara":
        break
    print(x)
    
for x in names:
    if x == "Sara":
        continue #stops the current iteration and goes to next one in loop.
    print(x)

# ranges...
for x in range(4): #0, 1, 2, 3
    print(x)

for x in range(2, 4): #start from 2 and ends before 4 i.e, [2, 3]
    print(x)

# modifying increment
for x in range(0, 100, 5): #now it will increment with 5 instead of 1.
    print(x)
else: #same as while
    print("Glad that's over...")

names = ['Dave', 'Sara', 'John']
actions = ['codes', 'eats', 'sleeps']

# nested loop
for name in names:
    for action in actions:
        print(name + " " + action + ".")
