from bs4 import BeautifulSoup
import requests
import smtplib

response= requests.get("https://www.amazon.com/NIKE-Vapormax-924453-004-Triple-Running/dp/B09LH25LJZ/ref=sr_1_1?crid=2LCZGO100NEBW&keywords=nike%2Bvapour&qid=1653395292&sprefix=nike%2Bvapour%2Caps%2C1830&sr=8-1&th=1")



web_page = response.text

stew = BeautifulSoup(web_page,"html.parser")

# heading =for i in stew.findAll(name='span', class_="a-offscreen")

print(heading)


# <span class="a-price a-text-price a-size-medium apexPriceToPay" data-a-size="b" data-a-color="price"><span class="a-offscreen">$799.99</span><span aria-hidden="true">$799.99</span></span>
