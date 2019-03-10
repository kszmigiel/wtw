import requests
import sys

URL = 'http://api.openweathermap.org/data/2.5/weather'
PARAMS = {
    'APPID': 'f0f8c83a56cf570b7402bbe407195551',
    'units': 'metric'}

PARAMS['q'] = sys.argv[1]

r = requests.get(url = URL, params = PARAMS)

if(r.status_code != 200):
    sys.exit('Failed to read weather, sorry :(')

data = r.json()

weather = {
    'city': data['name'],
    'country': data['sys']['country'],
    'desc': data['weather'][0]['description'],
    'temp': str(data['main']['temp']),
    'pressure': str(data['main']['pressure']),
    'humidity': str(data['main']['humidity']),
    'wind': str(data['wind']['speed']),
}

print('The weather in ' + weather['city'] + ', ' + weather['country'] + ' is ' + weather['desc'])
print('Temperature: ' + weather['temp'] +' C')
print('Pressure: ' + weather['pressure'] +' hPa')
print('Humidity: ' + weather['humidity'] +' %')
print('Wind: ' + weather['wind'] +' m/s')