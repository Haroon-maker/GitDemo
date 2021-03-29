from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\Haroon\\Downloads\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# driver.find_element_by_name("name").send_keys("Haroon")
driver.find_element_by_css_selector("input[name='name']").send_keys("Hassan")
driver.find_element_by_name("email").send_keys("haroon@technologyelement.com")
driver.find_element_by_id("exampleCheck1").click()
# select class provides the methods to handle options in dropdown
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
# dropdown.select_by_visible_text("Female")
dropdown.select_by_index(1)
driver.find_element_by_xpath("//input[@type='submit']").click()
# print(driver.find_element_by_class_name("alert-success").text)
message = driver.find_element_by_class_name("alert-success").text
assert "success" in message
driver.quit()
# //*[contains(@class, 'alert-success')]  xpath
# [class*='alert-success']   CSS