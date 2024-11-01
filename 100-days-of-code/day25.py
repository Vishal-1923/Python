# ***************************** operations on tuple ********************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/tree/main/25-Day25-Operations-on-Tuples/.tutorial

# If u want to manipulate tuple u need to convert it to list do operations and then convert back to tuple.

countries = ("India", "UK", "Spain", "France", "USA", "Germany")
print(countries)
temp = list(countries)
temp.append("Russia")
temp.pop(2)
temp[2] = "Italy"
countries = tuple(temp)
print(countries)

# We can directly concatenate 2 tuples as we r not changing anything but creating a new one.

# count
tup1 = (11,2, 3,1 ,3 ,4, 3, 4,3 ,4)
print(tup1.count(3))

# index
tup1 = (11,2, 3,1 ,3 ,4, 3, 4,3 ,4)
print(tup1.index(3)) #returns index of 1st occurence.
# index(ele, start, end) - we can search for 1st occurence in a given space or in between indexes.
# if ele is not present it will give value error.

res = len(tup1)

print(res)
