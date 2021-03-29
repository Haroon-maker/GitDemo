from selenium import webdriver


opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
opt.add_argument("headless")
opt.add_argument("--ignore certificate errors")
driver = webdriver.Chrome(executable_path="C:\\Users\\Haroon\\Downloads\\chromedriver.exe", options=opt)

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)