# *************************** Comment, Escape Sequence and Print Statement ************************

print("Hey!, I am a good boy") # will print any string or text enclosed within ""



# Comments
# these lines dont get executed and r often ignored by compiler.

#   Single Line Comment: start the line via #
#   Multi Line Comments: # infront of each lines or use 
'''this is multi line 
comments'''
# or this
"""this is multi line 
comments"""



# Escape Sequences
# used to insert such characters that can't be directly used in a string.
# an escape sequence character is \ followed by character.
# print("This does not "execute")
print("This does \"execute\"")


# print("Hey!, I am a good boy 
    # and this viewer is also a good boy/girl.") #this will result in error.
# the thing is we cant do like this. if u want some part to be displayed on next line then use escape sequence such as "\n" aka new line

print("Hey!, I am a good boy \n and this viewer is also a good boy/girl.") # now becoz of this \n, they r printed on diff lines.



# Print statement
# multiple items
print("HI", 5, 8)

# we can seperate them out with any char specify
print("Hi", 5, 7, sep="~")

# we can use any end string
print("Hi", 5, 7, sep="~", end="00000")
print("Vishal")#before printing Vishal it will append 0000 
# op:Hi~5~70000Vishal
# default seperator is space.
# default end arg is New line.
#1 more arg i.e., file: object with a write method. default is sys.stdout
# Param 2-4 are optional.
# print(object(s), sep=sep, end=end, file=file, flush=flush) -> syntax of print
