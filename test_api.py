import requests

search_fly_endpoint = "https://tequila-api.kiwi.com/v2/search"

params = {
    "fly_from": "HK",
    "fly_to": "SHA",
    "dateFrom": "01/08/2021",
    "dateTo": "02/08/2021",
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


print(
    f"flight.no. origin   dest    {params['curr']}   departure    arrival    duration    ")
for flight in flights:

    print(flight['route'][0]['airline'],
          flight['route'][0]['operating_flight_no'],
          flight["flyFrom"],
          flight["flyTo"],
          flight["price"],
          flight["local_departure"],
          flight["local_arrival"],
          round(flight["duration"]["total"]/3600, 1),


          )
