
# what we have been doing...
person = "Dave"
coins = 3

print("\n" + person + "has " + str(coins) + "coins left. ")

# Alternate - older methods
# 1. %s method of formatting strings.
message = "\n%s has %s coins left." % (person, coins)
print(message)


# 2. format method.
message = "\n{} has {} coins left.".format(person, coins)
print(message)

# another way in format method. --- can use index...
message = "\n{1} has {0} coins left.".format(coins, person)
message = "\n{0} has {1} coins left.".format(person, coins)
print(message)

# another way in format method.
message = "\n{person} has {coins} coins left.".format(person = person, coins = coins)
message = "\n{person} has {coins} coins left.".format(coins = coins, person = person)
print(message)

# another method --- dictionary
player = {"person": "Vishal", "coins": 3}
message = "\n{person} has {coins} coins left.".format(**player) #pull these values in from dictionary, based on what we have assigned the keys
print(message)


# if we have this, why move to newer method??
# these r longer and not user friendly (not pleasing to read)
# they can become complicated easily...

# f-strings - simple, readable, not-at-all complex :)
message = f"\n{person} has {coins} coins left."
print(message)

# we can pass equations too.
message = f"\n{person} has {2 * 5} coins left."
print(message)

# can use methods here too.
message = f"\n{person.lower()} has {coins} coins left."
print(message)

# dictionary
message = f"\n{player['person']} has {coins} coins left." #only work if u have used " " outside the message - for enclosing fstring.
# message = f'\n{player['person']} has {coins} coins left.' would result in error.
print(message)

# can pass formatting options
num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n") 
# : says formatting options r there
# .2 upto 2 decimal places
# f - fixed

# loop
for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

# loop
for num in range(1, 11):
    print(f"{num} is divided by 4.52 is {num / 4.52:.3%}")
