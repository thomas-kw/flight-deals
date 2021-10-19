#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager

sheet_endpoint = "https://api.sheety.co/39441e5d38b8d71a96bbb5417bbbeb42/flightDeals/prices"

# sheet_headers = {
#     "authorization": "Bearer evianwater"
# }

response = requests.get(url=sheet_endpoint)
sheet_data = response.json()
print(sheet_data)

# sheet_data = dict(prices=[{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2},
#                           {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3},
#                           {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4},
#                           {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5},
#                           {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6},
#                           {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7},
#                           {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8},
#                           {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9},
#                           {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}])


flight_search = FlightSearch(sheet_data)

print(flight_search.check_iata())
print(sheet_data)

data_manager = DataManager(sheet_data)

data_manager.add_iata()


