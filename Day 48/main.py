from html.parser import HTMLParser
from optparse import Option
from ssl import Options
from turtle import home
from selenium import webdriver 
from bs4 import BeautifulSoup
from selenium.webdriver.chrome import options
chrome_driver_path ="C:\\Users\\HP\\Desktop\\100 PROJECTS\\Day 48\\chromedriver_win32\\chromedriver.exe"
 
opts = options.Options()

opts.headless = True

driver = webdriver.Chrome(executable_path=chrome_driver_path,options=opts)

# driver.get("https://www.amazon.com/NIKE-Vapormax-924453-004-Triple-Running/dp/B09LH25LJZ/ref=sr_1_1?crid=2LCZGO100NEBW&keywords=nike%2Bvapour&qid=1653395292&sprefix=nike%2Bvapour%2Caps%2C1830&sr=8-1&th=1")

driver.get("https://www.python.org/")

# soup = driver.find_element_by_name("q")

# logo = driver.find_element_by_class_name("python-logo")

# logo = driver.find_element_by_css_selector

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")

# x_path = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')

# print(x_path.text)
home = {}
for i in range(1,6):
    time = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{i}]/time')

    new_time = time.text + "-2022"

    find = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{i}]/a')

    title = find.text

    final = {"time":new_time,"name":title}
    for i in range(0,5):
        home = {i:final}
    
    

print(home)

# //*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[1]/time


# //*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[2]/time
# content = driver.page_source

# stew = BeautifulSoup(content,"html.parser")

# soup = stew.findAll('span',class_='a-offscreen')

# small = soup[0]

# print(small.text)

driver.close()



driver.quit()



