import requests
from datetime import datetime, timedelta


FLIGHTS_ENDPOINT = 'https://api.tequila.kiwi.com'
API_KEY = ''


class FlightSearch:

    def __init__(self):
        self.endpoint_city = f"{FLIGHTS_ENDPOINT}/locations/query"
        self.endpoint_search = f"{FLIGHTS_ENDPOINT}/search"
        self.fly_from = "RMO"
        self.api_key = API_KEY
        self.header = {
            "apikey": self.api_key
        }

    def get_city_code(self, city):
        parameters = {
            "term": city
        }
        response = requests.get(url=self.endpoint_city, params=parameters, headers=self.header, verify=False)
        response.raise_for_status()
        data = response.json()
        city_code = data['locations'][0]['code']
        return city_code

    def search_flight(self, city):
        tomorrow = datetime.today() + timedelta(days=1)
        tomorrow_date = tomorrow.strftime("%d/%m/%Y")
        six_months_later = datetime.today() + timedelta(days=183)
        six_months_later_date = six_months_later.strftime("%d/%m/%Y")
        parameters = {
            "fly_from": self.fly_from,
            "fly_to": city,
            "date_from": tomorrow_date,
            "date_to": six_months_later_date,
        }
        response = requests.get(url=self.endpoint_search, params=parameters, headers=self.header, verify=False)
        response.raise_for_status()
        data = response.json()
        return data['data'][0]
