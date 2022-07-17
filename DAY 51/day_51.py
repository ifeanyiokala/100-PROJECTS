# import the needed modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys


PROMISED_DOWN = 300
PROMISED_UP = 50
chrome_driver_path ="/home/ifeanyi/100-PROJECTS/Day 48/chromedriver_win32/chromedriver_1.exe"
SPEED_TEST_PAGE = 'https://fast.com/'
TWITTER_EMAIL = 'YOUR_EMAIL'
TWITTER_PASSWORD = 'YOUR_PASSWORD'
TWITTER_PAGE = "https://twitter.com/login"



class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    # create two methods, one for speed test
    # Another for twitter
    def get_internet_speed(self):
        # go to fast.com
        self.driver.get(SPEED_TEST_PAGE)
        # wait for a few seconds
        # it automatically calculates your speed
        sleep(20)
        # click on the more details button
        show_more_info_btn = self.driver.find_element(By.ID, 'show-more-details-link')
        show_more_info_btn.click()
        # set the attribute self.up to current upload speed
        self.up = self.driver.find_element(By.ID, 'speed-value').text
        # set the attribute self.down to the current download speed
        self.down = self.driver.find_element(By.ID, 'upload-value').text

    def tweet_at_provider(self):
        # go to twitter.com
        self.driver.get(TWITTER_PAGE)
        sleep(5)
        # enter email id of Twitter account
        username = self.driver.find_element(By.NAME, 'text')
        username.send_keys(TWITTER_EMAIL)
        username.send_keys(Keys.ENTER)
        sleep(3)
        # enter the password of the Twitter account and enter
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(7)

        # Compose and send Tweet
        message = (f'@MTNNG, why is my internet speed {self.down}down/{self.up} up when i pay for '
                  f'{PROMISED_DOWN}down/{PROMISED_UP}up ?.')

        compose_tweet = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
        compose_tweet.send_keys(message)
        sleep(7)
        send_tweet = self.driver.find_element(By.XPATH, "//*[text()='Tweet']")
        send_tweet.click()


project = InternetSpeedTwitterBot(chrome_driver_path)
project.get_internet_speed()
project.tweet_at_provider()

