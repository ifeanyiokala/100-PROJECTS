# importing the needed modules 
from datetime import datetime
import requests
import os 

# stored the current date and time in a variable "today"
today = datetime.now()
# stored certain details as enviromental variables 
# OS module in Python provides functions for interacting with the operating system.
USERNAME = os.environ.get("OWM_API_USRNME")
TOKEN = os.environ.get("OWM_API_TKN")
GRAPH_ID = "graph1"
TODAY_1 = today.strftime("%Y%m%d")
pixela_endpoint = "https://pixe.la/v1/users"

# needed details required to create the pixela user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# made a post requests to create a pixela user account
response = requests.post(url=pixela_endpoint, json=user_params)

# The requests.Response() Object contains the server's response to the HTTP request.
# used to check for errors
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# needed paramters for the api stored in a dictionary
graph_config = {
    "id":"GRAPH_ID",
    "name": "Cycling Graph",
    "unit": "Pages",
    "type": "float",
    "color": "ajisai"
}

# url needed for the api
graph_new_point = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# parameters needed to post in piexla
graph_2 = {
# The strftime() function is used to convert date and time objects to their string representation.
# "%Y%m%d" gives you the year,month and day as an output with no spaces
    "date":today.strftime("%Y%m%d"),
# users will input the number of pages covered which will in turn be posted to the pixlia graph
    "quantity":input("How many pages did you cover today ?")
}

# authentication token
headers = {
    "X-USER-TOKEN": TOKEN
}
# made a post request to store the users input as a pixel in pixelia
response = requests.post(url=graph_new_point, json=graph_2, headers=headers)
print(response.text)

# specified a specific datetime
TODAY_2 = datetime(year=2022,month=4,day=10)
 
graph_new_point_PUT = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY_2.strftime('%Y%m%d')}"
graph_3= {
    "quantity":"8"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# made a post request to update and already existing data within my pixelia graph
response = requests.put(url=graph_new_point_PUT, json=graph_3, headers=headers)
print(response.text)

# made a delete request to delete an already existing pixel
graph_new_point_DEL = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY_2.strftime('%Y%m%d')}"
response = requests.delete(url=graph_new_point_DEL, headers=headers)
print(response.text)