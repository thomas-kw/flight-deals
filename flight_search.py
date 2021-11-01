import requests

TEQUILA_ENDPOINT = "http://tequila-api.kiwi.com/"
TEQUILA_API_KEY = "ewavzYF5kS0frIaQMDl9d6D0IpNm-d3l"

headers = {
    "apikey": TEQUILA_API_KEY
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city):
        response = requests.get(
                url=f"{TEQUILA_ENDPOINT}locations/query",
                params={"term": city},
                headers=headers
            )

        results = response.json()
        code = results["locations"][0]["code"]
        return code
