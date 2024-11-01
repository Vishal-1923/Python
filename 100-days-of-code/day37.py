# ********************************** Finally Keyword *****************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/37-Day37-Finally-keyword/.tutorial/Tutorial.md

# used with try ..except clause
# does clean up
# always execute irrespective of error occurs or not.

# try:
#     a = [1, 2, 3, 4]
#     idx = int(input("Enter a no: "))
#     print(a[idx])
# except:
#     print("Error occured!")

# finally:
#     print("Hey!, I am always executed!!!")

# right now in this scenario, even if we remove finally, then also it will work i.e., print statement will be executed
# try:
#     a = [1, 2, 3, 4]
#     idx = int(input("Enter a no: "))
#     print(a[idx])
# except:
#     print("Error occured!")

# print("Hey!, I am always executed!!!")

# So the difference between finally and normal statement is when we r using a functions

# here finally clause will be printed even if function is returned.
# def func():
#     try:
#         a = [1, 2, 3, 4]
#         idx = int(input("Enter a no: "))
#         print(a[idx])
#         return 1
#     except:
#         print("Error occured!")
#         return 0

#     finally:
#         print("Hey!, I am always executed!!!")

# x = func()
# print("Value of function is : ", x)

# here print statement will not be printed if function is returned.
def func():
    try:
        a = [1, 2, 3, 4]
        idx = int(input("Enter a no: "))
        print(a[idx])
        return 1
    except:
        print("Error occured!")
        return 0

    print("Hey!, I am always executed!!!")

x = func()
print("Value of function is : ", x)


# so thats the use case of finally