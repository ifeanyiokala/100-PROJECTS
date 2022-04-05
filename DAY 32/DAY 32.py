# import needed modules
from datetime import datetime
import smtplib
import pandas as pd
import random


my_email = "bbforlife998@yahoo.com"
password_1 = "badboysforlife"
# Assigning the month and day to a variable 
today = datetime.now()
today_tuple = (today.month, today.day)
print(today_tuple)


# Use pandas to read the csv file
data =  pd.read_csv("birthdays.csv")

# Use dictionary comprehension to create a dictionary from the csv file 
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
print(birthdays_dict)
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        birthday_person["email"]


    with smtplib.SMTP('smtp.mail.yahoo.com',465) as connection:
        connection.starttls()
        connection.login(my_email, password_1)
        connection.sendemail(
                from_addr=my_email, 
                to_addrs=birthday_person["email"], 
                msg=f"Subject:Happy Birthday\n\n{contents}"
)
