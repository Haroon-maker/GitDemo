import time

from selenium import webdriver

validateText = "Haroon"
driver = webdriver.Chrome(executable_path="C:\\Users\\Haroon\\Downloads\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
    if checkbox.get_attribute("value") == "option1":
        checkbox.click()
        assert checkbox.is_selected()
radiobuttons = driver.find_elements_by_name("radioButton")
radiobuttons[1].click()
assert radiobuttons[1].is_selected()
time.sleep(3)


driver.find_element_by_xpath("//input[@id='name']").send_keys(validateText)
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
assert validateText in alertText
# print(alert.text)
alert.accept()
time.sleep(2)
driver.find_element_by_id("confirmbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
alert.dismiss()
time.sleep(2)
assert driver.find_element_by_id("displayed-text").is_displayed()
driver.find_element_by_id("hide-textbox").click()
time.sleep(2)
print(driver.find_element_by_id("displayed-text").is_displayed())  # return False
time.sleep(3)
print(driver.find_element_by_id("show-textbox").is_selected())  # return False

time.sleep(3)
driver.close()

