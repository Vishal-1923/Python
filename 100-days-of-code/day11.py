# ************************ Strings *********************************



# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/11-Day11-Strings/.tutorial/01-string_methods.md

# anything enclosed inside ""/'' is a string

name = "Vishal" #string
friend = 'Kumar' #string

print("He said, \"I want to eat an apple\"") #1way

print('He said, "I want to eat an apple"') #2way


# multi-line string -> """ """ or ''' '''
print("""Hi, 
vishal
I am
your
new friend""")#it'll print in same way.

# as string is a sequence or like array of characters. Indexing starts from 0

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

# Looping through strings
print("\n")
for character in name:
    print(character)