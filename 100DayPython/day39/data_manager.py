import requests


ENDPOINT = 'https://api.sheety.co/715b37d5c4b06c54b6a983d5c287dd34/flightDeals/prices'
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response_sheet = requests.get(url=ENDPOINT)
        response_sheet.raise_for_status()
        self.destination_data = response_sheet.json()["prices"]
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city['iataCode']
                }
            }
            response = requests.put(
                url=f"{ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

