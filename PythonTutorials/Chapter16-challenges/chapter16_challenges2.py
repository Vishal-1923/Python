# nothing fancy just club the 2 games.
# basically welcome user with name
# give them choice to play certain game
# after they close the game, they must come back to game options

# *********************************************************************************************************


def start(name):
    print("")
    print("**********************************************************************************************")
    print("************************************* ARCADE *************************************************")
    print("**********************************************************************************************")
    print(f"Hi {name}!!!, \nWelcome to the Arcade.\nHere are the list of Games that you can play: \n1. Rock-Paper-Scissors \n2. Guess Number \n")

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