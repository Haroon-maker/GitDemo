from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\Haroon\\Downloads\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element_by_name("name").send_keys("Haroon")
print(driver.find_element_by_name("name").text)
# get text by selenium
print(driver.find_element_by_name("name").get_attribute("value"))
# get text by JS
print(driver.execute_script('return document.getElementsByName("name")[0].value'))
# click button by JS
shopbutton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();", shopbutton)
# scroll down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")