# ********************************** KBC ******************************

name = input("Enter your Name: ")
print("Hi ", name, "!")

print("So lets start playing KBC!")

print("\n****************************************\n")

print("First go through the Rules!!!")
rules = [
    "1. If you give wrong answer to a question, you will loose all the money.",
    "2. You will get 4 options to each question.",
    "3. Maximum prize amount is 1 crores."]
for rule in rules:
    print(rule)

print("\n****************************************\n")

print("We hope, you have read all the rules. ")
print("Lets start playing!")
print("All the Best!")

print("\n****************************************\n")

# questions
def options(quesn, i):
    print(quesn)
    match i:
        case 1:
            print(
                "A. New-Delhi",
                "B. Mumbai",
                "C. Banglore",
                "D. Chandigarh"
            )
            opt = input("enter your ans: ")
            if opt == "A":
                print("Oho!!!, thats the Correct Ans!.")
                print("You have won Rs. 50,000")
                print("Moving to new question.")
                print("\n *************************************** \n")
                return 1
            else:
                print("OOPS!")
                print("That was wrong ans! Better Luck next time.")
                return 0
        case 2:
            print(
                "A. New-Delhi",
                "B. Mumbai",
                "C. Banglore",
                "D. Indore"
            )
            opt = input("enter your ans: ")
            if opt == "D":
                print("Oho!!!, thats the Correct Ans!.")
                print("You have won Rs. 1,00,000")
                print("Moving to new question.")
                print("\n *************************************** \n")
                return 1
            else:
                print("OOPS!")
                print("That was wrong ans! Better Luck next time.")
                return 0
        case 3:
            print(
                "A. Virat Kohli",
                "B. MS Dhoni",
                "C. Sachin Tendulkar",
                "D. Rahul Dravid"
            )
            opt = input("enter your ans: ")
            if opt == "C":
                print("Oho!!!, thats the Correct Ans!.")
                print("You have won Rs. 10,00,000")
                print("Moving to new question.")
                print("\n *************************************** \n")
                return 1
            else:
                print("OOPS!")
                print("That was wrong ans! Better Luck next time.")
                return 0
        case 4:
            print(
                "A. UK",
                "B. INDIA",
                "C. South-Africa",
                "D. Australia"
            )
            opt = input("enter your ans: ")
            if opt == "B":
                print("Oho!!!, thats the Correct Ans!.")
                print("You have won Rs. 50,00,000")
                print("Moving to new question.")
                print("\n *************************************** \n")
                return 1
            else:
                print("OOPS!")
                print("That was wrong ans! Better Luck next time.")
                return 0
        case 5:
            print(
                "A. Narendra Modi",
                "B. Yogi Adityanath",
                "C. Amit Shah",
                "D. Rajnath Singh"
            )
            opt = input("enter your ans: ")
            if opt == "A":
                print("Oho!!!, thats the Correct Ans!.")
                print("You have won Rs. 1,00,00,000")
                print("Congrats on wining KBC!!!")
                print("\n *************************************** \n")
                return 1
            else:
                print("OOPS!")
                print("That was wrong ans! Better Luck next time.")
                return 0


# while True:
quesns = [
    " Q. Which of the following city is the capital of INDIA ?",
    " Q. Name INDIA's most cleanest city ?",
    " Q. Name the cricketer who is called \"God of Cricket\" ?",
    " Q. Which country has won the recent \"World Cup\" ?",
    " Q. Name the Prime Minister of INDIA ?"
]
i = 1
for ques in quesns:
    status = options(ques, i)
    i = i+1
    if status == 0:
        break

print("Thank You !!!")
# list ka ek ele use main ek function main dalunga aur wo uske 4 options print krega and will also match correct ans.
