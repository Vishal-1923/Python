import os

# very usefull acronym
# r ---> Read
# a ---> Append
# w ---> Write
# x ---> Create

# Read - error if it does not exist
f = open("names.txt") # f here holds the file

# actually above is very short form of command as there r many things happening as by default.

# f = open("names.txt", "r") #read and if u not specify this, by default it is read mode only

# f = open("names.txt", "rt") #t means text file and it is also the by default value, b is for binary file

# f = open("names.txt") : this simply means open a file named names.txt with read mode and it is a text file

# 1. to read entire file
# print(f.read())

# 2. to read 1st 4 char
# print(f.read(4))

# NOTE: if i 1st do f.read() and then f.read(4) then later will not lead to any output as we r already at end of file due to courtsey of f.read().

# 3. to read an entire line
# print(f.readline())

# print(f.readline()) #this will automatically print the next line

# when u read the file, u r actually moving through the file and eventually reach at the end of file.

# 4. loop through each line of the file.
for line in f:
    print(line)


# NOTE: Whenever u open file with open, u must close the file via close()

# 5. close 
f.close()
# Closing a file is v imp as:
# 1. frees up system resources. file descriptors
# 2. flushes write buffers, when u write to a file it is temporary stored in memory, it is flushed to file upon closing only.
# 3. avoids file locks, some os locks file while they r open so if u not close that file that is an issue.

# 6. open file which does not exists

# this one is not correct as if error is raised then there is nothing in v and hence we r closing a file which is not being opened
#
# try:
    # v = open("Vishal.txt")
    # print(v.read())
# except:
    # print("File does not exists...")
# finally:
    # v.close()
#

# this is the correct way
file = None
try:
    file = open("Vishal.txt")
    print(file.read())
except:
    print("File does not exists...")
finally:
    if file:
        file.close()

print()

# what if it exists...
file = None
try:
    file = open("names.txt")
    print(file.read())
except:
    print("\nFile does not exists...")
finally:
    if file:
        file.close()

print()

# appending to file
# Append - creates the file if it doesn't exists...
file = open("names.txt", "a") # a stands for append mode.
file.write("\nVishal")
file.close()

file = open("names.txt")
print(file.read())
file.close()

# Write - creates the file if it doesn't exists...
file = open("context.txt", "w")
file.write("\nI have deleted all the prev ctx.") #write will erase everything and write fresh
file.close()

file = open("context.txt")
print(file.read())
file.close()

# Ways to create a new file...
# 1. opens a file for writing, creates the file if it does not exists.
f = open("Krish.txt", "w")
f.close()

# 2. creates a specified file, but returns an error if the file exists.
# so we need to check if that file exists or not...
# we will use os module.
if not os.path.exists("ap.txt"): #if ap does not exists then
    file = open("ap.txt", "x") # x -> create
    file.close()

# delete a file
# avoid an error if it does not exists.
if os.path.exists("ap.txt"):
    os.remove("ap.txt")
    print("file deleted")
else:
    print("The file does not exists...")


# people tend to use with instead of try except finally block
with open("more_names.txt") as file:
    content = file.read()

with open("context.txt", "w") as file:
    file.write(content)

# with is generally used as:
# 1. it automatically handles opening file - closing file(even when error occurs). although error is shown and can be handled it just means that there is no resource leak and file is safely closed...