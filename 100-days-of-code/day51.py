# ******************************** seek and tell ***********************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/51-Day51-seek-and-tell-functions/.tutorial/Tutorial.md

# seek and tell are used to work with file objects and their positions within a file.

# seek: allows u to move the current position within a file to a specific point.
# That position is specified in bytes and u can either move forward or backward from that point.

with open('day51_helper.txt') as f:
    print(type(f)) #<class '_io.TextIOWrapper'>
    f.seek(10) #move to 10th byte in a file.

    data = f.read(5) #read next 5 bytes.
    print(data)


# tell: returns current position within the file in bytes
# usefull for keeping track of your location within file / for seeking to a specific position relative to current position.

with open('day51_helper.txt') as f:
    data = f.read(10) #read 1st 10 bytes.
    current_pos = f.tell()
    print(current_pos)
    current_pos = current_pos + 2
    f.seek(current_pos)
    print(f.read())
    
    
# truncate: if u want to truncate file to a specific size
with open('day51_helper.txt', 'w') as f:
    f.write("123456789")
    f.truncate(5) #only 5 chars are allowed (5bytes)
with open('day51_helper.txt') as f:
    print(f.read())