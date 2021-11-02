# #This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
import datetime as dt

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = (dt.datetime.now() + dt.timedelta(days=1)).strftime("%d/%m/%Y")
six_months_time = (dt.datetime.now() + dt.timedelta(weeks=26)).strftime("%d/%m/%Y")

for row in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        row["iataCode"],
        from_time=tomorrow,
        to_time=six_months_time
    )

    print(flight.price)
    print(flight.destination_airport)
    print(flight.out_date)
    print(flight.return_date)
