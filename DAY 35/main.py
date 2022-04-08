#imported the needed modules
import requests 
from pprint import pprint
import os
from twilio.rest import Client

#stored confidential data as enviroment variables 
account_sid = os.environ.get("OWM_API_SID")
auth_token = os.environ.get("OWM_API_TKN")
api_key = os.environ.get("OWM_API_KEY")
#parameters needed by the api 
parameters = {
    "lat": "42.360081",
    "lon": "-71.058884",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

#request to use a certain api 
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params = parameters)

#test for error 
response.raise_for_status()

#assigned response.json it to a variable
weather_data = response.json()


will_rain = False 
#selected only the first 12 hours of the dataset
for x in weather_data['hourly'][:12]:
    num = x['weather'][0]['id']
    #any id below 700 signifies that rain will fall 
    if num < 700:
        will_rain = True

# will_rain becomes true when id is below 700
# the message is written from the sender to the reciever      
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain today,remeber to bring an ☂️",
                     from_='+16098811120',
                     to='+2348060613915'
    
    )
    print(message.status)



   

