# a simple prog which goes on internet and requests the weather from a service and returns the curr. weather to us.
# We r going to be able to requests weather from any city.

# openweathermap.org
import requests
from dotenv import load_dotenv #help us get the env variable value
import os
from pprint import pprint #stands for pretty print...

load_dotenv() #this will load env variables, so we can retrieve them.

def get_curr_weather():
    print("\n*** Get Current Weather Conditions ***")

    city = input('\nPlease enter a city name:\n')
    #everything till weather is good but after that we need to fix, after ? parameters starts... & means another param
    # request_url = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}&units=metric'
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    # we r loading env variable values via load_dotenv and get that value via os.getenv()
    # q is an abbreviation for query in their API system
    print(request_url)
    weather_data = requests.get(request_url).json() #we want to have json format of data, very common means of transporting data in many applications over web.
    # JSON DATA is not very pleasing to read in its raw format, need to do something about it.
    print(weather_data)
    print('')
    pprint(weather_data) #by name itself it prints data in such a format which is pleasing to read.

    # if i do this way, python will be confused becoz we r giving "" inside ""
    # print(f"\nCurrent weather for {weather_data["name"]} is {weather_data["main"]["temp"]}, but it feels like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}.")
    print(f'\nCurrent weather for {weather_data["name"]} is {weather_data["main"]["temp"]} degrees celcious, but it feels like {weather_data["main"]["feels_like"]} degrees celcious and have {weather_data["weather"][0]["description"]}.')


if __name__ == '__main__':
    get_curr_weather()