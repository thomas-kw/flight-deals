import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/39441e5d38b8d71a96bbb5417bbbeb42/flightDeals/prices"
CUSTOMER_EMAILS_ENDPOINT = "https://api.sheety.co/39441e5d38b8d71a96bbb5417bbbeb42/flightDeals/users"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )

    def get_customer_emails(self):
        customers_endpoint = CUSTOMER_EMAILS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
