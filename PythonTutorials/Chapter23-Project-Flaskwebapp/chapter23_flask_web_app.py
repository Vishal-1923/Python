# nothing fancy, we will be making a website which can show weather condition of any city

# we will be using Flask...

# 1. create a virtual environment
# 2. install modules
# 3. create requirements file
# 4. then create some folders:
# ---> static : hold any static files i.e., not changing
# ---> templates : here html files will be stored...with this we r going to insert some values from python into those html files and use those templates for our webpage...

# this is my weather module which will get weather details via api

from dotenv import load_dotenv
from pprint import pprint
import requests
import os

# 1. load all the values from .env file
load_dotenv()

# 2. defining get current weather function
def get_current_weather(city="Delhi"): #given for the case when person just pressed enter in form.
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == '__main__':
    # this is if this file is called directly
    print("\n*** Get Current Weather Conditions ***\n")
    city = input("Enter your city name...\n")
    
    # check for empty strings or string with only spaces...
    # strp() - strips aways empty spaces
    if not bool(city.strip()):
        city='Delhi' #default value
    
    weather_data = get_current_weather(city)
    print()
    pprint(weather_data)