import time

from selenium import webdriver

list = []
list2 = []

driver = webdriver.Chrome(executable_path="C:\\Users\\Haroon\\Downloads\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//input[@type='search']").send_keys("ber")
time.sleep(3)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(list)
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(3)
vegiee = driver.find_elements_by_css_selector("p.product-name")
for veg in vegiee:
    list2.append(veg.text)
print(list2)
assert list == list2
original_amount = driver.find_element_by_css_selector(".discountAmt").text
driver.find_element_by_xpath("//input[@type='text']").send_keys("rahulshettyacademy")
driver.find_element_by_xpath("//button[@class='promoBtn']").click()
time.sleep(3)

discount_amount = driver.find_element_by_css_selector(".discountAmt").text
# assert float(discount_amount) < int(original_amount)
print(driver.find_element_by_xpath("//span[@class='promoInfo']").text)

amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
sum = 0
for amount in amounts:
    sum = sum + int(amount.text)
print(sum)

totalAmount = int(driver.find_element_by_class_name("totAmt").text)

assert sum == totalAmount
