# DAY 49

# create a job application bot for linkedIn
# Importing the needed  modules

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

chrome_driver_path ="/home/ifeanyi/100-PROJECTS/Day 48/chromedriver_win32/chromedriver_1.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0')


sign_in = driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')

sign_in.click()

sleep(5)

user_name = driver.find_element(by=By.XPATH, value='//*[@id="username"]')
user_name.send_keys('ifeanyi.okala.247238@unn.edu.ng')
pssword = driver.find_element(by=By.XPATH, value='//*[@id="password"]')
pssword.send_keys('mumoli1!')
clicks = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')

clicks.click()

# i need to get my verificiation password and then apply
# not necessary for everyone
# sleep(30)
sleep(10)
# easy_apply = driver.find_element(by=By.XPATH, value='/html/body/div[6]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div')

#Applying for a single Job,
#Each Job has it's own pecularities

# easy_apply = driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
# easy_apply.click()
# # for i in range(2) :
#
# next_apply_1 = driver.find_element(By.CSS_SELECTOR, 'footer button')
# next_apply_1.click()


every_body = driver.find_elements(By.CSS_SELECTOR, 'job-card-container--clickable')

for one in every_body:
    one.click()
    # sleep(5)
    print('done')

    try:
        easy_apply = driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
        easy_apply.click()
        sleep(2)
    # If you can't submit after the first click
    # please skip and continue the loop
        next_apply_1 = driver.find_element(By.CSS_SELECTOR, 'footer button')
        if next_apply_1.text == 'Next':
            dismiss = driver.find_element(By.CLASS_NAME,'artdeco-modal__dismiss')
            dismiss.click()
            discard = driver.find_element(By.CLASS_NAME,'artdeco-modal__confirm-dialog-btn')
            discard.click()
            print('here')
            continue

        else:
            next_apply_1.click()
    # skip all NosuchElementException error's
    except NoSuchElementException:
        print('error')
        continue


# I spent a long time on this project
# I was very very frustrated
# I didn't plan to finish it
# THe hustle continues
# I must keep going,no matter how hard it becomes












# //*[@id="ember344"]
# next_apply_2 = driver.find_element(By.CSS_SELECTOR, '.display-flex button')
# next_apply_2.click()
#
# visa_apply = driver.find_element(By.CSS_SELECTOR, '')
# visa_apply.click()

# submit = driver.find_element(By.XPATH,'//*[@id="ember472"]')
# submit.click()

# dave = driver.find_element_by_xpath('//*[@id="ember332"]')

# print(dave)

# allow some time for the next stage to load
#
# sleep(4)
#
# click_next = driver.find_element(by=By.ID, value=ember419')
# click_next.click()
# sleep(2)#radio-urn\:li\:fs_easyApplyFormElement\:\(urn\:li\:fs_normalized_jobPosting\:3112922017\,58935010\,multipleChoice\)_0
#
# click_review = driver.find_element(by=By.ID, value='//*[@id="ember438"]')
# click_review.click()
# sleep(2)
# click_submit = driver.find_element(by=By.XPATH, value='//*[@id="ember449"]')
# click_submit.click()
#
# print(max(-0.0,0.0))
#
# print(round(7/2))


# LINKEDIN SIGN IN DOESNT ALLOW BOTS TO LOG IN WITHOUT VERIFICATION,
# I DECIDED TO STOP SO I DON'T GET PUSHED OUT OF MY LINKEDIN







