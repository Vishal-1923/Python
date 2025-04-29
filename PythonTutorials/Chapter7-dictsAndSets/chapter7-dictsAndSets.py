#Dictionaries
# are used to store data values which r in "key-value pairs"

# 1st way
band1 = {
    "vocals" : "Plant",
    "guitar" : "Page"
}

# 2nd way
band2 = dict(vocals="Plant", guitar="Page")

print("Band1: ", band1, "and is of type: ", type(band1))
print("Band2: ", band2, "and is of type: ", type(band2))

# ACCESSING ITEMS in Dictionary
print(band1["vocals"]) #or
print(band2.get("guitar"))

# list all the keys...
print(band1.keys())
print(band1.values())

# list of key value pair as tuple.
print(band1.items())

# verify a key exists
print("guitat" in band1)
print("guitar" in band1)
val = "guitat" in band1
print(val)

# change values in dictionary.
band1["vocals"] = "orchestra"
print(band1)
band1.update({'newKey': 'newVal'})
print(band1)
band1.update({'vocals': 'plant'})
print(band1)

# removing items
print(band1.pop("newKey")) #returns value of key which was removed.
print(band1)

band1["drums"] = "Bonham"
print(band1)

print(band1.popitem()) #now it will return a tuple
print(band1)

# delete/clear
band1["drums"] = "Bonham"
print(band1)

del band1["drums"]
print(band1)

print(band2)
band2.clear()
print(band2)
del band2

# Copying Dictionaries
# how u dont wanna do it.
#band2 = band1 #this creates a reference, basically both points to same memory location. Hence, change in 1 reflects change in other.

#print(band1)
#print(band2)

#band2["drums"] = "Dave"

#print(band1) #band1 also changed... #dangerous!!!


# how u wanna create a copy
# 1. via copy function
band3 = band1.copy() #now they dont have same reference...

band3["drums"] = "Vish"

print(band1)
print(band3) #they r diff.

# 2. via constructor function.
band4 = dict(band1)
print("Good Copy!!!")
print(band4)

# NESTED DICTIONARIES
# value for a key-value pair can be another dictionary.
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}

member2 = {
    "name": "Page",
    "instrument": "guitar"
}

band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"])
print(band["member1"]["name"])
print(band["member1"]["instrument"])

# *************************************************
#                        SETS 
# *************************************************
# 4th and final "data collection type "

# 2 ways of creating set
nums1 = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))
print(nums1)
print(type(nums1))
print(len(nums1))
print(nums2)
print(type(nums2))

# no duplicates are allowed!!!
nums1 = {1, 2, 2, 3}
print(nums1) #will automatically remove duplicate from set.

nums1 = {1, True, 2, False, 4, 0, 3}
print(nums1)

# check if a value is in set
print(True in nums1)

# u cant refer to an element in the set with an index position as in list or via key as we do in dictionary.


# adding a new value to set.
nums1.add(100)
print(nums1)

# add ele from 1 set to another.
moreNums = {8, 9, 6}
nums1.update(moreNums) #update can be used with lists, tuples and dictionaries too.
print(nums1)

list1 = [30, 40, 10]
nums1.update(list1)
print(nums1)

# in set the order is not guranteed. can we in any order.!!!

# MERGE 2 sets
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = set1.union(set2)
print(set3)

# keep only duplicates.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = set1.intersection(set2) #if i use intersection_update() then it will update the set itself (set1 in this case.)
print(set3)
print(set1)

# everything except duplicates.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.difference(set2)#difference_update to update set too.
print(set3)

set1.difference_update(set2) #removes common ele from original set.
print(set1)

set1.symmetric_difference_update(set2) #keeps only that ele which r in either of set.
print(set1)