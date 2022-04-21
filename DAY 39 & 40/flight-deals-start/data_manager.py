import requests

response = requests.get(url="https://api.sheety.co/43161fbeb3ed1a545a15cd95e7fc12cc/copyOfFlightDeals/prices")

# URLS = "https://api.sheety.co/43161fbeb3ed1a545a15cd95e7fc12cc/copyOfFlightDeals/prices/2"

class DataManager:
    def update(self):
        for i in range(2,11):
            header = {
                "price":{
                    "iataCode" : ""
            }
        }
            URLS = f"https://api.sheety.co/43161fbeb3ed1a545a15cd95e7fc12cc/copyOfFlightDeals/prices/{i}"
            response = requests.put(url = URLS, json=header )
        #This class is responsible for talking to the Google Sheet.

response = requests.get(url="https://api.sheety.co/43161fbeb3ed1a545a15cd95e7fc12cc/copyOfFlightDeals/prices")


# sheet_data = response.json()["prices"]



# for i in sheet_data:
#     i["iataCode"] = flight.get_destination_code()
