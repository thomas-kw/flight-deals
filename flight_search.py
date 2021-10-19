class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, sheet):
        self.sheet = sheet

    def check_iata(self):
        for city in self.sheet["prices"]:
            city["iataCode"] = "Testing"
