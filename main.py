# #This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
import datetime as dt
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification = NotificationManager()

ORIGIN_CITY_IATA = "LON"
CURRENCY = "GBP"

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

    if flight is None:
        continue

    if flight.price < row["lowestPrice"]:
        message = f"Low price alert! Only {CURRENCY}{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(message)

        notification.send_message(message)
