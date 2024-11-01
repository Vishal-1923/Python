# *************************** List Methods *******************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/23-Day-23-List-Methods/.tutorial/01-lists_methods.md


l = [1,2,3,4,5]
print(l)

# appending in list
# l.append(6, 7)#not take multiple args.
l.append(6)
print(l)

# sort
lsort = [8, 2, 5, 1, 0, 3, 4, 2, 67, 100, 86]
lsort.sort()#sort in ascending order
print(lsort)

lsort.sort(reverse = True)#sort in descending order
print(lsort)

# reversing a list
l.reverse()
print(l)

# index
print(l.index(4)) #1st occurence.

# count
lcount = [1, 2, 3, 4, 5, 2, 5, 2, 1, 4, 3, 5, 3]
print(lcount.count(5))

# issue in assigning
li = [1, 2, 3, 4, 5]
il = li
il[0] = 0
print(li, il) #changes will be done in both list. becoz il is just another reference to li

# copy
# returns copy of orginial list 
name = ["vishal", "krishna", "kumar"]
anotherName = name.copy()
print(name)
print(anotherName)
anotherName.reverse()
print(anotherName)

# insert
l = [1, 2, 3, 4, 5,6, 7, 8, 9]
print(l)
l.insert(5, 90) #to insert at a given index.
print(l)

# extend
# will add another list/any other collection datatype such as set, tuple, dictionary to an existing list
first = [1, 2, 4, 5, 6]
print(first)
second = [10, 100, 1000, 10000]
print(second)
first.extend(second)
print(first) #this will change first list.
print(second)

# concatenate
first = [1, 2, 3, 4]
second = [5]
third = first + second
print(first)
print(second)#will not modify original list.
print(third)