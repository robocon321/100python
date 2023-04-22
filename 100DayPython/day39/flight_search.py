import os
import requests
import datetime
from flight_data import FlightData

URL = 'https://tequila-api.kiwi.com'
API_KEY = os.environ['TEQUILA_KEY']

headers = {
    'apikey': API_KEY
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city_name):
        params = {
            'term': city_name,
            'location_types': 'city'
        }
        endpoint = '/locations/query'
        response = requests.get(url = f'{URL}{endpoint}', params = params, headers=headers)
        response.raise_for_status()
        code = response.json()['locations'][0]['code']
        return code

    def get_cheapest_destination(self, code):
        format = '%d/%m/%Y'
        now = datetime.datetime.now()
        date_from = now.strftime(format)
        date_to = (now + datetime.timedelta(hours=24*30*6)).strftime(format)
        params = {
            'fly_from': code,
            'date_from': str(date_from),
            'date_to': str(date_to)
        }
        endpoint = '/v2/search'
        response = requests.get(url = f'{URL}{endpoint}', params = params, headers=headers)
        response.raise_for_status()
        flight_data = FlightData(10000, "", "")
        destinations = response.json()["data"]
        for destination in destinations:
            if(destination["price"] < flight_data.price):
                flight_data.price = destination["price"]
                flight_data.departure_airport_code = destination["cityCodeTo"]
                flight_data.departure_city = destination["cityTo"]

        return flight_data