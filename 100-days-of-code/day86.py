# ******************************************************* Walrus Operator **********************************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/86-Day-86-Walrus-Operator/.tutorial/Tutorial.md

# new update 3.8 onwards.

# in other programming languages we can do assignment within an expression. but in Python we cant, until 3.8

a = True
# print(a = False) #error
print(a := False) # : is an walrus operator which makes it possible to do assignment within an expression

numbers = [1, 2, 3, 4, 5]
while( n := len(numbers) > 0): #len(numbers) is calculated and then assigned to n which is then evaluated with > 0
    print(numbers.pop())



# assigns values to variables as part of a larger expression

# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

foods = list()
while (food := input("What food do u like?: ") != "quit"):
    foods.append(food)