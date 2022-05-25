
from bs4 import BeautifulSoup
import requests
import smtplib
import os

PSWD = os.environ.get("PSWRD")
response = requests.get("https://www.amazon.com/Nike-Mens-Air-Force-Supreme/dp/B08RZH6P7Z/ref=sr_1_1?crid=18HOXSVEENEE9&keywords=Nike%2BMens%2BAir%2BForce%2B1%2BLow%2BSupreme%2B-%2BMini%2BCu9225%2BBox%2BLogo%2BSize&qid=1653407415&sprefix=nike%2Bmens%2Bair%2Bforce%2B1%2Blow%2Bsupreme%2B-%2Bmini%2Bcu9225%2Bbox%2Blogo%2Bsize%2Caps%2C322&sr=8-1&th=1&psc=1",
                        headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
                                 "Accept-Language":"en-US,en;q=0.9"}
                        )

url = "https://www.amazon.com/Nike-Mens-Air-Force-Supreme/dp/B08RZH6P7Z/ref=sr_1_1?crid=18HOXSVEENEE9&keywords=Nike%2BMens%2BAir%2BForce%2B1%2BLow%2BSupreme%2B-%2BMini%2BCu9225%2BBox%2BLogo%2BSize&qid=1653407415&sprefix=nike%2Bmens%2Bair%2Bforce%2B1%2Blow%2Bsupreme%2B-%2Bmini%2Bcu9225%2Bbox%2Blogo%2Bsize%2Caps%2C322&sr=8-1&th=1&psc=1"
web_page = response.text

stew = BeautifulSoup(web_page,"html.parser")

heading = stew.find(name='span', class_="a-offscreen")

title_old = stew.find(id="productTitle", class_="a-size-large product-title-word-break")

title = title_old.text



price = heading.text

new_price = price.split("$")[1]

prices = 300

if float(new_price) < float(prices) :
    message = f"{title} is now {prices}"

    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        result = connection.login("bbforlife998@yahoo.com",PSWD)
        connection.sendmail(
            from_addr="bbforlife998@yahoo.com",
            to_addrs="bbforlife998@yahoo.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"

        )
