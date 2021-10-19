import requests

sheet_endpoint = "https://api.sheety.co/39441e5d38b8d71a96bbb5417bbbeb42/flightDeals/prices/"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, sheet):
        self.sheet = sheet

    def add_iata(self):
        for id in self.sheet["prices"]:
            id_number = str(id["id"])
            print(id_number)
            print(sheet_endpoint + id_number)

            sheet_input = {
                "price": {
                    "iata code": "Testing"
                }
            }

            sheet_put = requests.put(url=sheet_endpoint + id_number, json=sheet_input)
            print(sheet_put.text)
