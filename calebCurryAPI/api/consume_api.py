import requests
import json

response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

print(response)
print(response.json())
print(response.json()['items']) #we r not working with items but we have now list of questions with us.
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

