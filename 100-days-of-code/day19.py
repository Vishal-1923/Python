# ***************************** break / continue *************************

# break: when u want ki loop abhi k abhi break ho jaye and hm bahar aa jaye
# continue: loop ki ek particular iteration ko skip krna ho to.

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/19-Day-19-break-and-continue/.tutorial/01%20break.md

i = 10
while(i <= 100):
    print(i)
    i = i + 10

# ye hr baar chalega

for i in range(12):
    print("5 X ", i+1, " = ", 5*(i+1))
    if i > 10:
        break

# continue
for i in range(12):
    if(i == 10):
        print("skip iteration")
        continue
    print("5 X ", i+1, " = ", 5*(i+1))



# Emulating Do While
# we'll do it via infinite loop

i = int(input("Enter a no.: "))
while True:
    print(i)
    i = i+1
    if(i % 2 == 0):
        print("Even")
        break