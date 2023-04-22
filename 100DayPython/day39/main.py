#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

flight_search = FlightSearch()

for row in sheet_data:
    flight_data = flight_search.get_cheapest_destination(row['iataCode'])
    print(flight_data)




