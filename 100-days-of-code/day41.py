# ********************************** Short hand - if else statements *********************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/41-Day41-Short-Hand-if-else/.tutorial/Tutorial.md

# very helpfull especially in case of expression

a = 330
b = 3303

print("A") if a > b else print("=") if a == b else print("B")
# print A if a>b
# print = if a==b
# else print B

# print(8) if a<b : this will give syntax error as else is mandatory as well as "" after else
print(8) if a<b else ""

c = 9 if b>a else 0
print(c)