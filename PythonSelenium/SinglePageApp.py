import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\Haroon\\Downloads\\chromedriver.exe")
driver.get("https://nuxtjs.org/")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath("//a[contains(text(),'Docs')]").click()
print(driver.find_element_by_xpath("//h1[contains(text(),'Installation')]").text)
print(driver.find_element_by_xpath("//h2[@id='prerequisites']").text)
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
time.sleep(2)
driver.find_element_by_xpath("//body/div[@id='__nuxt']/div[@id='__layout']/div[1]/main[1]/div[1]/div[1]/aside[1]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]").click()
driver.find_element_by_tag_name("lite-youtube").click()
time.sleep(59)
driver.find_element_by_xpath("//body/div[@id='__nuxt']/div[@id='__layout']/div[1]/main[1]/div[1]/div[1]/aside[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]").click()
print(driver.find_element_by_xpath("//h1[contains(text(),'Directory Structure')]").text)
print(driver.find_element_by_xpath("//body/div[@id='__nuxt']/div[@id='__layout']/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/article[1]/div[1]/div[1]/pre[1]").text)