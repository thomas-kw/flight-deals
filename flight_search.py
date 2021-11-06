import requests
import os
from flight_data import FlightData
import datetime as dt
from pprint import pprint

TEQUILA_ENDPOINT = "http://tequila-api.kiwi.com/"
TEQUILA_API_KEY = os.environ["TEQUILA_KEY"]

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

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):

        print(f"Checking flights for {destination_city_code}")
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "curr": "GBP",
            "flight_type": "round",
            "one_for_city": 1,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 30,
            "max_stopovers": 0,
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}v2/search",
            headers=headers,
            params=query
        )

        try:
            data = response.json()["data"][0]
            pprint(data)
            print(f"{destination_city_code} {data['price']}")

        except IndexError:
            print(f"No flights found for {destination_city_code} with 0 stopovers, searching with 1 stopover:")

            try:
                ''' ISSUE: THIS MAX STOPOVER NUMBER IS THE NUMBER OF STOP OVERS OVER THE ENTIRE ROUND TRIP, MEANING
                  1 MAX STOP OVER IS A ROUND TRIP WITH 3 SEPARATE FLIGHTS, AND 2 MAX STOP OVER IS 4 SEPARATE FLIGHTS
                  
                  BUG: IF 3 SEPARATE FLIGHTS, THE VIA CITY MAY BE WRONG, IF THE FIRST FLIGHT IS NON STOP
                  AND THE RETURN FLIGHT HAS A STOPOVER, THIS NEEDS FIXING BY SEPARATING OUT THE DIFFERENT INTERMEDIARY 
                  CITIES.
                  '''
                query["max_stopovers"] = 1
                response = requests.get(
                    url=f"{TEQUILA_ENDPOINT}v2/search",
                    params=query,
                    headers=headers
                )

                data = response.json()["data"][0]
                pprint(data)
                print(f"{destination_city_code} {data['price']} with 1 stopover in {data['route'][0]['cityTo']}")

            except IndexError:
                print("No flights available, even with 1 stopover.")

            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][0]["cityTo"],
                    destination_airport=data["route"][0]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][1]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data['route'][0]['cityTo']
                )
                return flight_data


        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            return flight_data


### TEST ####
tomorrow = (dt.datetime.now() + dt.timedelta(days=1)).strftime("%d/%m/%Y")
six_months_time = (dt.datetime.now() + dt.timedelta(weeks=26)).strftime("%d/%m/%Y")

flight = FlightSearch()
result = (flight.check_flights("LON", "SFO", tomorrow, six_months_time))
print(result.via_city)
