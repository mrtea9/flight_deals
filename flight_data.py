from flight_search import FlightSearch
from notification_manager import NotificationManager


class FlightData:

    def __init__(self, data_prices):
        self.flight_search = FlightSearch()
        self.data_prices = data_prices
        self.notification_manager = NotificationManager()

    def find_flight(self):
        for data in self.data_prices:
            cheaper_flight = self.flight_search.search_flight(data['iataCode'])
            lowest_price = cheaper_flight['price']
            code_to = cheaper_flight['flyTo']
            # date_from = cheaper_flight['utc_arrival']
            # date_to = cheaper_flight['utc_departure']
            print(lowest_price, data['lowestPrice'])
            if lowest_price < data['lowestPrice']:
                result = f"Low price alert! Only ${lowest_price} " \
                         f"to fly from Chisinau-KIV to {data['city']}-{code_to}"
                self.notification_manager.send_sms(result)
