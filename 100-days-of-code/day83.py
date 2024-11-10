# ***************************************** Assignment 9 ********************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/83-Day-83-Exercise-9/.tutorial/Tutorial.md

'''
Write a program to pronounce list of names using win32 API. If you are given a list l as follows:

l = ["Rahul", "Nishant", "Harry"]
Your program should pronouce:

Shoutout to Rahul
Shoutout to Nishant
Shoutout to Harry
Note: If you are not using windows, try to figure out how to do the same thing using some other package
'''

import subprocess

def pronounce(names):
    for name in names:
        name = "Shoutout to " + name
        subprocess.run(['espeak', name])

# Example usage
names = ["Rahul", "Nishant", "Harry", "Sia", "AP", "Anjali", "Vishal"]
pronounce(names)
