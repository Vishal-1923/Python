users = ['Vishal', 'Krishna', 'Kumar'] #3 values, 1 list - users

#List is not limited to String data type or any data type
data = ['Vishal', 5, True] #we can have multiple values of diff data type.

#it can even be an empty list
emptyList = []

#to check if any particular item is there in list.
print('Vishal' in users)
print('Vishal' in emptyList)
print(5 in data)
print('VV' in users)

#want to get specific item from list and we know its position.
print(users[0])
print(data[2])
# print(emptyList[0]) #will give index out of range.

# in order to reach last value of list, we would use -1
print(data[-1])
# print(emptyList[-1]) #will give index out of range
print(users[-1])
print(users[-2])

# want to know position of a specific value, use index()
# print(users.index('vishal')) #it is case sensitive., error -> vishal is not in the list.
print(users.index('Vishal'))

# if u want list of values
print(data[0:2])#will consider 0, 1 but not last index i.e., 2

print(users[0:])#will print all the values inside it from 0.
print(users[1:])
print(users[-3:-1])
print(users[-3:])

#len of list
print(len(data))
print(len(users))
print(len(emptyList))

#adding new ele to list
data.append("VKK")
print(data)

#adding 1 list to other.
data += ['v', 'k', 'k']
print(data)

data.extend(['vk', 'k'])
print(data)

# here's a catch
data += "vshal"#it will add each individual letters. agr bachna hai to list main naam dal and then add kr...
print(data)

users.extend(data)#we can add prev created list too.
print(users)

#insert at 1st position...
users.insert(0, 'BOB')
print(users)

#insert at 3rd position...
users[2:2] = ['VishalKK', 'VKKumar'] #i want to add at 2nd position only...no replacement, everything at 2nd posn.
#basically starts at 2 and ends at 2 only.
#basically it makes room for our values at our desired location...
print(users)

#replacing values.
users[1:3] = ['amantya', 'tech']
#will replace values which were at 1st and 2nd position with these values.
print(users)

#aka SLICE
users[1:3] = ['amantya', 'tech', 'op', 'pppp']
#in this case, 1st and 2nd value will be replaced but values after that will not replaced but shifted i.e,
# ['BOB', 'Vishal', 'VishalKK', 'VKKumar', 'Krishna', 'Kumar']
# ['BOB', 'amantya', 'tech', 'op', 'pppp', 'VKKumar', 'Krishna', 'Kumar']

# removing data from list.
users.remove('vk')
users.remove('v')
users.remove('s')
users.remove('h')
users.remove('a')
users.remove('l')
users.remove('v')
users.remove('k')
users.remove('k')
users.remove(5)
users.remove(True)
users.remove('k')
users.remove('VKK')

print(users)

# popping last value
print(users.pop()) #basically pop will return the poped value
print(users)

# DEL
# popped 1st value
del users[0]
print(users)

# we can delete entire list too.
# del data
# at this moment, there is nothing as of data.
# print(data) #give error

# CLEAR
data.clear() #will empty the list and list will exist
print(data)

# SORT
users.sort()
print(users)
# remember this will only work if ur list has single type of values, if there r mixed values then sort will not work.
#also sort here sorts the values via there ascii codes.

# what if! u wanna sort them such that lower case comes first, basically alphabetically.
users.sort(key=str.lower)
print(users)


# REVERSE - flips the array.
nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums) #5, 1, 78, 42, 4

# sort in ascending order
nums.sort()
print(nums)

# sort in descending order
nums.sort(reverse=True)
print(nums)

# this changes the original list
# What if u dont wanna do that?
# Global Approach...
# there is a global sorted function, it returns the list and not modifies the original list
nums.reverse()
print(sorted(nums, reverse=True)) #original list is not modified...
print(nums)

# make a copy and then sort that copy...
# 1. copy
numsCpy = nums.copy()
# 2. constructor
mynums = list(nums)
# 3. slice
mycpy = nums[:] #slice the full list and store it in the mycpy

print('')

print("org: ", nums)
print("numscpy: ", numsCpy)
print("mynums: ", mynums)
mynums.sort(reverse=True)
# print("mynums -> sort: ", mynums.sort()) -> will print none as sort does not return a value
print("mynums -> sort: ", mynums)
print("mycpy: ", mycpy)

# CHECK TYPE OF LIST
print(type(nums))

# can create a list with constructor.
myList = list([1, 2, 3, 4, 5])
print(myList)


# ******************************************************
# TUPLES
# -> r very like list, with major 2 differences.
# 1. data inside a tuple will not change.
# 2. order in which data is will not change.
# explore more about this.

# created using Constructor
myTuple = tuple(('vishal', 24, True))
print('tuple: ', myTuple, "| type: ", type(myTuple))

# created without Constructor
anotherTuple = ('Kumar', 5, False, 'VK')
print('tuple: ', anotherTuple, "| type: ", type(anotherTuple))

# everything that applies to list, applies to tuple
# but it cant change

# if we wanna do something, we can be creative and do so via copying the tuple
newList = list(myTuple) #convert tuple to list
newList.append('ap')
newTuple = tuple(newList)
print(newTuple)

# assigning a value to tuple means 'PACKING'
# we can unpack too, into various variable names.
(one, two, *rest) = anotherTuple
print(one)
print(two)
print(rest)
# *rest holds all the remaining values and it packs them into a list.

print('')

(one, *two, rest) = anotherTuple 
print(one)
print(two) #holds all but not last
print(rest) #holds last.

# (one, *two, *rest) = anotherTuple, will give error

# COUNT
print(anotherTuple.count(5))

# Tuple is immutable i.e., values will not change. This will give error -> tuple object does not support item assignment.
# anotherTuple[0] = 100
# anotherTuple.append(3) --> no method append as we cant change tuple

# This is so becoz tuples were designed to remain constant i.e., once created there items will remain as it is.
# ORDER matters.
t1 = (1, 2, 3)
t2 = (3, 2, 1)
# are considered diff.
print(t1 == t2)

# this is true even for lists
t1 = [1, 2, 3]
t2 = [3, 2, 1]
print(t1==t2) #will print false.

# we can have tuple/list inside tuple
# and list/tuple inside list.
t3 = (1, 2, t2, [1,2,3])
t4 = [1, 2, t1, [4,5,6]]
# 1 imp thing, if there is a list inside a tuple then that list is mutable but tuple's structure remains same.

# List -----> whiteboard (temperory)
# Tuple ----> Stone Carving (permanent)

# But why 2 things???
# 1. Mutability:
#       modification(update, delete, add)
# 2. Performance
#       tuples r faster, as it is permanent, memory and access speed optimizations r done.
# 3. Safety
#       accidential modification
# 4. Hashability
#       can be used as keys in dictionary / ele in sets as they r immutable
#       list cant as they r mutable

# List []
# Tuple ()
# both r ordered.

# Faster execution
# Less memory - list keeps some extra slot in case of modifications but no such things r required in tuple