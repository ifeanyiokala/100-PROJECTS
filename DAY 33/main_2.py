from datetime import datetime
from inspect import Parameter
from urllib import response
import requests
from datetime import datetime
import smtplib

MY_LAT = 51.507351
MY_LNG = -0.127758

my_email = "bbforlife998@yahoo.com"
password_1 = "badboysforlife"




# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# response.raise_for_status()


# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]


# iss_position = (longitude, latitude)

# print(iss_position)
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted":0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

response.raise_for_status()

data = response.json()
sunrise = int(data["results"]['sunrise'].split("T")[1].split(":")[0])
sunset =  int(data["results"]["sunset"].split("T")[1].split(":")[0])



print(sunrise)
print(sunset)

time_now = datetime.now()

if time_now == sunset + 2 :
    
    with smtplib.SMTP('smtp.mail.yahoo.com') as connection:
        connection.starttls()
        connection.login(my_email, password_1)
        connection.sendemail(
                from_addr=my_email, 
                to_addrs=my_email, 
                msg=f"Subject:ISS\n\n Look Up Bro")





# print(response.status_code)

