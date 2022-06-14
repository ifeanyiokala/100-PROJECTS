#DAY 48
#Imported the needed modules


from time import sleep,time
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#stored the chrome driver file path in a variable
chrome_driver_path ="/home/ifeanyi/100-PROJECTS/Day 48/chromedriver_win32/chromedriver_1.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# loaded the orteil website with driver.get
driver.get("http://orteil.dashnet.org/experiments/cookie/")



# stored the the user cookie button here  in a variable
new = driver.find_element_by_xpath('//*[@id="cookie"]')


# i left my comments here so you could see my mistakes
# my trials and errors
# new = driver.find_element_by_id(".store grayed")
# print(new)

# new.send_keys(Keys.ENTER)
# day = True
# while day :
# # for i in range(50):
#     new.click()

# price_7 = driver.find_element_by_xpath('//*[@id="buyCursor"]')

# stored the players money in a variable
price = driver.find_element_by_id("money")


# prices = int
# if prices > 15:
#     price_7.click()
# boss = driver.find_element_by_('100')
# print(boss)
# boss.click()
# price_1 = driver.find_element(by=By.XPATH, value='//*[@id="buyTime machine"]')
# print(price_1.text.split('-')[1])


# stored the names of all possible things to buy in a list
# it will be used to form the xpath in a for loop below
list = ['Time machine','Portal','Alchemy lab','Shipment','Mine','Factory','Grandma','Cursor']

#created a function
def check():
    home = {}
    take = []
    # stored the price value in a variable
    prices = (price.text)
    #removed all commas so i had a pure integer value
    prices = int(prices.replace(',', ''))

    for i in list:
        # used the list which contains the list of items to buy
        take_i = driver.find_element_by_xpath(f'//*[@id="buy{i}"]')
        # stored the path as a key and the actual price as a value in a dictionary
        home[take_i] = take_i.text.split("-")[1].split("\n")[0]


    # for i in list:
    #     take_i = driver.find_element_by_xpath(f'//*[@id="buy{i}"]')
    #     home[take_i] = take_i.text.split("-")[1].split("\n")[0]
    #     # print('e no do')



    for i in home.values():
        num = int(i.replace(',',''))
        # stored  the values as integers
        if prices >= num:
            take.append(num)
    big = max(take)


    for key,value in home.items():
        value = int(value.replace(',', ''))
        if big == value:
            ifeanyi = key
            ifeanyi.click()

# stored my current time into two variables
b = time()
a = time()
day = True

while day :

    new.click()
    # after every 5 seconds the function will be called
    if time() - a >= 5 :
        check()
        a = time()
    # after 5 mintues the while looop will be stoppped
    if time() - b >= 300 :
        day = False
        final = driver.find_element_by_xpath('//*[@id="cps"]')
        print(final.text)

#The End
# One of my many many mistakes
#     if prices > 123456789:
#         price_1 = driver.find_element_by_xpath('//*[@id="buyTime machine"]')
#         price_1.click()
#     elif prices > 1000000:
#         price_2 = driver.find_element_by_xpath('//*[@id="buyPortal"]')
#         price_2.click()
#     elif prices > 50000:
#         price_3 = driver.find_element_by_xpath('//*[@id="buyAlchemy lab"]')
#         price_3.click()
#     elif prices > 7000:
#         price_4 = driver.find_element_by_xpath('//*[@id="buyShipment"]')
#         price_4.click()
#     elif prices > 2000:
#         price_5 = driver.find_element_by_xpath('//*[@id="buyMine"]')
#         price_5.click()
#     elif prices > 500:
#         price_6 = driver.find_element_by_xpath('//*[@id="buyFactory"]')
#         price_6.click()
#     elif prices > 100:
#         price_8 = driver.find_element_by_xpath('//*[@id="buyGrandma"]')
#         price_8.click()
#     else :
#         price_7 = driver.find_element_by_xpath('//*[@id="buyCursor"]')
#         price_7.click()
#
#
# b = time()
# a = time()
# day = True
# while day :
#
#     # for i in range(50):
#     new.click()
#
#     if time() - a >= 5 :
#         check()
#         a = time()
#     if time() - b >= 300 :
#         day = False
#         final = driver.find_element_by_xpath('//*[@id="cps"]')
#         print(final.text)

    
    # check()
# a = time()
# sleep(6)

# if time() - a >= 5 :
    # check()
    # a = time()
# print(price.text)
# click = driver.find_element_by_tag_name('button')
# click.send_keys(Keys.ENTER)


#Day 48,this project was really special, i barely looked at angels's solutions
# i beat angelas cookies/second,i'm getting better
# i feel a lot more confident
# There is hope