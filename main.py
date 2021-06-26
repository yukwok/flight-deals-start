import requests
from data_manager import DataManager
from flight_data import FlightData
import pprint

dataManager = DataManager()
flight_data = FlightData()
cities = dataManager.get_destination_data()

print(cities)

for city in cities:
    if(city["iataCode"] == ""):
        unknown_iata_city = city["city"]

        city['iataCode'] = flight_data.find_iatacode(city=unknown_iata_city)
    print(city['iataCode'])


# --- update iata column
dataManager.update_destination_codes(cities=cities)
