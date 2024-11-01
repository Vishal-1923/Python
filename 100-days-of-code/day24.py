# *********************** Tuple ***********************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/tree/main/24-Day24-Introduction-to-Tuples/.tutorial

# Ordered collection of data items
# store multiple items in a single variable
# seperated by , and enclosed with ()
# cant change them after creation

tup = (1, 2,3 ,4 ,5)
print(type(tup), tup)

tup1 = (1)
print(type(tup1), tup1) #python considers this as int so if u want it to be treated as tuple use like this
tup1 = (1, )
print(type(tup1), tup1)

# tup[0] = 10 will flag error as tuple are unchangeable
# print(tup)

# we'll use tuple when we intentionally want that tuple should not change.

# rest same as list....

# we can do slicing of tuple but it gives another tuple and does not change original
tup2 = tup[:3] #new tuple tup2
print(tup2, tup)