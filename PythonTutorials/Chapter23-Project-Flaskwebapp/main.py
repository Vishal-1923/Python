# waitress is a package which will help serve the web app in production.



# many name it as server.py
from flask import Flask, render_template, request
from chapter23_flask_web_app import get_current_weather
from waitress import serve

# define my flask app
app = Flask(__name__)

# routes: these r the paths which we access on web
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    if not bool(city.strip()):
        city='Delhi' #default value
    weather_data = get_current_weather(city)
    
    # city is not found by api
    if not weather_data['cod'] == 200:
        # return "City not found!!!"
        return render_template('city-not-found.html')
    
    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port = 8000)#local host
    serve(app, host='0.0.0.0', port = 8000)#local host