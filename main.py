from notification_manager import NotificationManager
from flight_search import FlightSearch
import requests
from data_manager import DataManager
from flight_data import FlightData
import pprint

dataManager = DataManager()
flight_data = FlightData()
flight_search = FlightSearch()
notifyManager = NotificationManager()

# --- get the interested locations and user emails

cities = dataManager.get_destination_data()
user_list = dataManager.get_users_email_data()

user_emails = []
for user in user_list:
    print(user["email"])
    user_emails.append(user['email'])

print(user_emails)

print(cities)


for city in cities:
    if(city["iataCode"] == ""):
        unknown_iata_city = city["city"]

        city['iataCode'] = flight_data.find_iatacode(city=unknown_iata_city)
    print(city['iataCode'])


# --- update iata column
dataManager.update_destination_codes(cities=cities)


# --- cheapest flight search
cityFrom = "HK"
cities_updated_flights = []
cities_flights_sms = ""

for city in cities:
    if(city["iataCode"] != ""):
        flight_details = flight_search.cheapest_flight(
            cityFrom="HK", cityTo=city["iataCode"])
        cities_updated_flights.append(flight_details)
        cities_flights_sms = cities_flights_sms+flight_details+'\n'

print(cities_flights_sms)

# -- make sms to phone
# notifyManager.send_sms(cities_flights_sms)

notifyManager.send_emails(
    emails=user_emails, coming_cheapest=cities_flights_sms)
