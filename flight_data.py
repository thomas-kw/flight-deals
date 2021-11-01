import requests
from datetime import datetime

TEQUILA_ENDPOINT = "http://tequila-api.kiwi.com/"
TEQUILA_API_KEY = "ewavzYF5kS0frIaQMDl9d6D0IpNm-d3l"


class FlightData:
    # This class is responsible for structuring the flight data.

    def __init__(self):
        self.price = 0
        self.departure_airport_code = ""
        self.departure_city = ""

    def get_flight_data(self, city_code):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"fly_from": "LON", "fly_to": city_code, "date_from": "30/11/2021", "date_to": "30/01/2022",
                 "curr": "GBP", "flight_type": "round", "nights_in_dst_from": 7, "nights_in_dst_to": 28,
                 "max_stopovers": 0, "asc": 1}
        response = requests.get(url=f"{TEQUILA_ENDPOINT}search", params=query, headers=headers)
        results = response.json()["data"][0]["price"]
        return results


# flight_1 = FlightData()
# flight_data = flight_1.get_flight_data()["data"][0]["price"]
# print(flight_data)