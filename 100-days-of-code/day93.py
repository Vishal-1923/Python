# ********************************** assignment 10 sol **********************************************

import json
import requests

query = input("What type of news u r interested in ? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-10-28&sortBy=popularity&apiKey=a397f29d5ca74fa1a97181aaa4fe8972"
r = requests.get(url)

news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("----------------------------------------------------------")