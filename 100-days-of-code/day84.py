# ***************************************************** Time Module *****************************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/84-Day-84-Time-Module/.tutorial/Time%20Tutorial.md

# Time module helps in various time related operations

# The time module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time conversions.


'''
time.time():
The time.time() function returns the current time as a floating-point number, representing the number of seconds since the epoch (the point in time when the time module was initialized). 
'''
import time
print(time.time())#function returns the current time as a floating-point number

t1 = time.time()
for i in range(100):
    i += 1
    print("1")
t2 = time.time()
print(t2-t1)

# time.sleep()
time.sleep(5)
print("this will be printed after 5 s")

# time.strftime()
# format time as per your need.

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)
formatted_time = time.strftime("%m-%Y-%d %H:%M:%S", t)
print(formatted_time)
print(t)