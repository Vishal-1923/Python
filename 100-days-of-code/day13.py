# ************************ String Methods ************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/13-Day13-String-Methods/.tutorial/Tutorial.md

# Strings are immutable, they cant be changed inplace

a = "viShal"
print(len(a))

print(a.upper())# will not change a string but gives another string.
print(a.lower())

# striping trailing characters.
a = "!!sia!!!!!!!!!!!!!!!!"
print(a)
print(a.rstrip("!"))#will only strip rear ! and will not touch front ones.

# replace : replace all occurence of that string with another one.
print(a.replace("sia", "Kumar"))

# split : split string in list.
a = "Vishal Krishna Kumar"
print(a.split(" "))

# capitalize: 1st char ko capital and rest in small.
a = "intro to mechAnics...."
print(a.capitalize())#Intro to mechanics....

# center: move string to center
a = "Hey!, Vishal"
print(len(a))
print(len(a.center(50)))

# count: no of times a given str occurs in a string
a = "Hare Ram, Hare Ram, Ram Ram hare hare"
print(a.count("Ram"))

# endswith()
a = "Hey!, Vishal **"
print(a.endswith("**"))

a = "Hey!, Vishal **"
print(a.endswith("sh", 7, 10))
print(a.endswith("sh", 7, 11))

# find: finds 1st occurence of given value and return its index and if its not found then will return -1.
a = "Hey!, Vishal **"
print(a.find("Vishal"))
print(a.find("Viii"))

# index: finds 1st occurence of given value and return its index and if its not found then will raise an exception.
a = "Hey!, Vishal **"
print(a.index("Vishal"))
# print(a.index("Viss"))

# isalnum(): if string contains only a-z, A-Z, 0-9
a = "Hey!, Vishal **"
print(a.isalnum())
a = "Hey!, Vishal"
print(a.isalnum())

# isalpha(): if string contains only a-z, A-Z
a = "Hey!, Vishal **"
print(a.isalpha())
a = "Hey!, Vishal"
print(a.isalpha())

# islower(): returns true if all characters in string are lowercase.
a = "Hey Vishal!!!"
print(a.islower()) #false
a = "hey vishal!!!"
print(a.islower()) #true

# isprintable(): returns true if all values within given string is printable.
a = "Hi! Vishal"
print(a.isprintable()) #true

a = "Hi! Vishal\n"
print(a.isprintable()) #false

# isspace(): if string contains white spaces.
a = "   " #tab
b = "                  " #space bar
c = "vishal"
print(a.isspace()) #true
print(b.isspace()) #true
print(c.isspace()) #false

# istitle(): first letter of each word of string is capital.
a = "World Health Organization"
print(a.istitle()) #true

a = "World Health organization"
print(a.istitle()) #false

# isupper(): returns true if all characters in string are uppercase.
a = "Hey Vishal!!!"
print(a.isupper()) #false
a = "HEY!!!"
print(a.isupper()) #true

# startswith(): if string starts with given value
a = "Vishal Kumar"
print(a.startswith("vishal")) #false
print(a.startswith("Vishal")) #true

# swapcase(): uppercase -> lowercase and lowercase to uppercase
a = "VisHal KumaR"
print(a.swapcase()) #vIShAL kUMAr

# title(): capitalizes 1st letter of every word in string.
a = "Hi my name is Vishal!"
print(a.title())#Hi My Name Is Vishal!

