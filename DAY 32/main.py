# import smtplib

# my_email = "bbforlife998@yahoo.com"
# password_1 = "badboysforlife"

# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user =my_email, password=password_1)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="bbforlife298@gmail.com", 
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )


# import datetime as dt 

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
# # if year == 2022:
#     # print(type(year))

# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)

#importing the needed libraries 

# from calendar import weekday
# Import the needed modules
# import datetime as dt
# from multiprocessing import connection 
# import smtplib
# import random

# my_email = "bbforlife998@yahoo.com"
# password_1 = "badboysforlife"

# #assign the now method to a variable 
# now = dt.datetime.now()
# # assign the weekday method to a list 
# weekday = now.weekday()
# if weekday == 5:
#     with open("quotes.txt") as quote_file:
#         # convert quote_file to a list
#         all_quotes = quote_file.readlines()
#         # assign a random list from all_quotes to a variable
#         quote = random.choice(all_quotes)

    
#     print(quote)
#     #created a class 
#     with  smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#         connection.starttls()
#         connection.login(my_email, password_1)
#         connection.sendmail(
#             from_addr=my_email, 
#             to_addrs=my_email, 
#             msg=f"Subject: Monday Motivation \n\n{quote}"
#         )

    

def naive(a,b):
    y = b
    z = 0 
    while a > 0 :
        z = z + y 
        a = a - 1
    return z 


print(naive(10,2))


