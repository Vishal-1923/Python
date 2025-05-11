# nothing fancy just club the 2 games.
# basically welcome user with name
# give them choice to play certain game
# after they close the game, they must come back to game options

# *********************************************************************************************************
import sys
from chapter16_challenges import guess_my_num

def game_selector(choice, name):
    if choice == 1:
        print(f"\nHang on {name}, taking you to \"Rock-Paper-Scissors game\". \n")
        run_game = guess_my_num(name)
        run_game()
        
    elif choice == 2:
        print(f"\nHang on {name}, taking you to \"Guess Number\" game. \n")
        run_game = guess_my_num(name)
        run_game()

def start(name):
    print("")
    print("**********************************************************************************************")
    print("************************************* ARCADE *************************************************")
    print("**********************************************************************************************")
    print(f"Hi {name}!!!, \nWelcome to the Arcade.\nHere are the list of Games that you can play: \n1. Rock-Paper-Scissors \n2. Guess Number \n")
    
    playerChoice = int(input(f"{name}, please enter your game choice...\n"))
    
    while(True):
        if playerChoice not in [1, 2]:
            print(f"{name}, you have enter wrong choice, please choose from [1, 2]. \n")
        else:
            game_selector(playerChoice, name)
            break
    
    while True:
        play_again = input(f"\n{name}, do you wanna play again?\nY for yes. \nQ to quit.")
        if play_again.lower() not in ['y', 'q']:
            print(f"\n{name}, please enter correct choice.")
            continue
        else:
            break
    
    if play_again == "y":
        start(name)
    else:
        print("\n🎉🎉🎉🎉")
        sys.exit(f"Bye {name}! 👋")

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="Welcome to the Arcade. Nice to have you on board!!!"
    )

    parser.add_argument(
        '-n', "--name", metavar="name",
        required=True, help="Player's name"
    )

    args = parser.parse_args()

    start(args.name)