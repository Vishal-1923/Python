# ***************************** Typecasting ********************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/09-Day9-Typecasting-in-Python/.tutorial/Tutorial.md

# Conversion of 1 datatype into another is known as Typecasting.
# Python supports various function for this sole purpose:
#   int()
#   float()
#   str()
#   ord()
#   hex()
#   oct()
#   tuple()
#   list()
#   set()
#   dict()
# They will try to convert but not necessarily convert, it depends on what u r trying to convert and to what u r trying to convert.
# just like "harry" cant be converted to int.
# but "1" can be converted to int 1.


# 2 types of Typecasting:
#   Explicit Typecasting: done / specified by programmer.
#   Implicit Typecasting: done by Python as and when needed.

a="1"
b="2"
print(a+b) #will print 12 as it is concatenating 2 strings. and not adding 2 nos

print(int(a) + int(b))#now they have been typecasted to int, as it is done manually so Manual Typecasting.



a = 4.5
b = 3
print(a+b) #now it has been converted to float (3->3.0) so 3.0+4.5