

from selenium import webdriver 
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys


chrome_driver_path ="C:\\Users\\HP\\Desktop\\100 PROJECTS\\Day 48\\chromedriver_win32\\chromedriver.exe"


driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")


new = driver.find_element_by_xpath('//*[@id="langSelect-EN"]')
print(new)
new.send_keys(Keys.ENTER)
click = driver.find_element_by_tag_name('button')
click.send_keys(Keys.ENTER)
