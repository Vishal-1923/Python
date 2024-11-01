# ************************* String slicing and String Operation ****************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/12-Day12-Strings-Slicing/.tutorial/Tutorial.md

# length of String
name = "vishal"
print(len(name)) # len()

# extract some part of string.
names = "Vishal, Kumar, Krishna"
print(names[0 : 6]) # names[starting index : ending index] -> 0:6 which means start from 0th index and go till 6 i.e., 5th idx.

# we can ommit starting idx if its 0
print(names[: 6])

# we can ommit ending idx too
print(names[:]) #python will treat it like 0:length of string

# -ve slicing
print(names[:-3]) #python will treat it like 0: length of string + (-3)
print(names[-4:-3]) #python will treat it like length of string + (-4) : length of string + (-3)

nm = "harry"
print(nm[-4:-2]) # 5-4 = 1 : 5-2 = 3  -> 1 to 3 ----> ar

# printing char at a specified idx.
print(names[15])

# loop through string
loop = "loop through strings"
for char in loop:
    print(char)