# module contains 
# 1. data
# 2. functions
# 3. can import other modules too.

from random import choice

capital = "Topeka"

bird = "Western Meadowlark"

flower = "Sunflower"

song = "Home on the Range"


def randomfunfact():
    funfacts = [
        "Kansas is considered flat, but it does have a mountain.",
        "Wichita is the largest city in the state, but many would guess that it is Kansas City.",
        "A considerable portion of Kansas City is actually in Missouri.",
        "Most Kansans are annoyed by Wizard of Oz references from people outside of Kansas."
    ]

    index = choice("0123")

    print(funfacts[int(index)])


if __name__ == "__main__":
    randomfunfact() #will only be called if it is called from main file which in this case is this file only.
    # basically if we remove this check and then we run chapter14 file it will run the function and when this file gets imported function will once again run.
    # so we in order to make it run only once we do this
   
    # in short this will not run unless exampleModule is main file.
     
    
