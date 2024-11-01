
# ******************************* Enumerate function ***********************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/42-Day-42-Enumerate/.tutorial/Tutorial.md

# built-in function.
# loops over a sequence such as lists, tuple, string.
# gets index and value of each element in sequence.

# we have to write this much without enumerator
marks = [1, 4, 5, 7, 44, 66, 77, 88, 33, 99]
index = 0
for i in marks:
    if index == 4:
        print(i)
    i+=1

# with enumerator
for i, mark in enumerate(marks):
    if i == 5:
        print(mark)


fruits = ["apple", "mango", "lichy"]
for index, fruit in enumerate(fruits):
    print(index, fruit)


# basically, enumerate gives or returns tuple
for v in enumerate(fruits):
    print(type(v))
    print(v[0], v[1])

# and when u write it in pair, we r basically unpacking the tuple.

# bydefault it starts from 0 but we can change its starting position by passing it as args in enumerate function
for index, fruit in enumerate(fruits, start=2):
    print(index, fruit) #here it has now started from 2nd index instead of 0