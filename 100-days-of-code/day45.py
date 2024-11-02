# ***************************************** __name__ == "__main__" ***********************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/45-Day45-if-name-main-in-Python/.tutorial/Tutorial.md

# The if __name__ == "__main__" idiom is a common pattern used in Python scripts to determine whether 
# the script is being run directly or being imported as a module into another script.

# In Python, the __name__ variable is a built-in variable that is automatically set to the name of the current module. 
# When a Python script is run directly, the __name__ variable is set to the string __main__ 
# When the script is imported as a module into another script, the __name__ variable is set to the name of the module.

# This is very usefull in case u r importing any module/package given by friend or anyone. As sometimes even by importing some functions may run and those functions r capable of deleting all files of your system. So its a precautionary step.

import day45_helper as v

print("Hi")
# u can notice that hi is printed twice becoz just by importing day45_helper, its function  may run and execute. so to stop that we can use __name__ == "__main__" check!

