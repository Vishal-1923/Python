# *************************************************** exercise 10 ************************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/90-Day-90-Exercise-10/.tutorial/Tutorial.md

'''
Use the NewsAPI and the requests module to fetch the daily news related to different topics. Go to: https://newsapi.org/ and explore the various options to build you application
'''

import requests
from bs4 import BeautifulSoup

url = "https://newsapi.org/v2/everything?q=apple&from=2024-11-09&to=2024-11-09&sortBy=popularity&apiKey=a397f29d5ca74fa1a97181aaa4fe8972"

r = requests.get(url)
# print(r.text)

# soup = BeautifulSoup(r.text, 'html parser')
# print(soup.prettify())


def fetch_news(topic, from_date, to_date, api_key):
    # Construct the URL with dynamic query parameters
    url = f"https://newsapi.org/v2/everything?q={topic}&from={from_date}&to={to_date}&sortBy=popularity&apiKey={api_key}"
    
    # Make a GET request to the NewsAPI endpoint
    response = requests.get(url)
    
    # Check if the response was successful
    if response.status_code == 200:
        # Parse the JSON data
        news_data = response.json()
        if news_data["status"] == "ok":
            articles = news_data["articles"]
            print(f"Showing top news articles for '{topic}':\n")
            for idx, article in enumerate(articles[:5], 1):  # Display top 5 articles, articles[:5] will select 1st 5 articles. enumerate helps in keeping track of index and by mentioning 1 we r changing default index from 0 to 1.
                print(f"{idx}. {article['title']}")
                print(f"   Source: {article['source']['name']}")
                print(f"   Published: {article['publishedAt']}")
                print(f"   Link: {article['url']}\n")
        else:
            print("Error in API response.")
    else:
        print("Failed to fetch data:", response.status_code)

# Parameters for fetching news
topic = "cricket"  # You can change this to any topic of interest
from_date = "2024-10-10"
to_date = "2024-10-10"
api_key = "a397f29d5ca74fa1a97181aaa4fe8972"

# Fetch news on the topic
fetch_news(topic, from_date, to_date, api_key)
