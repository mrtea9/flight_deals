from data_manager import DataManager
from flight_data import FlightData


data = DataManager()
flight_data = FlightData(data.data_prices)

data.update_city_code()

flight_data.find_flight()

