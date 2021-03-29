import time
import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\Haroon\\Downloads\\chromedriver.exe")
driver.maximize_window()
driver.get("http://192.168.1.2:8007/#/accounts/login/")

time.sleep(2)
driver.find_element_by_css_selector("input[placeholder='Email']").send_keys('haroon@technologyelement.com')
driver.find_element_by_css_selector("input[placeholder='Password']").send_keys('123456789a')
driver.find_element_by_css_selector("button[type='submit']").click()
time.sleep(2)
driver.find_element_by_xpath("//body/div[@id='page-container']/div[@id='main-container']/div[@id='page-content']/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/a[1]").click()
time.sleep(2)
print(driver.find_element_by_xpath("//label[contains(text(),'Registration #')]").text)
driver.find_element_by_xpath("//input[@id='id_reg_number']").send_keys("&89879")
print(driver.find_element_by_xpath("//body/div[@id='page-container']/div[@id='main-container']/div[@id='page-content']/div[2]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/div[3]/label[1]").text)
driver.find_element_by_xpath("//input[@id='id_name']").send_keys("Haroon's corporation")
print(driver.find_element_by_xpath("//label[contains(text(),'Operating Name')]").text)
driver.find_element_by_xpath("//input[@id='id_operating_name']").send_keys("Private LTD")
driver.find_element_by_xpath()
time.sleep(6)
alldates = driver.find_element_by_xpath("//input[@id='id_start_date']")
for dateelement in alldates:
    date = dateelement.text
    print(date)
    if date== '26':
        dateelement.click()
time.sleep(2)
teamElement = driver.find_element_by_id("id_employees")
sel = Select(teamElement)
sel.select_by_index(4)
