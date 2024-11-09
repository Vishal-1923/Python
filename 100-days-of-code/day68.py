# ***************************** Assignment 7 *******************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/68-Day-68-Exercise-7/.tutorial/Tutorial.md

'''
Write a program to clear the clutter inside a folder on your computer. You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. Do the same for other file formats. For example:

sfdsf.png --> 1.png
vfsf.png --> 2.png
this.png --> 3.png
design.png --> 4.png
name.png --> 5.png

'''

import os, random, string

if not os.path.isdir("day68_helperFolder"):
    os.mkdir("day68_helperFolder")
    # creating files
    for i in range(1, 11):
        file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + '.txt'
        file_path = os.path.join("day68_helperFolder", file_name)
        with open(file_path, 'w') as file:
                file.write('0' * 1024)
        print("Files are: ", file_name)

folderPath = os.path.join(os.getcwd(), "day68_helperFolder")
print("Folder Path right now is: ", folderPath)




# def showFiles(folderPath):
#     for file in os.listdir(folderPath):
#         print(file)

def fileRename(folderPath, fileExt):
    i = 1
    for file in os.listdir(folderPath):
        print("files ar: ", file)
        filePath = os.path.join(folderPath, file)
        print("FilePath is: ", filePath)
        newFilePath = str(i) + fileExt
        newFilePath = os.path.join(folderPath, newFilePath)
        print("New file path: ", newFilePath)
        if os.path.splitext(filePath)[1] == fileExt:
            os.rename(filePath, newFilePath)
            i += 1
        # showFiles(folderPath)

fileRename(folderPath, ".txt")