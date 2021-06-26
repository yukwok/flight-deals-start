import requests
from data_manager import DataManager
from flight_data import FlightData
import pprint

dataManager = DataManager()
flight_data = FlightData()
cities = dataManager.get_destination_data()


for city in cities:
    if(city["iataCode"] == ""):
        city['iataCode'] = flight_data.find_iatacode(city=city["city"])
        print(city['iataCode'])


# --- find iata code
KIWI_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"

params = {

    "term": "shanghai",  # --- location
}

headers = {
    "apikey": "C_RSzwk5vah_aC6NPg5D8PqVtrTso5Fz",
}

response = requests.get(url=KIWI_ENDPOINT, params=params, headers=headers)

location_id = response.json()['locations'][0]['code']
pprint.pprint(f"Location ID: {location_id}")


# --- update iata column
# dataManager.update_destination_codes(cities=cities)
