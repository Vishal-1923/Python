# ********************** set methods ***************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/tree/main/32-Day32-Set-Methods/.tutorial

# union -> gives a new set
s1 = {1, 2, 3, 4}
s2 = {4, 5, 6, 7}
s3 = s1.union(s2)
print(s1)
print(s2)
print(s3) #combo of both sets

# update
s1 = {1, 2, 3, 4}
s2 = {4, 5, 6, 7}
s3 = s1.update(s2) #does not return a new set bit change the orginal set
print(s1)
print(s2)
print(s3)

# intersection -> gives a new set
s1 = {1, 2, 3, 4}
s2 = {4, 5, 6, 7}
s3 = s1.intersection(s2)
print(s1)
print(s2)
print(s3) #common of both sets

# intersection_update
s1 = {1, 2, 3, 4}
s2 = {4, 5, 6, 7}
s3 = s1.intersection_update(s2) #does not return a new set bit change the orginal set
print(s1)
print(s2)
print(s3)

# symmetric diff = (a union b) - (a intersection b)
# symmetric diff -> gives a new set
s1 = {1, 2, 3, 4}
s2 = {4, 5, 6, 7}
s3 = s1.symmetric_difference(s2)
print(s1)
print(s2)
print(s3) #unique in both sets

# symmetric_difference_update
s1 = {1, 2, 3, 4}
s2 = {4, 5, 6, 7}
s3 = s1.symmetric_difference_update(s2) #does not return a new set bit change the orginal set
print(s1)
print(s2)
print(s3)

# difference -> gives a new set (a-b)
s1 = {1, 2, 3, 4}
s2 = {4, 5, 6, 7}
s3 = s1.difference(s2)
print(s1)
print(s2)
print(s3) #pehle main hai but dusre main ni hai

# difference_update
s1 = {1, 2, 3, 4}
s2 = {4, 5, 6, 7}
s3 = s1.difference_update(s2) #does not return a new set bit change the orginal set
print(s1)
print(s2)
print(s3)

# there r several methods used for manipulting sets
# isdisjoint - checks if items of given set r present in another set.
# returns true or false.
# false if ele r there otherwise true
s1 = {1, 2, 3, 4}
s2 = {4, 5, 6, 7}
s3 = s1.isdisjoint(s2)
print(s1)
print(s2)
print(s3)#false

s1 = {1, 2, 3, 4}
s2 = {4, 2, 3, 1}
s3 = s1.isdisjoint(s2)
print(s1)
print(s2)
print(s3)#false

s1 = {1, 2, 3, 4}
s2 = {1, 2, 3, 4}
s3 = s1.isdisjoint(s2)
print(s1)
print(s2)
print(s3)#false

s1 = {1, 2, 3, 4}
s2 = {5, 6, 7, 8}
s3 = s1.isdisjoint(s2)
print(s1)
print(s2)
print(s3) #true

# issuperset - checks if all items of given set r present in another set.
# returns true or false.
# true if ele r there otherwise false
s1 = {1, 2, 3, 4}
s2 = {4, 5, 6, 7}
s3 = s1.issuperset(s2)
print(s1)
print(s2)
print(s3)#false


s1 = {1, 2, 3, 4}
s2 = {4, 2, 3, 1}
s3 = s1.issuperset(s2)
print(s1)
print(s2)
print(s3)#true

s1 = {1, 2, 3, 4}
s2 = {1, 2, 3, 4}
s3 = s1.issuperset(s2)
print(s1)
print(s2)
print(s3)#true

s1 = {1, 2, 3, 4}
s2 = {5, 6, 7, 8}
s3 = s1.issuperset(s2)
print(s1)
print(s2)
print(s3) #false

# issubset - checks if all items of original set r present in another set.
# returns true or false.
# true if ele r there otherwise false
s1 = {1, 2, 3, 4}
s2 = {4, 5, 6, 7}
s3 = s1.issubset(s2)
print(s1)
print(s2)
print(s3)#false


s1 = {1, 2, 3, 4}
s2 = {4, 2, 3, 1}
s3 = s1.issubset(s2)
print(s1)
print(s2)
print(s3)#true

s1 = {1, 2, 3, 4}
s2 = {1, 2, 3, 4}
s3 = s1.issubset(s2)
print(s1)
print(s2)
print(s3)#true

s1 = {1, 2, 3, 4}
s2 = {5, 6, 7, 8}
s3 = s1.issubset(s2)
print(s1)
print(s2)
print(s3) #false

# add - adding single item to set
s1 = {1, 2, 3, 4}
print(s1)
s1.add(5)
print(s1)

# for adding multiple items use update.

# remove/discard - remove items from set
s1.remove(5) #if ele not found, will raise an error
print(s1)
s1.discard(3)#if ele not found, will not raise an error
print(s1)

# pop()-will pop random item from set, but we dont know which item will be poped as items r unordered.
s1 = {1, 2, 3, 4}
print(s1, s1.pop(), s1)

# del - keyword - to delete a set entirely
del s1
# print(s1) #will give error as s1 has been deleted.

# clear - just to delete set items and not whole set
s1 = {1, 2, 3, 4, 5}
s1.clear()
print(s1) #will print an empty set.

# check if any item exits in set
s1 = {1, 2, 3, 4, 5}
for val in s1:
    if 1 == val:
        print(val)
    else:
        print(val, "not present")
