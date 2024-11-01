# assignement 2

# greet according to time.

# 6-12, 12-5, 5-8, 8-12

#  assuming time to be provided in 24hr format
'''
time = (input("enter current time: "))

# 06:34
timeStringList = time.split(":")
timeInt = int(timeStringList[0])

if(timeInt >= 6 and timeInt < 12):
    print("Right now, time is: ", timeInt % 12)
    print("Good Morning ji!")
elif(timeInt >= 12 and timeInt < 16):
    print("Right now, time is: ", timeInt if timeInt == 12 else timeInt%12)
    print("Good Afternoon ji!")
elif(timeInt >= 16 and timeInt < 20):
    print("Right now, time is: ", timeInt%12)
    print("Good Evening ji!")
else:
    print("Good Night ji!")
'''

# alternate solution: using time module of Python.

import time
timeStamp = time.strftime('%H:%M%S')
print("Time is: ", timeStamp)

timeStampHr = int(time.strftime('%H'))
print("Time is: ", timeStampHr)

timeStampMin = int(time.strftime('%M'))
print("Time is: ", timeStampMin)

timeStampSec = int(time.strftime('%S'))
print("Time is: ", timeStampSec)

if(timeStampHr >= 6 and timeStampHr < 12):
    print("Good Morning Ji!")
elif(timeStampHr >= 12 and timeStampHr < 17):
    print("Good Afternoon Ji!")
elif(timeStampHr >= 17 and timeStampHr < 21):
    print("Good Evening Ji!")
else:
    print("Good Night Ji!")