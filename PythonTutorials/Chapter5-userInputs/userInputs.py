import sys 
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3
    
print(RPS(1))
print(RPS(2))
print(RPS(3))
print(RPS.ROCK)
print(RPS['ROCK'])
print(RPS.ROCK.value)
#sys.exit() #in order to exit in between of program...

#we will play rps - rock paper scissor game
value = input('Please enter a value...\n')
print(value)

print("") #empty line.....
playerChoice = input("Enter ... \n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n")

player = int(playerChoice)

if player < 1 or player > 3:
    sys.exit("Please enter value in between 1-3")

computerChoice = random.choice("123")
computer = int(computerChoice)

print("")
print("You choosed: " + str(RPS(player)).replace('RPS.', '') + ",\nPython choosed: " + str(RPS(computer)).replace('RPS.', ''))
print("")

#logic of game...
if player == 1 and computer == 3:
    print("U win :):):)")
elif player == 2 and computer == 1:
    print("U win :):):)")
elif player == 3 and computer == 2:
    print("U win :):):)")
elif player == computer:
    print("Tie ...")
else:
    print("Python wins :(:(:(")


