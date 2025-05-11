import sys
import random
from enum import Enum

def rps(name="PlayerOne"): #we have set default value so that just in case when user name is not passed it handles that too.
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        # using parent function - rps variables
        nonlocal name
        nonlocal game_count #if at any place in this function, game_count is defined as global then we cant use nonlocal keyword becoz python evaluates function is 1 go not line by line
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            f"\n{name}, please enter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\n{name}, you choose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"Python choose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

        def decide_winner(player, computer):
            nonlocal name #experiment: what happens if we just not use nonlocal here then what happens...
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return f"🐍 Python wins!\nSorry, {name}.."

        game_result = decide_winner(player, computer)
        print(game_result)

        game_count += 1
        
        print(f"\n Game Count: {game_count}.") #fstring automatically converts expression to string
        print(f"\n {name}'s wins: {player_wins}.")
        print(f"\n Python wins: {python_wins}.")

        print(f"\nPlay again, {name}?")

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
            print(f"Thank you for playing {name}!\n")
            sys.exit(f"Bye {name}! 👋")

    return play_rps() #willl create "closure..."



if __name__ == '__main__': #will only execute if rps7.py is the main file.. so when we import this it will not automatically run but will run only when its called.
    import argparse

    parser =  argparse.ArgumentParser(
        description="Provides a personalized game experience greeting." #has set basic description for our args parser.
    )

    # metavar is just a display name if u get a msg that refers back to this args
    parser.add_argument(
        "-n", "--name", metavar="name", #dest="firstName"
        required=True, help="The name of person playing the game."
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
