# Create a new game ---> Guess my number...
# by name its clear, it takes a name as an argument and then match the no python chosed with the no user have entered.
# If it matches, u win, else python wins and this time u also have to say winning %
import random
import sys

def start(name):
    print(f"Welcome {name}, in the Game of \"Guess my Number\"")

def guess_my_num(name):
    player_wins = 0
    python_wins = 0
    game_count = 0
    winning_streak = 0
    
    def play_guess_my_num():
        nonlocal player_wins
        nonlocal python_wins
        nonlocal game_count
        nonlocal winning_streak
        
        player_choice = int(input("\n Choose from 1, 2, 3 \n"))
        
        if player_choice not in [1, 2, 3]:
            print("Choosen number must be from range 1, 2, 3.")
            return play_guess_my_num()
        
        player = player_choice
        computer = random.choice([1, 2, 3])
        
        print(f"\n{name} choose " + str(player) + ".")
        print("\nPython choose " + str(computer) + ".")
        
        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            
            if player == computer:
                player_wins += 1
                return f"{name} win!"
            else:
                python_wins += 1
                return "Python wins!"
        
        game_result = decide_winner(player, computer)
        print(game_result)
        
        game_count += 1
        
        if game_count > 0:
            streak = (player_wins/game_count) * 100
            print(f"\n {name}'s win : {player_wins}")
            print(f"\n Python wins : {python_wins}")
            print(f"\n {name} has played {game_count} games.")
            print(f"\n {name} wining streak is {streak:.2f}%")
        
        print("\nPlay again...?")
        
        while(True):
            play_again = input("\n Y for Yes or \n Q for Quit\n")
            if play_again.lower() not in ['y', 'q']:
                continue
            else:
                break
        
        if play_again.lower() == "y":
            return play_guess_my_num()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit(f"Bye {name}! 👋")
        
    return play_guess_my_num
            


if __name__ == '__main__':   
    import argparse

    parser = argparse.ArgumentParser(
        description = "Greet person to play game."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of person who will play game."
    )

    args = parser.parse_args()

    start(args.name)
    play = guess_my_num(args.name)
    
    play()
    