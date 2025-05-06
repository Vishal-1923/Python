# import sys 
# import random
# from enum import Enum

# def play_rps(playAgain):

#     if playAgain == 'Q' or playAgain == 'q': #if playAgain.lower() == q
#             playAgain = False
#             print("Thanks for playing...")
#             return
#     else:

#         class RPS(Enum):
#             ROCK = 1
#             PAPER = 2
#             SCISSOR = 3

#         print("") #empty line.....
#         playerChoice = input("Enter ... \n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n")
        
#         player = int(playerChoice)
#         if player < 1 or player > 3:
#             sys.exit("Please enter value in between 1-3")
        
#         computerChoice = random.choice("123")
#         computer = int(computerChoice)
        
#         print("")
#         print("You choosed: " + str(RPS(player)).replace('RPS.', '') + ",\nPython choosed: " + str(RPS(computer)).replace('RPS.', ''))
#         print("")
        
#         #logic of game...
#         if player == 1 and computer == 3:
#             print("U win :):):)")
#         elif player == 2 and computer == 1:
#             print("U win :):):)")
#         elif player == 3 and computer == 2:
#             print("U win :):):)")
#         elif player == computer:
#             print("Tie ...")
#         else:
#             print("Python wins :(:(:(")

#         playAgain = input("\nPlay again? \nY for Yes or \nQ to quit \n\n")

#         play_rps(playAgain)


# # sys.exit("Bye!!!")

# play_rps(True)

# #########################################################

import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        # using parent function - rps variables
        nonlocal game_count #if at any place in this function, game_count is defined as global then we cant use nonlocal keyword becoz python evaluates function is 1 go not line by line
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            "\nEnter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print("You must enter 1, 2, or 3.")
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\nYou chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return "🎉 You win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "🎉 You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "🎉 You win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return "🐍 Python wins!"

        game_result = decide_winner(player, computer)
        print(game_result)

        game_count += 1
        
        print(f"\n Game Count: {str(game_count)}.")
        print(f"\n Player wins: {str(player_wins)}.")
        print(f"\n Python wins: {str(python_wins)}.")

        print("\nPlay again?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit("Bye! 👋")

    return play_rps() #willl create "closure..."


rock_paper_scissors = rps()

if __name__ == '__main__': #will only execute if rps7.py is the main file.. so when we import this it will not automatically run but will run only when its called.
    rock_paper_scissors()
