# ************************* taking user input ******************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/10-Day10-Taking-User-Input/.tutorial/Tutorial.md

# Input in python is taken via "input" function.

a = input()
print(a) #will take input and will print it.
print("My name is ", a)

# to display any message while taking input
b = input("Enter your name: ")
print("My name is ", b)


x = input("Enter 1st no.: ")
y = input("Enter 2nd no.: ")
print(x + y) # again input() returns a string thus need to typecaste it 

x = int(input("Enter 1st no.: "))
y = int(input("Enter 2nd no.: "))
print(x + y)


# Arithmetic Operations - user input

a = int(input("Enter your 1st no.: "))
b = int(input("Enter your 2nd no.: "))

# Sum
print("Sum of ", a, " and ", b, " is: ", a + b)

# Subtract
print("Subtraction of ", a, " and ", b, " is: ", a - b)

# Multiply
print("Product of ", a, " and ", b, " is: ", a * b)

# Division
print("Division of ", a, " and ", b, " is: ", a / b)

# Remainder
print("Remainder of ", a, " and ", b, " is: ", a % b)

# Floor Division 
print("Floor Division of ", a, " and ", b, " is: ", a // b)

# Exponent
print("Power of ", a, " and ", b, " is: ", a ** b)