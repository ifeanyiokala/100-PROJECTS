from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



from selenium.webdriver.common.keys import Keys

TWITTER_EMAIL = 'ifeanyiokala'
TWITTER_PASSWORD = 'searchingfornade'



chrome_driver_path ="/home/ifeanyi/100-PROJECTS/Day 48/chromedriver_win32/chromedriver_1.exe"
# fox_path = '/home/ifeanyi/100-PROJECTS/Day 48/geckodriver.exe'
# fp = webdriver.FirefoxProfile('/home/ifeanyi/snap/firefox/common/.mozilla/firefox/vcz3mobu.default')
# car = webdriver.Firefox(firefox_profile=fp)
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver = webdriver.Firefox(executable_path=fox_path)
# driver.get('https://twitter.com/')
driver.get('https://fast.com/')
# sleep(5)
# sleep(40)
# go = driver.find_element(By.CSS_SELECTOR('.start-button a'))
# go.click()
#webbrouser

show_more_info_btn = driver.find_element(By.ID, 'show-more-details-link')
show_more_info_btn.click()

down_speed = driver.find_element(By.ID, 'speed-value')
print(down_speed.text)

up_speed = driver.find_element(By.ID, 'upload-value')
print(up_speed.text)

#webrowser
#
# log_in = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
# log_in.click()
#
# usr_mail = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
# usr_mail.send_keys('ifeanyiokala')
#
# usr_button = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
# usr_button.click()
#
# sleep(5)
#
# usr_password = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
# usr_password.send_keys('searchingfornade')
#
# log_in_twitter = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
#
# log_in_twitter.click()
#
# tweet = f"i didn't write this lol"


# dayo = driver.find_element_by_name('fName')
# dayo.send_keys('Dayo')
# surn = driver.find_element_by_name('lName')
# surn.send_keys('Adeniyi')/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div
# mail = driver.find_element_by_name('email')
# mail.send_keys("adedayo@gmail.com")
# click = driver.find_element_by_tag_name('button')
# click.send_keys(Keys.ENTER)
#
#
# driver.get("https://twitter.com/login")
#
# sleep(5)
#
# username = driver.find_element(By.NAME, 'text')
# username.send_keys(TWITTER_EMAIL)
# username.send_keys(Keys.ENTER)
# sleep(3)
#
# password = driver.find_element(By.NAME, 'password')
# password.send_keys(TWITTER_PASSWORD)
# password.send_keys(Keys.ENTER)
# sleep(3)
#
# # Compose and send Tweet
# message = 'Made this with python '
#
# compose_tweet = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
# compose_tweet.send_keys(message)
# sleep(5)
# send_tweet = driver.find_element(By.XPATH, "//*[text()='Tweet']")
# send_tweet.click()



# sleep(2)
# email = driver.find_element_by_xpath(
#     '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
# password = driver.find_element_by_xpath(
#     '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
#
# email.send_keys(TWITTER_EMAIL)
# password.send_keys(TWITTER_PASSWORD)
# sleep(2)
# password.send_keys(Keys.ENTER)
#
# sleep(5)
# tweet_compose = driver.find_element_by_xpath(
#     '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
#
# # tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
# tweet = 'Made this with python #TwitterBot !'
# tweet_compose.send_keys(tweet)
# sleep(3)
#
# tweet_button = self.driver.find_element_by_xpath(
#     '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
# tweet_button.click()
#
# sleep(2)
# driver.quit()
