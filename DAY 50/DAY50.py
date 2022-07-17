# Building A Tinder Bot

# Importing the needed modules

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.keys import Keys

chrome_driver_path ="/home/ifeanyi/100-PROJECTS/Day 48/chromedriver_win32/chromedriver_1.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://tinder.com/')
main_page = driver.current_window_handle

log_in = driver.find_element(By.XPATH,'//[@id="c1200009088"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
log_in.click()




sleep(4)

log_in_num = driver.find_element(By.XPATH, '//*[@id="t108358321"]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')


log_in_num.click()



for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle
        driver.switch_to.window(login_page)

sleep(5)

my_email = driver.find_element(By.XPATH, '//*[@id="email"]')
my_email.send_keys('okala_ifeanyi@yahoo.com')


my_password = driver.find_element(By.XPATH, '//*[@id="pass"]')
my_password.send_keys('mumoli')

my_password.send_keys(Keys.ENTER)

driver.switch_to.window(main_page)

sleep(5)

my_password.send_keys(Keys.ENTER)

# /html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/form/div[2]/div[2]/div/div[1]/button[1]
# accept_loc_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/button')
# accept_loc_button.click()

# boot_button = driver.find_element(By.XPATH, '')
# boot_button.click()



# gender_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/form/div[7]/button')
# gender_button.click()


