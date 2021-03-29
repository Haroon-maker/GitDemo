import threading
import time
from datetime import timedelta
from datetime import datetime

# import self as self
from selenium import webdriver

now = datetime.now()
run_at = now + timedelta(minutes=20)
delay = (run_at - now).total_seconds()
time.sleep(delay)

driver = webdriver.Chrome(executable_path="C:\\Users\\Haroon\\Downloads\\chromedriver.exe")
driver.get("https://www.opentimeclock.com/free.html")
time.sleep(3)
driver.find_element_by_id('txtUser').send_keys('676817')
driver.find_element_by_id('txtPassword').send_keys('h@roon321')
time.sleep(3)
driver.find_element_by_id("//div[@style='text-align:right;']/button[3]").click()