from selenium import webdriver

from selenium.webdriver.common.keys import Keys


chrome_driver_path ="/home/ifeanyi/100-PROJECTS/Day 48/chromedriver_win32/chromedriver_1.exe"
# fox_path = '/home/ifeanyi/100-PROJECTS/Day 48/geckodriver.exe'
# fp = webdriver.FirefoxProfile('/home/ifeanyi/snap/firefox/common/.mozilla/firefox/vcz3mobu.default')
# car = webdriver.Firefox(firefox_profile=fp)
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver = webdriver.Firefox(executable_path=fox_path)

driver.get("https://goal.com")


# dayo = driver.find_element_by_name('fName')
# dayo.send_keys('Dayo')
# surn = driver.find_element_by_name('lName')
# surn.send_keys('Adeniyi')
# mail = driver.find_element_by_name('email')
# mail.send_keys("adedayo@gmail.com")
# click = driver.find_element_by_tag_name('button')
# click.send_keys(Keys.ENTER)
#
