import requests
SHEETY_API = "https://api.sheety.co/e02e90cc81d3e6b66814fe14bef27a3e/flightDeals/prices"
SHEETY_USERS_API = "https://api.sheety.co/e02e90cc81d3e6b66814fe14bef27a3e/flightDeals/users"


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}
        self.user_emails = {}

    def get_destination_data(self):

        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_API)
        data = response.json()
        # print(data)
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    def update_destination_codes(self, cities):

        print("updating...")

        for city in cities:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"],

                }
            }
            response = requests.put(
                url=f"{SHEETY_API}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_users_email_data(self):
        SHEETY_USERS_API = "https://api.sheety.co/e02e90cc81d3e6b66814fe14bef27a3e/flightDeals/users"

        response = requests.get(url=SHEETY_USERS_API)
        data = response.json()
        self.user_emails = data["users"]

        return self.user_emails
