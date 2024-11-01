# ***************************** Assignment 4 **************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/40-Day40-Exercise-4/.tutorial/tutorial.md

# Question:
'''

Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language
Coding:
if the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting and the end else: simply reverse the string

Decoding:
if the word contains less than 3 characters, reverse it else: remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

Your program should ask whether you want to code or decode

'''

# **********************************************************************************************************************************
# Solution:
import string
import random

msg = input("Enter your message: ")
newCmsg = ""
def randChar():
    return random.choice(string.ascii_lowercase)

# encoding
def code(msg):
    newMsg = ""
    for message in msg.split():
        if len(message) < 3 and len(message) >= 0:
            cmsg = message[::-1] #using string slicing for reversing.
            newMsg = newMsg + cmsg
            newMsg = newMsg + " "
        else:
            firstL = message[0]
            cmsg = message[1:]#name->ame
            cmsg = cmsg + firstL#amen
            for i in range(0, 3):
                cmsg = cmsg + randChar()#amen...
            for i in range(0, 3):
                cmsg = randChar() + cmsg
            newMsg = newMsg + cmsg
            newMsg = newMsg + " "
    print(f"Coded message is: {newMsg}")

# decoding
def decode(msg):
    newMsg = ""
    for message in msg.split():
        if len(message) < 3 and len(message) >= 0:
            cmsg = message[::-1] #using string slicing for reversing.
            newMsg = newMsg + cmsg
            newMsg = newMsg + " "
        else:
            #removing 1st char
            message = message[3:]
            # removing last 3 char
            message = message[:-3]
            cmsg = message[len(message)-1]
            message = message[:-1]
            message = cmsg + message
            newMsg = newMsg + message + " "
    print(f"Decoded message is: {newMsg}")


ques = int(input(f"Do you want to \"Code\" or \"Decode\" the {msg} [1: decode - 0: code]? "))
if ques == 0:
    code(msg)
elif ques == 1:
    decode(msg)
else:
    print("Incorrect Choice, please enter in between 0 and 1")