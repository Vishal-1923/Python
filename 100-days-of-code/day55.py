# ******************************************* assignment 5 **********************************************

'''
Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water. Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.
'''

import random

def checkWin(x, y):
    if (x == 0 and y == 0) or (x == 1 and y == 1) or (x == 2 and y == 2):
        print("Match Draw!!!")
    elif ((x == 0 and y == 1) or (x == 1 and y == 2) or (x == 2 and y == 0)):
        print("User wins :)")
    else:
        print("Computer wins :(")


choice = ['snake', 'water', 'gun']
print("Hey!, Welcome to Snake-Water-Gun game!")

while True:
    print("Kindly choose in between Snake-Water-Gun[0-1-2]: ")
    userChoice = int(input())
    print(f"User's choice is: {choice[userChoice]}")
    computerChoice = random.randint(0, 2)
    print(f"Computer's choice is: {choice[computerChoice]}")

    checkWin(userChoice, computerChoice)
    
    if int(input("Do you want to play more ? (yes - 1 | no - 0) ")) == 0:
        break

print("Thanks for playing. Have a nice day!!!")