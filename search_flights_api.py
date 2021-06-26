import requests
import datetime as datetime


search_fly_endpoint = "https://tequila-api.kiwi.com/v2/search"


today = datetime.datetime.now()
today_short = today.strftime("%d/%m/%Y")
thirty_days_later = today + datetime.timedelta(days=30)
thirty_days_later_short = thirty_days_later.strftime("%d/%m/%Y")
six_months_later = today + datetime.timedelta(days=30*6)
six_months_later_short = six_months_later.strftime("%d/%m/%Y")


params = {
    "fly_from": "HK",
    "fly_to": "SHA",
    "dateFrom": today_short,
    "dateTo": six_months_later_short,
    "curr": "HKD",
    "max_stopovers": 0


}

headers = {
    "apikey": "C_RSzwk5vah_aC6NPg5D8PqVtrTso5Fz",
}

response = requests.get(url=search_fly_endpoint,
                        params=params, headers=headers)

print(f"Status Code:{response.status_code}")

flights = response.json()["data"]

print(flights[0]['route'][0])
print(f"No. of suggested Flights:{len(flights)}")

cheapest_flight_charges = 99999999.0

print(
    f"flight.no. origin   dest    {params['curr']}   departure    arrival    duration    ")
for flight in flights:
    if cheapest_flight_charges > flight["price"]:
        cheapest_flight_airline = flight['route'][0]['airline']
        cheapest_flight_no = flight['route'][0]['operating_flight_no']
        cheapest_flight_flyFrom = flight["flyFrom"]
        cheapest_flight_flyTo = flight["flyTo"]
        cheapest_flight_departtime = flight["local_departure"]
        cheapest_flight_arrvtime = flight["local_arrival"]
        cheapest_flight_duration = round(flight["duration"]["total"]/3600, 1),
        cheapest_flight_charges = flight["price"]

    print(flight['route'][0]['airline'],
          flight['route'][0]['operating_flight_no'],
          flight["flyFrom"],
          flight["flyTo"],
          flight["price"],
          flight["local_departure"],
          flight["local_arrival"],
          round(flight["duration"]["total"]/3600, 1),
          )

cheapest_flight_details = f"{cheapest_flight_airline}{cheapest_flight_no} {cheapest_flight_flyFrom}-{cheapest_flight_flyTo} HKD{cheapest_flight_charges} {cheapest_flight_departtime}-{cheapest_flight_arrvtime}"
print(cheapest_flight_details)
