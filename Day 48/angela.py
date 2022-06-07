from selenium import webdriver 
from selenium.webdriver.common.keys import Keys


chrome_driver_path ="C:\\Users\\HP\\Desktop\\100 PROJECTS\\Day 48\\chromedriver_win32\\chromedriver.exe"


driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")


dayo = driver.find_element_by_name('fName')
dayo.send_keys('Dayo')
surn = driver.find_element_by_name('lName')
surn.send_keys('Adeniyi')
mail = driver.find_element_by_name('email')
mail.send_keys("adedayo@gmail.com")
click = driver.find_element_by_tag_name('button')
click.send_keys(Keys.ENTER)

