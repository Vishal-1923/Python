# Closure - function having access to the scope of its parent function after parent function has returned.

# understand it with an example...
def parent_function(person):
    coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left. ")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left. ")
        else:
            print("\n" + person + " has no coins left. ")

    return play_game #returning function... 
    # as parent function returns closure is created...

tommy = parent_function("Tommy")
jenny = parent_function("Jenny")

# as parent_function was returning function so tommy and jenny r now function

tommy()
tommy()
jenny()

# this is what closure is
# notice: parent_function has already ended but we r still able to use coins variable which was under parent_function scope.
# also both tommy and jenny r able to use seperate value of coins for their respective uses...




# lets add coin as a parameter
def parent_function(person, coins):

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left. ")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left. ")
        else:
            print("\n" + person + " has no coins left. ")

    return play_game #returning function... 
    # as parent function returns closure is created...

tommy = parent_function("Tommy", 3)
jenny = parent_function("Jenny", 5)

# as parent_function was returning function so tommy and jenny r now function

tommy()
tommy()
jenny()

# here we have avoided using "Global Variable". Thus, via closure we can avoid using Global Variables.