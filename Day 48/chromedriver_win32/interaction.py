from selenium.webdriver.chrome import options
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys


chrome_driver_path ="C:\\Users\\HP\\Desktop\\100 PROJECTS\\Day 48\\chromedriver_win32\\chromedriver.exe"
 
# opts = options.Options()

# opts.headless = True

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")


# documentation_link = driver.find_element_by_css_selector(".mp-bordered a")

# print(documentation_link)

# temi = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')



# print(temi.text)

# temi.click()

# dayo = driver.find_element_by_link_text("Mariano Moreno")
dayo = driver.find_element_by_name("search")
dayo.send_keys('Ferrari')
dayo.send_keys(Keys.ENTER)
# press = driver.find_element_by_id("searchButton")
# press.click()
# dayo.click()/