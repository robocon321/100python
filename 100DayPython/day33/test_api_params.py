import requests

MY_LAT = 10.326950
MY_LONG = 106.315684

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG
}

response = requests.get('https://api.sunrise-sunset.org/json', params = parameters)
response.raise_for_status()
