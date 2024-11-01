# ****************************** Raising Custom Errors *******************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/38-Day38-Custom-Errors/.tutorial/Tutorial.md


# if we have below situation then we can raise error so that in future no logical error happens!
# although there r some cases when python will stop u itself when u r doing something wrong. like entring string instead of int
'''
val = int(input("Enter any value between 5 - 9: "))

if(val < 5 or val > 9):
    raise ValueError("Value out of range !!!")
'''

# We can infact define custom exceptions by creating a new class that is derived from built-in exception class.
'''
class CustomError(Exception):
    # code...
    pass

try:
    # code...

except CustomError:
    # code...
'''

# quiz: if user enter quit then error should not pop otherwise it should be printed.

val = input("Enter any value between 5 - 9: ")
try:
    if val.casefold() == "quit": #case insensitive comparision...
        print("Ok!!!")
    else:
        if(int(val) < 5 or int(val) > 9):
            raise ValueError("Value out of range !!!")
except Exception as e:
    print("Program halted!!!")

