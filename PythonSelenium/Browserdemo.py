from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\Haroon\\Downloads\\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="C:\\Users\\Haroon\\Downloads\\geckodriver.exe")
driver.maximize_window()
driver.get("https://app.taxslips.com")
print(driver.title)
print(driver.current_url)
# driver.set_page_load_timeout(200)
# driver.close()
