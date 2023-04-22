class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, departure_airport_code, departure_city):
        self.price = price
        self.departure_airport_code = departure_airport_code
        self.departure_city = departure_city

    def __str__(self):
        return f"Price:{self.price}, departure_airport_code: {self.departure_airport_code}, departure_city: {self.departure_city}"