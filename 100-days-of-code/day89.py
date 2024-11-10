# *********************************************** Request module *****************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/89-Day-89-Requests-Module/.tutorial/Tutorial.md

import requests
from bs4 import BeautifulSoup

# response = requests.get("https://www.google.com") #this is a simple get-request
# print(response.text)

# post request

# scrap a site and print all available h2 tags in its html
url = "https://blog.zomato.com/zomatos-order-scheduling-feature-convenience-at-your-fingertips"

r = requests.get(url)
print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())

for heading in soup.find_all("div"):
    print(heading.text)