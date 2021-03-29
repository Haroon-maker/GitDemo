from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\Haroon\\Downloads\\chromedriver.exe")
driver.get("https://app.taxslips.com/#/login")
driver.maximize_window()

driver.find_element_by_id("input-22").send_keys("haroon@technologyelement.com")
driver.find_element_by_id("input-27").clear()
driver.find_element_by_id("input-27").send_keys("123456789a")
driver.find_element_by_xpath("//button[@type='submit']").click()
driver.find_element_by_link_text("Forgot Password?").click()
driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[2]/div/div/span/form/button[1]/span").click()
import pdb; pdb.set_trace()  # use for debugging
driver.quit()
