# ***************************** Recursion ****************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/30-Day30-Recursion/.tutorial/Tutorial.md

# function calling a function is recursion

# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(3) = 3*2*1
# factorial(2) = 2*1
# factorial(1) = 1

# factorial(0) = 1

# thus factorial of any no lets say: f(n) = n * f(n-1)
# so in this case, we need to call same function inside itself.

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fact(n-1)

# n = int(input("enter a no: "))
# print("Factorial of ", n, " is: ", fact(n))


# Fibonacci series
def fib(n):
    if n == 0 or n == 1:
        return n

    return fib(n-1) + fib(n-2)

a = 4
for i in range(a):
    print(fib(i))
# 0 1 1 2 3