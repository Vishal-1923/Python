# **************** dictionary methods ******************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/34-Day34-Dictionary-Methods/.tutorial/01-Dictionary_methods.md

# update()
# updates the value of key provided if its present otherwise will create a new key-value pair.
ep1 = {122: 45, 123:89, 567:69, 670:69}
ep2 = {222:67, 566: 90}
ep1.update(ep2) #ep1 has been updated with the values of ep2.
print(ep1, ep2)

# clear()
# to clear all the dictionary
ep1.clear() #empty dictionary
print(ep1)

empt = {} #empty dictionary
print(empt)

# pop()
# pop key-value pair
ep1 = {122: 45, 123:89, 567:69, 670:69}
ep1.pop(122)
print(ep1)

# popitem()
# will remove last key-value pair.
ep1.popitem()
print(ep1)

# del
# keyword: delete entire dictionary
# del ep1
print(ep1)

# we can print 1 single entry too via del
del ep1[123]
del ep1["123"] #will give error as 123 is there in form of int and not string.
print(ep1)

