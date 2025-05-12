# print(x) this will give error -> NameError -> name x is not defined.
# this is also an exception

# w3schools --> python built in exceptions...
# in python we raise exceptions.

# we can also create our own custom exceptions...

# print(x) will raise error so lets handle it 
# we do so via
# try except block
try:
    print(x)
# except:
#     # this is more or less more generic thing i.e., it will catch all of the errors.
#     print("There is an error")
except NameError: #only catch name error
    print("There is a Name Error, something is probably undefined")


# #######################################
y = 2
try:
    print(y/0)
except NameError:
    # as this is / by 0 error thus it will not be catched via name error.
    print("Name error")
except ZeroDivisionError:
    print('Please do not divide by 0')
except:
    # everything is caught here...
    print("There is an error")
else:
    # only reach here if there r no errors
    print("HeHe no error :)")
finally:
    # whether there r errors or not this will reach here...
    print("I am going to print with or without error")


# raising our error
x = 2
try:
    if not type(x) is str:
        raise TypeError("Only strings r allowed..\n")
except Exception as error:
    print(error)

x = 2
try:
    raise Exception("I'm a custom exception..\n")
except Exception as error:
    print(error)
    
# with our own error
class JustNotCoolError(Exception):
    pass

x = 5
try:
    raise JustNotCoolError("This is just not cool man!!!")
except Exception as error:
    print(error)