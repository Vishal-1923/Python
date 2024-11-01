# **************************** List *******************************


# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/22-Day-22-Introduction-to-Lists/.tutorial/01-lists.md


# Ordered collection of data items.
# Store multiple items in a single variable.
# List Items are seperated via , and enclosed within []
# List are changeable i.e., we can modify them after creation.

l = [1, 2, 3]
print("List is: ", l)
print("Type: ", type(l))
# list index.
# these are +ve indexing.
print(l[0])
print(l[1])
print(l[2])

# these are -ve indexing.
print(l[-1]) #same as l[3+(-1)]
print(l[-2]) #same as l[3+(-2)]
print(l[-3]) #same as l[3+(-3)]
# print(l[-4]) #same as l[3+(-4)] error : index out of bonds.

# list can be changed but tuple can't.
# list k andr alg data type bhi aa skta hai jaise:
lit = [1, 2, "vish", True]
print(lit)

# To check if an ele is there in list or not. 
# This is applicable to strings too.
if 3 in l: #3 will be there but "3" will not be
    print("Yes")
else:
    print("No")

# printing whole list
print(l)
print(l[:])# means [starting index : ending index : jump] -> [0:2:0]
print(l[1:])# will start from index 1 and go till end
print(l[1:-1])#[1:3-1] and 3-1 is not included.

print(l[::2])#will jump 2


# List comprehension
# used for creating new lists from other iterables like lists, tuples, dictionaries, set, even array, string.
lst = [i for i in range(4)] #[expression for i in range()] -> now this expression will become an element of list.
print(lst)

lst = [i*i for i in range(4)]
print(lst)

# we can add conditions too.
lst = [i*i for i in range(10) if i%2 == 0] #jb condition true ho tbhi main ele add kru list main.
print(lst)