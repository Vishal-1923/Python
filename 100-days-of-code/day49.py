# ************************************* file io **********************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/49-Day49-File-IO/.tutorial/Tutorial.md

# open : open(name_of_file, mode(read(r), write(w), appending(a), etc...))
f = open('day49_helper.txt', 'r') #right now there is no myfile.txt thus it will throw an error.
print(f) #<_io.TextIOWrapper name='day49_helper.txt' mode='r' encoding='UTF-8'> 

# in order to read/print file contents
text = f.read()
print(text)
f.close()

# we cant open a file in write mode and then later u r reading from that file.

# write vs append
# write: previous content will be overwritten by new content
# append: appends new content after previous content

'''
file modes:
1. r: read mode => opens file for reading only, if file does not exists gives error. (default mode)
2. w: write mode => opens file for writing in it only, if file does not exists, it will create it.
3. a: append mode => opens file for appending only, creates a new file, if file not exists.
4. x: create mode => creates a file and gives error if file already exists.
5. t: text mode => specify how file must be handled. t: text files, by default t is there i.e., r is same as rt i.e., read text file and w is same as wt: write a text file.
6. b: binary mode => used to handle binary files (images, pdf, etc.)
'''

# write
f = open("day49_anotherhelper.txt", 'w')
f.write("This is another helper file.")

# append
f = open("day49_anotherhelper.txt", 'a')
f.write("OK!")

# closing file
f.close()

# with : alternate way of closing file
with open('day49_anotherhelper.txt', 'r') as f: #it will automatically close the file when my job is done.
    print(f.read())
    
# this can be usefull in case u want to use file as local database.

