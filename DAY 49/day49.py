# DAY 49

# create a job application bot for linkedIn
# Importing the neeeded  modules

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome_driver_path ="/home/ifeanyi/100-PROJECTS/Day 48/chromedriver_win32/chromedriver_1.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0')


sign_in = driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')

sign_in.click()

sleep(5)

user_name = driver.find_element(by=By.XPATH, value='//*[@id="username"]')
user_name.send_keys('###########')
pssword = driver.find_element(by=By.XPATH, value='//*[@id="password"]')
pssword.send_keys('@@@@')
clicks = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')

clicks.click()



#LINKEDIN SIGN IN DOESNT ALLOW BOT'S TO LOG IN WIHTOUT VERIFICIATION,I DECIDED TO STOP SO I DON'T GET PUSHED OUT OF MY LINKEDIN
#




