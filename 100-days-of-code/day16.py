# ************************* Switch case *************************

# addition in python above 3.10
# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/16-Day-16-Match-Case/.tutorial/Tutorial.md
import os

print("Writing python from: ")
os.system("python --version")

x = int(input("Enter a no: "))
match x:
    case 0:
        print("Entered no is 0")
    case 2 if x % 2 == 0:
        print("Entered no is even")
    case 3 if x % 2 != 0:
        printf("Entered no is odd")
    case _: #default
        printf("No is any.")
    
# no need to use break. once a case is matched it is matched. no further matching...
# we cant have an expression as a case

