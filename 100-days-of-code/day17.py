# ******************** loops *************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/17-Day17-For-Loops/.tutorial/Tutorial.md

# 2 types of loops:
# 1. while loop
# 2. for loop

# for: iterate over sequence of iterable objects in Python.
# Iterable Objects:
# 1. String
# 2. list
# and many more...

name = input("Entered a name: ")

for i in name:
    print(i, end = ", ")

print("\n")

list = ["Vishal", "Krishna", "Kumar"]
for str in list:
    print(str, end = ", ")
    for i in str:
        print(i)


for k in range(10): #0-(n-1)
    print(k)

for k in range(1, 10):#starting , end
    print(k+1)

for k in range(1, 21, 2):#start, stop, jump
    print(k)