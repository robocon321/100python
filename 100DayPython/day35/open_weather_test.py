import requests

api_key = 'cd6ae7a95471227385ed9c5e846b1cee'
url = 'https://api.openweathermap.org/data/2.5/onecall'
lat = 10.506547
long = 106.850281

params = {
    "lat": lat,
    "lon": long,
    "appid": api_key
}

response = requests.get(url, params)
response.raise_for_status()

weathers_12_hours = [item["weather"][0] for index, item in enumerate(response.json()["hourly"])][:12]

is_rain = False
for weather in weathers_12_hours:
    if(weather['id'] < 700):
        is_rain = True

if(is_rain):
    print("Bring your umbrella")
