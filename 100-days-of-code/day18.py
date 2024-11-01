# ******************** While loop *****************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/18-Day18-While-Loops/.tutorial/01%20While%20Loops.md

i = 0
while(i<3):
    print(i)
    i = i+1


# # Taking user input continuously
i = int(input("Enter a no: "))
while(i <= 50):
    i = int(input("Enter a no: "))
    print(i)

print("Done with loop!")

# Decrementing Loop
i = 5
while(i > -1):
    print(i)
    i = i-1
print("done!")

# using else with while
i = 5
while(i > -1):
    print(i)
    i = i-1
else:#while chalta rhega aur jb wo exit hoga to hm else main chale jaenge
    print("done!")

# There is no such thing like Do-while loop in python

# Emulate do while loop in python - popular interview question
# do-while: will execute atlest 1 and then upon clear condition


