# ******************************* if-else *****************************

# used to do conditional programming. 
# or
# decision making.

# 4 diff. types of Conditional Statements:
# ->    if
# ->    if-else
# ->    if-else-elif
# ->    nested-if-else-elif

# simple if-else statement
a = int(input("Enter your age: "))
print("your age is: ", a)

if(a >= 18):
    print("Congratulations, you can drive.\n")
else:
    print("Sorry, you can not drive.\n")
    print("HI") #part of else
print("Hey") #not part of else...
# Indentation in Python is similar to {} in c/c++

# elif
applePrice = 10
budget = 200

if(budget - applePrice > 50):
    print("Alexa, add apple to bucket.")
elif(budget - applePrice > 70):
    print("Its ok u can still buy!.")
else:
    print("Alexa, dont add apple to bucket.")


# There is 1 classic error in Python i.e., jb hm module k naam s file bnate hai to wo module ko na
# dekh k file main dekhne lg jata hai to errors aati hai.

num = int(input("enter a no: "))
print("Your no is: ", num)

if(num < 0):
    print("You have entered -ve nos.")
elif(num > 0):
    if(num < 10):
        print("Your no is less than 10")
    elif(num > 10 and num < 100):
        print("Your no is in between 10 to 100")
    else:
        print("You have entered a big no.")
else:
    print("Entered 0")