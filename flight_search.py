import requests

TEQUILA_ENDPOINT = "http://tequila-api.kiwi.com/"
TEQUILA_API_KEY = "ewavzYF5kS0frIaQMDl9d6D0IpNm-d3l"

headers = {
    "apikey": TEQUILA_API_KEY
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, cities):
        city_codes = []
        for city in cities:
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}locations/query",
                params={"term": city},
                headers=headers
            )
            city_data = response.json()
            city_codes.append(city_data["locations"][0]["code"])
        return city_codes


city_list = ["Paris", "London", "Tokyo"]

flight_search = FlightSearch()
list_1 = flight_search.get_destination_code(city_list)
print(list_1)