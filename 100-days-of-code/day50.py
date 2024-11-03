# **************************** read, readlines() and other functions ********************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/50-Day50-read-readlines-and-other-methods/.tutorial/Tutorial.md

# readlines: reads a single line from file
# f = open("day50_helper.txt")
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

f = open("day50_helper.txt")
while True:
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])# these marks are right now a string,so they need a typecasting.
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks in students in Maths are: {m1}")
    print(f"Marks in students in Science are: {m2}")
    print(f"Marks in students in Eng are: {m3}")
    print(line)


# writeline(): write a sequence of strings to a file.
f = open("day50_anotherhelper.txt", 'w')
lines = ['line1\n', 'line2\n', 'line3\n'] #lines jo ki iterable object hai iske sare ele ko 1 by 1 us file main chipka dega.
f.writelines(lines)
f.close()
# writelines() do not add newline characters between strings in sequence, we have to do it manually.

