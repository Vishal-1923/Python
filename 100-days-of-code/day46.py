# *************************************** os module **************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/46-Day-46-os-Module/.tutorial/Tutorial.md

# shutil is similar to os module.

import os

if (not os.path.exists("data")): #checking if files exists.
    os.mkdir("data") #will create a directory with name data


# for i in range(0, 100):
    # os.mkdir(f"data/Day{i}") # automatically creating folders.
    # os.rename(f"data/Day{i}", f"data/Day - {i}") #renaming created folders

folders = os.listdir("data") #list down all the files
for folder in folders:
    print(folder)
    fs = os.listdir(f"data/{folder}")
    print(fs)
    for f in fs:
        os.remove(f"data/{folder}/{f}") #will remove any files present inside my day-i directory.   

cmd = "date"
os.system(cmd)

print(os.getcwd()) #to know current working directory.

# chdir : to change the directory.

f = os.open("Python/100-days-of-code/day45.py", os.O_RDONLY)

contents = os.read(f, 1024)#read upto 1024 bytes in 1 read operation.
print(contents)
os.close(f)