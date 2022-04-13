#imported the needed modules
from datetime import datetime
import requests
from pprint import pprint
import os

# stored the app id and key as enviromental variables
APP_ID = os.environ.get("WRK_API_ID")
API_KEY = os.environ.get("WRK_API_KEY")
# called the datetime module and stored it in a variable
today = datetime.now()

# stored the need parameters for the nurtition api
graph_1 = {
 "query": input("How many miles did you cover"),
 "gender":"female",
 "weight_kg":"72.5",
 "height_cm":"167.64",
 "age":"30"
}

# needed parameters for the nutrition api
headers={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
}

# made a post request to the api 
response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", headers=headers,json = graph_1)
# stored the response as a json 
read = response.json()

# The strftime() function is used to convert date and time objects 
today_date = today.strftime("%d/%m/%Y")
today_time = today.strftime("%X")
end_point = os.environ.get("WRK_API_SHEET_KEY")

headers_1 ={
    "Authorization" : os.environ.get("WRK_API_AUTHO")
}
for i in read["exercises"]:
    inputs = {
        "workout":{
                "date":today_date,
                "time":today_time,
                "exercise":i['name'],
                "duration":i["duration_min"],
                "calories":i["nf_calories"],
        }
    }

response_1 = requests.post(url=end_point, headers=headers_1, json=inputs)
