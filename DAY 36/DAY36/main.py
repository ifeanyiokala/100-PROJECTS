#imported the needed modules 
import requests
import os
from twilio.rest import Client


#stored confidential details as enviromental variables
account_sid =  os.environ.get("OWM_API_SID")
auth_token =  os.environ.get("OWM_API_TKN") 

#stored the required parameters for the api in a dictionary
parameters = { 
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "TSLA",
    "apikey" :  os.environ.get("OWM_API_KEY_1")
}

parameters_2 = {
    "q" : "Tesla",
    "from" : "2022-04-09",
    "apikey" :  os.environ.get("OWM_API_KEY_2")
}

# intialized the twilio client 
client = Client(account_sid, auth_token)

# called on the necessary api's
response = requests.get(url="https://www.alphavantage.co/query", params = parameters )

news = requests.get(url="https://newsapi.org/v2/everything", params = parameters_2 )

# raises a http error if one occurs
response.raise_for_status()
news.raise_for_status()

# selected a key value ['Time Series (Daily)'] from response 
tsla_data_1 = response.json()['Time Series (Daily)']
# stored the list comprehension in tsla_data
#called only the value items in tsla_data_1 dictionary
tsla_data = [value for (key,value) in tsla_data_1.items()]

yesterday_data = tsla_data[0]["4. close"]

before_yesterday_data = tsla_data[1]["4. close"]
# performed a subtraction between the 
difference = (float(yesterday_data) - float(before_yesterday_data))


    
# calulate the percentage rise or fall in the stocks
percentage = round((difference/float(yesterday_data)) * 100)

if percentage > 0:
    value = f" TSLA: 🔺{percentage}"
else :
    value = f" TSLA:🔻{percentage}"

# sliced out dictionary key "articles"
tsla_news = news.json()["articles"]

msg_title = tsla_news[:3]

formatted_msg = [ f"{value} Headline: {tsla_news['title']}. \n Brief: {tsla_news['description']}" for tsla_news in msg_title]


for article in formatted_msg :
         x = ''.join(article)
message = client.messages \
        .create(
                     body=x,
                     from_='+16098811120',
                     to='+2349079465914'

        )

