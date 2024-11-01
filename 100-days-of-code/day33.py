# ******************* dictionary *********************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/33-Day-33-Dictionary/.tutorial/01-Dictionaries.md

# stores key value pair
# fast access, has its own index
# used to create a mapping.
# earlier they were unordered but after 3.7 they r ordered.
dic = {
    "harry": "Human Being",
    "spoon": "Item"
}
print(dic)#will print whole dictionary

print(dic["spoon"]) #to access a single key -> will give error if ele is not present
print(dic.get("spoon")) #another way to access a single key -> will not raise error in case ele is not present. will return NONE.

# accessing multiple values
print(dic.keys()) #will print entire key present in dictionary.
print(dic.values()) #will print all the values present in dictionary.

# iterating through keys
for key in dic.keys():
    print(key, "-", dic[key])

# more beautiful way to print key-value
for key in dic.keys():
    print(f"The value corresponding to {key} is {dic[key]}.")

# another way:
print(dic.items()) #to print key value pair

for key, value in dic.items():
    print(f"The value corresponding to {key} is {value}.")