#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import json
import requests
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager


flight = FlightSearch()
dt = DataManager()

# response = requests.get(url="https://api.sheety.co/43161fbeb3ed1a545a15cd95e7fc12cc/copyOfFlightDeals/prices")


# headers={
#     "apikey" : "odmj6vp0kmN26auxSIbCCsaFFQqyRN4w"
# }

# query = {
#     "term": "Paris",
#     "location_types" : "city"
# }

# place = requests.get(url="https://tequila-api.kiwi.com/locations/query", headers=headers, params=query)

# peace = place.json()["locations"][0]["code"]

# print(peace)

new_url = "https://api.sheety.co/43161fbeb3ed1a545a15cd95e7fc12cc/copyOfFlightDeals/prices"

response = requests.get(url=new_url)

print(response.text)


# sheet_data = response.json()["prices"]



# for i in sheet_data:
#     i["iataCode"] = flight.get_destination_code()



dt.update()


