# ********************** Sets ***************************

#https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/31-Day31-Sets/.tutorial/Tutorial.md

# Set is a collection of well defined objects.
# And in Python everything is objects. So no issues!
# a data-type which only stores unique elemets i.e., no duplicate elements will be there.

# Formally
# Sets are unordered collection of data items.
# store multiple items in a single variable, seperated by , and enclosed within {}.
# they r unchangeable i.e., u cant change the elements of set once created.
# ek jhola hai motio ka, usme ek moti aur dal do. ab wo mix ho gya tum use ni dundh paaoge.

info = {"Carla", 19, False, 5.9, 19} #also maintaining order is not at all guaranteed.
print(info)#set will only contain 19 once.

# all the operations are very similar to that of list but remember values cant be repeted.

quizset = {}#empty set's type is dict. becoz dict format is also same as set.
quizset = set() #via this we can create an empty set.
print(type(quizset))
quizset = {"",} #this is how u create a set with 1 ele which is an empty string.

for value in info:
    print(value)