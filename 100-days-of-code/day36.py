# ********************** Exception Handling *****************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/36-Day36-Exception-Handling/.tutorial/Tutorial.md

# Exception handling is the process of responding to unwanted/unexpected events when a program runs.
# We do exception handling in order to prevent program or system to crash in such cases.

# a = input("Enter a no: ")
# print("printing multiplication table")

# for i in range(1, 11):
#     print(f"{i} X {int(a)} = {int(a)*i}")

# this will run fine but when i input a string instead of a no, it will pop an error
# ValueError: invalid literal for int() with base 10: 'vis'

# Now i know that in for loop, there is some chance of error occuring so, i will use try before that

a = input("Enter a no: ")
print("printing multiplication table")

try:
    for i in range(1, 11):
        print(f"{i} X {int(a)} = {int(a)*i}")
except Exception as e:
    print(e)

print("Some other works ")
print("Ideal program termination point.")

# what this will do is: it will print the error or u can define what to do here and it will now continue with rest of the code.
# hence code does not halt in between.
# and also if i am not using e then no need to write:
# except Exception as e: just write
# except:


# we can also handle "specific type of error too."
try:
    num = int(input("Enter a no: "))
except ValueError:
    print("Number entered is not an Integer.")

# We can even handle multiple errors via multiple except.
try:
    num = int(input("Enter a no: "))
    idx = [4, 5]
    print(idx[num])

except ValueError:
    print("Number entered is not an Integer.")

except IndexError:
    print("Not a valid index!")

