# #This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_data import FlightData

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch

    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

# thecitylist = [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2},
#        {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3},
#        {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4},
#        {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5},
#        {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6},
#        {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7},
#        {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8},
#        {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9},
#        {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}]

flight_data = FlightData()

for row in sheet_data:
    print(flight_data.get_flight_data(row["iataCode"]))