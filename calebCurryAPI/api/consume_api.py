import requests
import json

# this is the way to get the response of any site or basically the response which we will get when we will click on the url or go to that site.
response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

print(response) #will print 200 -> OK
print(response.json()) #will print the returned data (exactly the same data which we would get via postman or manually going to site.)
print(response.json()['items']) #we r not working with items but we have now list of questions with us. Basically data was in key value format where items was the key and rest was the value so by doing this we r going deep i.e., exploring the values.

# iterating over the questions list
for question in response.json()['items']:
    print(question)
    print()
    print(question['title'])#basically it is question on stack ovrflow
    print(question['link']) #this is its ans's link...
    print('***********************************************')
    if question['answer_count'] == 0:
        print(question['title'])
        print(question['link'])
    else:
        print("HI---------------------")

