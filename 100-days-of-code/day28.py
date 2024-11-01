# *************************** fstring *********************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/28-Day28-f-strings/.tutorial/Tutorial.md

# used for string formatting
# introduced after Python 3.6


text = "For only {price:.2f} dollars!"
print(text.format(price = 29.00000045)) #will print till 2 decimal places. (:.2f ka mtlb hai ki upto 2 decimal places...)

letter = "Hey! My name is {} and I am from {}"
name = "Vishal"
country = "India"
print(letter.format(name, country))

# if we do like this then,
letter = "Hey! My name is {1} and I am from {0}"
name = "Vishal"
country = "India"
print(letter.format(country, name)) #if we r passing args in diff order then we must provide the index in string.

# More convinient way of doing this in Python is fstring.

name = "Vishal"
country = "India"
print(f"Hey! My name is {name} and I am from {country}") #it will populate its value.


price = 29.994837
print(f"for only {price:.2f} dollars")

print(type(f"{3*2}")) #we can do something like this.

#agr mujhe as it is {} print krwana hai to i'll do something like this
print(f"Hey! My name is {{name}} and I am from {{country}}")