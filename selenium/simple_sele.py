from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())


global driver
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://rahulshettyacademy.com")
print(driver.title) 
driver.maximize_window()
driver.refresh()
driver.back()
