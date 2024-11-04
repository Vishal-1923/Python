# ************************************* is vs == **********************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/54-Day54-is-vs-in-Python/.tutorial/Tutorial.md

# is compares exact location of object in memory
# == compares values.
# they both r comparision operators

a = 4
b = '4'


print(a == b) #values
print(a is b) #exact location

a = [1,2,3]
b=[1,2,3]#ye dono alg alg list hai
print(a==b)
print(a is b)

a = 4 #as it is a constant which will not change(immutable) thus python will not allocate another memory location for same constant
b=4#ye dono alg ni hai memory main
print(a is b) #t
print(a == b) #t

a = "vish"
b = "vish"
print(a == b) #t
print( a is b)#t

a = (1,2) #tuple
b = (1,2)
print(a == b)#t
print( a is b)#t

a = None
b = None
print(a == b) #t
print(a is b)#t
print(a is None)#t