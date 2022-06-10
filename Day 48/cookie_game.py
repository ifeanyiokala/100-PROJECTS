from time import sleep,time

from selenium import webdriver 
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys


chrome_driver_path ="C:\\Users\\HP\\Desktop\\100 PROJECTS\\Day 48\\chromedriver_win32\\chromedriver.exe"


driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")


new = driver.find_element_by_xpath('//*[@id="cookie"]')

# new.send_keys(Keys.ENTER)
# day = True
# while day :
# # for i in range(50):
#     new.click()




price_7 = driver.find_element_by_xpath('//*[@id="buyCursor"]')
price = driver.find_element_by_id("money")
prices = int(price.text)
# if prices > 15:
#     price_7.click()
    
    



def check():
    prices = (price.text)
    prices = int(prices.replace(',',''))
    if prices > 123456789:
        price_1 = driver.find_element_by_xpath('//*[@id="buyTime machine"]')
        price_1.click()
    elif prices > 1000000:
        price_2 = driver.find_element_by_xpath('//*[@id="buyPortal"]')
        price_2.click()
    elif prices > 50000:
        price_3 = driver.find_element_by_xpath('//*[@id="buyAlchemy lab"]')
        price_3.click()
    elif prices > 7000:
        price_4 = driver.find_element_by_xpath('//*[@id="buyShipment"]')
        price_4.click()
    elif prices > 2000:
        price_5 = driver.find_element_by_xpath('//*[@id="buyMine"]')
        price_5.click()
    elif prices > 500:
        price_6 = driver.find_element_by_xpath('//*[@id="buyFactory"]')
        price_6.click()
    elif prices > 100:
        price_8 = driver.find_element_by_xpath('//*[@id="buyGrandma"]')
        price_8.click()
    else :
        price_7 = driver.find_element_by_xpath('//*[@id="buyCursor"]')
        price_7.click()


b = time()   
a = time()
day = True
while day :

    # for i in range(50):
    new.click()
    
    if time() - a >= 5 :
        check()
        a = time()
    if time() - b >= 300 :
        day = False
        final = driver.find_element_by_xpath('//*[@id="cps"]')
        print(final.text)

    
    # check()
# a = time()
# sleep(6)

# if time() - a >= 5 :
    # check()
    # a = time()
# print(price.text)
# click = driver.find_element_by_tag_name('button')
# click.send_keys(Keys.ENTER)
