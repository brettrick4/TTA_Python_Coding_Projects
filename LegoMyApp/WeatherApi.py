import requests

WEATHER_API_KEY = '1b3f6f0f26855bf358a17618dd9d6ab4'

def get_user_location():
    url = 'http://ip-api.com/json/'
    data = requests.get(url).json()
    lat = data['lat']
    lon = data['lon']
    location = {
        'lat': lat,
        'lon': lon
    }
    return location

def get_weather(lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}'
    data = requests.get(url).json()
    weather = {
#        'city': data['current']['city'],
        'current_tempurature': (data['current']['temp']-273.15) * 9/5 + 32,
        'clouds': data['current']['clouds'],
        'humidity': data['current']['humidity'],
        'wind': data['current']['wind_speed']
    }
    return weather
