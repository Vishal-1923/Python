#String Data Type

#this is Literal Assignment...
first = "Vishal"
last = "Kumar"

print(type(first)) #will print the data type of first, [class str] will be the output
print(type(first) == str) #as data type of first is str, returns true
print(isinstance(first, str)) #as first is the instance of string, returns True


#Constructor Function
pizza = str('Pepperoni')
print(type(pizza)) 
print(type(pizza) == str)
print(isinstance(pizza, str))

#Concatenation
fullname = first + " " + last
print(fullname)

#can add things here
fullname += "!"
print(fullname)

decade = str(2002)
# decade = 2002
print(type(decade)) #when u print this, it gives us str.
print(decade)

statement = "I like rock music from the " + decade + "s." #for doing so decade must be a string(either orignal one or typecasted...)
print(statement)

#multi line
multiline = '''

Hey, how are you ?                    

I was just checking in.      
                                    All Good?

'''
print(multiline)#will print it as it is.


#escaping special characters
#sentence = 'I'm back' will give error as special character is not handled well.

sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

#String Methods
print(first)
print(first.lower())#will not change original string, will return new one
print(first.upper())#same here.
print(first)

print(multiline.title())
print(multiline.replace('Good', 'ok'))
print(multiline)

print(len(multiline))
multiline += "                                                       "
multiline = "                         " + multiline
print(len(multiline))

print(len(multiline.strip())) 
print(len(multiline.lstrip())) #only remove whitespace from left
print(len(multiline.rstrip())) #only remove whitespace from right

print("")

#Build a menu
title = "menu".upper()
print(title.center(20, "=")) #centeralized menu and filled rest of space with = which we have provided.

print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("CheeseCake".ljust(16, ".") + "$4".rjust(4))

print("")

#String Index Values -- Index starts from 0.
print(first[1]) #will give 2nd character from start
print(first[0]) #will give 1st character from start
print(first[-1]) #will give last character from start

#can give range of values
print(first[1:-1]) #will not include the last char
print(first[1:]) #will start from1 and go till end.

#Some methods just returns bool
print(first.startswith("V"))
print(first.endswith("i"))

#Boolean Data Type
myVal = True    #literal assignment
x = bool(False) #constructor function
print(type(x))
print(isinstance(myVal, bool))

#Numeric Data Types
