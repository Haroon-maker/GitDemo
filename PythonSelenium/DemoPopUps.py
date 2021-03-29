import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path="C:\\Users\\Haroon\\Downloads\\chromedriver.exe")
driver.maximize_window()
driver.get("http://192.168.1.2:8007/#/accounts/login/")
time.sleep(2)
driver.find_element_by_css_selector("input[placeholder='Email']").send_keys('haroon@technologyelement.com')
driver.find_element_by_css_selector("input[placeholder='Password']").send_keys('123456789a')
driver.find_element_by_css_selector("button[type='submit']").click()
time.sleep(2)

driver.find_element_by_xpath("//tbody/tr[1]/td[2]/a").click()
actions = ActionChains(driver)
time.sleep(3)
menu = driver.find_element_by_xpath("//a[text()='Compliance ']")
time.sleep(2)
actions.move_to_element(menu).perform()
T4 = driver.find_element_by_xpath("//a[text()=' T4 ']")
time.sleep(2)
actions.move_to_element(T4).perform()
time.sleep(2)
driver.find_element_by_xpath("//header/div[@id='horizontal-menu-collapse']/ul[1]/li[7]/ul[1]/li[1]/ul[1]/li[2]/a[1]").click()
time.sleep(3)
teamElement = driver.find_element_by_id("load_data")
sel = Select(teamElement)
sel.select_by_index(2)
time.sleep(5)
teamElement2 = driver.find_element_by_css_selector("[id='id_slip_type']")
sele = Select(teamElement2)
sele.select_by_index(1)
time.sleep(5)
try:
    driver.find_element_by_xpath("//button[contains(text(),'Confirm')]").click()
except NoSuchElementException:
    print("Confirm Element not found.")
except Exception as e:
    print(e)
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(3)
teamElement1 = driver.find_element_by_id("load_data")
sel1 = Select(teamElement1)
sel1.select_by_index(1)
time.sleep(5)
teamElement3 = driver.find_element_by_css_selector("[id='id_slip_type']")
sele3 = Select(teamElement3)
sele3.select_by_index(1)
try:
    driver.find_element_by_xpath("//button[contains(text(),'Confirm')]").click()
except NoSuchElementException:
    print("Confirm Element not found.")
except Exception as e:
    print(e)
time.sleep(3)

driver.find_element_by_xpath("//button[@type='submit']").click()
driver.close()
