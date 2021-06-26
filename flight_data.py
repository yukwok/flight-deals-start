import pprint
import requests


class FlightData:
    # This class is responsible for structuring the flight data.
    def find_iatacode(self, city="unknown") -> str:
        print(f"in find_iatacode function, city: {city}")

        # --- call iata api search
        # --- find iata code
        KIWI_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"

        params = {

            "term": city,  # --- location to find out iata
        }

        headers = {
            "apikey": "C_RSzwk5vah_aC6NPg5D8PqVtrTso5Fz",
        }

        response = requests.get(
            url=KIWI_ENDPOINT, params=params, headers=headers)

        location_id = response.json()['locations'][0]['code']
        # pprint.pprint(f"Location ID: {location_id}")

        return location_id
