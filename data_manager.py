import requests
from flight_search import FlightSearch


SHEET_ENDPOINT = 'https://api.sheety.co/ee71277f73b14d446d4e1324d0c57bc9/flightDeals/prices'


class DataManager:

    def __init__(self):
        response = requests.get(url=SHEET_ENDPOINT, verify=False)
        response.raise_for_status()
        self.data_prices = response.json()['prices']
        self.flight_search = FlightSearch()

    def update_city_code(self):
        body = {
            "price": ""
        }
        for city in self.data_prices:
            if city['iataCode'] == '':
                city_code = self.flight_search.get_city_code(city['city'])
                city['iataCode'] = city_code
                body['price'] = city
                response = requests.put(url=f"{SHEET_ENDPOINT}/{city['id']}", json=body, verify=False)
                print(response.json())

