# ******************* for loop with else ***************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/35-Day-35-For-loop-with-else/.tutorial/Tutorial.md

# we can use else with for as well as while loop too.

for i in range(5):
    print(i)
else:
    print("Sorry, no I!") #when control exits from for, else will be executed.

for i in []:
    print(i)
else:
    print("Sorry no i!") #this time control will directly go to else.

# interview question
for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("Sorry!")
# no this time it will not print. as else will only execute when loop successfully ends and not breaks.